import re
import sys
import requests
import base64
from bs4 import BeautifulSoup
import random
#import paramiko
from datetime import datetime, timedelta
import os.path
from os import path

pf_kgb_status, tp_kgb_status, infra_kgb_status = [-1]*3
# today = "24/01"
# today1 = 'Jan 24'
day = datetime.strftime(datetime.now() - timedelta(1), '%d')
mon = datetime.strftime(datetime.now() - timedelta(1), '%b')
if '0' in day[0]:
	day = day[1]
today = sys.argv[3]

if(int(day)-10 < 0):
        day=int(day)
        day1=day+1

        day = str(day)
        day1 = str(day1)

today1 = mon+" "+day
release = sys.argv[1]
shipment = sys.argv[2]
filename = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/STATUS_%s_%s_LLSV3_ST.html' %(release,shipment)
nmi_file = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/STATUS_WEEK_%s_%s_LLSV3_ST.html' %(release,shipment)
kgb_radiator = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/kgb_radiator_'+shipment+'.html'
kgb_radiator_content = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/kgb_radiator_content.html'
pf_kgb_taf_link, infra_kgb_taf_link = "", ""
pf_tc_file = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/result.txt'
tp_tc_file = "/proj/eiffel004_config/fem160/eiffel_home/bin/tp_tc.txt"
maintrack = shipment +" LINUX MAINTRACK is OPEN"
maintrack_color = '#15c415'


def pf_tp_tc(tc_file):
	f = open (tc_file, 'r')
	lines = f.readlines()
	f.close()
	tc_passed,tc_total = 0,0
	for line in lines:
		if today in line:
			tc_passed = line.strip().split("::")[1]
			tc_total = line.strip().split("::")[2]
	print(tc_passed)
	print(int(tc_total)-int(tc_passed))
	return tc_passed,int(tc_total)-int(tc_passed)

def nmi_kgb(task):
	smoke_passed, smoke_total, passed, total = [0]*4
	if path.exists(nmi_file):
		f = open(nmi_file,'r')
		lines = f.readlines()
		f.close()
		nmi_kgb_status = -1
		log_tc = '0/0'
		smoke_tc = '0/0'
		nmi_log_link,nmi_smoke_link,server = "","",""
		flag,inside = 0,0
		for line in lines:
			if today in line:
				flag = 1
				
			if flag:
				if 'Blade '+task+'_Test_Status' in line and today in line:
					inside = 1
					if 'td bgcolor="#04B45F"' in line  or 'td bgcolor="orange"' in line:
							nmi_kgb_status = 1
					if 'td bgcolor="red"' in line:
							nmi_kgb_status = 0
					if '<a href' in line:
						nmi_ii_tc_file = re.search(r'a href="https://eniqdmt.seli.wh.rnd.internal.ericsson.com/ibw_logs/EXEC_SUM/KGB_CI/WEEK/'+release+'/(.*)"',line).groups()[0]
						nmi_ii_tc_file = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/nmi/" + nmi_ii_tc_file
						file = open(nmi_ii_tc_file,"r")
						nmi_lines = file.readlines()
						file.close()
						first_server = False
						for nmi_line in nmi_lines:
							if '<td bgcolor="#0B3861"><font face="Verdana, Arial, Helvetica, sans-serif" size="2"><font color="white">' in nmi_line and not first_server:
								if re.search(r'>(\w+)<',nmi_line):
									server = re.search(r'>(\w+)<',nmi_line).groups()[0]
								print("inside server", server)
								first_server = True
							if "Blade "+task+"_Test_Status" in nmi_line:
								if re.search(r">(\d+/\d+) Cases Passed", nmi_line):
									test_cases = re.search(r">(\d+/\d+) Cases Passed", nmi_line).groups()
									passed, total  = test_cases[0].split("/")
								log_tc = passed+'/'+total
								match = re.search(r'href=[\'"]?([^\'" >]+)', nmi_line)
								if match:
									nmi_log_link = match.group(1)
							if "Blade "+task+"_smoke_Test_Status" in nmi_line:
								if re.search(r">(\d+/\d+) Cases Passed", nmi_line):
									test_cases = re.search(r">(\d+/\d+) Cases Passed", nmi_line).groups()
									smoke_passed, smoke_total  = test_cases[0].split("/")
								smoke_tc = str(smoke_passed) +'/'+ str(smoke_total)
								match2 = re.search(r'href=[\'"]?([^\'" >]+)', nmi_line)
								if match2:
									nmi_smoke_link = match2.group(1)
							if "FinishPoint" in  nmi_line:
								break
			if flag == 1 and inside == 1:
				break
		return nmi_kgb_status, log_tc, smoke_tc, nmi_log_link, nmi_smoke_link, server
	return -1,"0","0","","",""

