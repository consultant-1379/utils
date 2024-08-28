import os
import subprocess
import re

os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/ENIQ_Feature_Files_Linux/")
x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
for pkgs in list:
	os.chdir('/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/ENIQ_Feature_Files_Linux/'+pkgs)
	x=subprocess.Popen('ls | grep _properties', stdout=subprocess.PIPE, shell=True)
	out,err = x.communicate()
	out = out.strip()
	tpx = out.split('\n')
    	Ship = os.popen('cat /proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/ENIQ_Feature_Files_Linux/'+pkgs+'/'+tpx[0]+' | grep created').read()
	Ship = Ship.strip()
	os.system('rm '+tpx[0])
	#print pkgs+"_"+Ship
	if Ship!="":
        	x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
        	out,err = x.communicate()
        	out = out.strip()
        	tpi = out.split('\n')
		for tp in tpi:
			try:
				txts = Ship.split(' ')
				txt = txts[1]
				rel = txt[0:txt.index("+")]
				os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+tp+" https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_etl/ENIQ_Feature_Files_Linux/"+tp+"/"+tp+"_"+rel)
				#print rel+"_"+tp
			except Exception:
				print "Exception"+tp
