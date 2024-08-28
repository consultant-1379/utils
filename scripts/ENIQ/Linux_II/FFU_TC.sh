#!/usr/bin/bash

cd /var/tmp
rm -rf /var/tmp/TC_Result.html
fail=0
pass=0
total=0

echo "<html><head><title>FFU TestCase Results</title></head><body><table border=\"2\"><tr><th><b> TestCase Name </th><th><b> TestCase </th><th><b>PASS/FAIL</th></tr>" >> /var/tmp/TC_Result.html

#####LOG SANITY

Log=`ls /var/tmp/ES_FFU_UPG_atvts*.log`
echo "LOG $Log"

tc12=`cat $Log | egrep -i "ERROR"`
if [[ $tc12 =~ "ERROR" ]]
then
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
else
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
fi
echo "<tr> <td> ERROR CHECK </td> <td> cat $Log | egrep -i \"ERROR\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "warning"`
if [[ $tc12 =~ "warning" ]]
then
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
else
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
fi
echo "<tr> <td> WARNING CHECK </td> <td> cat $Log | egrep -i \"warning\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "permission denied"`
if [[ $tc12 =~ "permission denied" ]]
then
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
else
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
fi
echo "<tr> <td> PERMISSION CHECK </td> <td> cat $Log | egrep -i \"permission denied\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "cannot"`
if [[ $tc12 =~ "cannot" ]]
then
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
else
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
fi
echo "<tr> <td> Cannot CHECK </td> <td> cat $Log | egrep -i \"cannot\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "couldn"`
if [[ $tc12 =~ "couldn" ]]
then
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
else
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
fi
echo "<tr> <td> Could not CHECK </td> <td> cat $Log | egrep -i \"couldn\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "could not"`
if [[ $tc12 =~ "could not" ]]
then
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
else
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
fi
echo "<tr> <td> Could not CHECK </td> <td> cat $Log | egrep -i \"could not\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "can.t open"`
if [[ $tc12 =~ "can.t open" ]]
then
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
else
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
fi
echo "<tr> <td> Can.t open CHECK </td> <td> cat $Log | egrep -i \"can.t open\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "no such"`
if [[ $tc12 =~ "no such" ]]
then
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
else
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
fi
echo "<tr> <td> no such CHECK </td> <td> cat $Log | egrep -i \"no such\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html



