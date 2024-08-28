#!/bin/bash
DHCP_SERVER_IP=ieatrcx6786
MOUNTPOINT=/export/scripts/CLOUD/RHEL/
VCEN_HOSTNAME=141.137.215.157


hostname
VSP=`diff /tmp/vsp_after_add /tmp/vsp_before_add | xargs | cut -d"<" -f2 | xargs`
echo "===================================================================="
echo "Checking virtual serial port settings on ENIQS, please wait....:"
echo "===================================================================="
while [ `netstat -ntlp | grep $VSP | wc -l` -eq 0 ]
do
   echo "Checking the VSP port"
   sleep 5
done
echo "===================================================================="
echo "OK"
echo "===================================================================="

cat <<EOF> /tmp/expect.sh
#!/usr/bin/expect
set hostname [lindex \$argv 0]
set timeout 4800

spawn telnet \$hostname $VSP

expect ""
send "\r"

expect "Select the server type you wish to install"
send "1\r"

expect "Select the storage that the ENIQ system will be installed on"
send "1\r"

expect "Hit enter for (unity)"
send "local\r"

expect "Enter the location of the licence file"
send "/net/10.45.192.153/JUMP/ENIQ_S19.2\r"

expect "Hit enter for (192.168.0.0:255.255.0.0)"
send "\r"

expect "Select two group interfaces from the list above separated by a space (Example :<Interface_1> <Interface_2>)"
send "ens192 ens256\r"

expect "Enter the IP address of the PM Services Group (Example :10.25.46.130)"
send "192.168.0.51\r"

expect "Enter the netmask address for the PM Services Group (Example :255.255.249.0)"
send "255.255.0.0\r"

expect "Enter the Gateway IP address of the PM Services Group (Example :10.0.0.1)"
send "192.168.0.1\r"

expect "Enter the IP address of at least two highly available servers in the same subnet as PM Services Group (separated by comma)"
send "10.45.192.153,172.16.30.1\r" 

expect "Do you want to configure Backup Group (Y|N)?"
send "N\r"

expect "Is the information above correct (Yes|No)"
send "Yes\r"

expect "Enter the console IP address of the NAS"
send "172.16.30.18\r"

expect "Enter the virtual IP address for nas1 (1 of 8)"
send "172.16.30.14\r"

expect "Enter the virtual IP address for nas2 (2 of 8)"
send "172.16.30.16\r"

expect "Enter the virtual IP address for nas3 (3 of 8)"
send "172.16.30.14\r"

expect "Enter the virtual IP address for nas4 (4 of 8)"
send "172.16.30.16\r"

expect "Enter the virtual IP address for nas5 (5 of 8)"
send "172.16.30.14\r"

expect "Enter the virtual IP address for nas6 (6 of 8)"
send "172.16.30.16\r"

expect "Enter the virtual IP address for nas7 (7 of 8)"
send "172.16.30.14\r"

expect "Enter the virtual IP address for nas8 (8 of 8)"
send "172.16.30.16\r"

expect "Enter the name of the primary NAS storage pool (max. 7 characters)"
send "eniqs\r"

expect "Enter the password for user 'master' in the NAS system"
send "master\r"

expect "Enter the password for user 'support' in the NAS system"
send "symantec\r"

expect "Are the values above correct (Yes/No)"
send "Yes\r"

expect "Select Range of disks you want to allocate to the eniq_stats_pool FS Storage Pool"
send "7\r"

expect "Select the disk you want to allocate for IQ SYS MAIN database usage"
send "2\r"

expect "Select Range of disks you want to allocate for MainDB database usage"
send "3,4\r"

expect "Select Range of disks you want to allocate for TempDB database usage"
send "1\r"

expect "Are the disk allocations above correct (Yy/Nn)"
send "Y\r"

expect "Enter IP address of Defaultrouter"
send "\r"

expect "Enter IP address of DNS SERVER(s)"
send "192.168.0.1\r"

expect "Enter DNS domain name"
send "athtem.eei.ericsson.se\r"

expect "Enter TIMEZONE"
send "\r"

expect "Enter Amount of Shared Memory to Allocate to IQ in Mbytes"
send "\r"

expect "Select the partition plan you wish to install"
send "2\r"

expect "Please enter the IP address of the OSS Server"
send "1.1.1.1\r"

expect "Please enter the ENIQ feature software path"
send "/net/10.45.192.153/JUMP/ENIQ_STATS/ENIQ_STATS/FEATURE/\r"

expect "Select the ENIQ Features numbers you wish to"
send "1-63\r"

expect "Are the values above correct (Yes/No)"
send "Yes\r"

expect "Test"
send "\r"

EOF


cat <<EOF> /tmp/stagelist.sh
#!/bin/bash
sshpass -p 'shroot12' ssh eniqs '
sed -i 's/install_ENIQ_platform/#install_ENIQ_platform/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist
sed -i 's/install_ENIQ_features/#install_ENIQ_features/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist
sed -i 's/activate_ENIQ_features/#activate_ENIQ_features/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist
sed -i 's/setup_SMF_scripts/#setup_SMF_scripts/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist
sed -i 's/install_extra_fs/#install_extra_fs/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist
sed -i 's/install_rolling_snapshot/#install_rolling_snapshot/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist
sed -i 's/validate_SMF_contracts/#validate_SMF_contracts/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist
sed -i 's/add_alias_details_to_service_names/#add_alias_details_to_service_names/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist
'
EOF

ssh root@$HOSTNAME "bash /tmp/stagelist.sh"
sleep 2m
echo "===================================================================="
echo "Connecting to the ENIQS through VSP"
echo "===================================================================="

