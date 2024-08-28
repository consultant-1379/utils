import os
import subprocess
import re

os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/property_files/")
x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
for pkgs in list:
	os.chdir('/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/property_files/'+pkgs)
	x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
	out,err = x.communicate()
	out = out.strip()
	tpi = out.split('\n')
    	Ship = os.popen('cat /proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/property_files/'+pkgs+'/DC_E_NR.tpi_properties | grep BaseLine').read()
	Rstate = os.popen('cat /proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/property_files/'+pkgs+'/DC_E_NR.tpi_properties | grep RState').read()
	Rstate = Rstate.strip()
	Ship = Ship.strip()
	print pkgs+"_"+Ship
	if Rstate!= "" and Ship!='BaseLine = "obsolete"':
		Rstate = re.search(r'"(\w+)"',Rstate).groups()[0]
		buildnum = os.popen('cat /proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/property_files/'+pkgs+'/DC_E_NR.tpi_properties | grep buildNum').read()
		buildnum = buildnum.strip()
		if buildnum != 'buildNum = ""':
			buildnum = re.search(r'"(\w+)"',buildnum).groups()[0]
			if '_' in buildnum:
				buildnum = buildnum.replace('_','')
		for tp in tpi:
			pkg = tp.split('.')[0]
			try:
				txts = Ship.split('\"')
				txt = txts[1]
				rel = txt[6:10]
				ship = txt[10:]
				ship = ship.upper()
				rel = rel.upper()
				if buildnum != 'buildNum = ""':
					os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+tp+" https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/container1/"+pkg+"/"+rel+"/"+ship+"/"+Rstate+"_"+buildnum+"/"+tp)
					print rel+"_"+ship+"_"+Rstate+"_"+buildnum
				else:
					os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+tp+" https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/container1/"+pkg+"/"+rel+"/"+ship+"/"+Rstate+"_"+buildnum+"/"+tp)
					print rel+"_"+ship+"_"+Rstate
			except Exception:
				print "Exception"+rel+"_"+ship+"_"+Rstate
