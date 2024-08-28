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
# Name    : FULL_KGB_NMI_Install_Packages.sh
# Date    : 05/20/2019
# Author  : xathira
# Purpose : Script to install all NMI modules on ENIQ Stats server
# Note    : Installation of modules can be done ONLY on Eniq Stats server (stats_coordinator/eniq_stats)
# Usage   : FULL_KGB_NMI_Install_Packages.sh <PackageDirectory>
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
CD=/usr/bin/cd
CUT=/usr/bin/cut
ECHO=/usr/bin/echo
GREP=/usr/bin/grep
LS=/usr/bin/ls
PWD=/usr/bin/pwd
MKDIR=/usr/bin/mkdir
RM=/usr/bin/rm
SUDO=/usr/bin/sudo
SYSTEMCTL=/usr/bin/systemctl
TR=/usr/bin/tr
GUNZIP=/usr/bin/gunzip
MV=/usr/bin/mv

#input
if [ $# -lt 1 ] ; then
        $ECHO "Usage: FULL_KGB_NMI_Install_Packages.sh <PackageDirectory>"
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

        #create temp directory
        TEM_DIR=/tmp/eniq.$$
        if [ -d ${TEM_DIR} ] ; then
          $RM -rf ${TEM_DIR} >> /dev/null 2>&1
        fi
        $MKDIR ${TEM_DIR}
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
        #removes tmp directory
        $RM -rf ${TEM_DIR} >> /dev/null 2>&1
}

