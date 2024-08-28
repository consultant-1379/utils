import re
import sys
import requests
import base64
from bs4 import BeautifulSoup
import random
import paramiko
from datetime import datetime, timedelta
import os.path
from os import path

sb_mig_status, mb_mig_status, rack_mig_status = [-1]*3
# today = "08/11"
# today1 = 'Nov 12'
day = datetime.strftime(datetime.now() - timedelta(1), '%d')
mon = datetime.strftime(datetime.now() - timedelta(1), '%b')
if '0' in day[0]:
	day = day[1]
today = sys.argv[3]
today1 = mon+" "+day
release = sys.argv[1]
shipment = sys.argv[2]
mig_radiator_content = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/mig_radiator_content.html'
migration_radiator = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/migration_radiator.html'
filename = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/STATUS_%s_%s_LLSV3_ST.html' %(release,shipment)
maintrack = shipment +" LINUX MAINTRACK is OPEN"
maintrack_color = '#15c415'


def edit_icon(job):
	if job == 1:   ##job - boolean
		icon ="http://eniqdmt.lmera.ericsson.se/tick.svg" 
	elif job == -1:
		icon = "http://eniqdmt.lmera.ericsson.se/artifacts_icon.svg" 
	else :
		icon = "http://eniqdmt.lmera.ericsson.se/close-window.png"
	return icon

def mig_status(job_link,pipeline_link):
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
						if 'tooltip="Success &gt; Console Output"' in lines[index-9]:
							status = 1
						if 'tooltip="Failed &gt; Console Output"' in lines[index-9]:
							status = 0
						break
					if not run_status:
						status = 0
					
		if today_present:
			break
	return status
	
def mig_tc(job_link):
	pwd = base64.b64decode("TmFwbGVzITA1MTI=")
	job_page = requests.get(job_link, auth=('esjkadm100', pwd))
	job_contents = job_page.content
	job_lines = job_contents.split("\n")
	tc_passed, tc_total = 0,0
	today_present = False
	for line in job_lines:
		if today1 in line:
			today_present = True
			console_link = re.search(r'href="(.+)" class="build-health-link"', line).groups()[0]
			console_link = "https://fem167-eiffel004.lmera.ericsson.se:8443"+console_link+"/console"
			console_page = requests.get(console_link, auth=('esjkadm100', pwd))
			soup2 = BeautifulSoup(console_page.content, 'html.parser')
			#console_contents = console_page.content
			console_contents = soup2.prettify()
			console_lines = console_contents.split("\n")
			for cline in console_lines:
				if "Pass:" in cline:
					tc_passed = cline.split("Pass: ")[1].strip()
				if "Total: " in cline:
					tc_total = cline.split("Total: ")[1].strip()
	
	
	return tc_passed, tc_total
	
mb_mig_pipeline_link = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/view/MB_Migration_Pipeline/"
mb_mig_job_link = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/job/MB_Migration/"
mb_mig_status = mig_status(mb_mig_job_link,mb_mig_pipeline_link)
print mb_mig_status
rack_mig_pipeline_link = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/view/CDB_RACK_Migration_Pipeline/"
rack_mig_job_link = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/job/RACK_Migration/"
rack_mig_status = mig_status(rack_mig_job_link,rack_mig_pipeline_link)
print rack_mig_status
sb_mig_pipeline_link = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/view/CDB_Migration_SB_Pipeline/"
sb_mig_job_link = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/view/CDB_Migration_SB_Pipeline/job/CDB_SOL_RHEL_SB_MIGRATION/"
sb_mig_status = mig_status(sb_mig_job_link,sb_mig_pipeline_link)
sb_tc_job_link = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/view/CDB_Migration_SB_Pipeline/job/CDB_SB_Migraton_TC/"
mb_tc_job_link = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/view/CDB_Migration_SB_Pipeline/job/CDB_MB_Migration_TC/"
rack_tc_job_link = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/view/CDB_RACK_Migration_Pipeline/job/CDB_RACK_Migraton_TC/"
# sb_tc_passed, sb_tc_total = mig_tc(sb_tc_job_link)
# mb_tc_passed, mb_tc_total = mig_tc(mb_tc_job_link)
# rack_tc_passed, rack_tc_total = mig_tc(rack_tc_job_link)

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

f = open(mig_radiator_content,"r+")
lines = f.readlines()

