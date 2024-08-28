#!/bin/bash

sprint=$1
BUILD_USER_ID=$2
PWD=$3
product=CXP9022399
CT=/usr/atria/bin/cleartool
cep_pkg_dir="/home/$USER/eniq_events_releases"


function getCepPkg {
	cep_pkg=`ls -lrt $cep_pkg_dir | grep CEP_Platform | grep $rstate | tail -1 | awk '{print $9}'`
}

function deliverCep {
	echo "Running command: /vobs/dm_eniq/tools/scripts/deliver_eniq -auto events $sprint CI-DEV N $BUILD_USER_ID $product NONE $cep_pkg_dir/CEP_Platform_${rstate}.tar.gz"
	$CT setview -exec "/proj/eiffel013_config/fem101/jenkins_home/bin/lxb /vobs/dm_eniq/tools/scripts/deliver_eniq -auto events $sprint CI-DEV Y $BUILD_USER_ID $product NONE $cep_pkg_dir/CEP_Platform_${rstate}.tar.gz" deliver_ui
}

function getRstate {
	rstate=`cat $PWD/rstate.txt`
	echo "Deleting the temporary rstate.txt file..."
	rm -rf $PWD/rstate.txt
}

getRstate
getCepPkg
deliverCep

