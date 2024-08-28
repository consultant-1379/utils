import os
import stat
import sys
import datetime
import subprocess
import time
import re
import shutil

args = sys.argv
folder = args[1]
pack = args[2]
user = args[3]
check = args[4]
mac_ip = args[5]
reason = args[6]
dir = args[7]
num = args[8]
prop = pack+"_properties"
now = datetime.datetime.now()

def createProp():
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/")
	d = os.system('./server_conn.pl '+mac_ip+' '+pack)
	if d == 0:
		print "Copied package to workspace successfully"
	else:
		print "Issue in copying file !!! Please investigate"
		exit(1)
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/locks")
	file_object = open(prop, 'w')
	file_object.write('\n')
	file_object.write('Created by : '+user+'\n')
	file_object.write(now.strftime("%Y-%m-%dT%H:%M:%S"))
	file_object.write('\nReason : '+reason)
	file_object.close()
	os.system("cp "+pack+" /proj/eiffel004_config_fem156/eiffel_home/Linux_KGB_DATA/Pack/")
	os.system("cp "+prop+" /proj/eiffel004_config_fem156/eiffel_home/Linux_KGB_DATA/Prop/")

def uploadCheck():
	fd = os.system("cat /proj/eiffel004_config/fem160/eiffel_home/jobs/TP_Nexus_Upload/builds/"+num+"/log| grep -i error")
	fc = os.system("cat /proj/eiffel004_config/fem160/eiffel_home/jobs/TP_Nexus_Upload/builds/"+num+"/log| grep -i curl:")
	if fd == 0 or fc == 0:
		print "\n\n*****"+pack+" upload is failed*****\n\n"
		os.system("rm "+pack)
		os.system("rm "+prop)
		exit(1)
	else:
		print "\n\n*****"+pack+" is uploaded to Nexus*****\n\n"	
		
def uploadKPI():
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/locks")
	pkg = pack[:pack.index('.')]
	prop = pack+"_properties"
	groups=pkg.split('_')
	n=len(groups)
	split_pkg = '_'.join(groups[:n-1]), '_'.join(groups[n-1:])
	d = os.system("ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/kpi/"+split_pkg[0]+"/ | grep "+split_pkg[1])
	if d == 0:
		print "Already present in Nexus "+pack
		os.system("rm "+pack)
		os.system("rm "+prop)
		exit(1)
	else:
		d = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/kpi/"+split_pkg[0]+"/"+split_pkg[1]+"/"+pack)
		time.sleep(10)
		uploadCheck();
		d = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/kpi/"+split_pkg[0]+"/"+split_pkg[1]+"/"+prop)
		print "Verifying the uploaded package\n"
		time.sleep(10)
		uploadCheck();

def uploadBO():
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/locks")
	group=folder.split('_')
	m=len(group)
	split_fold = '_'.join(group[:m-1])
	fold_up = split_fold.upper()
	pkg = pack[:pack.index('.')]
	prop = pack+"_properties"
	groups=pkg.split('_')
	n=len(groups)
	split_pkg = '_'.join(groups[n-2:n-1]), '_'.join(groups[:n])
	d = os.system("ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+split_pkg[0]+"/ | grep "+split_pkg[1])
	if d == 0:
		print "Already present in Nexus "+pack
		os.system("rm "+pack)
		os.system("rm "+prop)
		exit(1)
	else:
		fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+split_pkg[0]+"/"+split_pkg[1]+"/"+pack)
		time.sleep(10)
		uploadCheck();
		fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+split_pkg[0]+"/"+split_pkg[1]+"/"+prop)
		print "Verifying the uploaded package\n"
		time.sleep(10)
		uploadCheck();

def uploadInterface():
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/locks")
	group=folder.split('_')
	m=len(group)
	split_fold = '_'.join(group[:m-1])
	fold_up = split_fold.upper()
	pkg = pack[:pack.index('.')]
	prop = pack+"_properties"
	groups=pkg.split('_')
	n=len(groups)
	split_pkg = '_'.join(groups[n-2:n-1]), '_'.join(groups[:n])
	d = os.system("ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+split_pkg[0]+"/ | grep "+split_pkg[1])
	if d == 0:
		print "Already present in Nexus "+pack
		os.system("rm "+pack)
		os.system("rm "+prop)		
		exit(1)
	else:
		fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+split_pkg[0]+"/"+split_pkg[1]+"/"+pack)
		time.sleep(10)
		uploadCheck();
		fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+split_pkg[0]+"/"+split_pkg[1]+"/"+prop)
		print "Verifying the uploaded package\n"
		time.sleep(10)
		uploadCheck();

