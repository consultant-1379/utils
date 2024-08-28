import re
import sys
import requests
import base64
from bs4 import BeautifulSoup
import random
from datetime import datetime, timedelta
import os.path
from os import path

# today = "4/12"
# today1 = 'Dec 4'
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

release = sys.argv[1]
shipment = sys.argv[2]
filename = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/STATUS_%s_%s_LLSV3_ST.html' %(release,shipment)
mb_file = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/STATUS_%s_%s_LLSV3_SM.html'  %(release,shipment)
radiator_content = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/radiator_content.html'
cdb_radiator = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/cdb_radiator_'+shipment+'.html'
test_passed_blade, test_total_build_blade, test_passed_build, test_total_build, smoke_passed_blade, smoke_total_build_blade  = [0]*6
test_passed_rack, test_total_rack, smoke_passed_rack, smoke_total_rack = [0]*4
vapp_status, blade_ii_status ,blade_smoke_status,mb_status, build_status, rack_ii_status, rack_smoke_status = [-1]*7
smoke_blade_tc_link = ""
build_tc_link = ""
blade_tc_link = ""
rack_tc_link , rack_smoke_tc_link = "",""
mb_tc_link = ""
rack_server , sb_server = "",""
#blade_server_path = '/proj/eniqdmt/public/html/'
maintrack = shipment +" LINUX MAINTRACK is OPEN"
maintrack_color='#15c415'


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
		
def mb_result():
	#status = -1
	if path.exists(mb_file):
		f = open(mb_file,'r')
		lines = f.readlines()
		for line in lines:
			if today in line and 'COORDINATOR Blade ii_Test_Status' in line:
				match = re.search(r'href=[\'"]?([^\'" >]+)', line)
				if match:
					mb_tc_link = match.group(1)
				return result_count(line)
				#if '<td bgcolor="red"' in line:
				#	status = 0
				#	break
		f.close()
	return 0, 0, -1
	#return status

def server_name(job_server_link):
	pwd = base64.b64decode("TmFwbGVzITA1MTI=")
	job_page = requests.get(job_server_link, auth=('esjkadm100', pwd))
	job_contents = job_page.content
	job_lines = job_contents.split("\n")
	name_server = ""
	today_present = False
	for line in job_lines:
		if today1 in line:
			today_present = True
			console_link = re.search(r'href="(.+)" class="build-health-link"', line).groups()[0]
			console_link = "https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443"+console_link+"/consoleFull"
			console_page = requests.get(console_link, auth=('esjkadm100', pwd))
			console_contents = console_page.content
			console_lines = console_contents.split("\n")
			for cline in console_lines:
				if 'Warning: Permanently added' in cline:
					name_server = re.search(r'Warning: Permanently added \'(.+),',cline).groups()[0]
					break
						
	return name_server		
		
def server_tc(job_server_link):
	pwd = base64.b64decode("TmFwbGVzITA1MTI=")
	job_page = requests.get(job_server_link, auth=('esjkadm100', pwd))
	job_contents = job_page.content
	job_lines = job_contents.split("\n")
	name_server = ""
	name_tc = ""
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
		
def edit_icon(job):
	if job == 1:   ##job - boolean
		icon ="http://eniqdmt.seli.wh.rnd.internal.ericsson.com/tick.svg" 
	elif job == -1:
		icon = "http://eniqdmt.seli.wh.rnd.internal.ericsson.com/artifacts_icon.svg" 
	else :
		icon = "http://eniqdmt.seli.wh.rnd.internal.ericsson.com/close-window.png"
	return icon
mb_passed, mb_total, mb_status = 0, 0, -1
mb_passed, mb_total, mb_status = mb_result()
print 'mbstatus:',mb_status  