def edit_icon(job):
	if job == 1:   ##job - boolean
		icon ="http://eniqdmt.seli.wh.rnd.internal.ericsson.com/tick.svg" 
	elif job == -1:
		icon = "http://eniqdmt.seli.wh.rnd.internal.ericsson.com/artifacts_icon.svg" 
	else :
		icon = "http://eniqdmt.seli.wh.rnd.internal.ericsson.com/close-window.png"
	return icon

	
def kgb_status(job_link,pipeline_link):
	pwd = base64.b64decode("TmFwbGVzITA1MTI=")
	pipeline_page = requests.get(pipeline_link, auth=('esjkadm100', pwd))
	soup1 = BeautifulSoup(pipeline_page.content, 'html.parser')
	pipeline_contents = soup1.prettify()
	pipelines = pipeline_contents.split("\n")
	today_present = False
	status = -1
	trigger_status = -1
	for index1,line1 in enumerate(pipelines):
		if today1 in line1:
			today_present = True
			if 'tooltip="Success &gt; Console Output"' in pipelines[index1-9] or 'tooltip="Unstable &gt; Console Output"' in pipelines[index1-9]:
				trigger_status = 1
			if 'tooltip="Failed &gt; Console Output"' in pipelines[index1-9]:
				trigger_status = 0
			if(trigger_status):
				page = requests.get(job_link, auth=('esjkadm100', pwd))
				soup = BeautifulSoup(page.content, 'html.parser')
				contents = soup.prettify()
				lines = contents.split("\n")
				run_status = False
				for index,line in enumerate(lines):
					if today1 in line:
						run_status = True
						print("index of date:", index)
						if 'tooltip="Success &gt; Console Output"' in lines[index-9] or 'tooltip="Unstable &gt; Console Output"' in pipelines[index1-9]:
							status = 1
						if 'tooltip="Failed &gt; Console Output"' in lines[index-9]:
							status = 0
						break
					if not run_status:
						status = 0
					
		if today_present:
			break
	return status
	
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
			#console_link = re.search(r'href="(.+)" class="build-health-link"', line).groups()[0]
			#console_link = "https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443"+console_link+"/console"
			console_link = job_link+"lastBuild/consoleFull" 
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
	return str(pass_tc)+ "/" + str(total_tc)
		
def kgb_tp_tc(job_link):
	pwd = base64.b64decode("TmFwbGVzITA1MTI=")
	job_page = requests.get(job_link, auth=('esjkadm100', pwd))
	job_contents = job_page.content
	job_lines = job_contents.split("\n")
	pass_tc, fail_tc = 0,0
	today_present = False
	for line in job_lines:
		if today1 in line:
			today_present = True
			#console_link = re.search(r'href="(.+)" class="build-health-link"', line).groups()[0]
			#console_link = "https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443"+console_link+"/console"
			console_link = job_link+"lastBuild/consoleFull" 
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
	return str(pass_tc), str(total_tc)
		
def server_name(job_server_link, fem):
	pwd = base64.b64decode("TmFwbGVzITA1MTI=")
	job_page = requests.get(job_server_link, auth=('esjkadm100', pwd))
	job_contents = job_page.content
	job_lines = job_contents.split("\n")
	name_server = ""
	today_present = False
	for line in job_lines:
		if today1 in line:
			today_present = True
			#console_link = re.search(r'href="(.+)" class="build-health-link"', line).groups()[0]
			#console_link = "https://"+fem+"-eiffel013.eiffel.gic.ericsson.se:8443"+console_link+"/consoleFull"
			console_link = job_server_link+"lastBuild/consoleFull"
			console_page = requests.get(console_link, auth=('esjkadm100', pwd))
			console_contents = console_page.content
			console_lines = console_contents.split("\n")
			for cline in console_lines:
				if 'atvts' in cline:
					name_server = re.search(r'@(.+) ~',cline).groups()[0]
					break
						
	return name_server
	
def taf_link(job_link):
	pwd = base64.b64decode("TmFwbGVzITA1MTI=")
	job_page = requests.get(job_link, auth=('esjkadm100', pwd))
	job_contents = job_page.content
	job_lines = job_contents.split("\n")
	console_link=" "
	for line in job_lines:
		if today1 in line:
			console_link = re.findall(r'<a href="(https.+)"><img src="/jenkins/plugin/allure-jenkins-plugin/img/icon.png" width="16" title="Allure Report"', line[:3000])
			break
	if len(console_link) > 0:
		return console_link[0]
	else:
		return console_link
	
	