def uploadETL():
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/locks")
	group=folder.split('_')
	m=len(group)
	split_fold = '_'.join(group[:m-1])
	fold_up = split_fold.upper()
	pkg = pack[:pack.index('.')]
	prop = pack+"_properties"
	groups=pkg.split('_')
	n=len(groups)
	split_pkg = '_'.join(groups[n-2:n-1]), '_'.join(groups[:n])
	d = os.system("ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+split_pkg[0]+"/ | grep "+split_pkg[1])
	if d == 0:
		print "Already present in Nexus "+pack
		os.system("rm "+pack)
		os.system("rm "+prop)		
		exit(1)
	else:
		fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+split_pkg[0]+"/"+split_pkg[1]+"/"+pack)
		time.sleep(10)
		uploadCheck();
		fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+split_pkg[0]+"/"+split_pkg[1]+"/"+prop)
		print "Verifying the uploaded package\n"
		time.sleep(10)
		uploadCheck();
			
def uploadReport():
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/locks")
	pkg = pack[:pack.index('.')]
	prop = pack+"_properties"
	groups=pkg.split('_')
	n=len(groups)
	split_pkg = '_'.join(groups[:n-1]), '_'.join(groups[n-1:])
	d = os.system("ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/"+folder+"/"+split_pkg[0]+"/ | grep "+split_pkg[1])
	if d == 0:
		print "Already present in Nexus "+pack
		os.system("rm "+pack)
		os.system("rm "+prop)		
		exit(1)
	else:
		fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/"+folder+"/"+split_pkg[0]+"/"+split_pkg[1]+"/"+pack)
		time.sleep(10)
		uploadCheck();
		fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/"+folder+"/"+split_pkg[0]+"/"+split_pkg[1]+"/"+prop)
		print "Verifying the uploaded package\n"
		time.sleep(10)
		uploadCheck();
			
def uploadFD():
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/locks")
	pg = folder[:folder.index('_etl')]
	fold_up = pg.upper()
	pkg = pack[:pack.index('.')]
	try:
		rstate = re.search(r'R\d+[A-Z]',pkg).group()
		y = re.search(r'(.+)R\d+[A-Z]',pkg).group()
		y = y[:y.index('_'+rstate)]
		d = os.system("ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+rstate+"/"+y+"/ | grep "+pack)
		if d == 0:
			print "Already present in Nexus "+pack
			os.system("rm "+pack)
			os.system("rm "+prop)			
			exit(1)
		else:
			fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+rstate+"/"+y+"/"+pack)
			time.sleep(10)
			uploadCheck();
			fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+rstate+"/"+y+"/"+prop)
			print "Verifying the uploaded package\n"
			time.sleep(10)
			uploadCheck();
	except Exception:
		fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+pkg+"/"+pack)
		time.sleep(10)
		uploadCheck();
		fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+pkg+"/"+prop)
		print "Verifying the uploaded package\n"
		time.sleep(10)
		uploadCheck();

def uploadRealnode():
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/locks")
	pkg = pack[:pack.index('.')]
	prop = pack+"_properties"
	d = os.system("ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/"+folder+"/ | grep "+pack)
	if d == 0:
		print "Already present in Nexus "+pack
		os.system("rm "+pack)
		os.system("rm "+prop)		
		exit(1)
	else:
		fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/"+folder+"/"+pack)
		time.sleep(10)
		uploadCheck();
		fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/"+folder+"/"+prop)
		print "Verifying the uploaded package\n"
		time.sleep(10)
		uploadCheck();

def uploadDIM():
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/locks")
	pkg = pack[:pack.index('.')]
	prop = pack+"_properties"
	rstate = re.search(r'R\d+[A-Z]',pkg).group()
	if "FD" in folder:
		y = re.search(r'(.+)R\d+[A-Z]',pkg).group()
		y = y[:y.index('_'+rstate)]
	else:
		y = pkg
	d = os.system("ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp/DIM/"+folder+"/"+rstate+"/"+y+"/ | grep "+pack)
	if d == 0:
		print "Already present in Nexus "+pack
		os.system("rm "+pack)
		os.system("rm "+prop)		
		exit(1)
	else:
		fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/DIM/"+folder+"/"+rstate+"/"+y+"/"+pack)
		time.sleep(10)
		uploadCheck();
		fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/DIM/"+folder+"/"+rstate+"/"+y+"/"+prop)
		print "Verifying the uploaded package\n"
		time.sleep(10)
		uploadCheck();

