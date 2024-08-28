import os
import subprocess

os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/Report_Package/")
x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
list.remove("ERBS")
for folds in list:
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/Report_Package/"+folds)
	x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
	out,err = x.communicate()
	out = out.strip()
	list1 = out.split('\n')
	for pkgs in list1:
        	pkg = pkgs[:pkgs.index('.')]
        	groups=pkg.split('_')
		n=len(groups)
        	split_pkg = '_'.join(groups[:n-1]), '_'.join(groups[n-1:])
        	os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pkgs+" https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/Report_Package/"+folds+"/"+split_pkg[0]+"/"+split_pkg[1]+"/"+pkgs)

os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/Report_Package/ERBS/")
x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
list.remove("Stored_Procedure")
for pkgs in list:
	pkg = pkgs[:pkgs.index('.')]
	groups=pkg.split('_')
	n=len(groups)
    	split_pkg = '_'.join(groups[:n-1]), '_'.join(groups[n-1:])
    	os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pkgs+" https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/Report_Package/ERBS/"+split_pkg[0]+"/"+split_pkg[1]+"/"+pkgs)

os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/Report_Package/ERBS/Stored_Procedure")
x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
for folds in list:
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/Report_Package/ERBS/Stored_Procedure/"+folds)
	x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
	out,err = x.communicate()
	out = out.strip()
	list1 = out.split('\n')
	for pkgs in list1:
        	os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pkgs+" https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/Report_Package/ERBS/Stored_Procedure/"+folds+"/"+pkgs)
