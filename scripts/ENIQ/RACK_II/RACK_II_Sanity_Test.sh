#!/bin/sh
host=ieatrcx6575.athtem.eei.ericsson.se

testENIQ_Sentinel_Server() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
sentinel_server=`cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i "Successfully installed ENIQ Sentinel server" | wc -l`
if [ $sentinel_server -eq 1 ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQ_IPMP_Info() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
ipmp_info=`cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i "Successfully gathered IPMP information|Successfully gathered BOND information" | wc -l`
if [ $ipmp_info -eq 1 ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQ_Sym_Info() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
sym_info=`cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i "Successfully created DB Sym Links" | wc -l`
if [ $sym_info -eq 1 ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQ_LUN_Info() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
lun_info=`cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i "Successfully created LUN Map ini file" | wc -l`
if [ $lun_info -eq 1 ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQ_create_repdb() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
create_repdb=`cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i "Successfully completed stage - create_repdb" | wc -l`
if [ $create_repdb -eq 1 ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQ_SYBASE_IQ() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
sybase_iq=`cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i "Successfully installed SYBASE IQ" | wc -l`
if [ $sybase_iq -eq 1 ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQ_SYBASE_IQ() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
sybase_asa=`cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i "Successfully installed SYBASE ASA" | wc -l`
if [ $sybase_asa -eq 1 ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQ_PLATFORM() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
platform=`cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i "Successfully installed ENIQ Platform" | wc -l`
if [ $platform -eq 1 ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQ_FEATURES() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
Features=`cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i "Successfully installed Features" | wc -l`
if [ $Features -eq 1 ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQ_SERVICE_SCRIPTS() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
service=`cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i "Successfully installed Service scripts" | wc -l`
if [ $service -eq 1 ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQ_STATUS() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
status=`cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i "Successfully updated ENIQ status file" | wc -l`
if [ $status -eq 1 ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQ_SW() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
sw=`cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i "ENIQ SW successfully installed" | wc -l`
if [ $sw -eq 1 ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

############################### SANITY TESTS ###################################

testENIQS_pmdata_wifi() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
pmdata=` df -hk | grep -w pmdata_wifi | wc -l | grep 0 `
if [ $pmdata == "0" ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQS_nas() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
nas=` df -hk | grep nas | wc -l | grep 22 `
if [ $nas == "22" ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}



testENIQS_DWHDB_STOP() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
eniqs_dwhdb_stop=` systemctl stop eniq-dwhdb; systemctl show -p ActiveState eniq-dwhdb | cut -f2 -d'=' | grep inactive `
if [ $eniqs_dwhdb_stop == "inactive" ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQS_DWHDB_RESTART() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
eniqs_dwhdb_start=` systemctl restart eniq-dwhdb; systemctl show -p ActiveState eniq-dwhdb | cut -f2 -d'=' | grep active `
if [ $eniqs_dwhdb_start == "active" ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQS_NASd_service() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
NASd_Started=` systemctl start NASd.service;systemctl status NASd.service | grep "Started Storage NASd" `
if [ $NASd_Started == "Started Storage NASd" ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQS_STOP_MILESTONE() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
stop_milestone=` systemctl stop NAS-online.service;systemctl status NAS-online.service | grep "Stopped Milestone NAS Service" `
if [ $stop_milestone == "Stopped Milestone NAS Service" ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQS_START_MILESTONE() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
start_milestone=` systemctl start NAS-online.service;systemctl status NAS-online.service | grep "Started Milestone NAS Service" `
if [ $start_milestone == "Started Milestone NAS Service" ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQS_DCUSER() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
dcuser1=` id dcuser | awk "{print $2}" | grep dc5000 `
if [ $dcuser1 == "dc5000" ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testENIQS_SystemMaxUse() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@$host '
SystemMaxUse=` cat /etc/systemd/journald.conf | grep SystemMaxUse | cut -f2 -d'=' | grep 8G `
if [ $SystemMaxUse == "8G" ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

# Load and run shUnit2.
. ./shunit2.sh