### Function: install_NASd ###
#
# Installation of NASd package
#
# Arguments     : None
# Return Values : None
#
install_NASd (){
        $LS -ltr ${PKG_REP}/NASd* >> /dev/null 2>&1

        if [ "$?" -ne "0" -a "${EU_TYPE}" = "eu" ]; then
                _err_msg_="runtime installation skipped as package doesn't exist in the EU upgrade"
                abort_script "$_err_msg_"
                exit 19
        fi

        arrayVal=($($LS ${PKG_REP}/NASd*))
        echo $arrayVal
        for i in ${arrayVal[@]}
        do
                $CP $i ${TEM_DIR}
                $MKDIR -p ${TEM_DIR}/applications
                $MV NASd* ${TEM_DIR}/applications
                #$CD ${TEM_DIR}
                #$CD applications
                cd ${TEM_DIR}/applications
                echo `pwd`
                $GUNZIP -c NASd* |tar xvf -
                E=${?}
                if [ "${E}" -ne "0" ] ; then
                        exit 8
                fi
                #$CHMOD u+x install_runtime.sh
                cd /eniq/installation/core_install/bin
                ./eniq_core_install.bsh -s install_nasd -d ${TEM_DIR}
                E=${?}
                if [ "${E}" -ne "0" ] ; then
                        exit 9
                fi
                $RM -rf ${TEM_DIR}/* >> /dev/null 2>&1
        done
}

### Function: install_sentinel ###
#
# Installation of sentinel package
#
# Arguments     : None
# Return Values : None
#
install_sentinel (){
        $LS -ltr ${PKG_REP}/sentinel* >> /dev/null 2>&1

        if [ "$?" -ne "0" -a "${EU_TYPE}" = "eu" ]; then
                _err_msg_="runtime installation skipped as package doesn't exist in the EU upgrade"
                abort_script "$_err_msg_"
                exit 19
        fi

        arrayVal=($($LS ${PKG_REP}/sentinel*))
        echo $arrayVal
        for i in ${arrayVal[@]}
        do
                $CP $i ${TEM_DIR}
                $MKDIR -p ${TEM_DIR}/applications
                $MV sentinel* ${TEM_DIR}/applications
                #$CD ${TEM_DIR}
                #$CD applications
                cd ${TEM_DIR}/applications
                echo `pwd`
                $GUNZIP -c sentinel* |tar xvf -
                E=${?}
                if [ "${E}" -ne "0" ] ; then
                        exit 8
                fi
                #$CHMOD u+x install_runtime.sh
                cd /eniq/installation/core_install/bin
                ./eniq_core_install.bsh -s install_sentinel -d ${TEM_DIR}
                E=${?}
                if [ "${E}" -ne "0" ] ; then
                        exit 9
                fi
                $RM -rf ${TEM_DIR}/* >> /dev/null 2>&1
        done
}

### Function: install_sql_anywhere ###
#
# Installation of sql_anywhere package
#
# Arguments     : None
# Return Values : None
#
install_sql_anywhere (){
        $LS -ltr ${PKG_REP}/sql_anywhere* >> /dev/null 2>&1

        if [ "$?" -ne "0" -a "${EU_TYPE}" = "eu" ]; then
                _err_msg_="runtime installation skipped as package doesn't exist in the EU upgrade"
                abort_script "$_err_msg_"
                exit 19
        fi

        arrayVal=($($LS ${PKG_REP}/sql_anywhere*))
        echo $arrayVal
        for i in ${arrayVal[@]}
        do
                $CP $i ${TEM_DIR}
                $MKDIR -p ${TEM_DIR}/applications
                $MV sql_anywhere* ${TEM_DIR}/applications
                #$CD ${TEM_DIR}
                #$CD applications
                cd ${TEM_DIR}/applications
                echo `pwd`
                $GUNZIP -c sql_anywhere* |tar xvf -
                E=${?}
                if [ "${E}" -ne "0" ] ; then
                        exit 8
                fi
                #$CHMOD u+x install_runtime.sh
                cd /eniq/installation/core_install/bin
                ./eniq_core_install.bsh -s install_sybase_asa -d ${TEM_DIR}
                E=${?}
                if [ "${E}" -ne "0" ] ; then
                        exit 9
                fi
                $RM -rf ${TEM_DIR}/* >> /dev/null 2>&1
        done
}

### Function: install_sybase_iq ###
#
# Installation of sybase_iq package
#
# Arguments     : None
# Return Values : None
#
install_sybase_iq (){
        $LS -ltr ${PKG_REP}/sybase_iq* >> /dev/null 2>&1

        if [ "$?" -ne "0" -a "${EU_TYPE}" = "eu" ]; then
                _err_msg_="runtime installation skipped as package doesn't exist in the EU upgrade"
                abort_script "$_err_msg_"
                exit 19
        fi

        arrayVal=($($LS ${PKG_REP}/sybase_iq*))
        echo $arrayVal
        for i in ${arrayVal[@]}
        do
                $CP $i ${TEM_DIR}
                $MKDIR -p ${TEM_DIR}/applications
                $MV sybase_iq* ${TEM_DIR}/applications
                #$CD ${TEM_DIR}
                #$CD applications
                cd ${TEM_DIR}/applications
                echo `pwd`
                $GUNZIP -c sybase_iq* |tar xvf -
                E=${?}
                if [ "${E}" -ne "0" ] ; then
                        exit 8
                fi
                #$CHMOD u+x install_runtime.sh
                cd /eniq/installation/core_install/bin
                ./eniq_core_install.bsh -s install_sybaseiq -d ${TEM_DIR}
                E=${?}
                if [ "${E}" -ne "0" ] ; then
                        exit 9
                fi
                $RM -rf ${TEM_DIR}/* >> /dev/null 2>&1
        done
}

# ********************************************************************
#
#       Main body of program
#
# ********************************************************************

#create directories
chk_create_dir

#installation of NMI modules
pkg_list=($( ls ${PKG_REP} | grep tar.gz ))

for pkg in ${pkg_list[@]} ; do
        echo -e "\n\n***$pkg Installation***\n\n"
        if [[ $pkg =~ "NASd" ]] ; then
                cd ${TEM_DIR}
                install_NASd
        elif [[ $pkg =~ "ENIQ_Bootstrap" ]] ; then
                cd ${TEM_DIR}
                install_ENIQ_Bootstrap
        elif [[ $pkg =~ "sentinel" ]] ; then
                cd ${TEM_DIR}
                install_sentinel
        elif [[ $pkg =~ "sql_anywhere" ]] ; then
                cd ${TEM_DIR}
                install_sql_anywhere
        elif [[ $pkg =~ "sybase_iq" ]] ; then
                cd ${TEM_DIR}
                install_sybase_iq
        else
                echo "Not NMI package\n"

        fi

done

#cleanup activity
cleanup