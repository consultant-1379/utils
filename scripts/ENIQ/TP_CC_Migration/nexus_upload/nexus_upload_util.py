import os
import subprocess
import re

os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/tp")
x=subprocess.Popen('find util -type f', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list1 = out.split("\n")
for dir in list1:
        pkgs = dir[dir.rindex('/')+1:]
        pkg = pkgs[:pkgs.index('.')]
        path = dir[0:dir.rindex('/')]
	try:
		os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+dir+" https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+path+"/"+pkgs)
	except Exception:
		print "Exception"
