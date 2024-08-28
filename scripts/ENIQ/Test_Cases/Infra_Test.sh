#! /bin/sh

testInstallationDirectory() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@HOST_IP '
installation_dir=`ls /eniq/ | grep installation | wc -l`
if [ $installation_dir -eq 1 ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}



testENIQS_STATS_Directory() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@HOST_IP '
eniq_stats_dir=`ls /net/10.45.192.153/JUMP/ | grep ENIQ_STATS | wc -l`
if [ $eniq_stats_dir -eq 1 ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

# Load and run shUnit2.
. ./shunit2
