import os
import subprocess
os.chdir("/proj/eiffel004_config_fem156/slaves/")
x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
print(list)
for i in list:
	os.chdir("/proj/eiffel004_config_fem156/slaves/"+i)
	os.system("rm -rf workspace")