# f = open (filename , 'r')
# lines = f.readlines()
# check_dict = {}
# for line in lines:
	# if 'Late' in line:
		# maintrack = shipment + " LINUX MAINTRACK is CLOSED"
		# maintrack_color = 'orange'
	# if 'Until Code Freeze' in line:
		# maintrack = shipment + " LINUX MAINTRACK is OPEN"
		# maintrack_color = '#15c415'
	# if today in line and "Blade build_Test_Status" in line and not "Blade build_Test_Status" in check_dict:
		# check_dict["Blade build_Test_Status"] = True
		# test_passed_build, test_total_build, build_status = result_count(line)
		# match = re.search(r'href=[\'"]?([^\'" >]+)', line)
		# if match:
			# build_tc_link = match.group(1)
		
	# if today in line and "Blade ii_Test_Status" in line and not "Blade ii_Test_Status" in check_dict:
		# check_dict["Blade ii_Test_Status"] = True
		# print "line",line
		# test_passed_blade, test_total_build_blade, blade_ii_status = result_count(line)
		# match = re.search(r'href=[\'"]?([^\'" >]+)', line)
		# if match:
			# blade_tc_link = match.group(1)
		
	
	# if today in line and "Blade ii_smoke_Test_Status" in line and not "Blade ii_smoke_Test_Status" in check_dict:
		# check_dict["Blade ii_smoke_Test_Status"] = True
		# smoke_passed_blade, smoke_total_build_blade, blade_smoke_status = result_count(line)
		# match = re.search(r'href=[\'"]?([^\'" >]+)', line)
		# if match:
			# smoke_blade_tc_link = match.group(1)
	
	# if today in line and "Rackmount ii_Test_Status" in line and not "Rackmount ii_Test_Status" in check_dict:
		# check_dict["Rackmount ii_Test_Status"] = True
		# test_passed_rack, test_total_rack, rack_ii_status = result_count(line)
		# match = re.search(r'href=[\'"]?([^\'" >]+)', line)
		# if match:
			# rack_tc_link = match.group(1)
			
	# if today in line and "Rackmount ii_smoke_Test_Status" in line and not "Rackmount ii_smoke_Test_Status" in check_dict:
		# check_dict["Rackmount ii_smoke_Test_Status"] = True
		# smoke_passed_rack, smoke_total_rack, rack_smoke_status = result_count(line)
		# match = re.search(r'href=[\'"]?([^\'" >]+)', line)
		# if match:
			# rack_smoke_tc_link = match.group(1)

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
	if "Blade build_Test_Status" in line and flag:
		test_passed_build, test_total_build, build_status = result_count(line)
		match = re.search(r'href=[\'"]?([^\'" >]+)', line)
		if match:
			build_tc_link = match.group(1)
	if "Blade ii_Test_Status" in line and flag:
		test_passed_blade, test_total_build_blade, blade_ii_status = result_count(line)
		match = re.search(r'href=[\'"]?([^\'" >]+)', line)
		if match:
			blade_tc_link = match.group(1)
                        console_page = requests.get(blade_tc_link)
                        console_contents = console_page.content
                        console_lines = console_contents.split("\n")
                        for line in console_lines:
                                if 'atrcx' in line:
                                        name_server = re.split('>',line)
                                        for name in name_server:
                                                if "atrcx" in name:
                                                        sb_server = re.split('<',name)[0]
                                                        break
                                        if len(sb_server) != 0:
                                                print(sb_server)
                                                break
	if "Blade ii_smoke_Test_Status" in line and flag:
		smoke_passed_blade, smoke_total_build_blade, blade_smoke_status = result_count(line)
		match = re.search(r'href=[\'"]?([^\'" >]+)', line)
		if match:
			smoke_blade_tc_link = match.group(1)
	if "Rackmount ii_Test_Status" in line and flag:
		test_passed_rack, test_total_rack, rack_ii_status = result_count(line)
		match = re.search(r'href=[\'"]?([^\'" >]+)', line)
		if match:
			rack_tc_link = match.group(1)
                        console_page = requests.get(rack_tc_link)
                        console_contents = console_page.content
                        console_lines = console_contents.split("\n")
                        for line in console_lines:
                                if 'atrcx' in line:
                                        name_server = re.split('>',line)
                                        for name in name_server:
                                                if "atrcx" in name:
                                                        rack_server = re.split('<',name)[0]
                                                        break
                                        if len(rack_server) != 0:
                                                print(rack_server)
                                                break
	if 	"Rackmount ii_smoke_Test_Status" in line and flag:
		smoke_passed_rack, smoke_total_rack, rack_smoke_status = result_count(line)
		match = re.search(r'href=[\'"]?([^\'" >]+)', line)
		if match:
			rack_smoke_tc_link = match.group(1)
	if re.search(r"B\d+ FinishPoint",line) and flag:
		flag = 0
		break
		
		
		

f.close()


#path = blade_tc_link.split('se/')
#blade_server_path = "'"+blade_server_path + path[1]+"'"

#f = open (blade_server_path,'r')


print("test_passed_blade, test_total_build_blade, blade_ii_status:", test_passed_blade, test_total_build_blade, blade_ii_status)	
print ("test_passed_build, test_total_build, build_status:",  test_passed_build, test_total_build, build_status)
print ("smoke_passed_blade, smoke_total_build_blade, blade_smoke_status:",  smoke_passed_blade, smoke_total_build_blade, blade_smoke_status)
print ("vapp_status:", vapp_status)
print ("rack statyus :",rack_ii_status)


