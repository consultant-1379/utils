#!/bin/bash
# ********************************************************************
# Ericsson Radio Systems AB                                     SCRIPT
# ********************************************************************
#
# Copyright (c) Ericsson Radio Systems AB 1999-2018 - All rights reserved.
#
# The copyright to the computer program(s) herein is the property
# of Ericsson Radio Systems AB, Sweden. The programs may be used 
# and/or copied only with the written permission from Ericsson Radio 
# Systems AB or in accordance with the terms and conditions stipulated 
# in the agreement/contract under which the program(s) have been 
# supplied.
#
# ********************************************************************
# Name    : install_PF_eniq.sh
# Date    : 01/14/2019
# Author  : zsxxhem
# Purpose : Script to install all platform modules on ENIQ Stats server
# Note    : Installation of modules can be done ONLY on Eniq Stats server (stats_coordinator/eniq_stats)
# Usage   : install_PF_eniq.sh <PackageDirectory> 
#
# ********************************************************************
#
#   Command Section
#
# ********************************************************************
AWK=/usr/bin/awk
CAT=/usr/bin/cat
CHMOD=/usr/bin/chmod
CP=/usr/bin/cp
CUT=/usr/bin/cut
ECHO=/usr/bin/echo
GREP=/usr/bin/grep
LS=/usr/bin/ls
MKDIR=/usr/bin/mkdir
RM=/usr/bin/rm
SUDO=/usr/bin/sudo
SYSTEMCTL=/usr/bin/systemctl
TR=/usr/bin/tr
UNZIP=/usr/bin/unzip

# ********************************************************************
#
#       Configuration Section
#
# ********************************************************************
# ENIQ BASE Directory
ENIQ_BASE_DIR=/eniq

# ENIQ SW Directory
ENIQ_SW_DIR=${ENIQ_BASE_DIR}/sw

# ENIQ SW Installer Directory
INSTALLER_DIR=${ENIQ_SW_DIR}/installer


