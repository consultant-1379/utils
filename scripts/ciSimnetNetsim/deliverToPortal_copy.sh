#!/bin/bash
#Author : xjagset(jagadish.sethi@wipro.com)

#Initializing variable
EXPECT="/usr/bin/expect"
isNexusOnly=false
isCIFWKUpdateOnly=false
isDeliverToDropOnly=false
proxy_machine="eselivm2v214l.lmera.ericsson.se"
proxy_repo="releases"
machine="eselivm2v238l.lmera.ericsson.se"
repo="oss_releases"
platform="common"
product="Simnet/Netsim"
artifactName="simulations"
packageM2Type="zip"
adminUser="ossadm100"
adminPassword="eric@123"
taskOption="1"


#Usage function showing how to use the script
usage ()
{
  echo "Usage: $cmd [-D for Debug] [-g groupId] [-a artifactId] [-r Rstate_version] [-P product][-i intendedDrop] [-p filePath] [-f fileName] [-t packageType] [-u user] [-e email] [-o Task options either 1,2 or 3 ] " 1>&2
  printf " -D To run the script in DEBUG mode \n"
  printf " -g GroupId of the poackage eg: com.ericsson.oss.common \n"
  printf " -a Artifact Id or Name of the package eg : ERICsimnetWRAN_CXP9027449\n"
  printf " -r R-State of the package in version format eg : 1.1.3\n"
  printf " -P product eg: Netsim/Simnet\n"
  printf " -i Intended Drop eg: 16.0.1\n"
  printf " -p Absolute path or location of the package in the server eg: /home/ossrcdm/jagan\n"
  printf " -f file name which needs to be uploaded into nexus. Note it should be in .zip extension eg: simnet_WRAN.zip\n"
  printf " -t packageType or type of the file eg: zip\n"
  printf " -u signum ID of the user eg: xjagset\n"
  printf " -e email ID of the user eg: jagadish.sethi@wipro.com\n"
# printf " -n To upload the zip file into nexus \n"
# printf " -c To update the zip file information in the CIFWK portal \n"
# printf " -d To deliver to the drop\n"
  printf " -o Task Options either 1,2,or 3. Where \n"
  printf " 1 represents deliver to nexus and portal only\n"
  printf " 2 represents deliver to drop\n"
  printf " 3 represents deliver to nexus and drop\n"
  exit 1
}

# Parse arguments

[ $# -gt 0 ] || usage
while getopts ":g:a:r:P:i:p:f:t:u:e:o:ncdD" opt; do
  case $opt in
    g)
      groupId=$OPTARG
      ;;
    a)
      artifactId=$OPTARG
      ;;
    r)
      rstate_ver_fmt=$OPTARG
      ;;
    P)
      product=$OPTARG
      ;;
    i)
      intendedDrop=$OPTARG
      ;;
    p)
      filePath=$OPTARG
      ;;
    f)
      fileName=$OPTARG
      ;;
    t)
      packageM2Type=$OPTARG
      ;;
    u)
      user=$OPTARG
      ;;
    e)
      email=$OPTARG
      ;;
    o)
      taskOption=$OPTARG
      ;;
    D)
      echo "Script is running in DEBUG mode."
      set -xv
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      usage
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      usage
      exit 1
      ;;
  esac
done

# Initialising tasks
if [[ $taskOption -eq 1 ]]; then
  isNexusOnly=true
  isCIFWKUpdateOnly=true
  isDeliverToDropOnly=false
elif [[ $taskOption -eq 2 ]]; then
  isNexusOnly=false
  isCIFWKUpdateOnly=false
  isDeliverToDropOnly=true
elif [[ $taskOption -eq 3 ]]; then
  isNexusOnly=true
  isCIFWKUpdateOnly=true
  isDeliverToDropOnly=true
else 
  echo " -o Task Options either 1,2,or 3. Where \n"
  echo " 1 represents deliver to nexus and portal only\n"
  echo " 2 represents deliver to drop\n"
  echo " 3 represents deliver to nexus and drop\n"
  exit 1
fi



echo "RState in version is $rstate_ver_fmt"


#Uploading simulations to nexus

