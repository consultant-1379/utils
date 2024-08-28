import os
import subprocess

os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/mgw_etl/FD/Manual Modification")
x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')

for pkgs in list:
	pkg = pkgs[:pkgs.index('.')]
	groups=pkg.split('_')
	split_pkg = '_'.join(groups[:4]), '_'.join(groups[4:5])
	os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pkgs+" https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/MGW/mgw_etl/FD/"+split_pkg[1]+"/"+split_pkg[0]+"/"+pkgs)
