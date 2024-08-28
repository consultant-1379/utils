import os
import datetime
import sys
import subprocess
import pexpect

def infra_checkins_count():
	os.chdir('/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/infra_spartan_20_2/infra_spartan')
	os.system("git pull")
	#p = subprocess.Popen("git rev-list --since=%s origin/%s | wc -l" %(today2,sys.argv[1]), stdout=subprocess.PIPE, shell=True)
	p = subprocess.check_output("git rev-list --since=%s origin/%s | wc -l" %(today2,sys.argv[1]), shell=True)
	print "git rev-list --since=%s origin/%s | wc -l" %(today2,sys.argv[1])
	count = p.strip()
	print "count: "+count
	return int(count)
	
def security_checkins_count():
	os.chdir('/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/Security_Spartan/')
	#os.system("git pull")
	child = pexpect.spawn('git pull')
        child.expect('Password')
        child.sendline('Shubh@8869')

	#p = subprocess.Popen("git rev-list --since=%s origin/%s | wc -l" %(today2,sys.argv[1]), stdout=subprocess.PIPE, shell=True)
	p = subprocess.check_output("git rev-list --since=%s origin/%s | wc -l" %(today2,sys.argv[1]), shell=True)
	print "git rev-list --since=%s origin/%s | wc -l" %(today2,sys.argv[1])
	count = p.strip()
	print "count: "+count
	return int(count)
	
if "19.2" in sys.argv[1]:
	from config import *
	print "importing config.py"
if "19.4" in sys.argv[1]:
	from config_19_4 import *
	print "importing config_19_4.py"
if "20.2" in sys.argv[1]:
	from config_20_2 import *
	print "importing config_20_2.py"
if "20.4" in sys.argv[1]:
        from config_20_4 import *
        print "importing config_20_4.py"

today = datetime.datetime.now().strftime ("%d-%m-%Y")
today2 = datetime.datetime.now().strftime ("%d-%b-%y")
#today = '16-02-2020'
#today2 = "16-Feb-20"


	
infra_checkins = infra_checkins_count() + security_checkins_count()
if today in date:
	infra_checkins_data[-1] = infra_checkins
else:
	infra_checkins_data.append(infra_checkins)
print infra_checkins_data

f = open("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/%s"%sys.argv[2],"w+")
f.write("date=[" + ",".join([ "'" + str(x) + "'" for x in date ]) + "]" + os.linesep)
f.write("tp_data=[" + ",".join([str(x) for x in tp_data ]) + "]" + os.linesep)
f.write("pf_data=[" + ",".join([str(x) for x in pf_data ]) + "]" + os.linesep)
f.write("infra_data=[" + ",".join([str(x) for x in infra_data ]) + "]" + os.linesep)
f.write("kpi_data=[" + ",".join([str(x) for x in kpi_data ]) + "]" + os.linesep)
f.write("nmi_data=["+ ",".join([str(x) for x in nmi_data ]) + "]" + os.linesep)

f.write("tp_checkins_data=[" + ",".join([str(x) for x in tp_checkins_data ]) + "]" + os.linesep)
f.write("pf_checkins_data=[" + ",".join([str(x) for x in pf_checkins_data ]) + "]" + os.linesep)
f.write("kpi_checkins_data=[" + ",".join([str(x) for x in kpi_checkins_data ]) + "]" + os.linesep)
f.write("nmi_checkins_data=[" + ",".join([str(x) for x in nmi_checkins_data ]) + "]" + os.linesep)
f.write("infra_checkins_data=[" + ",".join([str(x) for x in infra_checkins_data ]) + "]" + os.linesep)

f.close()
