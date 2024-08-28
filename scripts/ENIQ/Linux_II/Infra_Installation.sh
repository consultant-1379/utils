#!/bin/bash
DHCP_SERVER_IP=ieatmws300
MOUNTPOINT=/export/scripts/CLOUD/RHEL/
VCEN_HOSTNAME=141.137.215.157


echo "===================================================================="
echo "Resetting the ENIQS VM"
echo "===================================================================="
curl --insecure --write-out "\n%{http_code}\n" https://atvphspp17.athtem.eei.ericsson.se/Vms/reset_api/vm_name:eniqs.xml


echo "===================================================================="
echo "Installing VMWARE Tools on the gateway VM"
echo "===================================================================="
#Install VMWARE Tools on the gateway VM
ssh -qt $HOSTNAME -l root "$MOUNTPOINT/bin/inst_vmtools.bsh -m $MOUNTPOINT -d no" 2>/dev/null
echo "===================================================================="
echo "Successfully installed VMWARE Tools on the gateway VM"
echo "===================================================================="


echo "===================================================================="
echo "Setting the boot order to Network"
echo "===================================================================="
curl --insecure --write-out "\n%{http_code}\n" https://atvphspp17.athtem.eei.ericsson.se/Vms/set_boot_device_api/boot_devices:net/vm_name:eniqs.xml
echo "===================================================================="
echo "Successfully changed the boot order to Network"
echo "===================================================================="


echo "===================================================================="
echo "Power OFF the ENIQS VM"
echo "===================================================================="
curl --insecure --write-out "\n%{http_code}\n" https://atvphspp17.athtem.eei.ericsson.se/Vms/poweroff_api/vm_name:eniqs.xml
echo "===================================================================="
echo "Successfully powered OFF the ENIQS VM"
echo "===================================================================="


echo "===================================================================="
echo "Adding the Virtual Serial Port(VSP) to ENIQS VM"
echo "===================================================================="
netstat -ntlp |grep 5000 | awk '{print $4}' | cut -d":" -f2 | sort > /tmp/vsp_before_add
vapp_vms_list=`curl --insecure --write-out "\n%{http_code}\n" https://atvphspp17.athtem.eei.ericsson.se/Vms/list_vms_raw_api/`
eniqs_vm_id=`echo $vapp_vms_list | cut -d";" -f2`
HOSTNAME=$HOSTNAME
echo "/export/scripts/CLOUD/RHEL/bin/run_vcli_command.sh -r '/export/scripts/CLOUD/RHEL/bin/serial.pl --op add --vmname '\''$eniqs_vm_id'\'' --vspc '\''$HOSTNAME'\''' -v $VCEN_HOSTNAME" > /tmp/vsp.sh
ssh root@$HOSTNAME 'bash /tmp/vsp.sh'
echo "===================================================================="
echo "Successfully added the Virtual Serial Port(VSP) to ENIQS VM"
echo "===================================================================="


echo "===================================================================="
echo "Power ON the ENIQS VM"
echo "===================================================================="
curl --insecure --write-out "\n%{http_code}\n" https://atvphspp17.athtem.eei.ericsson.se/Vms/poweron_api/vm_name:eniqs.xml
echo "===================================================================="
echo "Successfully powered ON the ENIQS VM"
echo "===================================================================="


echo "===================================================================="
echo "Setting the boot order to Disk"
echo "===================================================================="
sleep 20
curl --insecure --write-out "\n%{http_code}\n" https://atvphspp17.athtem.eei.ericsson.se/Vms/set_boot_device_api/boot_devices:hd/vm_name:eniqs.xml
echo "===================================================================="
echo "Successfully changed the boot order to Disk"
echo "===================================================================="


echo "===================================================================="
echo "Checking virtual serial port settings on ENIQS, please wait....:"
echo "===================================================================="
netstat -ntlp |grep 5000 | awk '{print $4}' | cut -d":" -f2 | sort > /tmp/vsp_after_add
VSP=`diff /tmp/vsp_after_add /tmp/vsp_before_add | xargs | cut -d"<" -f2 | xargs`
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
set timeout 2500

spawn telnet \$hostname $VSP

expect "Infra Installation"
send "\r"

EOF

echo "===================================================================="
echo "Connecting to the ENIQS through VSP"
echo "===================================================================="
