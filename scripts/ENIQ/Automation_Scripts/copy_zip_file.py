import os
import subprocess
import sys
os.chdir("/home/eniqdmt/zpunvai/")
#os.chdir("/proj/eiffel013_config_fem6s11/eiffel_home/slaves/ComputeFarm1/workspace/")
w=subprocess.Popen('ls | grep ENIQ_Feature_Files_R', stdout=subprocess.PIPE, shell=True)
out2,err2 = w.communicate()
out2 = out2.strip()
list2 = out2.split('\n')
os.system('sshpass -p shroot12 scp -P 2251 -o StrictHostKeyChecking=no /home/eniqdmt/zpunvai/'+list2[0]+' root@'+sys.argv[1]+'.athtem.eei.ericsson.se:/eniq/home/dcuser')
#os.system('sshpass -p shroot12 scp -P 2251 -o StrictHostKeyChecking=no /proj/eiffel013_config_fem6s11/eiffel_home/slaves/ComputeFarm1/workspace/'+list2[0]+' root@'+sys.argv[1]+'.athtem.eei.ericsson.se:/eniq/home/dcuser')
#os.system("rm -rf /proj/eiffel013_config_fem6s11/eiffel_home/slaves/ComputeFarm1/workspace/" + list2[0])
os.system("rm -rf /home/eniqdmt/zpunvai/" + list2[0])
os.system("rm -rf /home/eniqdmt/zpunvai/" + list2[0])