#vapp 
job_link = "https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/vApp_II_Pipeline_20.4/job/ES_CDB_Vapp_NMI_20.4/"
pipeline_link = "https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/vApp_II_Pipeline_20.4/job/DHCP_Test_20.4/"
pwd = base64.b64decode("TmFwbGVzITA1MTI=")
pipeline_page = requests.get(pipeline_link, auth=('esjkadm100', pwd))
pipeline_contents = pipeline_page.content
pipelines = pipeline_contents.split("\n")
today_present = False
for line1 in pipelines:
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
					vapp_status = 1
				if 'tooltip="Failed &gt; Console Output"' in lines[index-9]:
					vapp_status = 0
				break
			if not run_status:
				vapp_status = 0
			
	if today_present:
		break


vapp_server = server_name("https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/vApp_II_Pipeline_20.4/job/ES_CDB_Vapp_II_Infra_20.4/") if vapp_status !=-1 else ""
vapp_tc = server_tc("https://fem7s11-eiffel013.eiffel.gic.ericsson.se:8443/jenkins/view/vApp_II_Pipeline_20.4/job/ES_CDB_Vapp_II_TC_20.4/") if vapp_status !=-1 else ""
print ("vapp_server:", vapp_server)


	
f = open(radiator_content,"r+")
lines = f.readlines()

