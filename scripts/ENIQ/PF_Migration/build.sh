#!bin/bash

echo " "
echo ".... CLONING ALARM REPO ..."
echo " "
##### ALARM ######

cd /proj/eiffel004_config_fem160/

if [ -d "/proj/eiffel004_config_fem160/CI-Training-repo/" ]
then
        cd /proj/eiffel004_config_fem160/CI-Training-repo/
        git pull

else
	git clone ssh://esjkadm100@gerrit.ericsson.se:29418/OSS/ENIQ-CR-Parent/CI-Training-repo && scp -p -P 29418 esjkadm100@gerrit.ericsson.se:hooks/commit-msg CI-Training-repo/.git/hooks/
	cd /proj/eiffel004_config_fem160/CI-Training-repo/
	git checkout 20.2_ConsolidationCXP
fi

unset LS_COLORS
whoami
hostname

getArray() {
    array=() # Create array
    while IFS= read -r line # Read a line
    do
        array+=("$line") # Append line to the array
    done < "$1"
}

getArray "/proj/eiffel004_config_fem160/newfile.txt"

for e in "${array[@]}"
do
    cd /proj/eiffel004_config_fem160/
    
echo ".... CLONING DEPENDANCY $e JAR FILE ...."
echo " "

if [ -d "/proj/eiffel004_config_fem160/$e/" ]
then
	cd /proj/eiffel004_config_fem160/$e/
	git pull
    
else
	git clone ssh://esjkadm100@gerrit.ericsson.se:29418/OSS/ENIQ-CR-Parent/com.ericsson.eniq.stats.plat/$e && scp -p -P 29418 esjkadm100@gerrit.ericsson.se:hooks/commit-msg $e/.git/hooks/
    cd /proj/eiffel004_config_fem160/$e/
    git checkout 20.2_ConsolidationCXP
fi
done

echo ".... CLONING DEPENDANCY ENGINE JAR FILE ...."
echo " "

### ENGINE #####
cd /proj/eiffel004_config_fem160/

if [ -d "/proj/eiffel004_config_fem160/Engine_Dummy" ]
then
	cd /proj/eiffel004_config_fem160/Engine_Dummy
	git pull
    
else
	git clone ssh://esjkadm100@gerrit.ericsson.se:29418/OSS/ENIQ-CR-Parent/Engine_Dummy && scp -p -P 29418 esjkadm100@gerrit.ericsson.se:hooks/commit-msg Engine_Dummy/.git/hooks/
    cd /proj/eiffel004_config_fem160/Engine_Dummy
    git checkout 20.2_ConsolidationCXP
fi


echo ".... CLONING DEPENDANCY COMMON JAR FILE ...."
echo " "
##### COMMON ######

cd /proj/eiffel004_config_fem160/

if [ -d "/proj/eiffel004_config_fem160/Dummy_Repo_For_Build/" ]
then
	cd /proj/eiffel004_config_fem160/Dummy_Repo_For_Build/
	git pull
    
else
	git clone ssh://esjkadm100@gerrit.ericsson.se:29418/OSS/ENIQ-CR-Parent/Dummy_Repo_For_Build && scp -p -P 29418 esjkadm100@gerrit.ericsson.se:hooks/commit-msg Dummy_Repo_For_Build/.git/hooks/
    cd /proj/eiffel004_config_fem160/Dummy_Repo_For_Build/
    git checkout 20.2_ConsolidationCXP
fi

#/proj/eiffel004_config_fem160/test_ant/ant/bin/ant -version
echo ".... BUILDING ALARM ...."
/proj/jkadm100/bin/lxb "/proj/eiffel004_config_fem160/test_ant/ant/bin/ant -buildfile /proj/eiffel004_config_fem160/ant_unsigned.xml -Dpackage.build.file=/proj/eiffel004_config_fem160/CI-Training-repo/dev/build/build.xml -Dbuild.label=CXP9019718-R19E01_EC99 -Dbuild.revision=R19E01_EC99 -Dproject.root=/proj -Dexclude_files='dep_arch/**,build/**,src/**,doc/**,test/**,jar/**,template/**,.classpath,.project' -Dproduct.number=CXP9019718 -Dlogname=esjkadm100 -Dpackage_dir=/proj/eiffel004_config_fem160/CI-Training-repo/dev -Dpackage=alarm -Djar_dir=/proj/eiffel004_config_fem160/CI-Training-repo/ -Ddelivery_dir=/proj/eiffel004_config_fem160/CI-Training-repo/ -Djobname=eniq_alarm -Dbranch=eniq_stats_20.2_consolidation"


