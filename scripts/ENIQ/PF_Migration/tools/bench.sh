#!/bin/sh
pkgName=$1

if [ -f "/proj/eiffel013_config_fem6s11/tools/vulnerability_count.txt" ]; then
                  expectedCount=`grep -w $pkgName /proj/eiffel013_config_fem6s11/tools/vulnerability_count.txt | awk -F' ' '{print $2}'`
                  logDir="/proj/eiffel013_config_fem6s11/eiffel_home/jobs/${pkgName}/builds/"
                  buildNumber=`ls -lrt ${logDir} |tail -1 | awk -F' ' '{print $9}'`
                  #actualCount=`grep warnings ${logDir}/${buildNumber}/log | awk -F' ' '{print $2}'`
                  #actualCount=`grep -B 2 postcompile ${logDir}/${buildNumber}/log | grep warning | awk -F' ' '{print $2}'`
                  #actualCount=`tail -6 ${logDir}/${buildNumber}/log | grep warning | awk -F' ' '{print $2}'`
                  actualCount=`grep '[0-9] warning' ${logDir}/${buildNumber}/log | awk -F' ' '{print $2}'`
                  if [ ${actualCount} -le ${expectedCount} ]; then
                                                  echo "SUCCESS"
                  else
                                                  echo "FAILURE"
                  fi
fi

