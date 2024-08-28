import re
import sys
import requests
import base64
from bs4 import BeautifulSoup
import random
from datetime import datetime, timedelta, date
import calendar
#import paramiko

# today1 = "Jun 17"
# today = "17/06"
days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
yesterday = date.today() - timedelta(days=1)
today1 = yesterday.strftime("%b %d")
today = yesterday.strftime("%d/%m")
year = int(yesterday.strftime("%y"))
mon = int(yesterday.strftime("%m"))
day = int(yesterday.strftime("%d"))
day_week = days[calendar.weekday(year,mon,day)]
#day_week = days[calendar.weekday(2019,6,17)]
pf_tc_file = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/result.txt'
#tp_tc_file = "/proj/eiffel004_config/fem160/eiffel_home/bin/tp_tc.txt"

if(int(day)-10 < 0):
        day=int(day)
        day1=day+1

        day = str(day)
        day1 = str(day1)

def Vapp():
	if day_week == "Monday":
		f = open("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/vapp_details.txt",'w')
	else:
		f = open("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/vapp_details.txt",'a')
	job_link = "https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/vApp_II_Pipeline/job/ES_CDB_Vapp_NMI/"
	pipeline_link = "https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/vApp_II_Pipeline/job/DHCP_Test/"
	pwd = base64.b64decode("TmFwbGVzITA1MTI=")
	pipeline_page = requests.get(pipeline_link, auth=('esjkadm100', pwd))
	pipeline_contents1 = BeautifulSoup(pipeline_page.content, 'html.parser')
	pipeline_contents = pipeline_contents1.prettify()
	pipelines = pipeline_contents.split("\n")
	today_present = False
	flag = 1
	vapp_status = -1
	loops,passed,fail = [0] *3 
	for line1 in pipelines:
		if today1 in line1:
			loops = loops + 1
			today_present = True
			page = requests.get(job_link, auth=('esjkadm100', pwd))
			soup = BeautifulSoup(page.content, 'html.parser')
			contents = soup.prettify()
			lines = contents.split("\n")
			run_status = False
			for index,line in enumerate(lines):
				if today1 in line:
					run_status = True
					if 'tooltip="Success &gt; Console Output"' in lines[index-9]:
						vapp_status = 1
						passed = passed + 1
					if 'tooltip="Failed &gt; Console Output"' in lines[index-9]:
						vapp_status = 0
						fail = fail + 1
					break
				if not run_status:
					vapp_status = 0
			if not run_status:
				fail = fail + 1
		#if today_present:
		#	break
					
			
	total = 77
	if vapp_status =='1':
		test_pass = 61
	elif vapp_status =='0':
		test_pass = 16
	else:
		test_pass = 0
	test_fail = total - test_pass


	#print day_week+"::"+str(loops)+"::"+str(passed)+"/"+str(fail)+"::"+str(total)+"::"+str(test_pass)+"/"+str(test_fail)
	f.write(day_week+"::"+str(loops)+"::"+str(passed)+"/"+str(fail)+"::"+str(total)+"::"+str(test_pass)+"/"+str(test_fail)+'\n')
	#f.write("Vapp End\n")
	f.close()
	
def kgb_status(pipeline_link,job_link):
	pwd = base64.b64decode("TmFwbGVzITA1MTI=")
	pipeline_page = requests.get(pipeline_link, auth=('esjkadm100', pwd))
	soup1 = BeautifulSoup(pipeline_page.content, 'html.parser')
	pipeline_contents = soup1.prettify()
	pipelines = pipeline_contents.split("\n")
	today_present = False
	status = -1
	trigger_status = -1
	loops,passed,fail = [0]*3
	for index1,line1 in enumerate(pipelines):
		if today1 in line1:
			today_present = True
			if 'tooltip="Success &gt; Console Output"' in pipelines[index1-9] or 'tooltip="Unstable &gt; Console Output"' in pipelines[index1-9]:
				trigger_status = 1
				loops = loops + 1
			if 'tooltip="Failed &gt; Console Output"' in pipelines[index1-9]:
				trigger_status = 0
				#loops = "No checkins"
			if(trigger_status):
				page = requests.get(job_link, auth=('esjkadm100', pwd))
				soup = BeautifulSoup(page.content, 'html.parser')
				contents = soup.prettify()
				lines = contents.split("\n")
				run_status = False
				for index,line in enumerate(lines):
					if today1 in line:
						run_status = True
						if 'tooltip="Success &gt; Console Output"' in lines[index-9]:
							status = 1
							passed = passed + 1
						if 'tooltip="Failed &gt; Console Output"' in lines[index-9]:
							status = 0
							fail = fail + 1
						break
					if not run_status:
						status = 0
					
		#if today_present:
		#	break
	if loops ==1 and passed ==0:
		fail = 1;
	return str(loops),str(passed),str(fail)

