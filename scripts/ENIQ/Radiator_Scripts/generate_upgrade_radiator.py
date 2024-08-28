import re
import sys
import requests
import base64
from bs4 import BeautifulSoup
import random
from datetime import datetime, timedelta
import os.path
from os import path

# today = "13/01"
# today1 = 'Jan 13'
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
else:
	day1 = datetime.strftime(datetime.now(), '%d')

today1 = mon+" "+day

mon1 = datetime.strftime(datetime.now(), '%b')
today2 = mon1+" "+day1
#today1 = 'Jan 15'
#today2 = 'Jan 16'

release = sys.argv[1]
shipment = sys.argv[2]
filename = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/STATUS_%s_%s_LLSV3_ST.html' %(release,shipment)
mb_file = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/STATUS_%s_%s_LLSV3_SM.html'  %(release,shipment)
ug_radiator_content = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/upgrade_radiator_content.html'
cdb_upgrade_radiator = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/cdb_upgrade_radiator_'+shipment+'.html'
ug_sb_log_tc, ug_sb_sanity_tc ,ug_mb_log_tc, ug_mb_sanity_tc, ug_rack_log_tc, ug_rack_sanity_tc,ug_sb_log_tc_passed,ug_sb_sanity_tc_passed, ug_mb_log_tc_passed, ug_mb_sanity_tc_passed,ug_rack_log_tc_passed,ug_rack_sanity_tc_passed = [0]*12
ug_sb_status,ug_mb_status,ug_rack_status,ug_sb_sanity_status,ug_mb_sanity_status,ug_rack_sanity_status = [-1]*6
ug_sb_log_link, ug_sb_sanity_link, ug_mb_log_link, ug_mb_sanity_link,ug_rack_log_link, ug_rack_sanity_link = "","","","","",""
maintrack = shipment +" LINUX MAINTRACK is OPEN"
maintrack_color='#15c415'
ffu_status = -1
ffu_server = ""
ffu_shipment = ""


def result_count(line):
	if "Cases Passed" in line:
		test_cases = re.search(r">(\d+/\d+) Cases Passed", line).groups()
		passed, total  = test_cases[0].split("/")
		passed = int(passed)
		total = int(total)
		job_status = 0
		if passed >= 0.6 * total:
			job_status = 1
		return passed, total, job_status
	else:
		return 0 , 0 ,-1
		
def edit_icon(job):
	if job == 1:   ##job - boolean
		icon ="http://eniqdmt.seli.wh.rnd.internal.ericsson.com/tick.svg" 
	elif job == -1:
		icon = "http://eniqdmt.seli.wh.rnd.internal.ericsson.com/artifacts_icon.svg" 
	else :
		icon = "http://eniqdmt.seli.wh.rnd.internal.ericsson.com/close-window.png"
	return icon
		

def ffu_details():
	ffu_status = -1
        job_link = "https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/job/ES_20B(20.2)_CI_FFU_Upgrade/"
        pwd = base64.b64decode("TmFwbGVzITA1MTI=")
        job_page = requests.get(job_link, auth=('esjkadm100', pwd))
        job_contents = job_page.content
        job = job_contents.split("\n")
        today_present = False
        for line1 in job:
                        if today1 in line1:
                                        print today1
                                        today_present = True
                                        page = requests.get(job_link, auth=('esjkadm100', pwd))
                                        print today1
                                        soup = BeautifulSoup(page.content, 'html.parser')
                                        contents = soup.prettify()
                                        lines = contents.split("\n")
                                        run_status = False
                                        for index,line in enumerate(lines):
                                                        if today1 in line:
                                                                        run_status = True
                                                                        print("index of date:", index)
                                                                        if 'tooltip="Success &gt; Console Output"' in lines[index-9]:
                                                                                        ffu_status = 1
                                                                        if 'tooltip="Failed &gt; Console Output"' in lines[index-9]:
                                                                                        ffu_status = 0
                                                                        break
                                                        if not run_status:
                                                                        ffu_status = 0

                        if today_present:
                                        break


        print(ffu_status)
        if(ffu_status !=-1):
            #pwd = base64.b64decode("TmFwbGVzITA1MTI=")
        #job_page = requests.get(job_link, auth=('esjkadm100', pwd))
        #job_contents = job_page.content
                name_server = ""
                shipment_name = ""
                job_lines = job_contents.split("\n")
                today_present = False
                for line in job_lines:
                        if today1 in line:
                                today_present = True
                                #console_link = re.search(r'href="(.+)" class="build-health-link"', line).groups()[0]
                                #console_link = "https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443"+console_link+"/consoleFull"
                                console_link = job_link+"lastBuild/consoleFull"
                                console_page = requests.get(console_link, auth=('esjkadm100', pwd))
                                console_contents = console_page.content
                                console_lines = console_contents.split("\n")
                                for cline in console_lines:
                                        out=[]
                                        if 'VAPP Name' in cline:
                                                # name_server = re.search(r'VAPP Name \'(.+),',cline).groups()[0]
                                        #       print(cline)
                                                out = cline.split(": ")
                                        #       print(out)
                                                name_server = out[1]
                                                print(name_server)
                                                break
                                        if 'SHIPMENT' in cline:
                                                out = cline.split(": ")
                                                shipment_name = out[1]
                                                print(shipment_name)

                return ffu_status,name_server,shipment_name
        else:
                return ffu_status,name_server,shipment_name

