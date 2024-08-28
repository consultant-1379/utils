from subprocess import *

def getCmdOutput(cmd):
    proc = Popen(cmd, shell=True, stdout=PIPE, )
    outputVal = proc.communicate()[0]
    return outputVal
	
Infra_TCs = {"testInstallationDirectory":"ls /eniq/ | grep installation | wc -l", "testENIQS_STATS_Directory":"ls /net/10.45.192.153/JUMP/ | grep ENIQ_STATS | wc -l"}
NMI_TCs = {"testENIQ_Sentinel_Server":"cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i \"Successfully installed ENIQ Sentinel server\" | wc -l", \
			"testENIQ_Sym_Info":"cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i \"Successfully created DB Sym Links\" | wc -l",\
			"testENIQ_LUN_Info":"cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i \"Successfully created LUN Map ini file\" | wc -l",\
			"testENIQ_create_repdb":"cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i \"Successfully completed stage - create_repdb\" | wc -l",\
			"testENIQ_SYBASE_IQ":"cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i \"Successfully installed SYBASE IQ\" | wc -l",\
			"testENIQ_SYBASE_ASA":"cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i \"Successfully installed SYBASE ASA\" | wc -l",\
			"testENIQ_PLATFORM":"cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i \"Successfully installed ENIQ Platform\" | wc -l",\
			"testENIQ_FEATURES":"cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i \"Successfully installed Features\" | wc -l",\
			"testENIQ_SERVICE_SCRIPTS":"cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i \"Successfully installed Service scripts\" | wc -l",\
			"testENIQ_STATUS":"cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i \"Successfully updated ENIQ status file\" | wc -l",\
			"testENIQ_SW":"cat /eniq/local_logs/installation/ieatrcx6575_install.log | egrep -i \"ENIQ SW successfully installed\" | wc -l"}
Sanity_TCs = {"testENIQS_pmdata_wifi":"df -hk | grep -w pmdata_wifi | wc -l | grep 0",\
			"testENIQS_nas":"df -hk | grep nas | wc -l | grep 22",\
			"testENIQS_DWHDB_STOP":"systemctl stop eniq-dwhdb; systemctl show -p ActiveState eniq-dwhdb | cut -f2 -d'=' | grep inactive",\
			"testENIQS_DWHDB_RESTART":"systemctl restart eniq-dwhdb; systemctl show -p ActiveState eniq-dwhdb | cut -f2 -d'=' | grep active",\
			"testENIQS_NASd_service":"systemctl start NASd.service;systemctl status NASd.service | grep 'Started Storage NASd'",\
			"testENIQS_STOP_MILESTONE":"systemctl stop NAS-online.service;systemctl status NAS-online.service | grep 'Stopped Milestone NAS Service'",\
			"testENIQS_START_MILESTONE":"systemctl start NAS-online.service;systemctl status NAS-online.service | grep 'Started Milestone NAS Service'",\
			"testENIQS_DCUSER":"id dcuser | awk \"{print $2}\" | grep dc5000",\
			"testENIQS_SystemMaxUse":"cat /etc/systemd/journald.conf | grep SystemMaxUse | cut -f2 -d'=' | grep 8G"}
			
print "****************************************************************"
print "************************Infra Test Cases************************"
print "****************************************************************\n"

for infra in Infra_TCs.keys():
	outputVal = getCmdOutput(Infra_TCs[infra])
	if outputVal.strip() == '1':
		print "{}: PASS".format(infra)
	else:
		print "{}: FAIL".format(infra)
	
print "\n\n**************************************************************"
print "************************NMI Test Cases************************"
print "**************************************************************\n"

for nmi in NMI_TCs.keys():
	outputVal = getCmdOutput(NMI_TCs[nmi])
	if outputVal.strip() == '1':
		print "{}: PASS".format(nmi)
	else:
		print "{}: FAIL".format(nmi)
		
print "\n\n*****************************************************************"
print "************************Sanity Test Cases************************"
print "*****************************************************************\n"

for sanity in Sanity_TCs.keys():
	outputVal = getCmdOutput(Sanity_TCs[sanity])
	val = Sanity_TCs[sanity].split("grep")[-1].strip().strip("'")
	#print "***" + str(val)
	if val in outputVal.strip():
		print "{}: PASS".format(sanity)
	else:
		print "{}: FAIL".format(sanity)