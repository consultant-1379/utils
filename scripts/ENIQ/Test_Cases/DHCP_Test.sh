#! /bin/sh

testDHCPNetwork() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@ieatrcx6786 '
installation_dir=`cat /etc/dhcp/dhcpd.conf | grep 192.168.0.0 | wc -l`
if [ $installation_dir -eq 1 ]
then
        exit 0;
else
        exit 1;
fi
'
 assertEquals 0 $?
}

testDHCPClient() {
sshpass -p 'shroot12' ssh -q -o stricthostkeychecking=no root@ieatrcx6786 '
eniq_stats_dir=`cat /etc/dhcp/dhcpd.conf | grep eniqs | wc -l`
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
