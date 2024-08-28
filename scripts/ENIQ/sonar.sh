#!bin/bash

#####Taking the module from the input file into an array
getArray() {
    array=() # Create array
    while IFS= read -r line # Read a line
    do
        array+=("$line") # Append line to the array
    done < "$1"
}
getArray "/proj/eiffel013_config_fem5s11/eiffel_home/jobs/PF_Sonar_Analysis/Module.txt"


######Cloning the reguired module
for e in "${array[@]}"
do
    cd /proj/eiffel013_config_fem5s11/eiffel_home/jobs/PF_Sonar_Analysis/

echo ".... CLONING $e ...."
echo " "
if [ -d "/proj/eiffel013_config_fem5s11/eiffel_home/jobs/PF_Sonar_Analysis/$e/" ]
then
        cd /proj/eiffel013_config_fem5s11/eiffel_home/jobs/PF_Sonar_Analysis/$e/
        git pull
    python /proj/eiffel013_config_fem6s11/branch_checkout.py /proj/eiffel013_config_fem5s11/eiffel_home/jobs/PF_Sonar_Analysis/$e/ $Branch
else
        git clone ssh://esjkadm100@gerrit.ericsson.se:29418/OSS/ENIQ-CR-Parent/com.ericsson.eniq.stats.plat/$e && scp -p -P 29418 esjkadm100@gerrit.ericsson.se:hooks/commit-msg $e/.git/hooks/
    cd /proj/eiffel013_config_fem5s11/eiffel_home/jobs/PF_Sonar_Analysis/$e/
    python /proj/eiffel013_config_fem6s11/branch_checkout.py /proj/eiffel013_config_fem5s11/eiffel_home/jobs/PF_Sonar_Analysis/$e/ $Branch
fi

cd /proj/eiffel013_config_fem5s11/eiffel_home/jobs/PF_Sonar_Analysis/
python sonar_analysis.py /proj/eiffel013_config_fem5s11/eiffel_home/jobs/PF_Sonar_Analysis/$e/dev/build/build.xml

cd /proj/eiffel013_config_fem5s11/eiffel_home/jobs/PF_Sonar_Analysis/
rm -rf $e

done

