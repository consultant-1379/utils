#!/bin/bash
# ******************************************************************************************************
# Ericsson Radio Systems AB                                     SCRIPT
# ******************************************************************************************************

read -p "Enter the file path having the list of pkgs:" pkg_list_file_path
PKG_PATH=${pkg_list_file_path}
if [ ! -f ${PKG_PATH} ]; then
        echo "Given file ${PKG_PATH} does not exists... Aborting"
        exit 1
fi

if [ ! -r ${PKG_PATH} ] ; then
        echo "ERROR: ${PKG_PATH} file is not readable... Aborting"
        exit 2
fi

file_pkg_count=`cat ${PKG_PATH} |wc -l`

read -p "Enter the path having the Clear Case pkgs:" clear_case_pkg_path
if [ ! -d ${clear_case_pkg_path} ]; then
        echo "Given Clear case pkg path ${clear_case_pkg_path} does not exists... Aborting"
        exit 3
fi

cc_pkg_count=`ls ${clear_case_pkg_path} |grep tar | wc -l`

read -p "Enter the path having the GIT pkgs:" git_pkg_path
if [ ! -d ${git_pkg_path} ]; then
        echo "Given GIT pkg path ${git_pkg_path} does not exists... Aborting"
        exit 4
fi

git_pkg_count=`ls ${git_pkg_path} |grep tar | wc -l`

if [ ${cc_pkg_count} -ne ${git_pkg_count} ]; then
        echo "Clear case pkg count and GIT package count are not matching... Aborting"
        exit 5
fi

if [ ${file_pkg_count} -ne ${cc_pkg_count} ]; then
        echo "Pkg file list count and Clear case package count are not matching... Aborting"
        exit 6
fi

if [ ${file_pkg_count} -ne ${git_pkg_count} ]; then
        echo "Pkg file list count and GIT package count are not matching... Aborting"
        exit 7
fi
dir=`pwd`
echo "`date '+%y%m%d_%H%M%S'` : Started differentiating the Clear Case pkgs with GIT pkgs"
mkdir -p /var/tmp/cc_diff
mkdir -p /var/tmp/git_diff