def pf_tc (tc_file):
	f = open (tc_file, 'r')
	lines = f.readlines()
	f.close()
	tc_passed,tc_total = 0,0
	for line in lines:
		if today in line:
			tc_passed = line.strip().split("::")[1]
			tc_total = line.strip().split("::")[2]
	return tc_passed,tc_total,int(tc_total)-int(tc_passed)
	
def infra_tc(job_link):
	pwd = base64.b64decode("TmFwbGVzITA1MTI=")
	job_page = requests.get(job_link, auth=('esjkadm100', pwd))
	job_contents = job_page.content
	job_lines = job_contents.split("\n")
	pass_tc, total_tc = 0,0
	today_present = False
	for line in job_lines:
		if today1 in line:
			today_present = True
			console_link = re.search(r'href="(.+)" class="build-health-link"', line).groups()[0]
			console_link = "https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443"+console_link+"/console"
			console_page = requests.get(console_link, auth=('esjkadm100', pwd))
			console_contents = console_page.content
			console_lines = console_contents.split("\n")
			for cline in console_lines:
				if "Total tests run" in cline:
					tc = cline.strip().split("span>")[1]
					total, fail,skip = tc.split(",")
					total_tc = int(total.split(":")[1].strip())
					fail_tc = int(fail.split(":")[1].strip())
					skip_tc = int(skip.split(":")[1].strip())
					pass_tc = total_tc - fail_tc - skip_tc

		if today_present:
			break
	return str(pass_tc),str(total_tc),total_tc-pass_tc
	

def tp_tc(job_link):
	pwd = base64.b64decode("TmFwbGVzITA1MTI=")
	job_page = requests.get(job_link, auth=('esjkadm100', pwd))
	job_contents = job_page.content
	job_lines = job_contents.split("\n")
	pass_tc, fail_tc = 0,0
	today_present = False
	for line in job_lines:
		if today1 in line:
			today_present = True
			console_link = re.search(r'href="(.+)" class="build-health-link"', line).groups()[0]
			console_link = "https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443"+console_link+"/console"
			console_page = requests.get(console_link, auth=('esjkadm100', pwd))
			soup2 = BeautifulSoup(console_page.content, 'html.parser')
			#console_contents = console_page.content
			console_contents = soup2.prettify()
			console_lines = console_contents.split("\n")
			for cline in console_lines:
				if "PASS RT" in cline:
					tc = cline.strip().split("span>")[1]
					pass_tc = str(tc.split("=")[1].strip())
				if "FAIL RT" in cline:
					tc = cline.strip().split("span>")[1]
					fail_tc = str(tc.split("=")[1].strip())
		if today_present:
			break
	total_tc = int(pass_tc) + int(fail_tc)
	return str(pass_tc),str(total_tc),str(fail_tc)
	
	
def pf_daily_tc(job_link):
	pwd = base64.b64decode("TmFwbGVzITA1MTI=")
	job_page = requests.get(job_link, auth=('esjkadm100', pwd))
	job_contents = job_page.content
	job_lines = job_contents.split("\n")
	pass_tc, total_tc, fail_tc = 0,0 ,0
	today_present = False
	for line in job_lines:
		if today1 in line:
			today_present = True
			#console_link = re.search(r'href="(.+)" class="build-health-link"', line).groups()[0]
			#console_link = "https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443"+console_link+"/console"
			console_link = job_link+"lastBuild/consoleFull"
			print console_link
			console_page = requests.get(console_link, auth=('esjkadm100', pwd))
			console_contents = console_page.content
			console_lines = console_contents.split("\n")
			pass_tc = re.search(r'Pass=(\d+)',console_contents).groups()[0]
			fail_tc = re.search(r'Fail=(\d+)',console_contents).groups()[0]
			total_tc = re.search(r'Total=(\d+)',console_contents).groups()[0]
				
				
		if today_present:
			break
	return str(pass_tc),str(total_tc),str(fail_tc)
	
	
