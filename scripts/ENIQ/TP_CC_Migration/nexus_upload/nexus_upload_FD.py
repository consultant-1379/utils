import os
import subprocess
import re

os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/tp1")
x=subprocess.Popen('ls | grep _etl', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
list.remove("ipprobe_etl")
list.remove("iptransport_etl")
list.remove("udm_etl")
list.remove("erbsg2_etl")
list.remove('erbs_etl')
#list.remove("Manual Modifications")

for etls in list:
	cap_name = etls[:etls.index('_etl')]
	cap_name = cap_name.upper()
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/tp1/"+etls)
	if (os.path.isdir("FD")):
		x=subprocess.Popen('find FD -type f', stdout=subprocess.PIPE, shell=True)
		out,err = x.communicate()
		out = out.strip()
		list1 = out.split("\n")
		for dir in list1:
			pkgs = dir[dir.rindex('/')+1:]
			pkg = pkgs[:pkgs.index('.')]
			try:
				rstate = re.search(r'R\d+[A-Z]',pkg).group()
				y = re.search(r'(.+)R\d+[A-Z]',pkg).group()
				y = y[:y.index('_'+rstate)]
				#groups=pkg.split('_')
				#split_pkg = '_'.join(groups[:4]), '_'.join(groups[4:5])
				#print "split_pkg[1]+"/"+split_pkg[0]+"/"+pkgs
				if "Manual" in dir:
					dir = 'FD/Manual\ Modification/'+pkgs

				os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+dir+" https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_etl/"+cap_name+"/"+etls+"/FD/"+rstate+"/"+y+"/"+pkgs)
			except Exception:
				print "Exception"
				os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+dir+" https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_etl/"+cap_name+"/"+etls+"/FD/"+pkg+"/"+pkgs)
