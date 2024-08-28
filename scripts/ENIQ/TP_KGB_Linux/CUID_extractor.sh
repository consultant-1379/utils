#!/usr/bin/bash

#CURRENT_PATH=`dirname $0`
CURRENT_PATH="/eniq/sw/installer/bouniverses/"
TEMP_ZIP_PATH="$CURRENT_PATH/temp_zip"
TEMP_ZIP_CONTENT_PATH="$CURRENT_PATH/temp_content"
#OUTPUT_PATH="$CURRENT_PATH/output"
LCMBIAR_PATH=""
LCMBIAR_NAME=""
OUTPUT_FILE_NAME="CUID_LIST.csv"

#[ ! -d $OUTPUT_PATH ] && mkdir -p $OUTPUT_PATH
[ ! -d $TEMP_ZIP_PATH ] && mkdir -p $TEMP_ZIP_PATH
[ ! -d $TEMP_ZIP_CONTENT_PATH ] && mkdir -p $TEMP_ZIP_CONTENT_PATH
#[ ! -f $CURRENT_PATH/$OUTPUT_FILE_NAME ] && echo "BO_PKG_NAME,TP UNV NAME,CUID" | cat > $CURRENT_PATH/$OUTPUT_FILE_NAME
[ ! -f $CURRENT_PATH/$OUTPUT_FILE_NAME ] | cat > $CURRENT_PATH/$OUTPUT_FILE_NAME

#echo "$CURRENT_PATH/$OUTPUT_FILE_NAME"
#echo "$CURRENT_PATH is CURRENT_PATH"
#echo "$TEMP_ZIP_PATH is TEMP_ZIP_PATH"
#echo "Gointg to print list of BO in directory"
LIST_OF_BO_PKG=`ls /eniq/sw/installer/bouniverses/ | grep BO.*`
#echo "${LIST_OF_BO_PKG[*]} is list of BO"
for i in ${LIST_OF_BO_PKG}
	do
		BO_FOLDER_EXIST=`ls $CURRENT_PATH/$i/ | grep BO.*`
		if [ "$BO_FOLDER_EXIST" = "$i" ];then
			echo "checking passed cond"
			LCMBIAR_PATH="$CURRENT_PATH/$i/$BO_FOLDER_EXIST/unv"
		       LCMBIAR_NAME=`ls $CURRENT_PATH/$i/$BO_FOLDER_EXIST/unv/ | grep .*lcmbiar`
		else	
			LCMBIAR_PATH="$CURRENT_PATH/$i/unv"
			LCMBIAR_NAME=`ls $CURRENT_PATH/$i/unv/ | grep .*lcmbiar`
		fi
		echo "***************************************************************************\n\n"
		echo "$LCMBIAR_NAME is the LCMBIAR_NAME"
		echo "***************************************************************************\n\n"
		if [ "$LCMBIAR_NAME" != "" ]; then

			ZIP_FILENAME=`echo "$LCMBIAR_NAME" | cut -d "." -f1`".zip"
		
			cp "$LCMBIAR_PATH/$LCMBIAR_NAME" "$TEMP_ZIP_PATH/$ZIP_FILENAME"
			unzip "$TEMP_ZIP_PATH/$ZIP_FILENAME" -d $TEMP_ZIP_CONTENT_PATH > /dev/null 2>&1
			
			TEMP_FILE=`ls "$TEMP_ZIP_CONTENT_PATH/"*.001`
		
			TEMP_FILE_CONTENT=`cat $TEMP_FILE | grep primary* | cut -d"=" -f2`		
		
			echo "$TEMP_FILE_CONTENT" | while read -r line
			do	
			
				TEMP_CUID=`echo "$line" | awk -F"@\#%@" '{print $1}'`		
				TEMP_UNV_NAME=`echo "$line" | awk -F"@\#%@" '{print $3}'`
		
				echo $i".zip",$TEMP_UNV_NAME,$TEMP_CUID | cat >> $CURRENT_PATH/$OUTPUT_FILE_NAME
			done
			rm $TEMP_ZIP_CONTENT_PATH/*
			rm $TEMP_ZIP_PATH/*
			echo "CUID extraced successfully"
		#else
		#	echo $i".zip","NON lcmbiar file","N/A" | cat >> $CURRENT_PATH/$OUTPUT_FILE_NAME

		fi
	done
rm -r $TEMP_ZIP_PATH
rm -r $TEMP_ZIP_CONTENT_PATH
echo "Copying output file"
cp $CURRENT_PATH/$OUTPUT_FILE_NAME /eniq/sw/installer/boreports/ 
