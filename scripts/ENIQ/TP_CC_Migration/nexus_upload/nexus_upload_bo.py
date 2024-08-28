import os
import subprocess

os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/tp")
x=subprocess.Popen('ls | grep _bo', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
for folds in list:
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/tp/"+folds)
	x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
	out,err = x.communicate()
	out = out.strip()
	list1 = out.split('\n')
	group=folds.split('_')
	n=len(group)
	split_fold = '_'.join(group[:n-1])
	fold_up = split_fold.upper()
	for pkgs in list1:
	        pkg = pkgs[:pkgs.index('.')]
       		groups=pkg.split('_')
		n=len(groups)
        	split_pkg = '_'.join(groups[n-2:n-1]), '_'.join(groups[:n])
        	os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pkgs+" https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folds+"/"+split_pkg[0]+"/"+split_pkg[1]+"/"+pkgs)
		
