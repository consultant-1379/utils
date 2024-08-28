import os
import subprocess

import os
import subprocess

os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/tp")
x=subprocess.Popen('ls | grep dim', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
for pkgs in list:
	x=subprocess.Popen('ls -p '+pkgs+'| grep -v /', stdout=subprocess.PIPE, shell=True)
	out,err = x.communicate()
	out = out.strip()
	files_list = out.split('\n')
	for files in files_list:
		if '.' in files:
			file = files[:files.index('.')]
			group = file.split('_')
			rstate = group[len(group)-2]
			os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pkgs+"/"+files+" https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/DIM/"+pkgs+"/"+rstate+"/"+file+"/"+files)