def deletePkg():
	#pkgs = dir[dir.rindex('stats')+1:]
	#kgs = pkgs[pkgs.index('/')+1:]
	pkgs = dir[dir.rindex('stats'):]
	pkg = pkgs[pkgs.rindex('/')+1:]
	pat = pkgs[:pkgs.rindex('/')+1]
	d = os.system("ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/"+pat+" | grep "+pkg)
	if d==0:
		os.system("curl -v -u esjkadm100:Naples!0512 --request DELETE "+dir)
		f = os.system("ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/"+pat+" | grep "+pkg)
		if f==0:
			print "\n\n*****"+dir+" is not deleted*****\n\n"
		else:
			print "\n\n*****"+dir+" is deleted successfully*****\n\n"
	else:
		print "\n\n*****"+dir+" doesn't exist in nexus*****\n\n"

def uploadSpecial():
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/locks")
	pg = folder[:folder.index('_etl')]
	fold_up = pg.upper()
	if "udm_etl/Customer" in folder:
		pkg = pack[:pack.index('.')]
		rstate = re.search(r'R\d+[A-Z]',pkg).group()
		if "Manual" in folder:
			y = re.search(r'(.+)R\d+[A-Z]',pkg).group()
			y = y[:y.index('_'+rstate)]
		else:
			y = pkg
		d = os.system("ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+rstate+"/ | grep "+y)
		if d == 0:
			print "Already present in Nexus "+pack
			os.system("rm "+pack)
			os.system("rm "+prop)
			exit(1)
		else:
			fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+rstate+"/"+y+"/"+pack)
			time.sleep(10)
			uploadCheck();
			fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+rstate+"/"+y+"/"+prop)
			print "Verifying the uploaded package\n"
			time.sleep(10)
			uploadCheck();
	if "erbsg2_etl/CSV_PM" in folder:
		pkg = pack[:pack.rindex('.')]
		d = os.system("ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+pkg+"/ | grep "+pack)
		if d == 0:
			print "Already present in Nexus "+pack
			os.system("rm "+pack)
			os.system("rm "+prop)
			exit(1)
		else:
			fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+pkg+"/"+pack)
			time.sleep(10)
			uploadCheck();
			fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+pkg+"/"+prop)
			print "Verifying the uploaded package\n"
			time.sleep(10)
			uploadCheck();
	if "ipprobe_etl/TWAMP_doc" in folder:
		d = os.system("ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/ | grep "+pack)
		if d == 0:
			print "Already present in Nexus "+pack
			os.system("rm "+pack)
			os.system("rm "+prop)
			exit(1)
		else:
			fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+pack)
			time.sleep(10)
			uploadCheck();
			fd = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/tp/"+fold_up+"/"+folder+"/"+prop)
			print "Verifying the uploaded package\n"
			time.sleep(10)
			uploadCheck();
			
def uploadPLM():
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/locks")
	d = os.system("ls /proj/eiffel013_config_arm1s11/eiffel_home/storage/releases/com/ericsson/eniq/stats/"+folder+"/ | grep "+pack)
	if d == 0:
		print "Already present in Nexus "+pack
		os.system("rm "+pack)
		os.system("rm "+prop)		
		exit(1)
	else:
		d = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+pack+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/"+folder+"/"+pack)
		time.sleep(10)
		uploadCheck();
		d = os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+prop+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/"+folder+"/"+prop)
		print "Verifying the uploaded package\n"
		time.sleep(10)
		uploadCheck();

		
if 'upload' in check:							
	createProp();
if "kpi" in folder:
	uploadKPI();
if "_bo" in folder:
	uploadBO();
if "_etl" in folder:
	if "FD" in folder:
		uploadFD();
	elif "ipprobe_etl/TWAMP" in folder or "erbsg2_etl/CSV_PM" in folder or "udm_etl/Customer" in folder:
		uploadSpecial();
	else:
		uploadETL();
if "tp_plm" in folder:
	uploadPLM();
if "_interface" in folder:
	uploadInterface();
if "Report_Package" in folder:
	uploadReport();
if "Realnode_Files" in folder:
	uploadRealnode();
if "dim" in folder:
	uploadDIM();
if "delete" in check:
	deletePkg();
	fd = os.system("cat /proj/eiffel004_config/fem160/eiffel_home/jobs/TP_Nexus_Upload/builds/"+num+"/log| grep -i error")
	fc = os.system("cat /proj/eiffel004_config/fem160/eiffel_home/jobs/TP_Nexus_Upload/builds/"+num+"/log| grep -i curl:")
	if fd == 0 or fc == 0:
		print "\n\n*****"+dir+" deletion is failed*****\n\n"
		exit(1)
	else:
		print "\n\n*****"+dir+" is deleted*****\n\n"
if 'upload' in check:
	os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/locks")
	os.system("rm "+pack+" "+prop)
