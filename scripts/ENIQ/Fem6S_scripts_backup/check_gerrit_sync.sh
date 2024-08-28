#!/bin/bash

RETRY=6
SLEEP=10

# Handle job configurations with multiple git repositories.
[ -z "${GIT_URL}" ] && GIT_URL=${GIT_URL_1}

[ -z "${GIT_URL}" ] && echo "Error! GIT_URL not set." && exit 1

#if [[ "${GIT_URL}" =~ gerritmirror ]]; then
gmu=${GIT_URL} && gcu=$(echo ${GIT_URL})
#else
#  gcu=${GIT_URL} && gmu=$(echo ${GIT_URL} | sed 's/gerrit/gerritmirror.lmera/')
#fi

# check if branch was passed as arg, else use Jenkins working branch
[ -n "$1" ] && branch=$1 || branch=${GIT_BRANCH##*/} 

# get the commit ID's on GC master and mirror
echo "INFO: Checking commit ID's for '$branch' branch on Gerrit Central."
gcr=$(git ls-remote -h ${gcu} ${branch} | awk '{print $1}')
gmr=$(git ls-remote -h ${gmu} ${branch} | awk '{print $1}')
echo "INFO: central: ${gcr}"
echo "INFO: mirror:  ${gmr}"

# compare master and mirror
if [[ "${gcr}" != "${gmr}" ]]; then
  echo "INFO: Gerrit central and mirror are out of sync."
  echo "INFO: Waiting a maximum of $((RETRY*SLEEP)) seconds for sync."

  retry=0
  # retry a number of times
  while (( retry < RETRY )); do
    echo "INFO: Attempting retry #$((retry+1)) of $RETRY in $SLEEP seconds."
    sleep $SLEEP

    gcr=$(git ls-remote -h ${gcu} ${branch} | awk '{print $1}')
    gmr=$(git ls-remote -h ${gmu} ${branch} | awk '{print $1}')
    echo "INFO: central: $gcr, mirror: $gmr"

    # compare master and mirror, again
    if [ "${gcr}" = "${gmr}" ]; then
        echo "INFO: fetching latest changes on branch $branch."
        git fetch
        break
    fi

    ((retry++))
  done
  now=$( date )
  curl --silent -X POST https://fem101-eiffel004.lmera.ericsson.se:8443/jenkins/j"{\"parameter\": [{\"name\":\"GERRIT_REPO\", \"value\":\"${gcr}\"}, {\"name\":\"retries\", \"value\":\"${retry}\"}, {\"name\":\"time\", \"value\":\"${now}\"}]}" || true
fi

# if still out of sync, fail the job
[ "${gcr}" != "${gmr}" ] && echo "ERROR: Gerrit central and mirror out of sync." && exit 1
# Check we're on the correct (synced) revision
[ "${GIT_COMMIT}" != "${gmr}" ] && echo -e "*** WARNING: Not using latest revision.\nFetching upstream changes again from $gmu. ***" && git fetch
echo "INFO: Branch in sync between Gerrit central and mirror."
