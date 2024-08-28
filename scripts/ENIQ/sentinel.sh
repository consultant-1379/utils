#!/bin/sh
# ********************************************************************
# Ericsson Radio Systems AB                                     SCRIPT
# ********************************************************************
#
#
# (c) Ericsson Radio Systems AB 2018 - All rights reserved.
#
# The copyright to the computer program(s) herein is the property
# of Ericsson Radio Systems AB, Sweden. The programs may be used
# and/or copied only with the written permission from Ericsson Radio
# Systems AB or in accordance with the terms and conditions stipulated
# in the agreement/contract under which the program(s) have been
# supplied.
#
#
# ********************************************************************
# Name    : sentinel.sh
# Updated : 07/09/2018
# Revision: E
# Purpose : Main Wrapper script to start and stop the Sentinel License
#           Server. This script is called by the relevant service
#           files during start/stop phase. If sets environment variables
#           before starting the license server.
#
# ********************************************************************
#
#       Command Section
#
# ********************************************************************
AWK=/usr/bin/awk
BASENAME=/usr/bin/basename
CAT=/usr/bin/cat
DIRNAME=/usr/bin/dirname
ECHO='/usr/bin/echo -e'
EGREP=/usr/bin/egrep
EXPR=/usr/bin/expr
GETENT=/usr/bin/getent
HEAD=/usr/bin/head
HOSTNAME=/usr/bin/hostname
SED=/usr/bin/sed
SLEEP=/usr/bin/sleep
SYSTEMCTL=/usr/bin/systemctl

# ********************************************************************
#
#       Configuration Section
#
# Used to set-up the Sentinel License Managers Environment
# This can be defined in an environment file in the etc directory.
# ********************************************************************
#
# Find Home Directory
_dir_=`$DIRNAME $0`
SCRIPTHOME=`cd $_dir_ 2>/dev/null && pwd || $ECHO $_dir_`
SENTINEL_BASE_DIR="/eniq/sentinel/"

# Default location of the Sentinel License Server files.
LSDEFAULTDIR=${SENTINEL_BASE_DIR}
export LSDEFAULTDIR

# Sentinel License File
LSERVRC=${SENTINEL_BASE_DIR}lic/lservrc
export LSERVRC

# Location of Logfile and max size before rotating
LSERVOPTS="-l ${SENTINEL_BASE_DIR}log/usage.log -z 1m "
export LSERVOPTS

#Sentinel service File
SENTINEL_SERVICE="licensing-sentinel.service"

ENVIRONMENT_FILE=${SENTINEL_BASE_DIR}/etc/sentinel.env
# Check for Environment file?
if [ ! -z ${ENVIRONMENT_FILE} -a -s ${ENVIRONMENT_FILE} ]; then
	. ${ENVIRONMENT_FILE}
fi

# ********************************************************************
#
# 		Functions
#
# ********************************************************************
#

### Function: allowed_to_start ###
#
# Checks if this server is allowed to start the Sentinel License Server.
# Checks the sentinel environment file to get the IPs of the server sentinel should run on.
# Checks this servers IP to see if it is allowed to start service.
#
allowed_to_start()
{
    MY_HOSTNAME=`$HOSTNAME`  
    myIP=`$GETENT ahosts ${MY_HOSTNAME} | $AWK '{print $1}' | $HEAD -1`

    # Check Sentinel environment file for a ", separated" list of I.P.s that sentinel can run on.
    if [ -s ${ENVIRONMENT_FILE} ]; then
        sentEnvFileIP=`$CAT ${ENVIRONMENT_FILE} | $EGREP '^[ 	]*LSHOST=' |$AWK -F\= '{print $2}'|$SED -e 's|,| |g'`
    else
        # If file does not exist or is not accessible then do not start.
        $ECHO "ERROR: Environment File ' ${ENVIRONMENT_FILE} ' not found; EXITING"
        return 1
    fi

    for sentIP in ${sentEnvFileIP}; do
        if [ "${myIP}" = "${sentIP}" ]; then
            return 0
        fi
    done
    return 1
}