pf_kgb_pipeline_link = 'https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/PF_KGB/job/PF_KGB_PACKAGE_INSTALL/'
pf_kgb_job_link = 'https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/PF_KGB/job/PF_KGB_TAF_TESTCASES/'
tp_kgb_job_link = 'https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/TP_KGB_Linux/job/TP_KGB_RT_Linux/'
tp_kgb_pipeline_link = 'https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/TP_KGB_Linux/job/TP_KGB_Install_Package/'
infra_kgb_job_link = 'https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/INFRA_KGB_Pipeline/job/INFRA_KGB_TAF/'
infra_kgb_pipeline_link = 'https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/INFRA_KGB_Pipeline/job/INFRA_KGB_Parameters/'
infra_job_server_link = "https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/INFRA_KGB_Pipeline/job/INFRA_KGB_Pre_requisite/"
pf_job_server_link = "https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/PF_KGB/job/PF_KGB_PACKAGE_INSTALL/"
tp_job_server_link = "https://fem5s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/TP_KGB_Linux/job/TP_KGB_Install_Package/"
pf_kgb_status = kgb_status(pf_kgb_job_link,pf_kgb_pipeline_link)
tp_kgb_status = kgb_status(tp_kgb_job_link, tp_kgb_pipeline_link)
print ("pf_kgb_status:"+str(pf_kgb_status))
print ("tp_kgb_status:"+str(tp_kgb_status))
pf_server = server_name(pf_job_server_link,"fem5s11") if pf_kgb_status !=-1 else ""
tp_server = server_name(tp_job_server_link,"fem5s11") if tp_kgb_status !=-1 else ""
#tp_server = 'atvts4142'
#tp_tc = kgb_tp_tc(tp_kgb_job_link) if tp_kgb_status != -1 else 0,0
infra_kgb_status = kgb_status(infra_kgb_job_link, infra_kgb_pipeline_link)
infra_kgb_tc = infra_tc(infra_kgb_job_link) if infra_kgb_status != -1 else "0/0 Cases passed"
infra_server = server_name(infra_job_server_link,"fem5s11") if infra_kgb_status != -1 else ""
infra_kgb_taf_link = taf_link(infra_kgb_job_link) if infra_kgb_status !=-1 else ""
pf_kgb_taf_link = taf_link(pf_kgb_job_link) if pf_kgb_status !=-1 else ""
#pf_kgb_taf_link = ""
nmi_kgb_ii_status, log_ii_tc, smoke_ii_tc, nmi_log_ii_link, nmi_smoke_ii_link, server_ii = nmi_kgb("ii")
nmi_kgb_ug_status, log_ug_tc, smoke_ug_tc, nmi_log_ug_link, nmi_smoke_ug_link, server_ug = nmi_kgb("ug")
nmi_kgb_rb_status, log_rb_tc, smoke_rb_tc, nmi_log_rb_link, nmi_smoke_rb_link, server_rb = nmi_kgb("rb")
print ("nmi_kgb_ii_status:",nmi_kgb_ii_status)
print ("nmi_kgb_ug_status:",nmi_kgb_ug_status)
print ("nmi_kgb_rb_status:",nmi_kgb_rb_status)

print("server",server_ii,server_ug, server_rb)
print pf_kgb_status
print tp_kgb_status
print infra_kgb_status

f = open (filename , 'r')
lines = f.readlines()
for line in lines:
	if 'Late' in line:
		maintrack = shipment + " LINUX MAINTRACK is CLOSED"
		maintrack_color = 'orange'
	if 'Until Code Freeze' in line:
		maintrack = shipment + " LINUX MAINTRACK is OPEN"
		maintrack_color = '#15c415'
f.close()

f = open(kgb_radiator_content,"r+")
lines = f.readlines()

