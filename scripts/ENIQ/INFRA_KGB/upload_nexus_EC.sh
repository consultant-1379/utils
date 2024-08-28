#!bin/bash
set -e

usage ()
{
        echo ""
        echo  "Usage: $cmd [-thx] -r Rstate -m Module
        er -S sms_signum" 1>&2
        echo ""
        printf "  -r Rstate of Module"
        printf "  -m Module name"
        echo ""
        exit 1
}


while getopts r:m: opt;do
        case $opt in
            r) Rstate=$OPTARG
               ;;
            m) Module=$OPTARG
               ;;
        esac
done
shift `expr $OPTIND - 1`
[ "$Rstate" != "" ] || usage
[ "${Module}" != "" ] || usage



Base_Dir=/home/lciadm100/jenkins/workspace/INFRA_KGB_Nexus_Delivery_EC

if [ "$Module" == "storage" ]
then
	cd ${Base_Dir} 
	cd ../INFRA_KGB_Build_EC/rpm_files
	for i in *.rpm ; do
	    curl -v -u esjkadm100:Naples\!0512 --upload-file $i https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/eniqs-public/com/ericsson/eniq/stats/infra/rpm-list/storage/$Rstate/$i
	done
	cd ${Base_Dir}
	cd ../INFRA_KGB_Build_EC/tar_files 
	filename="${Module}_${Rstate}"
	curl -v -u esjkadm100:Naples\!0512 --upload-file $filename.tar.gz https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/eniqs-public/com/ericsson/eniq/stats/infra/tar-list/$Module/$Rstate/$filename.tar.gz
		

elif [ "$Module" == "omtools" ]
then
	cd ${Base_Dir} 
	cd ../INFRA_KGB_Build_EC/rpm_files
	curl -v -u esjkadm100:Naples\!0512 --upload-file ERICkickstart-$Rstate.rpm https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/eniqs-public/com/ericsson/eniq/stats/infra/rpm-list/ERICkickstart/$Rstate/ERICkickstart-$Rstate.rpm
	cd ${Base_Dir}
	cd ../INFRA_KGB_Build_EC/tar_files
	filename="${Module}_${Rstate}"
	curl -v -u esjkadm100:Naples\!0512 --upload-file $filename.tar.gz https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/eniqs-public/com/ericsson/eniq/stats/infra/tar-list/$Module/$Rstate/$filename.tar.gz

elif [ "$Module" == "security" ]	
then
	cd ${Base_Dir} 
	cd ../INFRA_KGB_Build_EC/rpm_files
	curl -v -u esjkadm100:Naples\!0512 --upload-file ERICnodehardening-$Rstate.rpm https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/eniqs-public/com/ericsson/eniq/stats/infra/rpm-list/ERICnodehardening/$Rstate/ERICnodehardening-$Rstate.rpm
	cd ${Base_Dir}
	cd ../INFRA_KGB_Build_EC/tar_files
	filename="${Module}_${Rstate}"
	curl -v -u esjkadm100:Naples\!0512 --upload-file $filename.tar.gz https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/eniqs-public/com/ericsson/eniq/stats/infra/tar-list/$Module/$Rstate/$filename.tar.gz

elif [ "$Module" == "bootstrap" ]
then
	cd ${Base_Dir}
	cd ../INFRA_KGB_Build_EC/tar_files
	filename="${Module}_${Rstate}"
	curl -v -u esjkadm100:Naples\!0512 --upload-file $filename.tar.gz https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/eniqs-public/com/ericsson/eniq/stats/infra/tar-list/$Module/$Rstate/$filename.tar.gz

elif [ "$Module" == "EMC" ]
then
	cd ${Base_Dir}
	cd ../INFRA_KGB_Build_EC/tar_files
	filename="${Module}_${Rstate}"
	curl -v -u esjkadm100:Naples\!0512 --upload-file $filename.tar.gz https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/eniqs-public/com/ericsson/eniq/stats/infra/tar-list/$Module/$Rstate/$filename.tar.gz
	
elif [ "$Module" == "HWcomm" ]
then
	cd ${Base_Dir}
	cd ../INFRA_KGB_Build_EC/tar_files
	filename="${Module}_${Rstate}"
	curl -v -u esjkadm100:Naples\!0512 --upload-file $filename.tar.gz https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/eniqs-public/com/ericsson/eniq/stats/infra/tar-list/$Module/$Rstate/$filename.tar.gz

elif [ "$Module" == "patch" ]
then
	cd ${Base_Dir}
	cd ../INFRA_KGB_Build_EC/tar_files
	filename="${Module}_${Rstate}"
	curl -v -u esjkadm100:Naples\!0512 --upload-file $filename.tar.gz https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/eniqs-public/com/ericsson/eniq/stats/infra/tar-list/$Module/$Rstate/$filename.tar.gz
	
else
		echo "Invalid Module Name Provided....!!!!!!!!!!!!!"
		false
fi	