ffu_status,ffu_server,ffu_shipment = ffu_details()
print(ffu_status)
print ("ffu_server:", ffu_server)
print("Shipment:",ffu_shipment)
#if(ffu_shipment != shipment):
#	ffu_status = -1
#	ffu_server = ""
#	ffu_shipment = ""
	
def server_tc(job_server_link):
	name_tc = ""
	pwd = base64.b64decode("TmFwbGVzITA1MTI=")
	job_page = requests.get(job_server_link, auth=('esjkadm100', pwd))
	job_contents = job_page.content
	job_lines = job_contents.split("\n")
	name_server = ""
	today_present = False
	for line in job_lines:
		if today1 in line or today2 in line:
			today_present = True
			#console_link = re.search(r'href="(.+)" class="build-health-link"', line).groups()[0]
			#console_link = "https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443"+console_link+"/consoleFull"
			console_link = job_server_link+"lastBuild/consoleFull"
			console_page = requests.get(console_link, auth=('esjkadm100', pwd))
			console_contents = console_page.content
			console_lines = console_contents.split("\n")
			for cline in console_lines:
				if 'Pass:' in cline:
					name_tc = re.split(':',cline)[1]
					break
						
	return name_tc

vapp_tc = server_tc("https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/job/ES_CDB_FFU_TC/")


