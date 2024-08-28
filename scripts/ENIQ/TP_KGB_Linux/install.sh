#!/usr/bin/bash
#set -x
### Below function is to install all the Tech pack which got transferred w.r.to Check-ins...
export CONF_DIR=/eniq/sw/conf
#/usr/bin/bash /eniq/admin/bin/eniq_services_deploy.bsh /tmp/eniq_service_deploy.log
echo "The CONF_DIR value is : $CONF_DIR"

file="/eniq/sw/installer/Tech_pack_order.txt"
Installer="/eniq/sw/installer/tp_installer"
Path="/eniq/sw/installer/"
cd /eniq/sw/installer

if [ -f /eniq/sw/installer/install_lockfile ]
then
	echo "/eniq/sw/installer/install_lockfile file found and hence deleting it to proceed further"
	rm -rf /eniq/sw/installer/install_lockfile
else
	echo "We dont have /eniq/sw/installer/install_lockfile :) :) :) "
fi

if [ ! -f "$file" ]
then
        echo "The $file doesn't exists.....!!!"
else
	echo "The info from Tech_pack_order.txt is :"
	cat $file
	cd $Path
        while read line           
        do           
        echo  "Tech Pack name is: $line"        
        Name=`ls /eniq/sw/installer/ | grep $line | grep tpi`    
        echo " Installing $Name tech pack" 
	pkg=$(echo $Name | rev | cut -d_ -f2 | rev)
	result=$(echo $Name | sed 's/_'$pkg'.*//')
	echo "$result";
        #su dcuser -c "$Installer -p . -t $Path/$Name" 
	$Installer -p $Path -t $result
	sleep 3
        done < $file
fi


