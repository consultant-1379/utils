#!/usr/bin/bash

echo "Checking whether RT_suite has generated HTML files or not...."

ls -lrt /eniq/home/dcuser/RegressionLogs/

ls -lrt /eniq/home/dcuser/RegressionLogs/ | grep -i "eniqs_*"
if [ $? -ne 0 ]
then
        echo " ENIQS html file is missing..." 1>&2
        exit 1
else
        echo " ENIQS html file is PRESENT!!!!!"

fi

exit 0
