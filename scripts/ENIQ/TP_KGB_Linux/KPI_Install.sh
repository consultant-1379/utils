#############!/view/eniq_view/vobs/cello/cade_A_tools_perl/SunOS/sparc/bin/perl -w

#!/usr/bin/bash

# This Script is to Extract the BO files...
if [ ! -d "/eniq/sw/installer/boreports/" ]
then
	su - dcuser -c "mkdir /eniq/sw/installer/boreports/"
else
	echo "BOREPORTS directory is present....!!!!"
fi

KPI_Check=`ls /eniq/sw/installer/reporttest/*.zip |wc -l`

if [ $KPI_Check -eq 0 ]
    then
        echo "No BO TPI tech packs are available at the BO packages dir"
else
		echo " We have the BO tech packs ..and hence we have to extract these as well"

		# Below code is to rename all the BO tech packs from tpi to zip file extensions.

        cd /eniq/sw/installer/reporttest/
	chmod 777 /eniq/sw/installer/reporttest/*.zip
	/usr/bin/chown dcuser:dc5000 /eniq/sw/installer/reporttest/*.zip
        echo " Bo files are "
        ls -lrt /eniq/sw/installer/reporttest/*.zip

        Files=`ls -lrt /eniq/sw/installer/reporttest/ | grep zip | awk -F" " '{print $9}'`

        #for i in ${Files[@]}
        #do
        #    echo $i
        #    name=`echo $i | cut -d "." -f1`
        #    mv $i $name.zip
        #    zipfile=$name.zip
        #done
	sleep 5
	#su - dcuser -c "cd /eniq/sw/installer/;/usr/bin/bash /eniq/sw/installer/extract_report_packages.bsh /eniq/sw/installer/BO_package/ /eniq/sw/installer/bouniverses/ > /tmp/SomeFile.txt"
	su - dcuser -c "cd /eniq/sw/installer/;/usr/bin/bash /eniq/sw/installer/extract_report_packages.bsh /eniq/sw/installer/reporttest/ /eniq/sw/installer/report"
	VAR=`cat /tmp/extractresult | grep WARNING`
	if [ "$VAR" != "" ]; then
		echo "Extracted with any WARNINGS"
	else
		echo "Extracted without WARNINGS"
	fi
        VAR=`cat /tmp/extractresult | grep FAILED`
        if [ "$VAR" != "" ]; then
                echo "Build Failed"
		exit 1
        else
                echo "Extracted without failure"
        fi
	VAR=`cat /tmp/extractresult | grep "The license is empty"`
	if [ "$VAR" != "" ]; then
		echo "INVALID LICENSE !!! PLEASE CHECK !!!\n"
	else
		echo "Extracted without WARNINGS"
	fi
	echo " Executing the CUID_extractor_kpi.sh script to the CUID of Report packages"
	su - dcuser -c "cd /tmp ;/usr/bin/bash CUID_extractor_kpi.sh"
	echo "COMPARE_CUID DONE"
fi