for index, line in enumerate(lines):
	if 'date' in line:
		line = '<font class="hoverEffectBox" face="Courier New" size="5" color="white">'+today+'<br></font><font id="date" face="Courier New" size="2" color="white"></font></td></tr></tbody></table></td><!--date-->'
		lines[index] = line
		
	if 'maintrack_status' in line:
		lines[index] = '<td><table border="0" width="100%" height="100" align="left"><tbody><tr><td align="center"><b><font face="Courier New" size="7" align="center">'+maintrack+'</font></b></td></tr></tbody></table></td><!--maintrack_status-->'
	
	if 'ii_path' in line:
		line = '<td border="1" align="center"><table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="center"><font face="Courier New" size="6" color="white">' +shipment+'</font></td></tr></tbody></table><!-- ii_path-->'
		lines[index] = line
	
	if "mb icon" in line:
		icon = edit_icon(mb_mig_status)
		if mb_mig_status == -1:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" title="Not Triggered" width="50" height="50"></a></div> <!-- mb icon-->'
		else:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_mb_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" width="50" height="50"></a></div> <!-- mb icon-->'
		lines[index+2] = '<div id="popup61_mb_%s'%sys.argv[3]+'" class="overlay">'	
		lines[index] = line
		
	if "sb icon" in line:
		icon = edit_icon(sb_mig_status)
		if sb_mig_status == -1:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" title="Not Triggered" width="50" height="50"></a></div> <!-- sb icon-->'
		else:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_sb_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" width="50" height="50"></a></div> <!-- sb icon-->'
		lines[index+2] = '<div id="popup61_sb_%s'%sys.argv[3]+'" class="overlay">'	
		lines[index] = line
		
	if "rack icon" in line:
		icon = edit_icon(rack_mig_status)
		if rack_mig_status == -1:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" title="Not Triggered" width="50" height="50"></a></div> <!-- rack icon-->'
		else:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_rack_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" width="50" height="50"></a></div> <!-- rack icon-->'
		lines[index+2] = '<div id="popup61_rack_%s'%sys.argv[3]+'" class="overlay">'	
		lines[index] = line
		
	if "sb log tc" in line:
		passed,total = mig_tc(sb_tc_job_link)
		line = '<td border="1" align="center"><p><font face="Courier New" size="3" color="white">'+ str(passed) + '/'+ str(total) + ' Cases Passed</font></p></a></td><!--sb log tc -->'
		lines[index] = line
		
	if "mb log tc" in line:
		passed,total = mig_tc(mb_tc_job_link)
		line = '<td border="1" align="center"><p><font face="Courier New" size="3" color="white">'+ str(passed) + '/'+ str(total) + ' Cases Passed</font></p></a></td><!--mb log tc -->'
		lines[index] = line
		
	if "rack log tc" in line:
		passed,total = mig_tc(rack_tc_job_link)
		line = '<td border="1" align="center"><p><font face="Courier New" size="3" color="white">'+ str(passed) + '/'+ str(total) + ' Cases Passed</font></p></a></td><!--rack log tc -->'
		lines[index] = line
		
f.close()

template = open(migration_radiator, 'r+')
file = template.readlines()

for indx, line in enumerate(file):
	if 'maintrack_color' in line:
		line = '<table bgcolor="'+maintrack_color+'" class="roundedCorners" border="0" width="100%" height="19%"><!--maintrack_color-->'
		file[indx] = line
	if 'maintrack_status' in line:
		line = '<td align="center"><b><font color="white" face="Courier New" size="7" align="center">'+maintrack+'</font></b><!--maintrack_status-->'
		file[indx] = line
	if "Start body" in line:
		file.insert( indx +1, "\n")
		file.insert(indx +2 , "\n".join(lines))
		#print(file[indx +2])
		break
template.close()

template = open(migration_radiator, 'w')

#template.writelines([str(line).strip() + "\n" for line in file])
for line in file:
	template.write(line + "\n")

template.close()

#### deleting extra rows ############
template = open(migration_radiator, 'r+')
file = template.read()
rows_count = file.count("content start")
template.close()
print(rows_count)
if rows_count > 15:
	template = open(migration_radiator, 'r+')
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
	
	template = open(migration_radiator, 'w')
	for line in lines:
		if line.rstrip():
                        template.write(line )
	template.close()