for index, line in enumerate(lines):
	if "pf_kgb icon" in line:
		icon = edit_icon(pf_kgb_status)
		if pf_kgb_status == -1:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" title="Not Triggered" width="50" height="50"></a></div> <!-- pf_kgb icon-->'
		else:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_pf_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" width="50" height="50"></a></div> <!-- pf_kgb icon-->'
		lines[index+2] = '<div id="popup61_pf_%s'%sys.argv[3]+'" class="overlay">'	
		lines[index] = line
	if 'date' in line:
		line = '<font class="hoverEffectBox" face="Courier New" size="5" color="white">'+today+'<br></font><font id="date" face="Courier New" size="2" color="white"></font></td></tr></tbody></table></td><!--date-->'
		lines[index] = line
	if "tp_kgb icon" in line:
		icon = edit_icon(tp_kgb_status)
		if tp_kgb_status == -1:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" title="Not Triggered" width="50" height="50"></a></div> <!-- pf_kgb icon-->'
		else:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_tp_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" width="50" height="50"></a></div> <!-- pf_kgb icon-->'
		lines[index+3] = '<div id="popup61_tp_%s'%sys.argv[3]+'" class="overlay">'	
		lines[index] = line
	
	if "tp_kgb tc" in line:
		passed,total = kgb_tp_tc(tp_kgb_job_link)
		#passed,failed = 1444, 1670
		line = '<td border="1" align="center"><p><font face="Courier New" size="3" color="white">'+ str(passed) + '/'+ str(total) + ' Cases Passed</font></p></a></td><!--tp_kgb tc -->'
		lines[index] = line
	
	if "tp_kgb server" in line:
		lines[index] = '<table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="left"><font face="Courier New" size="6" color="white">'+tp_server+'</font></td></tr></tbody></table><!-- tp_kgb server -->'
	
	if "infra_kgb icon" in line:
		icon = edit_icon(infra_kgb_status)
		if infra_kgb_status == -1:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" title="Not Triggered" width="50" height="50"></a></div> <!-- infra_kgb icon-->'
		else:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_infra_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" width="50" height="50"></a></div> <!-- infra_kgb icon-->'
		lines[index+3] = '<div id="popup61_infra_%s'%sys.argv[3]+'" class="overlay">'	
		lines[index] = line	
	
	if "infra_kgb tc" in line:
		line = '<td border="1" align="center"><a href="'+str(infra_kgb_taf_link)+'"><p><font face="Courier New" size="3" color="white">'+ infra_kgb_tc +' Cases Passed</font></p></td><!-- infra_kgb tc-->'
		lines[index] = line
		
	if "infra_kgb server" in line:
		lines[index] = '<table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="left"><font face="Courier New" size="6" color="white">'+infra_server+'</font></td></tr></tbody></table><!-- infra_kgb server -->'
	
	if "pf_kgb tc" in line:
		passed,failed = pf_tp_tc(pf_tc_file)
		total = int(passed) + int(failed)
		lines[index] = '<td border="1" align="center"><a href="'+str(pf_kgb_taf_link)+'"><p><font face="Courier New" size="3" color="white">'+ str(passed) + '/'+ str(total) + ' Cases Passed</font></p></a></td><!-- pf_kgb tc-->'
		
	if "pf_kgb server" in line:
		lines[index] = '<table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="left"><font face="Courier New" size="6" color="white">'+pf_server+'</font></td></tr></tbody></table><!-- pf_kgb server -->'
	
	if "nmi_kgb_ii icon" in line:
		icon = edit_icon(nmi_kgb_ii_status)
		if nmi_kgb_ii_status == -1:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" title="Not Triggered" width="50" height="50"></a></div> <!-- nmi_kgb_ii icon-->'
		else:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_nmi_ii_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" width="50" height="50"></a></div> <!-- nmi_kgb_ii icon-->'
		lines[index+3] = '<div id="popup61_nmi_ii_%s'%sys.argv[3]+'" class="overlay">'	
		lines[index] = line
	
	if "nmi_kgb_ii log tc" in line:
		lines[index] = '<td border="1" align="center"><a href="'+nmi_log_ii_link+'"><p><font face="Courier New" size="3" color="white">'+ log_ii_tc + ' Cases Passed</font></p></a></td><!-- nmi_kgb_ii log tc-->'
	
	if "nmi_kgb_ii smoke tc" in line:
		lines[index] = '<td border="1" align="center"><a href="'+nmi_smoke_ii_link +'"><p><font face="Courier New" size="3" color="white">'+ smoke_ii_tc + ' Cases Passed</font></p></a></td><!-- nmi_kgb_ii smoke tc-->'
	
	if "nmi_kgb_ug icon" in line:
		icon = edit_icon(nmi_kgb_ug_status)
		if nmi_kgb_ug_status == -1:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" title="Not Triggered" width="50" height="50"></a></div> <!-- nmi_kgb_ug icon-->'
		else:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_nmi_ug_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" width="50" height="50"></a></div> <!-- nmi_kgb_ug icon-->'
		lines[index+3] = '<div id="popup61_nmi_ug_%s'%sys.argv[3]+'" class="overlay">'	
		lines[index] = line
	
	if "nmi_kgb_ug log tc" in line:
		lines[index] = '<td border="1" align="center"><a href="'+nmi_log_ug_link+'"><p><font face="Courier New" size="3" color="white">'+ log_ug_tc + ' Cases Passed</font></p></a></td><!-- nmi_kgb_ug log tc-->'
	
	if "nmi_kgb_ug smoke tc" in line:
		lines[index] = '<td border="1" align="center"><a href="'+nmi_smoke_ug_link +'"><p><font face="Courier New" size="3" color="white">'+ smoke_ug_tc + ' Cases Passed</font></p></a></td><!-- nmi_kgb_ug smoke tc-->'
	
	if "nmi_kgb_rb icon" in line:
		icon = edit_icon(nmi_kgb_rb_status)
		if nmi_kgb_rb_status == -1:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" title="Not Triggered" width="50" height="50"></a></div> <!-- nmi_kgb_ug icon-->'
		else:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_nmi_rb_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" width="50" height="50"></a></div> <!-- nmi_kgb_ug icon-->'
		lines[index+3] = '<div id="popup61_nmi_rb_%s'%sys.argv[3]+'" class="overlay">'	
		lines[index] = line
	
	if "nmi_kgb_rb log tc" in line:
		lines[index] = '<td border="1" align="center"><a href="'+nmi_log_rb_link+'"><p><font face="Courier New" size="3" color="white">'+ log_rb_tc + ' Cases Passed</font></p></a></td><!-- nmi_kgb_rb log tc-->'
	
	if "nmi_kgb_rb smoke tc" in line:
		lines[index] = '<td border="1" align="center"><a href="'+nmi_smoke_rb_link +'"><p><font face="Courier New" size="3" color="white">'+ smoke_rb_tc + ' Cases Passed</font></p></a></td><!-- nmi_kgb_rb smoke tc-->'
	
	if "nmi_kgb_ii server" in line:
		lines[index] = '<table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="left"><font face="Courier New" size="6" color="white">'+server_ii+'</font></td></tr></tbody></table><!-- nmi_kgb_ii server -->'
	
	if "nmi_kgb_ug server" in line:
		lines[index] = '<table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="left"><font face="Courier New" size="6" color="white">'+server_ug+'</font></td></tr></tbody></table><!-- nmi_kgb_ug server -->'
		
	if "nmi_kgb_rb server" in line:
		lines[index] = '<table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="left"><font face="Courier New" size="6" color="white">'+server_rb+'</font></td></tr></tbody></table><!-- nmi_kgb_rb server -->'
	
	if 'ii_path' in line:
		line = '<td border="1" align="center"><table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="center"><font face="Courier New" size="6" color="white">' +shipment+'</font></td></tr></tbody></table><!-- ii_path-->'
		lines[index] = line
		
	if 'maintrack_status' in line:
		lines[index] = '<td><table border="0" width="100%" height="100" align="left"><tbody><tr><td align="center"><b><font face="Courier New" size="7" align="center">'+maintrack+'</font></b></td></tr></tbody></table></td><!--maintrack_status-->'
	
