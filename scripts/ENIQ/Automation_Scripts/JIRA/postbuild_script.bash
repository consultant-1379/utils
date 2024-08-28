echo "Running Automatic Jira Creation Scripts"

cd ${WORKSPACE}
pwd


#!/bin/bash

# Function to check if the given string is present in any file within the folder
check_string_in_files() {
    search_string="$1"
    folder_path="$2"

    for file in $folder_path/*xml; do
        if [ -f $file ] && [ -r $file ]; then
            if grep -q $search_string $file; then
                return 0  # Found the string, return success
            fi
        fi
    done

    return 1  # String not found in any file, return failure
}

# Check for the string in files
search_string='="FAIL"'  # Replace with the string you want to search for
folder_path="/root/robotenvironment/ENIQ_TC_Automation/INFRA/Other/KGB_Outputs"  # Replace with the path to the folder containing output.xml files

if check_string_in_files $search_string $folder_path; then
    # If the string is present, run the specified script
    #/path/to/your/JIRA/script.sh
    echo " Atleast one test case failed"
    python3 /root/sai_tmp/poc.py  $JOB_NAME $BUILD_URL ${PROJECT} ${TYPE} "${FIX}" "${COMPONENTS}" ${DROP} "${AREA}"     #Check the jira file being called here. jira_kgb for kgb and jira_cdb for cdb
	
else
    echo "All test cases have passed."
fi