### Function: start_sentinel ###
#
# Starts the Sentinel License Server
#
start_sentinel()
{
    REPEATING_ERROR_COUNT=0

    # Sentinel binaries are located on the NAS storage which must be mounted before we continue.
    # This check is to make sure the NAS is available before we try to start sentinel.
    while [ ! -s ${SENTINEL_BASE_DIR}bin/lserv ]; do
        $ECHO "WARNING: File ' ${SENTINEL_BASE_DIR}bin/lserv ' not found; waiting to try again."
        ${SLEEP} 30
        REPEATING_ERROR_COUNT=`${EXPR} ${REPEATING_ERROR_COUNT} + 1`
        if [ "${REPEATING_ERROR_COUNT}" -ge "10" ]; then
       	    ${SLEEP} 90 
        fi
        if [ "${REPEATING_ERROR_COUNT}" -ge "40" ]; then
            ${SYSTEMCTL} stop ${SENTINEL_SERVICE}
        fi
    done

    # Check if I am allow to start the sentinel server on this blade.
    # Get mt IP and see if it is in the environment file.
    # If Yes then start, else stop the service.
    if  allowed_to_start ; then
        if [ -s ${SENTINEL_BASE_DIR}bin/lserv ]; then
            # Sentinel LM should not be running at this point.
            # Ensure there are no instances of it that were not shut down properly.
            if [ -s ${SENTINEL_BASE_DIR}bin/lsrvdown ]; then
                # We do not want to stop all remote instances of the Sentinel LM.
                # Only stop the instance of Sentinel LM running on this server.
            	${SENTINEL_BASE_DIR}bin/lsrvdown localhost >> /dev/null 2>&1
            fi

            cd ${SENTINEL_BASE_DIR}
        	${SENTINEL_BASE_DIR}bin/lserv
            else
    	    $ECHO "ERROR: Unable to locate file ' ${SENTINEL_BASE_DIR}bin/lserv ' to start Sentinel LM"
    	    ${SYSTEMCTL} stop ${SENTINEL_SERVICE} 
    	    ${SLEEP} 2
    	    exit 1
    	fi
    else
    # Sentinel LM should not start on this server. Disable Sentinel service.
    $ECHO "ERROR: Sentinel LM should not be started on this server."

    ${SYSTEMCTL} stop ${SENTINEL_SERVICE}
    ${SLEEP} 2
    exit 1
    fi
}


### Function: stop_sentinel ###
#
# Stops the Sentinel License Server
#
stop_sentinel()
{
    if [ -s ${SENTINEL_BASE_DIR}bin/lsrvdown ]; then
        # We do not want to stop all remote instances of the Sentinel LM.
        # Only stop the instance of Sentinel LM running on this server.
    	${SENTINEL_BASE_DIR}bin/lsrvdown localhost
    $SYSTEMCTL reset-failed ${SENTINEL_SERVICE}
    else
        $ECHO "WARNING: Unable to locate file ${SENTINEL_BASE_DIR}bin/lsrvdown"
    fi
}


usage()
{
	$ECHO "`$BASENAME $0` -a [start|stop]"
}

# ***********************************************************************
#
#                    Main body of program
#
# ***********************************************************************
#

while getopts ":a:" arg; do
    case $arg in
        a) 	SENTINEL_ACTION="$OPTARG"
       	    ;;
        \?) usage
		    exit 1
       	    ;;
    esac
done
shift `${EXPR} $OPTIND - 1`

if [ ! "${SENTINEL_ACTION}" ]; then
    usage
    exit 1
fi


case "${SENTINEL_ACTION}" in
     start) start_sentinel
    	    ;;

      stop) stop_sentinel
    	    ;;

         *) # SHOULD NOT GET HERE
         	usage
         	exit 1
       	    ;;
esac
exit 0