tc12=`cat $Log | egrep -i "Successfully finished unpacking core SW on eniqs"`
if [[ $tc12 =~ "Successfully finished unpacking core SW on eniqs" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> unpacking core SW on eniqs CHECK </td> <td> cat $Log | egrep -i \"Successfully finished unpacking core SW on eniqs\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "Parsers installed successfully"`
if [[ $tc12 =~ "Parsers installed successfully" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> Parsers installaltion CHECK </td> <td> cat $Log | egrep -i \"Parsers installed successfully\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "ERBS combined views are created successfully"`
if [[ $tc12 =~ "ERBS combined views are created successfully" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> ERBS combined views CHECK </td> <td> cat $Log | egrep -i \"ERBS combined views are created successfully\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "NAS is online"`
if [[ $tc12 =~ "NAS is online" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> NAS CHECK </td> <td> cat $Log | egrep -i \"NAS is online\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "Successfully completed Feature Upgrade"`
if [[ $tc12 =~ "Successfully completed Feature Upgrade" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> Feature Upgrade CHECK </td> <td> cat $Log | egrep -i \"Successfully completed Feature Upgrade\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "Successfully added ENIQ features"`
if [[ $tc12 =~ "Successfully added ENIQ features" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> ENIQ features CHECK </td> <td> cat $Log | egrep -i \"Successfully added ENIQ features\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "Successfully added selected features for eniq_oss_1"`
if [[ $tc12 =~ "Successfully added selected features for eniq_oss_1" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> selected features for eniq_oss_1 CHECK </td> <td> cat $Log | egrep -i \"Successfully added selected features for eniq_oss_1\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "Successfully completed add new features"`
if [[ $tc12 =~ "Successfully completed add new features" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> add new features CHECK </td> <td> cat $Log | egrep -i \"Successfully completed add new features\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "Successfully completed the cleanup"`
if [[ $tc12 =~ "Successfully completed the cleanup" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))

fi
echo "<tr> <td> cleanup CHECK </td> <td> cat $Log | egrep -i \"Successfully completed the cleanup\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "Completed upgrade_feature_only Procedure"`
if [[ $tc12 =~ "Completed upgrade_feature_only Procedure" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> upgrade_feature_only Procedure CHECK </td> <td> cat $Log | egrep -i \"Completed upgrade_feature_only Procedure\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "TP upgraded  successfully"`
if [[ $tc12 =~ "TP upgraded  successfully" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> TP upgraded CHECK </td> <td> cat $Log | egrep -i \"TP upgraded  successfully\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "Successfully completed the encryption of passwords on eniqs"`
if [[ $tc12 =~ "Successfully completed the encryption of passwords on eniqs" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> encryption of passwords on eniqs CHECK </td> <td> cat $Log | egrep -i \"Successfully completed the encryption of passwords on eniqs\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "Successfully updated status file"`
if [[ $tc12 =~ "Successfully updated status file" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> status file CHECK </td> <td> cat $Log | egrep -i \"Successfully updated status file\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "Required files and scripts successfully found"`
if [[ $tc12 =~ "Required files and scripts successfully found" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> Required files and scripts CHECK </td> <td> cat $Log | egrep -i \"Required files and scripts successfully found\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "hostsync.service service is restarted successfully"`
if [[ $tc12 =~ "hostsync.service service is restarted successfully" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> hostsync.service CHECK </td> <td> cat $Log | egrep -i \"hostsync.service service is restarted successfully\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "NASd service has been successfully enabled"`
if [[ $tc12 =~ "NASd service has been successfully enabled" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> NASd CHECK </td> <td> cat $Log | egrep -i \"NASd service has been successfully enabled\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "Successfully deleted /var/tmp/upgrade on eniqs"`
if [[ $tc12 =~ "Successfully deleted /var/tmp/upgrade on eniqs" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> Deleted /var/tmp/upgrade on eniqs CHECK </td> <td> cat $Log | egrep -i \"Successfully deleted /var/tmp/upgrade on eniqs\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "Successfully started svc:/eniq/roll-snap:default service"`
if [[ $tc12 =~ "Successfully started svc:/eniq/roll-snap:default service" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> svc:/eniq/roll-snap:default service CHECK </td> <td> cat $Log | egrep -i \"Successfully started svc:/eniq/roll-snap:default service\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "Successfully completed stage - post upgrade configuration "`
if [[ $tc12 =~ "Successfully completed stage - post upgrade configuration " ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> post upgrade configuration CHECK </td> <td> cat $Log | egrep -i \"Successfully completed stage - post upgrade configuration \" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "/eniq/admin/version/eniq_history file updated correctly"`
if [[ $tc12 =~ "/eniq/admin/version/eniq_history file updated correctly" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> /eniq/admin/version/eniq_history file CHECK </td> <td> cat $Log | egrep -i \"/eniq/admin/version/eniq_history file updated correctly\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc12=`cat $Log | egrep -i "/eniq/admin/version/eniq_status file updated correctly"`
if [[ $tc12 =~ "/eniq/admin/version/eniq_status file updated correctly" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
		total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
		total=$((total+1))
fi
echo "<tr> <td> /eniq/admin/version/eniq_status file CHECK </td> <td> cat $Log | egrep -i \"/eniq/admin/version/eniq_status file updated correctly\" </td> $status </td> </tr>" >> /var/tmp/TC_Result.html


####SERVER SANITY

tc2=`df -hk | grep nas | wc -l | grep 22`
if [[ $tc2 =~ "22" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
				total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
				total=$((total+1))
fi
echo "<tr> <td> NAS </td> <td> df -hk | grep nas | wc -l | grep 22 </td> $status </td> </tr>" >> /var/tmp/TC_Result.html

tc2=`systemctl restart eniq-dwhdb; systemctl show -p ActiveState eniq-dwhdb | cut -f2 -d'=' | grep active`
if [[ $tc2 =~ "active" ]]
then
        status="<td style=\"color:green;\"> PASS"
                pass=$((pass+1))
				total=$((total+1))
else
        status="<td style=\"color:red;\"> FAIL"
                fail=$((fail+1))
				total=$((total+1))
fi
echo "<tr> <td> dwhdb </td> <td> systemctl restart eniq-dwhdb; systemctl show -p ActiveState eniq-dwhdb | cut -f2 -d'=' | grep active </td> $status </td> </tr>" >> /var/tmp/TC_Result.html


echo "</table></body></html>" >> /var/tmp/TC_Result.html
echo "Total: $total"  >> /var/tmp/TC_Result.html
echo "Pass: $pass"  >> /var/tmp/TC_Result.html
echo "Fail: $fail"  >> /var/tmp/TC_Result.html
echo "*********************************************************************************"

echo "Total: $total"
echo "Pass: $pass"
echo "FAIL: $fail"


