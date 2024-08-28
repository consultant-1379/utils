import os
import subprocess

os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/tp/CXC")
x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
for pkgs in list:
        #pkg = pkgs[:pkgs.index('.')]
        groups=pkgs.split('_')
        n=len(groups)
        split_pkg = '_'.join(groups[2:3]), '_'.join(groups[3:4])
	os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pkgs+" https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/CXC/"+split_pkg[0]+"/"+split_pkg[1]+"/"+pkgs)

