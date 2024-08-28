import os
import stat
import sys
import datetime
import subprocess
import datetime
import shutil
args = sys.argv
folder = args[1]
pack = args[2]
user = args[3]
check = args[4]
mac_ip = args[5]
reason = args[6]
def checkOut():
	if "CXC" in folder:
		groups=pack.split('_')
		n=len(groups)
		split_pkg = '_'.join(groups[2:3]), '_'.join(groups[3:4])
		pathdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" +split_pkg[0]+"/"+split_pkg[1]+"/" + pack
		propdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" +split_pkg[0]+"/"+split_pkg[1]+"/" + pack+"_properties"
	elif "eature" in folder:
		pathdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" + pack
		propdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" +"property_files/"+ pack+".properties"
	elif "TP_KPI_Script" in folder:
		pathdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" + pack
		propdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" +"property_files/"+ pack+".properties"
	else:
		pathdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" + pack
		propdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" +"property_files/"+ pack+".properties"
		
	os.chdir("/proj/eiffel013_config_fem6s11/slaves/RHEL_ENIQ_STATS/git_work/locks")
	x=subprocess.Popen('ls | grep '+pack+'_lck', stdout=subprocess.PIPE, shell=True)
	out,err = x.communicate()
	out = out.strip()
	if pack+'_lck' in out:
		grp=out.split('_')
		print "Already checked out by "+grp[0]
		exit(1)
	else:
		os.system('touch '+user+'_'+pack+'_lck')
		os.system('curl -O -u esjkadm100:Naples\!0512 '+pathdir)
		d=os.system('sshpass -p shroot12 scp -P 2251 -o StrictHostKeyChecking=no '+pack+' root@'+mac_ip+'.athtem.eei.ericsson.se:/eniq/home/dcuser')
		if d == 0:
			print "Copied the package to server"
			os.system('rm '+pack)
		else:
			print "Not able to copy the package to server"
			os.system('rm '+pack)
			exit(1)
