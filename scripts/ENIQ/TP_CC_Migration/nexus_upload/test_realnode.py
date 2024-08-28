import os
import subprocess

os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work")
x=subprocess.Popen('find $(pwd)/Realnode_Files/ -type f', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
for pkg in list:
	groups=pkg.split('/')
	split_pkg = '/'.join(groups[:6]), '/'.join(groups[6:])
	print "curl -v -u esjkadm100:Naples\!0512 --upload-file "+pkg+" https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/"+split_pkg[1]
	os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pkg+" https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/"+split_pkg[1])