#input
if [ $# -lt 1 ] ; then
	$ECHO "Usage: install_PF_eniq.sh <PackageDirectory>"
	exit 100
else
	PKG_REP=$1
fi


### Function: chk_create_dir ###
#
# Check/Create directories
#
# Arguments     : None
# Return Values : None
#
chk_create_dir()
{
	#create platform_installer directory
	if [ ! -d ${LOG_DIR}/platform_installer ] ; then
		$MKDIR -p ${LOG_DIR}/platform_installer
	fi
	
	#Create folder to track already executed platform SQL files
	if [ ! -d ${INSTALLER_DIR}/sqlfiles ] ; then
		$MKDIR -p ${INSTALLER_DIR}/sqlfiles
	fi

	#create temp directory
	TEM_DIR=/tmp/eniq.$$
	if [ -d ${TEM_DIR} ] ; then
	  $RM -rf ${TEM_DIR} >> /dev/null 2>&1
	fi
	$MKDIR ${TEM_DIR}
}

### Function: create_log_dirs ###
#
# Check/Create log directories
#
# Arguments     : None
# Return Values : None
#
create_log_dirs (){	
	if [ ! -d /eniq/log/sw_log/services ] ; then		
  		$MKDIR -p /eniq/log/sw_log/services
  		$ECHO "Created /eniq/log/sw_log/services directory"
	fi	
	if [ ! -d /eniq/log/sw_log/servicesaudit ] ; then
  		$MKDIR -p /eniq/log/sw_log/servicesaudit
  		$ECHO "Created /eniq/log/sw_log/servicesaudit directory"
	fi	
}

### Function: cleanup ###
#
# Removes path files of upgrade and install
#
# Arguments     : None
# Return Values : None
#
cleanup()
{
	if [ -f /var/tmp/FFU_upgrade_path_file ] ; then
		$RM -rf /var/tmp/FFU_upgrade_path_file
	fi
	if [ -f /var/tmp/FFU_install_path_file ] ; then
		$RM -rf /var/tmp/FFU_install_path_file
	fi
	
	#removes tmp directory
	$RM -rf ${TEM_DIR} >> /dev/null 2>&1
}

### Function: clean_installer_dir ###
#
# Removes older .zip or .tpi files present in eniq/sw/installer
#
# Arguments     : None
# Return Values : None
#
clean_installer_dir()
{
	#Ensure that there are no .zip or .tpi files present in eniq/sw/installer
	$ECHO "Removing old .zip and .tpi files from ${INSTALLER_DIR}"
	$RM -f ${INSTALLER_DIR}/*.tpi ${INSTALLER_DIR}/*.zip
	if [ $? -ne 0 ]; then
		_err_msg_ "Could not remove old .zip/.tpi files from ${INSTALLER_DIR}. Remove all .zip/.tpi files from ${INSTALLER_DIR} manually before continuing."
		abort_script "_err_msg_"
		exit 13
	fi
}

### Function: platform_installer ###
#
# Calls the platform_installer script for installation of a particular module
#
# Arguments     : $1 module to be installed
# Return Values : 0 on successful installation
#
platform_installer (){
    module=${1}
    $ECHO "Installing Package ${module}"
    if [[ "${module}" =~ .*\.zip$ ]] ; then
        zip_file=${module}
    else
        zip_file=$(${LS} ${module}*.zip)
    fi
	$ECHO "Install Task '${INSTALLER_DIR}/platform_installer ${zip_file}'"
    ${INSTALLER_DIR}/platform_installer ${zip_file}
    E=${?}
    if [ "${E}" -ne "0" ] ; then
        $ECHO "Failed to install/upgrade ${module}"
        exit 14
    fi
    return 0
}


### Function: install_runtime ###
#
# installation of runtime package
#
# Arguments     : None
# Return Values : None
#
install_runtime (){
	$LS -ltr ${PKG_REP}/runtime* >> /dev/null 2>&1
	
	if [ "$?" -ne "0" -a "${EU_TYPE}" = "eu" ]; then
		_err_msg_="runtime installation skipped as package doesn't exist in the EU upgrade"
		abort_script "$_err_msg_"
		exit 19
	fi
	
	arrayVal=($($LS ${PKG_REP}/runtime*))
	for i in ${arrayVal[@]}
	do
		$CP $i ${TEM_DIR}
		$UNZIP `$LS runtime*`
		$CHMOD u+x install_environment.sh
		./install_environment.sh -v
		E=${?}
		if [ "${E}" -ne "0" ] ; then
			exit 8
		fi
		$CHMOD u+x install_runtime.sh
		./install_runtime.sh -v
		E=${?}
		if [ "${E}" -ne "0" ] ; then
			exit 9
		fi
		$RM -rf ${TEM_DIR}/* >> /dev/null 2>&1
	done
}

### Function: install_installer ###
#
# installation of installer package
#
# Arguments     : None
# Return Values : None
#
install_installer (){
	$LS -ltr ${PKG_REP}/installer* >> /dev/null 2>&1
	
	if [ "$?" -ne "0" -a "${EU_TYPE}" = "eu" ]; then
		_err_msg_="installer installation skipped as package doesn't exist in the EU upgrade"
		abort_script "$_err_msg_"
		exit 20
	fi
	
	arrayVal=($($LS ${PKG_REP}/installer*))
	for i in ${arrayVal[@]}
	do
		$CP $i ${TEM_DIR}
		$UNZIP `$LS installer*`
		$CHMOD u+x install_installer.sh
		./install_installer.sh -v
		E=${?}
		if [ "${E}" -ne "0" ] ; then
			exit 10
		fi
		$RM -rf ${TEM_DIR}/* >> /dev/null 2>&1
	done
}

### Function: install_libs ###
#
# installation of libs package
#
# Arguments     : None
# Return Values : None
#
install_libs (){
	$LS -ltr ${PKG_REP}/libs_* >> /dev/null 2>&1
	
	if [ "$?" -ne "0" -a "${EU_TYPE}" = "eu" ]; then
		_err_msg_="libs installation skipped as package doesn't exist in the EU upgrade"
		abort_script "$_err_msg_"
		exit 21
	fi
	
	arrayVal=($($LS ${PKG_REP}/libs_*))
	for i in ${arrayVal[@]}
	do
		$CP $i ${TEM_DIR}
		zipfile=`$LS libs_*`
		$UNZIP ${zipfile}
		$CHMOD u+x install/install.bsh
		./install/install.bsh ${zipfile}
		E=${?}
		if [ "${E}" -ne "0" ] ; then
			exit 11
		fi
		$RM -rf ${TEM_DIR}/* >> /dev/null 2>&1
	done
}

### Function: install_eniq_config ###
#
# installation of eniq_config package
#
# Arguments     : None
# Return Values : None
#
install_eniq_config (){
	$LS -ltr ${PKG_REP}/eniq_config_* >> /dev/null 2>&1
	
	if [ "$?" -ne "0" -a "${EU_TYPE}" = "eu" ]; then
	    _err_msg_="eniq_config installation skipped as package doesn't exist in the EU upgrade"
	    abort_script "$_err_msg_"
	    exit 22
	fi
	
	arrayVal=($($LS ${PKG_REP}/eniq_config*))
	for i in ${arrayVal[@]}
	do
		$CP $i ${TEM_DIR}
		zipfile=`$LS eniq_config*`
		$UNZIP ${zipfile}
		$CHMOD u+x install_eniq_config.sh
		#Copy the script and make a backup.
		if [ -f ${ADMIN_BIN}/slot_configuration.ini ]; then
			$ECHO "Found a copy of slot_configuration.ini, so deleting it"
			$RM -f ${ADMIN_BIN}/slot_configuration.ini 
		fi
		$CP ${TEM_DIR}/slot_configuration.ini ${ADMIN_BIN}
		if [ -f ${ADMIN_BIN}/install_eniq_config.sh ]; then
			$ECHO "Found a copy of install_eniq_config.sh, so deleting it"
			$RM -f ${ADMIN_BIN}/install_eniq_config.sh 
		fi
		$CP ${TEM_DIR}/install_eniq_config.sh ${ADMIN_BIN}
	
		./install_eniq_config.sh ${SERVER_TYPE} -v
		E=${?}
		if [ "${E}" -ne "0" ] ; then
			exit 12
		fi
		$RM -rf ${TEM_DIR}/* >> /dev/null 2>&1
	done
}

# ********************************************************************
#
# 	Main body of program
#
# ********************************************************************

#create directories
chk_create_dir

$ECHO "Creating creating extra log directories...."
create_log_dirs
$ECHO "Finished creating extra log directories...."
	
#cleanup activity on installer dir
clean_installer_dir

$ECHO "Installing Platform modules.."
$CP ${PKG_REP}/*.zip ${INSTALLER_DIR}

$ECHO "Temp Directory : ${TEM_DIR}\n"

#installation of platform modules
pkg_list=($( ls ${PKG_REP} | grep zip ))

for pkg in ${pkg_list[@]} ; do
	echo -e "\n\n***$pkg Installation***\n\n"
	if [[ $pkg =~ "runtime" ]] ; then
		cd ${TEM_DIR}
		install_runtime
	elif [[ $pkg =~ "installer" ]] ; then
		cd ${TEM_DIR}
		install_installer
	elif [[ $pkg =~ "libs" ]] ; then
		cd ${TEM_DIR}
		install_libs
	elif [[ $pkg =~ "eniq_config" ]] ; then
		cd ${TEM_DIR}
		install_eniq_config
	else
		cd ${INSTALLER_DIR}
		platform_installer ${pkg}
		#install_module ${pkg}
	fi
done

#cleanup activity
cleanup