while read line; do
                cp ${clear_case_pkg_path}/${line}* /var/tmp/cc_diff/
        cp ${git_pkg_path}/${line}* /var/tmp/git_diff/
        cd /var/tmp/cc_diff/
                if [ ${line} == "Packages_INC" ]; then
                                unzip ${line}*zip > /dev/null
                                rm -f ${line}*zip
                                count_cc=`find . | grep -v .settings |wc -l`
                                cd /var/tmp/git_diff
                                unzip ${line}*zip > /dev/null
                                rm -f ${line}*zip
        else
                                tar -xvf ${line}*tar.gz > /dev/null
                                rm -f ${line}*tar.gz
                                count_cc=`find . | grep -v .settings |wc -l`
                                cd /var/tmp/git_diff
                                tar -xvf ${line}*tar.gz > /dev/null
                                rm -f ${line}*tar.gz
                fi
        count_git=`find . |grep -v .gitkeep |grep -v .settings |wc -l`
        if [ ${count_cc} -ne ${count_git} ]; then
                echo "There is a total file count difference in GIT and CC pkgs for pkg ${line}, continuing to next pkg"
                continue
        else
                echo "Verifying the file content except .gitkeep files for pkg ${line}"
                for file in `find . -type f |grep -v .gitkeep |grep -v .settings |grep -v "version.properties" |grep -v "/version" |grep -v "TPIDE_BOIntf.pdb" |grep -v "TPIDE_BOIntf.exe" |grep -v .jar |grep -v .tar`; do
                                                echo "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
                                                cmp ${file} /var/tmp/cc_diff/${file} > /dev/null
                                                if [ $? -ne 0 ]; then
                                                        echo "Difference found in file ${file} for pkg ${line}, continuing"
                                                        continue
                                                fi
                                done
                                if [ ${line} != "NASd" ] && [ ${line} != "ENIQ_Installation" ]; then
                                        for tarFile in `find . |grep -v .settings |grep .tar.gz`; do
                                                echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
                                                diff <(tar -tvf ${tarFile} | rev | cut -d\/ -f1 | rev |grep -v "/version") <(tar -tvf /var/tmp/cc_diff/${tarFile} | rev | cut -d\/ -f1 | rev |grep -v "/version") > /dev/null
                                                if [ $? -ne 0 ]; then
                                                        echo "Difference found in file ${tarFile} for pkg ${line}, continuing"
                                                        continue
                                                fi
                                        done
                                fi
        fi
                if [ ${line} == "ENIQ_Installation" ]; then
                                cd /var/tmp/cc_diff/install
                                for tarFile in `find . |grep -v .settings |grep .tar.gz`; do
                                                tar -xvf ${tarFile} > /dev/null
                                                rm -rf ${tarFile}
                                                tar_cc_count=`find . |grep -v .gitkeep |grep -v .settings|wc -l`
                                                cd /var/tmp/git_diff/install
                                                tar -xvf ${tarFile} > /dev/null
                                                rm -rf ${tarFile}
                                                tar_git_count=`find . |grep -v .gitkeep |grep -v .settings|wc -l`
                                                if [ ${tar_cc_count} -ne ${tar_git_count} ]; then
                                                                echo "There is a total file count difference in tar file of GIT and CC pkgs for pkg ${line}, continuing to next pkg"
                                                                continue
                                                fi
                                                echo "**********************************************************"
                                                for file in `find . -type f |grep -v .gitkeep |grep -v .settings |grep -v "version.properties" |grep -v "/version" |grep -v "TPIDE_BOIntf.pdb" |grep -v "TPIDE_BOIntf.exe" |grep -v .jar |grep -v .war`; do
                                                        cmp ${file} /var/tmp/cc_diff/install/${file} > /dev/null
                                                        if [ $? -ne 0 ]; then
                                                                echo "Difference found in file ${file} for pkg ${line}, continuing"
                                                                continue
                                                        fi
                                                done
                                done
                fi
                if [ ${line} == "NASd" ]; then
                                cd /var/tmp/cc_diff/NASd
                                for tarFile in `find . |grep -v .settings |grep .tar.gz`; do
                                                tar -xvf ${tarFile} > /dev/null
                                                rm -rf ${tarFile}
                                                tar_cc_count=`find . |grep -v .gitkeep |grep -v .settings|wc -l`
                                                cd /var/tmp/git_diff/NASd
                                                tar -xvf ${tarFile} > /dev/null
                                                rm -rf ${tarFile}
                                                tar_git_count=`find . |grep -v .gitkeep |grep -v .settings|wc -l`
                                                if [ ${tar_cc_count} -ne ${tar_git_count} ]; then
                                                                echo "There is a total file count difference in tar file of GIT and CC pkgs for pkg ${line}, continuing to next pkg"
                                                                continue
                                                fi

                                                for file in `find . -type f |grep -v .gitkeep |grep -v .settings |grep -v "version.properties" |grep -v "cc_list" |grep -v "pkginfo" |grep -v "TPIDE_BOIntf.exe" |grep -v .jar |grep -v .war`; do
                                                        echo "###########################################################################"
                                                                                                                cmp ${file} /var/tmp/cc_diff/NASd/${file} > /dev/null
                                                        if [ $? -ne 0 ]; then
                                                                echo "Difference found in file inside tar ${file} for pkg ${line}, continuing"
                                                                continue
                                                        fi
                                                done
                                done
                fi
        rm -rf /var/tmp/cc_diff
        rm -rf /var/tmp/git_diff
done < ${PKG_PATH}

cd ${dir}
rm -rf /var/tmp/cc_diff
rm -rf /var/tmp/git_diff

echo "`date '+%y%m%d_%H%M%S'` : Finished differentiating the Clear Case pkgs with GIT pkgs"

