#!/usr/bin/bash

#CURRENT_PATH=`dirname $0`
CURRENT_PATH="/eniq/sw/installer/report"
TEMP_ZIP_PATH="$CURRENT_PATH/temp_zip"
TEMP_ZIP_CONTENT_PATH="$CURRENT_PATH/temp_content"
#OUTPUT_PATH="$CURRENT_PATH/output"
LCMBIAR_PATH=""
LCMBIAR_NAME=""
OUTPUT_FILE_NAME="CUID_LIST.csv"

#[ ! -d $OUTPUT_PATH ] && mkdir -p $OUTPUT_PATH
#[ ! -d $TEMP_ZIP_PATH ] && mkdir -p $TEMP_ZIP_PATH
#[ ! -d $TEMP_ZIP_CONTENT_PATH ] && mkdir -p $TEMP_ZIP_CONTENT_PATH
#[ ! -f $CURRENT_PATH/$OUTPUT_FILE_NAME ] && echo "BO_PKG_NAME,TP UNV NAME,CUID" | cat > $CURRENT_PATH/$OUTPUT_FILE_NAME
#[ ! -f $CURRENT_PATH/$OUTPUT_FILE_NAME ] | cat > $CURRENT_PATH/$OUTPUT_FILE_NAME

#echo "$CURRENT_PATH/$OUTPUT_FILE_NAME"
#echo "$CURRENT_PATH is CURRENT_PATH"
#echo "$TEMP_ZIP_PATH is TEMP_ZIP_PATH"
#echo "Gointg to print list of BO in directory"
LIST_OF_KPI_PKG=`ls /eniq/sw/installer/report | grep Report`
#echo "${LIST_OF_BO_PKG[*]} is list of BO"
for i in ${LIST_OF_KPI_PKG}
	do
		KPI_FOLDER_EXIST=`ls $CURRENT_PATH/$i/ | grep Report`
		if [ "$KPI_FOLDER_EXIST" = "$i" ];then
			echo "checking passed cond"
			LCMBIAR_PATH="$CURRENT_PATH/$i/$KPI_FOLDER_EXIST/"
		       LCMBIAR_NAME=`ls $CURRENT_PATH/$i/$KPI_FOLDER_EXIST/ | grep .*lcmbiar`
		else	
			LCMBIAR_PATH="$CURRENT_PATH/$i/unv"
			LCMBIAR_NAME=`ls $CURRENT_PATH/$i/ | grep .*lcmbiar`
		fi
		echo "***************************************************************************\n\n"
		echo "$LCMBIAR_NAME is the LCMBIAR_NAME"
		echo "***************************************************************************\n\n"
        L=`ls $CURRENT_PATH/$i | grep ERIC_ERBS_Basic_Report`
        if [ -n "$L" ];then
            cd $CURRENT_PATH/$i/
            K=`ls | wc -l`
            if [ "$K" == 3 ];then
                echo "Folder structure of $i is correct\n\n"
            else
                echo "Folder structure of $i is not correct\nPLEASE CHECK\n\n"
            fi
        else
            cd $CURRENT_PATH/$i/
            K=`ls | wc -l`
            if [ "$K" == 2 ];then
                echo "Folder structure of $i is correct\n\n"
            else
                echo "Folder structure of $i is not correct\nPLEASE CHECK\n\n"
            fi
        fi

	done
rm -r $TEMP_ZIP_PATH
rm -r $TEMP_ZIP_CONTENT_PATH
echo "Copying output file"
cp -r $CURRENT_PATH/* /eniq/sw/installer/boreports/ 