for index, line in enumerate(lines):
	if "build icon" in line:
		icon = edit_icon(build_status)
		if build_status == -1:
			line = '<td class= "hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+ icon + '" alt="Minor Fault" title="Not Triggered" width="50" height="50"></a></div> <!-- build icon -->'	
		else:
			line = '<td class= "hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_build_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+ icon + '" alt="Minor Fault" width="50" height="50"></a></div> <!-- build icon -->'
		lines[index+2] = '<div id="popup61_build_%s'%sys.argv[3]+'" class="overlay">'	
		lines[index] = line
		
	if "sb icon" in line:
		icon = edit_icon(blade_ii_status)
		if blade_ii_status == -1:
			line = '<td class= "hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+ icon + '" alt="Minor Fault" title="Not Triggered" width="50" height="50"></a></div> <!-- build icon -->'
		else:
			line = '<td class= "hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_sb_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+ icon + '" alt="Minor Fault" width="50" height="50"></a></div> <!-- build icon -->'
		lines[index+3] = '<div id="popup61_sb_%s'%sys.argv[3]+'" class="overlay">'
		lines[index] = line
	
        if "sb server" in line:
                line = '<table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="left"><font face="Courier New" size="6" color="white">'+sb_server+'</font></td></tr></tbody></table><!-- sb server -->'
                lines[index] = line

	if "build tc" in line:
		line = '<td border="1" align="center"><a href="' + build_tc_link +'"><p><font face="Courier New" size="3" color="white">'+ str(test_passed_build) + '/' + str(test_total_build)+ ' Cases Passed</font></p></a></td><!-- build tc-->'
		lines[index] = line
	if "sb log tc" in line:
		line = '<td border="1" align="center"><a href="' + blade_tc_link +'"><p><font face="Courier New" size="3" color="white">'+ str(test_passed_blade) + '/'+ str(test_total_build_blade)  + ' Cases Passed</font></p></a></td><!-- sb log tc-->'
		lines[index] = line
	
	if "sb smoke tc" in line:
		line = '<td border="1" align="center"><a href="' + smoke_blade_tc_link +'"><p><font face="Courier New" size="3" color="white">'+ str(smoke_passed_blade)  + '/'+ str(smoke_total_build_blade)  + ' Cases Passed</font></p></a></td><!-- sb smoke tc-->'
		lines[index] = line
	
	if 'date' in line:
		line = '<font class="hoverEffectBox" face="Courier New" size="5" color="white">'+today+'<br></font><font id="date" face="Courier New" size="2" color="white"></font></td></tr></tbody></table></td><!--date-->'
		lines[index] = line
		
	if 'maintrack_status' in line:
		line = '<td><table border="0" width="100%" height="100" align="left"><tbody><tr><td align="center"><b><font face="Courier New" size="7" align="center">'+shipment+' LINUX MAINTRACK BUILD</font></b></td></tr></tbody></table></td><!--maintrack_status-->'
		lines[index] = line
		
	if "cloud icon" in line:
		if release == "ENIQ_S19.4":
			vapp_status = -1
		icon = edit_icon(vapp_status)
		if vapp_status == -1:
				line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" title="Not Triggered" width="50" height="50"></a></div><!-- cloud icon-->'
		else:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_cloud_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" width="50" height="50"></a></div><!-- cloud icon-->'
		lines[index+3] = '<div id="popup61_cloud_%s'%sys.argv[3]+'" class="overlay">'
		lines[index] = line
		
	if "cloud server" in line:
		lines[index] = '<table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="left"><font face="Courier New" size="6" color="white">'+vapp_server+'</font></td></tr></tbody></table><!-- cloud server -->'
	
	if 'ii_path' in line:
		line = '<td border="1" align="center"><table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="center"><font face="Courier New" size="6" color="white">' +shipment+'</font></td></tr></tbody></table><!-- ii_path-->'
		lines[index] = line
	if 'cloud tc' in line:
		if vapp_status == 1:
			line = '<td border="1" align="center"><a href=""><p><font face="Courier New" size="3" color="white">'+vapp_tc+'/559 Cases Passed</font></p></a></td><!--cloud tc-->'
		elif vapp_status == 0:
			line = '<td border="1" align="center"><a href=""><p><font face="Courier New" size="3" color="white">'+vapp_tc+'/559 Cases Passed</font></p></a></td><!--cloud tc-->'
		lines[index] = line
		
	if 'mb icon' in line:
		icon = edit_icon(mb_status)
		if mb_status == -1:
			line = '<td class= "hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+ icon + '" alt="Minor Fault" title="Not Triggered" width="50" height="50"></a></div> <!-- build icon -->'
		else:
			line = '<td class= "hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_mb_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+ icon + '" alt="Minor Fault" width="50" height="50"></a></div> <!-- build icon -->'
		lines[index+3] = '<div id="popup61_mb_%s'%sys.argv[3]+'" class="overlay">'
		lines[index] = line
		
	if 'mb log tc' in line:
		lines[index] = '<td border="1" align="center"><a href="'+mb_tc_link+'"><p><font face="Courier New" size="3" color="white">'+str(mb_passed) +'/' +str(mb_total)+' Cases Passed</font></p></a></td><!-- mb log tc -->'
		
	if 'rack icon' in line:
		icon = edit_icon(rack_ii_status)
		if rack_ii_status == -1:
			line = '<td class="hoverEffectIcon" border="1" align="center"><div class="box"><img id="_x0000_i1025" src="'+icon+'" alt="Minor Fault" width="50" height="50"></div><!-- rack icon-->'
		else:
			line = '<td class= "hoverEffectIcon" border="1" align="center"><div class="box"><a class="button" href="#popup61_rack_%s'%sys.argv[3]+'"><img id="_x0000_i1025" src="'+ icon + '" alt="Minor Fault" width="50" height="50"></a></div> <!-- rack icon -->'
		lines[index+3] = '<div id="popup61_rack_%s'%sys.argv[3]+'" class="overlay">'
		lines[index] = line
		
        if 'rack server' in line:
                line = '<table class="roundedCorners" bgcolor="orange" width="80%" height="50%"><tbody><tr><td align="left"><font face="Courier New" size="6" color="white">'+rack_server+'</font></td></tr></tbody></table><!-- rack server -->'
                lines[index] = line
	if 'rack log tc' in line:
		line = '<td border="1" align="center"><a href="' + rack_tc_link +'"><p><font face="Courier New" size="3" color="white">'+ str(test_passed_rack) + '/'+ str(test_total_rack)  + ' Cases Passed</font></p></a></td><!-- rack log tc-->'
		lines[index] = line
		
	if 'rack smoke tc' in line:
		line = '<td border="1" align="center"><a href="' + rack_smoke_tc_link +'"><p><font face="Courier New" size="3" color="white">'+ str(smoke_passed_rack) + '/'+ str(smoke_total_rack)  + ' Cases Passed</font></p></a></td><!-- rack smoke tc-->'
		lines[index] = line
		
f.close()

template = open(cdb_radiator, 'r+')
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

template = open(cdb_radiator, 'w')

#template.writelines([str(line).strip() + "\n" for line in file])
for line in file:
	template.write(line + "\n")

template.close()

#### deleting extra rows ############
template = open(cdb_radiator, 'r+')
file = template.read()
rows_count = file.count("content start")
template.close()
print(rows_count)
if rows_count > 15:
	template = open(cdb_radiator, 'r+')
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
	
	with open (cdb_radiator,'r+') as fd:
		lines = fd.readlines()
		fd.seek(0)
		fd.writelines(line for line in lines if line.strip())
		fd.truncate()