def checkIn():
	cnt =0
	if "CXC" in folder:
		groups=pack.split('_')
		n=len(groups)
		split_pkg = '_'.join(groups[2:3]), '_'.join(groups[3:4])
		prop = pack+"_properties"
		propdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" +split_pkg[0]+"/"+split_pkg[1]+"/" + pack+"_properties"
		pathdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" +split_pkg[0]+"/"+split_pkg[1]+"/" + pack
	elif "eature" in folder:
		prop = pack+".properties"
		pathdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" + pack
		propdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" +"property_files/"+ pack+".properties"
	elif "TP_KPI_Script" in folder:
		prop = pack+".properties"
		pathdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" + pack
		propdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" +"property_files/"+ pack+".properties"
	else:
		prop = pack+".properties"
		pathdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" + pack
		propdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" +"property_files/"+ pack+".properties"
	os.chdir("/proj/eiffel013_config_fem6s11/slaves/RHEL_ENIQ_STATS/git_work/locks")
	x=subprocess.Popen('ls | grep '+pack+'_lck', stdout=subprocess.PIPE, shell=True)
	out,err = x.communicate()
	out = out.strip()
	#list = out.split('\n')
	k=0
	if pack+'_lck' in out:
		grp=out.split('_')
		if grp[0] != user:
			print "Already checked out by "+grp[0]
			k=1
			exit(1)
		else:
			k=2
	else:
		if "CXC" in folder:
			groups=pack.split('_')
			n=len(groups)
			split_pkg = '_'.join(groups[2:3]), '_'.join(groups[3:4])
			p = os.system('ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder + "/" + split_pkg[0]+"/"+split_pkg[1]+"/ | grep " + pack)
		elif "eature" in folder:
			p = os.system('ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder + "/ | grep " + pack)
		elif "TP_KPI_Script" in folder:
			p = os.system('ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder + "/ | grep " + pack)
		else:
			p = os.system('ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder + "/ | grep " + pack)
		if p == 0:
			print "Please checkout the file before checkin"
			exit(1)
		else:
			nexusUpload();
		
	if k==2:
		os.system('curl -O -u esjkadm100:Naples\!0512 '+pathdir)
		now = datetime.datetime.now()
		oldpack = pack+'_'+now.strftime("%Y-%m-%dT%H:%M:%S")
		os.system('mv '+pack+' old_'+pack)
		os.system('curl -O -u esjkadm100:Naples\!0512 '+propdir)
		os.chdir("/proj/eiffel013_config_fem6s11/slaves/RHEL_ENIQ_STATS/git_work/")
		d = os.system('./server_conn.pl '+mac_ip+' '+pack)
		if d == 0:
			print "Copied package to workspace successfully"
		else:
			print "Issue in copying file !!! Please investigate"
			os.system('rm old_'+pack)
			os.system('rm '+prop)
			exit(1)
		os.chdir("/proj/eiffel013_config_fem6s11/slaves/RHEL_ENIQ_STATS/git_work/locks")
		os.system('cp '+pack+' '+oldpack)
		if "TP_KPI_Script" in folder or ".zip" in pack:
			dif = 1
		else:
			dif = os.system('diff '+pack+' old_'+pack)
		if dif != 0:
			os.chdir("/proj/eiffel013_config_fem6s11/slaves/RHEL_ENIQ_STATS/git_work/locks")
			file_object = open(prop, 'a')
			file_object.write('\n')
			file_object.write('Created by : '+user+'\n')
			file_object.write(now.strftime("%Y-%m-%dT%H:%M:%S"))
			file_object.write('\nReason = '+reason)
			file_object.close()
			if "ENIQ_Feature_Files" in pack and ".zip" in pack:
				os.system("cp "+pack+" /proj/eiffel013_config_fem6s11/eiffel_home/jobs/TP_Vobs_Delivery/")
			if "eature" in folder or "TP_KPI_Script" in folder or "CXC" not in folder:
				os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_plm/"+ folder + "/" + pack)
				p = os.system('diff '+pack+' /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder + "/" + pack)
				if ".zip" in pack:
					p = 0
				if p == 0:
					print "\n\n *******"+pack+" uploaded to nexus successfully*******\n\n"
				else:
					print "\n\n *******"+pack+" upload failed*******\n\n"
					os.system('rm old_'+pack)
					os.system('rm '+oldpack)
					os.system('rm '+prop)
					os.system('rm '+pack)
					exit(1)
				os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_plm/"+ folder + "/" +"property_files/"+ prop)
				p = os.system('diff '+prop+' /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder + "/" +"property_files/"+ prop)
				if p == 0:
					print "\n\n *******"+prop+" uploaded to nexus successfully*******\n\n"
				else:
					print "\n\n *******"+prop+" upload failed*******\n\n"
					os.system('rm old_'+pack)
					os.system('rm '+oldpack)
					os.system('rm '+prop)
					os.system('rm '+pack)
					exit(1)
				if "/" in folder:
					grp = folder.split('/')[0]
					grps = folder.split('/')[1]
					os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+oldpack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_plm/"+ grp +"_version/"+grps+"/"+pack+"/"+ oldpack)
					p = os.system('diff '+oldpack+' /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ grp +"_version/"+grps+"/" +pack+"/"+ oldpack)
				else:
					os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+oldpack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_plm/"+ folder + "_version/" +pack+"/"+ oldpack)
					p = os.system('diff '+oldpack+' /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder +"_version/" +pack+"/"+ oldpack)
				if ".zip" in pack:
					p = 0
				if p == 0:
					print "\n\n *******"+oldpack+" uploaded to nexus successfully*******\n\n"
				else:
					print "\n\n *******"+oldpack+" upload failed*******\n\n"
					os.system('rm old_'+pack)
					os.system('rm '+oldpack)
					os.system('rm '+prop)
					os.system('rm '+pack)
					exit(1)
			if "CXC" in folder:
				os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_plm/"+ folder + "/" +split_pkg[0]+"/"+split_pkg[1]+"/" + pack)
				p = os.system('diff '+pack+' /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder + "/" + split_pkg[0]+"/"+split_pkg[1]+"/" + pack)
				if p == 0:
					print "\n\n *******"+pack+" uploaded to nexus successfully*******\n\n"
				else:
					print "\n\n *******"+pack+" upload failed*******\n\n"
					os.system('rm old_'+pack)
					os.system('rm '+oldpack)
					os.system('rm '+prop)
					os.system('rm '+pack)
					exit(1)
				os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_plm/"+ folder + "/" +split_pkg[0]+"/"+split_pkg[1]+"/" + prop)
				p = os.system('diff '+prop+' /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder + "/" +split_pkg[0]+"/"+split_pkg[1]+"/"+ prop)
				if p == 0:
					print "\n\n *******"+prop+" uploaded to nexus successfully*******\n\n"
				else:
					print "\n\n *******"+prop+" upload failed*******\n\n"
					os.system('rm old_'+pack)
					os.system('rm '+oldpack)
					os.system('rm '+prop)
					os.system('rm '+pack)
					exit(1)
				os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+oldpack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_plm/"+ folder + "_version/" +pack+"/"+ oldpack)
				p = os.system('diff '+oldpack+' /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder +"_version/" +pack+"/"+ oldpack)
				if p == 0:
					print "\n\n *******"+oldpack+" uploaded to nexus successfully*******\n\n"
				else:
					print "\n\n *******"+oldpack+" upload failed*******\n\n"
					os.system('rm old_'+pack)
					os.system('rm '+oldpack)
					os.system('rm '+prop)
					os.system('rm '+pack)
					exit(1)
			os.system('rm -rf '+user+'_'+pack+'_lck')
			print "File checked in and removed locks"
			os.system('rm -rf '+pack)
			os.system('rm -rf '+prop)
			os.system('rm -rf '+oldpack)
			os.system('rm -rf old_'+pack)
		else:
			print "No changes are made in the file "+pack
			os.system('rm -rf '+pack)
			os.system('rm -rf '+prop)
			os.system('rm -rf '+oldpack)
			os.system('rm -rf old_'+pack)
			exit(1)
		cnt = 1
			
def nexusUpload():
	cnt =0
	if "CXC" in folder:
		groups=pack.split('_')
		n=len(groups)
		split_pkg = '_'.join(groups[2:3]), '_'.join(groups[3:4])
		prop = pack+"_properties"
		propdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" +split_pkg[0]+"/"+split_pkg[1]+"/" + pack+"_properties"
		pathdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" +split_pkg[0]+"/"+split_pkg[1]+"/" + pack
	#if "eature" in folder or "TP_KPI_Script" in folder or "CXC" not in folder:
	else:
		prop = pack+".properties"
		pathdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" + pack
		propdir = "https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/releases/content/com/ericsson/eniq/stats/tp_plm/" + folder + "/" +"property_files/"+ pack+".properties"
	os.chdir("/proj/eiffel013_config_fem6s11/slaves/RHEL_ENIQ_STATS/git_work/")
	d = os.system('./server_conn.pl '+mac_ip+' '+pack)
	if d == 0:
		print "Copied package to workspace successfully"		
	else:
		print "Issue in copying file !!! Please investigate"
		exit(1)
	os.chdir("/proj/eiffel013_config_fem6s11/slaves/RHEL_ENIQ_STATS/git_work/locks")
	now = datetime.datetime.now()
	oldpack = pack+'_'+now.strftime("%Y-%m-%dT%H:%M:%S")
	os.system('cp '+pack+' '+oldpack)
	file_object = open(prop, 'a')
	file_object.write('\n')
	file_object.write('Created by : '+user+'\n')
	file_object.write(now.strftime("%Y-%m-%dT%H:%M:%S"))
	file_object.write('\nReason = '+reason)
	file_object.close()
	if "eature" in folder or "TP_KPI_Script" in folder or "CXC" not in folder:
		os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_plm/"+ folder + "/" + pack)
		p = os.system('diff '+pack+' /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder + "/" + pack)
		if ".zip" in pack:
			p = 0
		if p == 0:
			print "\n\n *******"+pack+" uploaded to nexus successfully*******\n\n"
		else:
			print "\n\n *******"+pack+" upload failed*******\n\n"
			os.system('rm '+oldpack)
			os.system('rm '+prop)
			os.system('rm '+pack)
			exit(1)
		os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_plm/"+ folder + "/" +"property_files/"+ prop)
		p = os.system('diff '+prop+' /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder + "/" +"property_files/"+ prop)
		if p == 0:
			print "\n\n *******"+prop+" uploaded to nexus successfully*******\n\n"
		else:
			print "\n\n *******"+prop+" upload failed*******\n\n"
			os.system('rm '+oldpack)
			os.system('rm '+prop)
			os.system('rm '+pack)
			exit(1)
		if "/" in folder:
			grp = folder.split('/')[0]
			grps = folder.split('/')[1]
			os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+oldpack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_plm/"+ grp +"_version/"+grps+"/"+pack+"/"+ oldpack)
			p = os.system('diff '+oldpack+' /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ grp +"_version/"+grps+"/"+pack+"/"+ oldpack)
		else:
			os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+oldpack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_plm/"+ folder + "_version/"+pack+"/"+ oldpack)
			p = os.system('diff '+oldpack+' /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder +"_version/" +pack+"/"+ oldpack)
		if ".zip" in pack:
			p = 0
		if p == 0:
			print "\n\n *******"+oldpack+" uploaded to nexus successfully*******\n\n"
		else:
			print "\n\n *******"+oldpack+" upload failed*******\n\n"
			os.system('rm '+oldpack)
			os.system('rm '+prop)
			os.system('rm '+pack)
			exit(1)
	if "CXC" in folder:
		os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_plm/"+ folder + "/" +split_pkg[0]+"/"+split_pkg[1]+"/" + pack)
		p = os.system('diff '+pack+' /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder + "/" + split_pkg[0]+"/"+split_pkg[1]+"/" + pack)
		if p == 0:
			print "\n\n *******"+pack+" uploaded to nexus successfully*******\n\n"
		else:
			print "\n\n *******"+pack+" upload failed*******\n\n"
			os.system('rm '+oldpack)
			os.system('rm '+prop)
			os.system('rm '+pack)
			exit(1)
		os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_plm/"+ folder + "/" +split_pkg[0]+"/"+split_pkg[1]+"/" + prop)
		p = os.system('diff '+prop+' /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder + "/" +split_pkg[0]+"/"+split_pkg[1]+"/"+ prop)
		if p == 0:
			print "\n\n *******"+prop+" uploaded to nexus successfully*******\n\n"
		else:
			print "\n\n *******"+prop+" upload failed*******\n\n"
			os.system('rm '+oldpack)
			os.system('rm '+prop)
			os.system('rm '+pack)
			exit(1)
		os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+oldpack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp_plm/"+ folder + "_version/" +pack+"/"+ oldpack)
		p = os.system('diff '+oldpack+' /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp_plm/'+ folder +"_version/" +pack+"/"+ oldpack)
		if p == 0:
			print "\n\n *******"+oldpack+" uploaded to nexus successfully*******\n\n"
		else:
			print "\n\n *******"+oldpack+" upload failed*******\n\n"
			os.system('rm '+oldpack)
			os.system('rm '+prop)
			os.system('rm '+pack)
			exit(1)
	os.system('rm -rf '+pack)
	os.system('rm -rf '+prop)
	os.system('rm -rf '+oldpack)
			
def nexusUncheck():
	os.chdir("/proj/eiffel013_config_fem6s11/slaves/RHEL_ENIQ_STATS/git_work/locks")
	x=subprocess.Popen('ls | grep '+pack+'_lck', stdout=subprocess.PIPE, shell=True)
	out,err = x.communicate()
	out = out.strip()
	list = out.split('\n')
	k=0
	for pkg in list:
		if pack+'_lck' in pkg:
			grp=pkg.split('_')
			if grp[0] != user:
				print "Already checked out by "+grp[0]
				k=2
			else:
				os.system('rm -rf '+user+'_'+pack+'_lck')
				print "Removed the lock"
				k=1
				break
	if k==0:
		print "Lock doesn't exist for "+pack
							
if "checkout" in check:
	checkOut();
if "checkin" in check:
	checkIn();
if "uncheck" in check:
	nexusUncheck();