if [ -f $filePath/$fileName ];
then
   echo "File $filePath/$fileName exists"
else
echo "File $filePath/$fileName does not exists"
   exit 1

fi


if [[ "$isNexusOnly" == "true" ]];then
  $EXPECT - <<"EOF" $filePath $rstate_ver_fmt $artifactId $groupId $proxy_repo $fileName $proxy_machine $packageM2Type $adminUser $adminPassword
  set timeout 5400
  set multiPrompt "(>|%|#|\\|\$) $"
  set filepath [lindex $argv 0]
  set rstate [lindex $argv 1]
  set artifact [lindex $argv 2]
  set gid [lindex $argv 3]
  set repoid [lindex $argv 4]
  set filename [lindex $argv 5]
  set pmach [lindex $argv 6]
  set ptype [lindex $argv 7]
  set aUser [lindex $argv 8]
  set aPassword [lindex $argv 9]

  spawn scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no $filepath/$filename $aUser@selid1t600.lmera.ericsson.se:/tmp/oss
  expect {
    "assword:" { 
      send "$aPassword\r" 
      expect {
        timeout { send_user "\nFailed to get prompt\n"; exit 1 }
        eof { append output $expect_out(buffer); send_user "\n $output \n"; }
        -re $multiPrompt { append output $expect_out(buffer); send_user "\n$output \n"; }
        }
      }       
  timeout { send_user "\nFailed to get prompt\n"; exit 1 }
  eof { append output $expect_out(buffer); send_user "\n $output \n"; }
  -re $multiPrompt { append output $expect_out(buffer); send_user "\n$output \n"; }
}

  spawn ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no $aUser@selid1t600.lmera.ericsson.se "chmod 777 /tmp/oss/${filename};setenv JAVA_HOME /proj/ossrcdm/tools/jdk1.7.0_11-sol10sparc;/proj/ossrcdm/tools/apache-maven-3.0.5/bin/mvn deploy:deploy-file -Durl=http://$pmach:8081/nexus/content/repositories/releases/ -DrepositoryId=$repoid -DgroupId=$gid -DartifactId=$artifact -Dversion=$rstate -Dpackaging=$ptype -Dfile=/tmp/oss/$filename;rm /tmp/oss/$filename"
  expect {
    "assword:" { 
    send "$aPassword\r" 
    expect {
      timeout { send_user "\nFailed to get prompt\n"; exit 1 }
      eof { append output $expect_out(buffer); send_user "\n $output \n"; exit 1 }
      -re $multiPrompt { append output $expect_out(buffer); send_user "\n$output \n"; exit 1 }
      }
	  }	
  timeout { send_user "\nFailed to get prompt\n"; exit 1 }
  eof { append output $expect_out(buffer); send_user "\n $output \n"; exit 1 }
  -re $multiPrompt { append output $expect_out(buffer); send_user "\n$output \n"; exit 1 }
  }
EOF

fi


#Update in CIFWK portal

if [[ "$isCIFWKUpdateOnly" == "true" ]];then
  /usr/bin/wget -q -O - --no-check-certificate --post-data="packageName=${artifactId}&version=${rstate_ver_fmt}&groupId=${groupId}&signum=${user}&m2Type=${packageM2Type}&intendedDrop=${intendedDrop}&product=${product}&repository=${repo}&platform=${platform}&mediaCategory=3pp&autoDeliver=false" https://${machine}/cifwkPackageImport/

  if [ $? -ne 0 ]; then
    echo "Updation in CIFWK portal failed"
    exit 1;
  fi
  echo "Updation in CIFWK portal passed"
fi

#Deliver to drop

if [[ "$isDeliverToDropOnly" == "true" ]];then
  /usr/bin/wget -q -O - --no-check-certificate --post-data="packageName=${artifactId}&version=${rstate}&drop=${intendedDrop}&product=${product}&platform=${platform}&type=${packageM2Type}&email=${email}" https://$machine/deliverToDrop/

  if [ $? -ne 0 ]; then
    echo "Updation in deliver to drop failed"
    exit 1;
  fi
  echo "Updation in deliver to drop passed"

fi


