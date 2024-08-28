#!/bin/bash

###################################################################
################Post step scripts and git commands ################
###################################################################

#Get the job name from the pwd
jobName=${PWD##*/};
echo "Job Name: "$jobName

#Getting the branch name from the config.xml
pushBranch=$(cat ${HUDSON_HOME}/jobs/$jobName/config.xml | sed -n 's:.*<branchName>\(.*\)</branchName>.*:\1:p')

if [[ $pushBranch == "" ]]; then
        echo "Not pushing to any branch"
else
        echo "Merging with "$pushBranch
        #Merge code with Relased  before push
        git merge gcn/$pushBranch
fi

