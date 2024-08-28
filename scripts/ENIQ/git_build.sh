#!/bin/bash

if [ "$1" == "" ]; then
    echo usage: $0 \<Branch\> \<PWD\>
    exit -1
else
        theDate=\#$(date +"%c")
        product=CXP9022399
        branch=$1
	PWD=$2
        revision="R3A"
fi

TAR_DIR="$PWD/tar"
TAR_ROOT="$TAR_DIR"
RPM_DIR="$TAR_ROOT/packages"
RPM_FILE="$PWD/rpm/*.rpm"
RPM_FILE1="$PWD/rpm/jdk-7u80-linux-x64.rpm"
TAR_NAME="CEP_Platform_${rstate}.tar.gz"
git="/app/git/1.8.4/LMWP3/bin/git"

function getRstate {

	if git tag | grep $product-$revision; then
		rstate=`git tag | grep $revision | tail -1 | sed s/.*-// | perl -nle 'sub nxt{$_=shift;$l=length$_;sprintf"%0${l}d",++$_}print $1.nxt($2) if/^(.*?)(\d+$)/';`
	else
       		ammendment_level=01
        	rstate=$revision$ammendment_level
	fi
	echo "Building R-State:$rstate"

}

function cleanup {
        if [ -d $TAR_DIR ] ; then
          echo "removing $TAR_DIR"
          rm -rf $TAR_DIR
        fi
}

function createTar {
    mkdir $TAR_DIR
    #mkdir $TAR_ROOT
    mkdir $RPM_DIR

    echo "Copying $RPM_FILE into $RPM_DIR"
    cp $RPM_FILE $RPM_DIR
	#cp $RPM_FILE1 $RPM_DIR
    #cd $TAR_DIR
	cd $TAR_ROOT
    tar -czvf $PWD/CEP_Platform_${rstate}.tar.gz packages
    echo "Copying tar file into /home/$USER/eniq_events_releases"
    cp $PWD/CEP_Platform_${rstate}.tar.gz /home/$USER/eniq_events_releases
}

cleanup
git clean -df
git checkout $branch
git pull

getRstate


git tag $product-$rstate
git pull
git push --tag origin $branch

echo "Creating tar file..."
createTar

if [ -a $PWD/rstate.txt ]
then
        rm -rf $PWD/rstate.txt
fi

echo "Creating temporary rstate file for auto-delivery. The file will contain $rstate"
touch $PWD/rstate.txt
echo $rstate >> $PWD/rstate.txt
