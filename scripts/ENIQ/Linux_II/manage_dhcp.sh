#!/bin/bash
set -x
DHCP_SERVER_IP=ieatrcx6786
MOUNTPOINT=/export/scripts/CLOUD/RHEL/
VCEN_HOSTNAME=141.137.215.157



echo "===================================================================="
echo "Deleting the DHCP client from MWS server"
echo "===================================================================="
#Delete the DHCP client if it exists
sshpass -p 'shroot12' ssh -o StrictHostKeyChecking=no root@$DHCP_SERVER_IP '
dhcp_client=`cat /etc/dhcp/dhcpd.conf | grep eniqs | wc -l`
echo $dhcp_client

if [ $dhcp_client -eq 1 ]
then
        /ericsson/kickstart/bin/manage_linux_dhcp_clients.bsh -a remove -c eniqs -N
else
        echo "There is no DHCP clinet in the server"
fi
'
echo "===================================================================="
echo "Successfully deleted the DHCP client from MWS server"
echo "===================================================================="


echo "===================================================================="
echo "Adding the DHCP client in MWS server"
echo "===================================================================="
#Add the DHCP client for ENIQS VM
sshpass -p 'shroot12' ssh -o StrictHostKeyChecking=no root@$DHCP_SERVER_IP '

find /JUMP/ENIQ_STATS/ENIQ_STATS/ -name ".eniq_stats_identity" | sort > /tmp/app_media
find /JUMP/LIN_MEDIA/ -name ".linux_boot_media" | sort > /tmp/kick_menu
find /JUMP/OM_LINUX_MEDIA/OM_LINUX_019_2/ -name ".om_linux_identity" | sort > /tmp/om_location
sleep 5
app_media=`grep -rn "SPRINT" /tmp/app_media | cut -d":" -f1 | xargs`
kick_menu=`grep -rn "1" /tmp/kick_menu | cut -d":" -f1 | xargs`
echo "********************************"
echo "$kick_menu"
echo "********************************"
om_location=`grep -rn "SPRINT" /tmp/om_location | cut -d":" -f1 | xargs`

/usr/bin/expect - <<EOF

spawn /ericsson/kickstart/bin/manage_linux_dhcp_clients.bsh -a add

expect "Enter the client hostname"
send "eniqs\r"

expect "Enter the IP address of eniqs"
send "192.168.0.51\r"

expect "Enter the IP Netmask of 192.168.0.51"
send "255.255.0.0\r"

expect "Please enter the MAC address for eniqs"
send "00:50:56:00:00:51\r"

expect "Do you want IPV6 enabled - YES/NO?"
send "NO\r"

expect "Enter the Timezone to be set for eniqs"
send "GB\r"

expect "Select the application type you wish to install on eniqs"
send "1\r"

expect "*"
send " "

expect "Select number of the area you wish to use"
send "$app_media\r"

expect "Select the kickstart you wish to use for eniqs"
send "$kick_menu\r"

expect "*"
send " "

expect "Select number of the O&M Linux media you wish to use"
send "$om_location\r"

expect "Select the install patch kickstart you wish to use for eniqs"
send "1\r"

expect "Select the display type of eniqs"
send "1\r"

expect "Enter the installation parameters for the client"
send "inst_type=eniq config=stats deployment=ft\r"

expect "Are you sure you wish to add this kickstart client? (Yes|No)"
send "Yes\r"

expect " "
send "\r"
EOF

mv /JUMP/LIN_MEDIA/1/kickstart/eniqs/01005056000051 /tmp/01005056000051_bak
sed -i 's/size=40960/size=20480/g' /tmp/01005056000051_bak
#sed -i 's/size=4096/size=4096/g' /tmp/01005056000051_bak
grep -v "logvol\ /var" /tmp/01005056000051_bak > /tmp/01005056000051_bak1
grep -v "logvol\ /Dump" /tmp/01005056000051_bak1 > /JUMP/LIN_MEDIA/1/kickstart/eniqs/01005056000051
echo "Succesfully changed the disk size in anaconda file"
'
echo "===================================================================="
echo "Successfully added the DHCP client in MWS server"
echo "===================================================================="
