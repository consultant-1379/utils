#!/bin/bash
# ********************************************************************
# Name    : nexus_upload.sh
# Date    : 03-May-2019
# Author  : zrddkpp
# Purpose : This script will upload artifacts to "arm104" nexus to with "assure-releases" repo id by user nmiteam and with encrypted password
# Usage   : nexus_upload.sh <RSTATE> </PATH/FILE_NAME>
# ********************************************************************


#####################################################################################################
##                  DECLARING VARIABLES START                                                  ##
#####################################################################################################

M2_HOME=~/.m2
MVN_PATH=/tmp/apache-maven-3.0.5/bin/mvn
USER_NAME=nmiteam
NEXUS_URL=https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/assure-releases/
NEXUS_REPO_ID=assure-releases
ARTIFACT_VERSION=$2
SHIPMENT=$1
SCRIPT_NAME=$(basename $0)
SCRIPT_NAME="${SCRIPT_NAME%.*}"
ARTIFACT_GROUP_ID=com.ericsson.eniq.stats.nmi.${SHIPMENT//./_}
LOGPATH=/tmp/${SCRIPT_NAME}_log
LOG_FILE=$LOGPATH/$(date +%F).log
LINK_PATH=com/ericsson/eniq/stats/nmi/${SHIPMENT//./_}
UEP={5D3lAgKYiHgHcZ51FFhETCFvPlIatXrcRHHGkHPYHA8=}
MEP={3g2ExFC9KWYH8iAXowQZQOdUBL7loY90Zz4ROmh9Zhw=}

[ ! -d $LOGPATH ] &&  mkdir $LOGPATH

#####################################################################################################
##                  DECLARING VARIABLES END                                                  ##
#####################################################################################################

#####################################################################################################
#                            DECLARING  LOGGER FUNCTIONS START                                     ##
#####################################################################################################

SCRIPTENTRY(){
  timeAndDate=`date`
  script_name=`basename "$0"`
  script_name="${script_name%.*}"
  echo "[$timeAndDate] [DEBUG]  : $script_name $FUNCNAME" >> $LOG_FILE
}

ENTRY(){
  local cfn="${FUNCNAME[1]}"
  timeAndDate=`date`
  echo "[$timeAndDate] [DEBUG]  : $cfn $FUNCNAME" >> $LOG_FILE
}

INFO(){
  local msg="$1"
  timeAndDate=`date`
  echo "[$timeAndDate] [INFO]   : $msg" |& tee -a $LOG_FILE
}

DEBUG(){
  local msg="$1"
  timeAndDate=`date`
  echo "[$timeAndDate] [DEBUG]  : $msg" >> $LOG_FILE
}


SUCCESS(){
  local function_name="${FUNCNAME[1]}"
  local msg="$1"
  timeAndDate=`date`
  echo "[$timeAndDate] [SUCCESS]  : $msg" |& tee -a  $LOG_FILE
}

ERROR(){
  local function_name="${FUNCNAME[1]}"
  local msg="$1"
  timeAndDate=`date`
  echo "[$timeAndDate] [ERROR]  : $msg" |& tee -a  $LOG_FILE
}

EXIT(){
  local cfn="${FUNCNAME[1]}"
  timeAndDate=`date`
  echo "[$timeAndDate] [DEBUG]  : $cfn $FUNCNAME" >> $LOG_FILE
}

SCRIPTEXIT(){
  echo "[$timeAndDate] [DEBUG]  : $script_name $FUNCNAME" >> $LOG_FILE
}


#####################################################################################################
##                  DECLARING LOGGER FUNCTION END                                                  ##
#####################################################################################################

SCRIPTENTRY

# ********************************************************************
#Validating arguments/inputs &  exit with Usage message
#else it will create dir. to save log and copy checksum of file to log file
#  ********************************************************************

if [[ $# -ne 3 || ! -f $3 || $ARTIFACT_VERSION != R* ]] ;
  then
    INFO "Usage: $0 SHIPMENT RSTATE /PATH/FILE_NAME"
    DEBUG "script exited with Usage message"
    SCRIPTEXIT
    exit 100
  else
    ENTRY
    FILE_NAME=$(basename $3)
    ARTIFACT_ID=${FILE_NAME%%.*}
    CHECKSUM_LOG_FILE=$LOGPATH/$(date +%F).$ARTIFACT_ID.checksum
    md5sum $FILE_NAME > $CHECKSUM_LOG_FILE
fi

DEBUG "checksum calulated for $ARTIFACT_ID file"

#####################################################################################################
##                  DECLARING SCRIPT FUNCTION START                                                  ##
#####################################################################################################

### Function: insert_before_servers ###
#
# It will insert username info in setting.xml b/w </servers> section
#
# Arguments     : None
# Return Values : None
#

insert_before_servers () {
DEBUG "$USER_NAME not found in $M2_HOME/settings.xml file"
sed -i "/<servers>/a     <server>\n    <id>assure-releases<\/id>\n    <username>$USER_NAME<\/username>\n    <password>$UEP<\/password>\n<\/server>" $M2_HOME/settings.xml
DEBUG "$USER_NAME added to $M2_HOME/settings.xml file"
}

### Function: insert_before_settings ###
#
# It will insert username info in setting.xml b/w </settings> section
#
# Arguments     : None
# Return Values : None
#

insert_before_settings () {
DEBUG "$USER_NAME not found in $M2_HOME/settings.xml file"
sed -i "/<\/settings>/i   <servers>\n  <server>\n    <id>assure-releases<\/id>\n    <username>$USER_NAME<\/username>\n    <password>$UEP<\/password>\n  <\/server>\n<\/servers>" $M2_HOME/settings.xml
DEBUG "$USER_NAME added to $M2_HOME/settings.xml file"
}

### Function: setting_security_file ###
#
# creating settings.xml file and copying username and encrypted password
#
# Arguments     : None
# Return Values : None
#

setting_security_file () {
cat <<EOF > $M2_HOME/settings-security.xml
<settingsSecurity>
  <master>${MEP}</master>
</settingsSecurity>
EOF
DEBUG "$M2_HOME/settings-security.xml file created"
}

### Function: setting_file ###
#
# creating settings-security.xml file and copying mastr encrypted password
#
# Arguments     : None
# Return Values : None
#

setting_file () {
DEBUG "$M2_HOME/settings.xml file  not found"
cat <<EOF > $M2_HOME/settings.xml
<?xml version="1.0"?>
<settings>
  <servers>
     <server>
        <id>assure-releases</id>
        <username>${USER_NAME}</username>
        <password>${UEP}</password>
    </server>
  </servers>
</settings>
EOF
DEBUG "$M2_HOME/settings.xml file created"
}

### Function: success ###
#
# creating settings-security.xml file and copying mastr encrypted password
#
# Arguments     : None
# Return Values : None
#

success () {
INFO  "CHECKSUM OF $FILE_NAME IS `awk '{print $1}' $CHECKSUM_LOG_FILE` and saved in $CHECKSUM_LOG_FILE"
sleep 2s
SUCCESS "$FILE_NAME is successfully uploaded by $USER_NAME and nexus link is $NEXUS_URL$LINK_PATH/$ARTIFACT_ID/$ARTIFACT_VERSION/"
INFO "you can check maven_log from $LOG_FILE"
EXIT
SCRIPTEXIT
}

### Function: unsuccess ###
#
# creating settings-security.xml file and copying mastr encrypted password
#
# Arguments     : None
# Return Values : None
#

unsuccess () {
ERROR "$FILE_NAME is Failed to upload and please check the log from $LOG_FILE and try again"
EXIT
SCRIPTEXIT
}

### Function: maven_cmd ###
#
# creating settings-security.xml file and copying mastr encrypted password
#
# Arguments     : None
# Return Values : None
#

maven_cmd () {
$MVN_PATH -version &>> $LOG_FILE
if [ $? = 0 ] ;
  then
    INFO "$FILE_NAME is uploading..."
    $MVN_PATH -B deploy:deploy-file -Durl=$NEXUS_URL -DrepositoryId=$NEXUS_REPO_ID -DgroupId=$ARTIFACT_GROUP_ID -Dversion=$ARTIFACT_VERSION -DartifactId=$ARTIFACT_ID  -Dfile=$FILE_NAME >> $LOG_FILE
  else
   ERROR "Please set environment variable for maven path to $MVN_PATH"
   EXIT
   SCRIPTEXIT
   exit 401
fi
}


#####################################################################################################
##                  DECLARING SCRIP FUNCTION END                                                  ##
#####################################################################################################

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