def mb_details():
	name_tc_total = "0"
	name_tc_pass = "0"
	name_tc_fail = "0"
        mb_status = -1
        name_tc = ""
        shipment_name = ""
        job_link = "https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/job/ES_LINUX_MB_UPGRADE/"
        pwd = base64.b64decode("TmFwbGVzITA1MTI=")
        job_page = requests.get(job_link, auth=('esjkadm100', pwd))
        job_contents = job_page.content
        job = job_contents.split("\n")
        today_present = False
        for line1 in job:
                        if today1 in line1:
                                        print today1
                                        today_present = True
                                        page = requests.get(job_link, auth=('esjkadm100', pwd))
                                        print today1
                                        soup = BeautifulSoup(page.content, 'html.parser')
                                        contents = soup.prettify()
                                        lines = contents.split("\n")
                                        run_status = False
                                        for index,line in enumerate(lines):
                                                        if today1 in line:
                                                                        run_status = True
                                                                        print("index of date:", index)
                                                                        if 'tooltip="Success &gt; Console Output"' in lines[index-9]:
                                                                                        mb_status = 1
                                                                        if 'tooltip="Failed &gt; Console Output"' in lines[index-9]:
                                                                                        mb_status = 0
                                                                        break
                                                        if not run_status:
                                                                        mb_status = 0

                        if today_present:
                                        break


        print(mb_status)
        if(mb_status !=-1):
            #pwd = base64.b64decode("TmFwbGVzITA1MTI=")
        #job_page = requests.get(job_link, auth=('esjkadm100', pwd))
        #job_contents = job_page.content
                #name_server = ""
                shipment_name = ""
                job_lines = job_contents.split("\n")
                today_present = False
                for line in job_lines:
                        if today1 in line:
                                today_present = True
                                #console_link = re.search(r'href="(.+)" class="build-health-link"', line).groups()[0]
                                #console_link = "https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443"+console_link+"/consoleFull"
                                console_link = job_link+"lastBuild/consoleFull"
                                console_page = requests.get(console_link, auth=('esjkadm100', pwd))
                                console_contents = console_page.content
                                console_lines = console_contents.split("\n")
                                for cline in console_lines:
                                        out=[]
                                        #if 'MACHINE:' in cline:
                                                # name_server = re.search(r'VAPP Name \'(.+),',cline).groups()[0]
                                        #       print(cline)
                                                #out = cline.split(": ")
                                        #       print(out)
                                                #name_server = out[1]
                                                #print(name_server)
                                                #break
                                        if 'SHIPMENT' in cline:
                                                out = cline.split(": ")
                                                shipment_name = out[1]
                                                print(shipment_name)
                                                break
                job_link = "https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/job/MB_UG_TC/"
                job_page = ""
                job_contents = ""
                job_lines = []
                job_page = requests.get(job_link, auth=('esjkadm100', pwd))
                job_contents = job_page.content
                job_lines = job_contents.split("\n")
                today_present = False
                for line in job_lines:
                        if today1 in line or today2 in line:
                                today_present = True
                                #console_link = re.search(r'href="(.+)" class="build-health-link"', line).groups()[0]
                                #console_link = "https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443"+console_link+"/consoleFull"
                                console_link = job_link+"lastBuild/consoleFull"
                                console_page = ""
                                console_contents = ""
                                console_lines = []
                                console_page = requests.get(console_link, auth=('esjkadm100', pwd))
                                console_contents = console_page.content
                                console_lines = console_contents.split("\n")
                                for cline in console_lines:
                                        if 'Total' in cline:
                                                name_tc_total = re.split(':',cline)[1]
                                        if 'Pass' in cline:
                                                name_tc_pass = re.split(':',cline)[1]
                                        if 'Fail' in cline:
                                                name_tc_fail = re.split(':',cline)[1]
                                                break




                return mb_status,name_tc_total,shipment_name,name_tc_pass,name_tc_fail
        else:
                return mb_status,name_tc_total,shipment_name,name_tc_pass,name_tc_fail

mb_status,name_tc,mb_shipment,name_tc_pass,name_tc_fail = mb_details()
print(mb_status)
print ("name_tc:", name_tc)
print("Shipment:",mb_shipment)
print("passes",name_tc_pass)
print("fail",name_tc_fail)




f = open (filename , 'r')
lines = f.readlines()
flag = 0
for line in lines:
	if 'Late' in line:
		maintrack = shipment + " LINUX MAINTRACK is CLOSED"
		maintrack_color = 'orange'
	if 'Until Code Freeze' in line:
		maintrack = shipment + " LINUX MAINTRACK is OPEN"
		maintrack_color = '#15c415'
	if re.search(r"B\d+",line):
		if today in line:
			print line
			flag=1
	if "Blade ug_Test_Status" in line and flag:
		ug_sb_log_tc_passed, ug_sb_log_tc, ug_sb_status = result_count(line)
		match = re.search(r'href=[\'"]?([^\'" >]+)', line)
		if match:
			ug_sb_log_link = match.group(1)
	if "Blade ug_smoke_Test_Status" in line and flag:
		ug_sb_sanity_tc_passed, ug_sb_sanity_tc, ug_sb_sanity_status = result_count(line)
		match = re.search(r'href=[\'"]?([^\'" >]+)', line)
		if match:
			ug_sb_sanity_link = match.group(1)
	if "Rackmount ug_Test_Status" in line and flag:
		ug_rack_log_tc_passed, ug_rack_log_tc, ug_rack_status = result_count(line)
		match = re.search(r'href=[\'"]?([^\'" >]+)', line)
		if match:
			ug_rack_log_link = match.group(1)
	if "Rackmount ug_smoke_Test_Status" in line and flag:
		ug_rack_sanity_tc_passed, ug_rack_sanity_tc, ug_rack_sanity_status = result_count(line)
		match = re.search(r'href=[\'"]?([^\'" >]+)', line)
		if match:
			ug_rack_sanity_link = match.group(1)
	if re.search(r"B\d+ FinishPoint",line) and flag:
		flag = 0
		break
		
