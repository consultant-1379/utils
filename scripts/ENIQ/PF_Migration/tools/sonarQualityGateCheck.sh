#!/bin/bash

pkgName=$1
res=1

if [ -f "/proj/eiffel013_config_fem6s11/tools/qualityGateSkip.txt" ]; then
        grep -w $pkgName /proj/eiffel013_config_fem6s11/tools/qualityGateSkip.txt > /dev/null
        res=$?
fi

if [ $res -eq 0 ]; then
        echo "SKIPPED"
else
	cat /proj/esjkadm100/Sonar/sonarOut.txt | awk -F"conditions" '{print $1}' |grep '"status":"OK"' >> /dev/null
	if [ $? -eq 0 ]; then
		echo "OK"
	else
		echo "ERROR"
	fi
fi
rm -f /proj/esjkadm100/Sonar/sonarOut.txt