f.close()

template = open(kgb_radiator, 'r+')
file = template.readlines()

for indx, line in enumerate(file):
	if 'maintrack_color' in line:
		line = '<table bgcolor="'+maintrack_color+'" class="roundedCorners" border="0" width="100%" height="19%"><!--maintrack_color-->'
		file[indx] = line
	if 'maintrack_status' in line:
		line = '<td align="center"><b><font color="white" face="Courier New" size="7" align="center">'+maintrack+'</font></b><!--maintrack_status-->'
		file[indx] = line
	if "Start body" in line:
		#file.insert( indx +1, "\n")
		file.insert(indx +2 , "\n".join(lines))
		#print(file[indx +2])
		break
template.close()

template = open(kgb_radiator, 'w')

#template.writelines([str(line).strip() + "\n" for line in file])
for line in file:
	template.write(line + "\n")

template.close()

#### deleting extra rows ############
template = open(kgb_radiator, 'r+')
file = template.read()
rows_count = file.count("content start")
template.close()
print(rows_count)
if rows_count > 15:
	template = open(kgb_radiator, 'r+')
	lines = template.readlines()
	row_count = 0
	for index, line in enumerate(lines):
		if "End body" in line:
			break
		if "content start" in line:
			row_count+=1
		if row_count >15:
			del lines[index]
			##print("deleted lines at index:", index)
	template.close()
	
	template = open(kgb_radiator, 'w')
	for line in lines:
		if line.rstrip():
                        template.write(line )
	template.close()