f.close()
	
	
f = open(ug_radiator_content,"r+")
lines = f.readlines()
print len(lines)

for index, line in enumerate(lines):
	if "sb icon" in line:
		print index
		icon = edit_icon(ug_sb_status)
		if ug_sb_status == -1:
			line = '<td class= "hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+ icon + '" alt="Minor Fault" title="Not Triggered" width="50" height="50"></a></div> <!-- build icon -->'
		else:
			line = '<td class= "hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_sb_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+ icon + '" alt="Minor Fault" width="50" height="50"></a></div> <!-- build icon -->'
		lines[index+3] = '<div id="popup61_sb_%s'%sys.argv[3]+'" class="overlay">'
		lines[index] = line
	if "sb log tc" in line:
		line = '<td border="1" align="center"><a href="' + ug_sb_log_link +'"><p><font face="Courier New" size="3" color="white">'+ str(ug_sb_log_tc_passed) + '/'+ str(ug_sb_log_tc)  + ' Cases Passed</font></p></a></td><!-- sb log tc-->'
		lines[index] = line
		
	if "sb smoke tc" in line:
		line = '<td border="1" align="center"><a href="' + ug_sb_sanity_link +'"><p><font face="Courier New" size="3" color="white">'+ str(ug_sb_sanity_tc_passed)  + '/'+ str(ug_sb_sanity_tc)  + ' Cases Passed</font></p></a></td><!-- sb smoke tc-->'
		lines[index] = line
		
	if 'date' in line:
		line = '<font class="hoverEffectBox" face="Courier New" size="5" color="white">'+today+'<br></font><font id="date" face="Courier New" size="2" color="white"></font></td></tr></tbody></table></td><!--date-->'
		lines[index] = line
		

	if(mb_shipment == shipment):
                if 'mb icon' in line:
                        icon = edit_icon(mb_status)
                        if mb_status == -1:
                                line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" title="Not Triggered" width="50" height="50"></div><!-- mb icon-->'
                        else:
                                line = '<td class= "hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_mb_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+ icon + '" alt="Minor Fault" width="50" height="50"></a></div> <!-- mb icon -->'
                        lines[index+3] = '<div id="popup61_mb_%s'%sys.argv[3]+'" class="overlay">'
                        lines[index] = line

                if "mb_maintrack_status" in line:
                        lines[index] = '<td><table border="0" width="100%" height="100" align="left"><tbody><tr><td align="center"><b><font face="Courier New" size="7" align="center">'+shipment+ ' MAINTRACK BUILD</font></b></td></tr></tbody></table></td><!--mb_maintrack_status-->'

                
                if 'ii_path' in line:
                        line = '<td border="1" align="center"><table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="center"><font face="Courier New" size="6" color="white">' +shipment+'</font></td></tr></tbody></table><!-- ii_path-->'
                        lines[index] = line

                if 'mb tc' in line:
                        if ffu_status == 1:
                                line = '<td border="1" align="center"><a href=""><p><font face="Courier New" size="3" color="white">'+name_tc_pass+'/'+name_tc+' Cases Passed</font></p></a></td><!--mb tc-->'
                        elif ffu_status == 0:
                                line = '<td border="1" align="center"><a href=""><p><font face="Courier New" size="3" color="white">'+name_tc_pass+'/'+name_tc+' Cases Passed</font></p></a></td><!--mb tc-->'
                        lines[index] = line
						
	else:
                if 'mb icon' in line:
                        icon = "http://eniqdmt.seli.wh.rnd.internal.ericsson.com/artifacts_icon.svg"
                        line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" title="Not Triggered" width="50" height="50"></div><!-- mb icon-->'
                        lines[index] = line


		
	if 'rack icon' in line:
		icon = edit_icon(ug_rack_status)
		if ug_rack_status == -1:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" width="50" height="50"></div><!-- rack icon-->'
		else:
			line = '<td class= "hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_rack_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+ icon + '" alt="Minor Fault" width="50" height="50"></a></div> <!-- rack icon -->'
		lines[index+3] = '<div id="popup61_rack_%s'%sys.argv[3]+'" class="overlay">'
		lines[index] = line
		
	if 'rack log tc' in line:
		line = '<td border="1" align="center"><a href="' + ug_rack_log_link +'"><p><font face="Courier New" size="3" color="white">'+ str(ug_rack_log_tc_passed) + '/'+ str(ug_rack_log_tc)  + ' Cases Passed</font></p></a></td><!-- rack log tc-->'
		lines[index] = line
		
	if 'rack smoke tc' in line:
		line = '<td border="1" align="center"><a href="' + ug_rack_sanity_link +'"><p><font face="Courier New" size="3" color="white">'+ str(ug_rack_sanity_tc_passed) + '/'+ str(ug_rack_sanity_tc)  + ' Cases Passed</font></p></a></td><!-- rack smoke tc-->'
		lines[index] = line
		
	if 'ii_path' in line:
		line = '<td border="1" align="center"><table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="center"><font face="Courier New" size="6" color="white">' +shipment+'</font></td></tr></tbody></table><!-- ii_path-->'
		lines[index] = line

	if(ffu_shipment == shipment):
		if 'ffu icon' in line:
			icon = edit_icon(ffu_status)
			if ffu_status == -1:
				line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" title="Not Triggered" width="50" height="50"></div><!-- ffu icon-->'
			else:
				line = '<td class= "hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_ffu_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+ icon + '" alt="Minor Fault" width="50" height="50"></a></div> <!-- ffu icon -->'
			lines[index+3] = '<div id="popup61_ffu_%s'%sys.argv[3]+'" class="overlay">'
			lines[index] = line

		if "ffu_maintrack_status" in line:
			lines[index] = '<td><table border="0" width="100%" height="100" align="left"><tbody><tr><td align="center"><b><font face="Courier New" size="7" align="center">'+shipment+ ' MAINTRACK BUILD</font></b></td></tr></tbody></table></td><!--ffu_maintrack_status-->'	

		if "ffu server" in line:
			lines[index] = '<table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="left"><font face="Courier New" size="6" color="white">'+ffu_server+'</font></td></tr></tbody></table><!-- ffu server -->'

		if 'ii_path' in line:
			line = '<td border="1" align="center"><table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="center"><font face="Courier New" size="6" color="white">' +shipment+'</font></td></tr></tbody></table><!-- ii_path-->'
			lines[index] = line

		if 'ffu tc' in line:
			if ffu_status == 1:
				line = '<td border="1" align="center"><a href=""><p><font face="Courier New" size="3" color="white">'+vapp_tc+'/31 Cases Passed</font></p></a></td><!--ffu tc-->'
			elif ffu_status == 0:
				line = '<td border="1" align="center"><a href=""><p><font face="Courier New" size="3" color="white">'+vapp_tc+'/31 Cases Passed</font></p></a></td><!--ffu tc-->'
			lines[index] = line		
	else:
		if 'ffu icon' in line:
                        icon = "http://eniqdmt.seli.wh.rnd.internal.ericsson.com/artifacts_icon.svg" 
                        line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" title="Not Triggered" width="50" height="50"></div><!-- ffu icon-->'
                        lines[index] = line


f.close()
template = open(cdb_upgrade_radiator, 'r+')
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

template = open(cdb_upgrade_radiator, 'w')

#template.writelines([str(line).strip() + "\n" for line in file])
for line in file:
	template.write(line + "\n")

template.close()

#### deleting extra rows ############
template = open(cdb_upgrade_radiator, 'r+')
file = template.read()
rows_count = file.count("content start")
template.close()
print(rows_count)
if rows_count > 15:
	template = open(cdb_upgrade_radiator, 'r+')
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
	
	with open (cdb_upgrade_radiator,'r+') as fd:
		lines = fd.readlines()
		fd.seek(0)
		fd.writelines(line for line in lines if line.strip())
		fd.truncate()
	with open (template,'r+') as fd:
		lines = fd.readlines()
		fd.seek(0)
		fd.writelines(line for line in lines if line.strip())
		fd.truncate()
