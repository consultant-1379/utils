#!/bin/bash
#This script will create setting.xml and settings-security.xml file with user name esjkadm100 and encrypted password
#It will upload artifacts to nexus

M2_HOME=~/.m2
MVN_PATH=/usr/bin/mvn
USER_NAME=esjkadm100
NEXUS_URL=https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/assure-releases/
NEXUS_REPO_ID=assure-releases
ARTIFACT_GROUP_ID=com.ericsson.eniq.stats.nmi
ARTIFACT_VERSION=$2
ARTIFACT_ID=$1
LOGPATH=/tmp/maven_log
LINK_PATH=com/ericsson/eniq/stats/nmi

#If inputs/arguments less than 3 then script will exit with Usage message
#else it will create dir. to save log and copy checksum of file to log file
if [ $# -lt 3 ] ;
  then
    echo "Usage: $0 <ARTIFACT NAME> <RSTATE> </PATH/FILE_NAME>"
    exit 100
  else
    FILE_NAME=$(basename $3)
    mkdir -p $LOGPATH
    md5sum $FILE_NAME > $LOGPATH/checksum.$(date +%F).$FILE_NAME
fi

#Function: It will insert username lines in setting.xml before </servers>
insert_before_servers () {
sed -i '/<servers>/a     <server>\n    <id>assure-releases<\/id>\n    <username>esjkadm100<\/username>\n    <password>{SFSxjSfrUUkHDjXvDFwMb8mRKBk4abJHjk9WRtnoWC4=}<\/password>\n<\/server>' $M2_HOME/settings.xml
}

#Function: It will insert username lines in setting.xml before </settings>
insert_before_settings () {
sed -i '/<\/settings>/i   <servers>\n  <server>\n    <id>assure-releases<\/id>\n    <username>esjkadm100<\/username>\n    <password>{SFSxjSfrUUkHDjXvDFwMb8mRKBk4abJHjk9WRtnoWC4=}<\/password>\n  <\/server>\n<\/servers>' $M2_HOME/settings.xml
}

#Function: creating settings.xml file and copying username and encrypted password
setting_security_file () {
cat <<EOF > $M2_HOME/settings-security.xml
<settingsSecurity>
  <master>{3g2ExFC9KWYH8iAXowQZQOdUBL7loY90Zz4ROmh9Zhw=}</master>
</settingsSecurity>
EOF
}

#Function: creating settings-security.xml file and copying mastr encrypted password
setting_file () {
cat <<EOF > $M2_HOME/settings.xml
<?xml version="1.0"?>
<settings>
  <servers>
     <server>
        <id>assure-releases</id>
        <username>esjkadm100</username>
        <password>{SFSxjSfrUUkHDjXvDFwMb8mRKBk4abJHjk9WRtnoWC4=}</password>
    </server>
  </servers>
</settings>
EOF
}

#Function: If file successfully uploaded then it will disply below message
success () {
echo  CHECKSUM OF $FILE_NAME IS `awk '{print $1}' $LOGPATH/checksum.$(date +%F).$FILE_NAME` and saved in $LOGPATH/checksum.$(date +%F).$FILE_NAME
sleep 2s
echo $FILE_NAME is successfully uploaded by $USER_NAME and nexus link is $NEXUS_URL$LINK_PATH/$ARTIFACT_ID/$ARTIFACT_VERSION/
echo you can check maven_log from $LOGPATH/maven.$(date +%F).log
}

#Function: If file is unsuccess then it will disply below message
unsuccess () {
echo Failed to upload and please check the log from $LOGPATH/maven.$(date +%F).log and try again
}

#Function: upload artifacts to nexus and excution will save to $LOGPATH
maven_cmd () {
echo $FILE_NAME is uploading...
$MVN_PATH -B deploy:deploy-file -Durl=$NEXUS_URL -DrepositoryId=$NEXUS_REPO_ID -DgroupId=$ARTIFACT_GROUP_ID -Dversion=$ARTIFACT_VERSION -DartifactId=$ARTIFACT_ID  -Dfile=$FILE_NAME >> $LOGPATH/maven.$(date +%F).log
}

#Excution: If 2 files or not exist then it will create and upload artifact to nexus and maven log will save to $LOGPATH
if [[ ! -f $M2_HOME/settings.xml || ! -f $M2_HOME/settings-security.xml ]];
  then
    setting_file
    setting_security_file
    maven_cmd
      if [ $? = 0 ] ;
        then
          success
        else
          unsuccess
      fi
#Excution: If $USER_NAME exist then will upload artifact to nexus and maven log will save to $LOGPATH
  elif grep -wq "$USER_NAME" $M2_HOME/settings.xml ;
    then
      setting_security_file
      maven_cmd
        if [ $? = 0 ] ;
          then
            success
          else
            unsuccess
        fi
#Excution: If </settings> and </servers>section exist the will append $USER_NAME to settings.xml file and it will upload artifact to nexus and maven log will save to $LOGPATH
  elif grep -wq settings $M2_HOME/settings.xml ;
    then
      if grep -wq servers $M2_HOME/settings.xml ;
        then
          insert_before_servers
          setting_security_file
          maven_cmd
            if [ $? =  0 ] ;
              then
                success
              else
                unsuccess
            fi
#Excution: If </settings> section exsit and </servers> not exist then will append </servers> section and $USER_NAME & will upload artifact to nexus and maven log will save to $LOGPATH
        else
          insert_before_settings
          setting_security_file
          maven_cmd
            if [ $? = 0 ] ;
              then
                success
              else
                unsuccess
            fi
      fi
#Excution: If both sections not exist then its consider settings.xml file is empty and append all sections with $USER_NAME & will upload artifact to nexus and maven log will save to $LOGPATH
    else
      setting_file
      setting_security_file
      maven_cmd
        if [ $? = 0 ] ;
          then
            success
          else
            unsuccess
        fi
fi
#END
