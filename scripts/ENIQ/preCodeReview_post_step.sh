#!/bin/bash

###################################################################
################Post step scripts and git commands ################
###################################################################

#for POM_FILE in `find . -type f -name pom.xml -exec egrep -l "<directoryIncluded>true</directoryIncluded>" {} \;`
#do
#   echo $POM_FILE
#   echo "The PreCodeReview job has been set to fail.  This precodeReview build contains a reference to <directoryIncluded>true</directoryIncluded>.  This reference should be set to <directoryIncluded>false</directoryIncluded>.  Please update the pom file reference and push the change for code review. This update is REQUIRED for ENM installation on RHEL7"
#   exit 1
#done

#Display what host the job is building on
echo "###############################################"
echo "  Hostname: $HOSTNAME   ";
echo "###############################################"

