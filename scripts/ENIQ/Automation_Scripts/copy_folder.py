import os
import subprocess
import sys

#path = "/proj/eiffel1004_artifacts_arm104/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp/"
#for 
#os.system("wget -r -l inf  https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp/ENIQ_Feature_Files_Linux/" + )
os.system("cp -r /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp/ENIQ_Feature_Files_Linux /proj/eiffel013_config_fem6s11/eiffel_home/slaves/ComputeFarm1/workspace")
os.system("scp -r /proj/eiffel013_config_fem6s11/eiffel_home/slaves/ComputeFarm1/workspace/ENIQ_Feature_Files_Linux/ eniqdmt@10.120.176.102:/home/eniqdmt/gagan")
os.system("scp /proj/eiffel013_config_fem6s11/eiffel_home/slaves/ComputeFarm1/workspace/ENIQ_Feature_File_build_automation/scripts/ENIQ/Automation_Scripts/newfile1.py eniqdmt@10.120.176.102:/home/eniqdmt/zpunvai")
os.system("rm -rf /proj/eiffel013_config_fem6s11/eiffel_home/slaves/ComputeFarm1/workspace/ENIQ_Feature_Files_Linux")
