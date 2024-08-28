#!/bin/bash
#Author : xjagset(jagadish.sethi@wipro.com)


GAVs_success=""
GAVs_failure=""

usage ()
{
  echo "Usage: $cmd [Absolute path of the file]" 1>&2
  exit 1
}


[[ $# -eq 1 ]] || usage

cat $1 | while read line
do

read groupId artifactId version status <<<$(IFS="::"; echo $line)

echo "line $line"

echo "groupId $groupId"
echo "artifactId $artifactId"
echo "version $version"
echo "status $status"


	if [[ "$status" == "ONLINE" ]];then
		GAVs_success+="#$artifactId::$version::$groupId"
	else
		GAVs_failure+="#$artifactId::$version::$groupId"
	fi

echo "GAVs_success   $GAVs_success"
echo "GAVs_failure   $GAVs_failure"

echo "GAVs_success=$GAVs_success" > /tmp/${BUILD_TAG}
echo "GAVs_failure=$GAVs_failure" >> /tmp/${BUILD_TAG}


done