#Vapp();
pf_pipeline_link = 'https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/PF_KGB/job/PF_KGB_PACKAGE_CHECKIN/'
pf_job_link = 'https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/PF_KGB/job/PF_KGB_TAF_TESTCASES/'
pf_loops,pf_passed,pf_failed,pf_tc_passed,pf_tc_total,pf_tc_failed = [0]*6
pf_loops,pf_passed,pf_failed = kgb_status(pf_pipeline_link,pf_job_link)
pf_tc_passed,pf_tc_total,pf_tc_failed = pf_tc(pf_tc_file)
f = open("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/pipeline_details.txt",'a')
f.write("PF KGB 1\n")
f.write(day_week+"::"+str(pf_loops)+"::"+str(pf_passed)+"/"+str(pf_failed)+"::"+str(pf_tc_total)+"::"+str(pf_tc_passed)+"/"+str(pf_tc_failed)+"\n")
infra_job_link = 'https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/INFRA_KGB_Pipeline/job/INFRA_KGB_TAF/'
infra_pipeline_link = 'https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/INFRA_KGB_Pipeline/job/INFRA_KGB_Parameters/'
infra_loops,infra_passed,infra_failed,infra_tc_passed,infra_tc_total,infra_tc_failed = [0]*6
infra_loops,infra_passed,infra_failed = kgb_status(infra_pipeline_link,infra_job_link)
infra_tc_passed,infra_tc_total,infra_tc_failed = infra_tc(infra_job_link)
if infra_loops=='0':
	infra_tc_passed = 0
	infra_tc_total = 0
	infra_tc_failed = 0
f.write("Infra KGB\n")
f.write(day_week+"::"+str(infra_loops)+"::"+str(infra_passed)+"/"+str(infra_failed)+"::"+str(infra_tc_total)+"::"+str(infra_tc_passed)+"/"+str(infra_tc_failed)+"\n")
tp_job_link = 'https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/TP_KGB_Linux/job/TP_KGB_RT_Linux/'
tp_pipeline_link = 'https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/TP_KGB_Linux/job/TP_KGB_CHECKIN_Linux/'
tp_loops,tp_passed,tp_failed,tp_tc_passed,tp_tc_total,tp_tc_failed = [0]*6
tp_loops,tp_passed,tp_failed = kgb_status(tp_pipeline_link,tp_job_link)
tp_tc_passed,tp_tc_total,tp_tc_failed = tp_tc(tp_job_link)
##tp_tc_passed,tp_tc_total,tp_tc_failed = pf_tp_tc(tp_tc_file)
f.write("TP KGB\n")
f.write(day_week+"::"+str(tp_loops)+"::"+str(tp_passed)+"/"+str(tp_failed)+"::"+str(tp_tc_total)+"::"+str(tp_tc_passed)+"/"+str(tp_tc_failed)+"\n")
pf_daily_job_link = "https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/PF_KGB_Daily_Pipeline/job/PF_TAF_DAILY/"
pf_daily_pipeline_link  = "https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/PF_KGB_Daily_Pipeline/job/GET_LATEST_VAPP/"
pf_daily_tc_link = "https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/PF_KGB_Daily_Pipeline/job/PF_KGB_Mail/"
pf_daily_loops,pf_daily_passed,pf_daily_failed,pf_daily_tc_passed,pf_daily_tc_total,pf_daily_tc_failed = [0]*6
pf_daily_loops,pf_daily_passed,pf_daily_failed = kgb_status(pf_daily_pipeline_link,pf_daily_job_link)
pf_daily_tc_passed,pf_daily_tc_total,pf_daily_tc_failed = pf_daily_tc(pf_daily_tc_link)
f.write("Standalone PF KGB\n")
f.write(day_week+"::"+str(pf_daily_loops)+"::"+str(pf_daily_passed)+"/"+str(pf_daily_failed)+"::"+str(pf_daily_tc_total)+"::"+str(pf_daily_tc_passed)+"/"+str(pf_daily_tc_failed)+"\n")
if day_week == "Friday":
	f.write("PF KGB 1")
f.close()
