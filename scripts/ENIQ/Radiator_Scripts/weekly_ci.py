import re
import sys
from os import path

RELEASE = sys.argv[1]
ship = sys.argv[2]
flag = 0
html_dir = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics"
#html_dir = "/home/esjkadm100/gagan"
html_dir_nmi = "/proj/pduosslegacy/eniqdmt/ibw_logs/EXEC_SUM/KGB_CI/WEEK"
wday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday']
jira_details = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/JIRA/jira_week.txt"
#html_dir_nmi = "/proj/pduosslegacy/eniqdmt/ibw_logs1/EXEC_SUM/KGB_CI/WEEK"

def II_Dashboard():
	flag = 0;
	html_new = html_dir+"/STATUS_"+RELEASE+"_"+ship+"_LLSV3_ST_week2.html";
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
#	HTMLT.write("<html>\n<head><center><h1>Weekly CI Dashboard</h1></center><br/><h2>Customer Deployable Baseline (CDB)</h2></head>\n<body>")
	HTMLT.write("<table cellspacing=\"18\"><tr align=\"center\"><td><b><font size=\"4\">Single Blade II</b></font>\n")
	HTMLT.write("<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		deli,loops,passed,fail,test_pass,test_fail,total,x,y = [0]*9
		if path.exists(html_new):
			HTMLNEW = open(html_new,'r')
			lines = HTMLNEW.readlines()
			for line in lines:
				if weekday in line:
					flag = 1
				if flag == 1:
					if "Blade ii_Test_Status" in line and "Not Executed" not in line:
						loops = loops + 1
					if "Cases Passed" in line and "Blade ii_Test_Status" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						test_pass, total  = test_cases[0].split("/")
						test_pass = int(test_pass)
						total = int(total)
						test_fail = total - test_pass
						x = 1
					if "Cases Passed" in line and "Blade ii_smoke_Test_Status" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						test_pass1, total1  = test_cases[0].split("/")
						test_pass1 = int(test_pass1)
						total1 = int(total1)
						test_pass = test_pass + test_pass1
						total = total + total1
						test_fail1 = total1 - test_pass1
						test_fail = test_fail + test_fail1
						y = 1
						x = 0
					if ((x ==1 and y == 0) or x == 1):
						if test_pass > 0.65 * total:
							passed = passed + 1
						else:
							fail = fail + 1
					x = 0
					y = 0			
				if weekday+" END" in line:
					flag = 0
					break
		
			HTMLNEW.close()
		loop_status = str(passed)+"/"+str(fail)
		test_status = str(test_pass)+"/"+str(test_fail)
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+str(loops)+"</td>\n<td>"+loop_status+"</td>\n<td>"+str(total)+"</td>\n<td>"+test_status+"</td>\n</tr>")
	#HTMLT.write("</br></table>\n</br></td>")
	HTMLT.write("</table>\n</br></td>")	
def MBII_Dashboard():
	flag = 0;
	html_new = html_dir+"/STATUS_"+RELEASE+"_"+ship+"_LLSV3_ST_week2.html";
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
	HTMLT.write("<td><b><font size=\"4\">Multi Blade II</b></font>\n<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		deli,loops,passed,fail,test_pass,test_fail,total,x,y = [0]*9
		if path.exists(html_new):
			HTMLNEW = open(html_new,'r')
			lines = HTMLNEW.readlines()
			for line in lines:
				if weekday in line:
					flag = 1
				if flag == 1:
					if "MBlade ii_Test_Status" in line and "Not Executed" not in line:
						loops = loops + 1
					if "Cases Passed" in line and "MBlade ii_Test_Status" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						test_pass, total  = test_cases[0].split("/")
						test_pass = int(test_pass)
						total = int(total)
						test_fail = total - test_pass
						x = 1
					if "Cases Passed" in line and "MBlade ii_smoke_Test_Status" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						test_pass1, total1  = test_cases[0].split("/")
						test_pass1 = int(test_pass1)
						total1 = int(total1)
						test_pass = test_pass + test_pass1
						total = total + total1
						test_fail1 = total1 - test_pass1
						test_fail = test_fail + test_fail1
						y = 1
						x = 0
					if ((x ==1 and y == 0) or x == 1):
						if test_pass > 0.65 * total:
							passed = passed + 1
						else:
							fail = fail + 1
					x = 0
					y = 0			
				if weekday+" END" in line:
					flag = 0
					break
		
			HTMLNEW.close()
		loop_status = str(passed)+"/"+str(fail)
		test_status = str(test_pass)+"/"+str(test_fail)
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+str(loops)+"</td>\n<td>"+loop_status+"</td>\n<td>"+str(total)+"</td>\n<td>"+test_status+"</td>\n</tr>")
	#HTMLT.write("</br></table>\n</br></td></tr>")
	HTMLT.write("</table>\n</br></td>")
	
def VappII_Dashboard():
	pipeline_details = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/vapp_details.txt";
	f = open(pipeline_details,'r')
	lines = f.readlines()
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
	HTMLT.write("<td><b><font size=\"4\">VApp II</b></font>\n<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		loops,total = ['0']*2
		loop_status,test_status = ['0/0']*2
		for line in lines:
			#if "Vapp" in line:
			#	flag = 1
			if weekday in line:
				det = line.split("::")
				loops = det[1]
				loop_status = det[2]
				total = det[3]
				test_status = det[4]
			#if "KGB" in line:
			#	flag = 0
			
		
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+loops+"</td>\n<td>"+loop_status+"</td>\n<td>"+total+"</td>\n<td>"+test_status+"</td>\n</tr>")

	#HTMLT.write("</br></table>\n</br></td></tr>")
	HTMLT.write("</table>\n</br></td>")
	

def RackII_Dashboard():
	flag = 0;
	html_new = html_dir+"/STATUS_"+RELEASE+"_"+ship+"_LLSV3_ST_week2.html";
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
	HTMLT.write("<tr align=\"center\"><td><b><font size=\"4\">Rack II</b></font>\n<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		deli,loops,passed,fail,test_pass,test_fail,total,x,y = [0]*9
		if path.exists(html_new):
			HTMLNEW = open(html_new,'r')
			lines = HTMLNEW.readlines()
			for line in lines:
				if weekday in line:
					flag = 1
				if flag == 1:
					if "Rackmount ii_Test_Status" in line and "Not Executed" not in line:
						loops = loops + 1
					if "Cases Passed" in line and "Rackmount ii_Test_Status" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						test_pass, total  = test_cases[0].split("/")
						test_pass = int(test_pass)
						total = int(total)
						test_fail = total - test_pass
						x = 1
					if "Cases Passed" in line and "Rackmount ii_smoke_Test_Status" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						test_pass1, total1  = test_cases[0].split("/")
						test_pass1 = int(test_pass1)
						total1 = int(total1)
						test_pass = test_pass + test_pass1
						total = total + total1
						test_fail1 = total1 - test_pass1
						test_fail = test_fail + test_fail1
						y = 1
						x = 0
					if ((x ==1 and y == 0) or x == 1):
						if test_pass > 0.65 * total:
							passed = passed + 1
						else:
							fail = fail + 1
					x = 0
					y = 0			
				if weekday+" END" in line:
					flag = 0
					break
		
			HTMLNEW.close()
		loop_status = str(passed)+"/"+str(fail)
		test_status = str(test_pass)+"/"+str(test_fail)
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+str(loops)+"</td>\n<td>"+loop_status+"</td>\n<td>"+str(total)+"</td>\n<td>"+test_status+"</td>\n</tr>")
	#HTMLT.write("</br></table>\n</br></td><tr>")
	#HTMLT.write("</br></table>\n</br></td>")
	HTMLT.write("</table>\n</br></td>")
	

def RackUpgrade_Dashboard():
	flag = 0;
	html_new = html_dir+"/STATUS_"+RELEASE+"_"+ship+"_LLSV3_ST_week2.html";
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
	HTMLT.write("<tr align=\"center\"><td><b><font size=\"4\">Rack Upgrade</b></font>\n<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		deli,loops,passed,fail,test_pass,test_fail,total,x,y = [0]*9
		if path.exists(html_new):
			HTMLNEW = open(html_new,'r')
			lines = HTMLNEW.readlines()
			for line in lines:
				if weekday in line:
					flag = 1
				if flag == 1:
					if "Rackmount ug_Test_Status" in line and "Not Executed" not in line:
						loops = loops + 1
					if "Cases Passed" in line and "Rackmount ug_Test_Status" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						test_pass, total  = test_cases[0].split("/")
						test_pass = int(test_pass)
						total = int(total)
						test_fail = total - test_pass
						x = 1
					if "Cases Passed" in line and "Rackmount ug_smoke_Test_Status" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						test_pass1, total1  = test_cases[0].split("/")
						test_pass1 = int(test_pass1)
						total1 = int(total1)
						test_pass = test_pass + test_pass1
						total = total + total1
						test_fail1 = total1 - test_pass1
						test_fail = test_fail + test_fail1
						y = 1
						x = 0
					if ((x ==1 and y == 0) or x == 1):
						if test_pass > 0.65 * total:
							passed = passed + 1
						else:
							fail = fail + 1
					x = 0
					y = 0			
				if weekday+" END" in line:
					flag = 0
					break
		
			HTMLNEW.close()
		loop_status = str(passed)+"/"+str(fail)
		test_status = str(test_pass)+"/"+str(test_fail)
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+str(loops)+"</td>\n<td>"+loop_status+"</td>\n<td>"+str(total)+"</td>\n<td>"+test_status+"</td>\n</tr>")
	#HTMLT.write("</br></table>\n</br></td><tr>")
	#HTMLT.write("</br></table>\n</br></td>")
	HTMLT.write("</table>\n</br></td>")
	

def Mb_Ug_Dashboard():
	pipeline_details = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/mb_ug_details.txt";
	f = open(pipeline_details,'r')
	lines = f.readlines()
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
	HTMLT.write("<tr align=\"center\"><td><b><font size=\"4\">Multi Blade Upgrade</b></font>\n<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		loops,total = ['0']*2
		loop_status,test_status = ['0/0']*2
		for line in lines:
			#if "Vapp" in line:
			#	flag = 1
			if weekday in line:
				det = line.split("::")
				loops = det[1]
				loop_status = det[2]
				total = det[3]
				test_status = det[4]
			#if "KGB" in line:
			#	flag = 0
			
		
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+loops+"</td>\n<td>"+loop_status+"</td>\n<td>"+total+"</td>\n<td>"+test_status+"</td>\n</tr>")

	#HTMLT.write("</br></table>\n</br></td>")
	HTMLT.write("</table>\n</br></td>")

def SB_UG_Dashboard():
        flag = 0;
        html_new = html_dir+"/STATUS_"+RELEASE+"_"+ship+"_LLSV3_ST_week2.html";
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
        HTMLT = open (html_table , 'a')
        HTMLT.write("<tr align=\"center\"><td><b><font size=\"4\">SB UG</b></font>\n<table border=\"3\" style=\"width:100\">\n")
        HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
        for weekday in wday:
                deli,loops,passed,fail,test_pass,test_fail,total,x,y = [0]*9
                if path.exists(html_new):
                        HTMLNEW = open(html_new,'r')
                        lines = HTMLNEW.readlines()
                        for line in lines:
                                if weekday in line:
                                        flag = 1
                                if flag == 1:
                                        if "Blade ug_Test_Status" in line and "Not Executed" not in line:
                                                loops = loops + 1
                                        if "Cases Passed" in line and "Blade ug_Test_Status" in line:
                                                test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
                                                test_pass, total  = test_cases[0].split("/")
                                                test_pass = int(test_pass)
                                                total = int(total)
                                                test_fail = total - test_pass
                                                x = 1
                                        if "Cases Passed" in line and "Blade ug_smoke_Test_Status" in line:
                                                test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
                                                test_pass1, total1  = test_cases[0].split("/")
                                                test_pass1 = int(test_pass1)
                                                total1 = int(total1)
                                                test_pass = test_pass + test_pass1
                                                total = total + total1
                                                test_fail1 = total1 - test_pass1
                                                test_fail = test_fail + test_fail1
                                                y = 1
                                                x = 0
                                        if ((x ==1 and y == 0) or x == 1):
                                                if test_pass > 0.65 * total:
                                                        passed = passed + 1
                                                else:
                                                        fail = fail + 1
                                        x = 0
                                        y = 0
                                if weekday+" END" in line:
                                        flag = 0
                                        break

                        HTMLNEW.close()
                loop_status = str(passed)+"/"+str(fail)
                test_status = str(test_pass)+"/"+str(test_fail)
                HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+str(loops)+"</td>\n<td>"+loop_status+"</td>\n<td>"+str(total)+"</td>\n<td>"+test_status+"</td>\n</tr>")
        #HTMLT.write("</br></table>\n</br></td>")
	HTMLT.write("</table>\n</br></td>")

def VappFFU_Dashboard():
        pipeline_details = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/ffuvapp_details.txt";
        f = open(pipeline_details,'r')
        lines = f.readlines()
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
        HTMLT = open (html_table , 'a')
        HTMLT.write("<td><b><font size=\"4\">VApp Upgrade</b></font>\n<table border=\"3\" style=\"width:100\">\n")
        HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
        for weekday in wday:
                loops,total = ['0']*2
                loop_status,test_status = ['0/0']*2
                for line in lines:
                        #if "Vapp" in line:
                        #       flag = 1
                        if weekday in line:
                                det = line.split("::")
                                loops = det[1]
                                loop_status = det[2]
                                total = det[3]
                                test_status = det[4]
                        #if "KGB" in line:
                        #       flag = 0


                HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+loops+"</td>\n<td>"+loop_status+"</td>\n<td>"+total+"</td>\n<td>"+test_status+"</td>\n</tr>")

        #HTMLT.write("</br></table>\n</br></td>")
	HTMLT.write("</table>\n</br></td>")
	


def Build_Dashboard():
	flag = 0;
	html_new = html_dir+"/STATUS_"+RELEASE+"_"+ship+"_LLSV3_ST_week2.html";
	pipeline_details = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/package_details.txt";
	f = open(pipeline_details,'r')
	lined = f.readlines()
	print html_new
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
	HTMLT.write("<table cellspacing=\"18\"><tr align=\"center\"><td><b><font size=\"4\">Build</b></font>\n<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF PACKAGES DELIVERED</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		deli,loops,passed,fail,test_pass,test_fail,total,x,y = [0]*9
		#if path.exists(html_new):
		HTMLNEW = open(html_new,'r')
		lines = HTMLNEW.readlines()
		for line in lines:
			if weekday in line:
				flag = 1
			if flag == 1:
				if "New Deliveries to this Build" in line:
					del1 = int(line[-7:-6])
					deli = deli + del1
					loops = loops + 1
				if "Cases Passed" in line and "Blade build_Test_Status" in line:
					test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
					test_pass, total  = test_cases[0].split("/")
					test_pass = int(test_pass)
					total = int(total)
					test_fail = total - test_pass
					if test_pass >= 0.7*total:
						passed = passed + 1
					else:
						fail = fail + 1
			if weekday+" END" in line:
				flag = 0
				break
		
		for line in lined:
			if weekday in line:
				det = line.split("::")
				deli = det[1]	
		HTMLNEW.close()
		loop_status = str(passed)+"/"+str(fail)
		test_status = str(test_pass)+"/"+str(test_fail)
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+str(deli)+"</td>\n<td>"+str(loops)+"</td>\n<td>"+loop_status+"</td>\n<td>"+str(total)+"</td>\n<td>"+test_status+"</td>\n</tr>")
	#HTMLT.write("</br></table>\n</br></td><tr></table>")
	HTMLT.write("</table>\n</br></td><tr></table>")
	JP = open(jira_details,'r')
	jiras = JP.readlines()
	HTMLT.write("&nbsp;&nbsp;&nbsp;&nbsp;<b>"+str(jiras[0])+" </b></br>\n")
	HTMLT.write("&nbsp;&nbsp;&nbsp;&nbsp;<b>"+str(jiras[1])+" </b></br>\n")
	HTMLT.write("&nbsp;&nbsp;&nbsp;&nbsp;<b>"+str(jiras[2])+" </b></br>\n")
	JP.close()
	
def PFKGB_Dashboard():
	flag = 0
	pipeline_details = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/pipeline_details.txt";
	f = open(pipeline_details,'r')
	lines = f.readlines()
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
	#HTMLT.write("<h4><font color='red'>NOTE: The following runs are based on the plan shared by SoS for the fortnight</font></h4>")
	HTMLT.write("</br><h2>Known Good Baseline (KGB)</h2>")
	HTMLT.write("<h4><font color='red'>Note: 0 indicates no check-ins on that day</font></h4>")
	HTMLT.write("<table cellspacing=\"18\"><tr align=\"center\"><td><b><font size=\"4\">PF KGB</b></font>\n<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		loops,total = ['0']*2
		loop_status,test_status = ['0/0']*2
		for line in lines:
			if "PF KGB 1" in line:
				flag = 1
			if flag and weekday in line:
				det = line.split("::")
				loops = det[1]
				loop_status = det[2]
				total = det[3]
				test_status = det[4]
			if "Infra KGB" in line:
				flag = 0
			
		
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+loops+"</td>\n<td>"+loop_status+"</td>\n<td>"+total+"</td>\n<td>"+test_status+"</td>\n</tr>")

	#HTMLT.write("</br></table>\n</br></td>")
	HTMLT.write("</table>\n</br></td>")

def TPKGB_Dashboard():
	flag = 0
	pipeline_details = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/pipeline_details.txt";
	f = open(pipeline_details,'r')
	lines = f.readlines()
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
	HTMLT.write("<td><b><font size=\"4\">TP KGB</b></font>\n<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		loops,total = ['0']*2
		loop_status,test_status = ['0/0']*2
		for line in lines:
			if "TP KGB" in line:
				flag = 1
			if flag and weekday in line:
				det = line.split("::")
				loops = det[1]
				loop_status = det[2]
				total = det[3]
				test_status = det[4]
			if "Standalone PF KGB" in line:
				flag = 0
			
		
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+loops+"</td>\n<td>"+loop_status+"</td>\n<td>"+total+"</td>\n<td>"+test_status+"</td>\n</tr>")

	#HTMLT.write("</br></table>\n</br></td></tr>")
	HTMLT.write("</table>\n</br></td>")
	
def InfraKGB_Dashboard():
	flag = 0
	pipeline_details = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/pipeline_details.txt";
	f = open(pipeline_details,'r')
	lines = f.readlines()
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
	HTMLT.write("<tr align=\"center\"><td><b><font size=\"4\">Infra KGB</b></font>\n<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		loops,total = ['0']*2
		loop_status,test_status = ['0/0']*2
		for line in lines:
			if "Infra KGB" in line:
				flag = 1
			if flag and weekday in line:
				det = line.split("::")
				loops = det[1]
				loop_status = det[2]
				total = det[3]
				test_status = det[4]
			if "TP KGB" in line:
				flag = 0
			
		
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+loops+"</td>\n<td>"+loop_status+"</td>\n<td>"+total+"</td>\n<td>"+test_status+"</td>\n</tr>")

	#HTMLT.write("</br></table>\n</br></td>")
	HTMLT.write("</table>\n</br></td>")
	
def NMIKGB_IIDashboard():
	flag = 0;
	html_new = html_dir_nmi+"/STATUS_"+RELEASE+"_"+ship+"_LLSV3_ST_week2nmi.html";
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
	HTMLT.write("<td><b><font size=\"4\">NMI KGB [Initial Install]</b></font>\n<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		deli,loops,passed,fail,test_pass,test_fail,total,x,y = [0]*9
		if path.exists(html_new):
			HTMLNEW = open(html_new,'r')
			lines = HTMLNEW.readlines()
			for line in lines:
				if weekday in line:
					flag = 1
				if flag == 1:
					if "LOOP PASSED" in line and "Blade ii_Test_Status" in line:
						loop = re.search(r'>(\d+/\d+) LOOP PASSED',line).groups()
						passed,loops  = loop[0].split("/")
						fail = int(loops) - int(passed)
					if "Blade ii_Test_Status" in line:
						if "<a href=" in line:
							link = line.split(">")
							link = link[2]
							path1 = link.split("=")
							path1 = path1[1][path1[1].index("/ibw"):-1]
							path1 = "/proj/pduosslegacy/eniqdmt"+path1
							II = open(path1,'r')
							lines1 = II.readlines()
							for line1 in lines1:
								x = 0
								if "Blade ii_Test_Status" in line1 and "Cases Passed" in line1:
									test_cases = re.search(r'>(\d+/\d+) Cases Passed',line1).groups()
									test_pass, total  = test_cases[0].split("/")
									test_pass = int(test_pass)
									total = int(total)
									test_fail = total - test_pass
								if "Blade ii_smoke_Test_Status" in line1 and "Cases Passed" in line1:
									test_cases = re.search(r'>(\d+/\d+) Cases Passed',line1).groups()
									test_pass1, total1  = test_cases[0].split("/")
									test_pass1 = int(test_pass1)
									total1 = int(total1)
									test_pass = test_pass + test_pass1
									total = total + total1
									test_fail1 = total1 - test_pass1
									test_fail = test_fail + test_fail1
									x = 1
								if x:
									break
				if weekday+" END" in line:
					flag = 0
					break
			
			HTMLNEW.close()
		loop_status = str(passed)+"/"+str(fail)
		test_status = str(test_pass)+"/"+str(test_fail)
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+str(loops)+"</td>\n<td>"+loop_status+"</td>\n<td>"+str(total)+"</td>\n<td>"+test_status+"</td>\n</tr>")

	#HTMLT.write("</br></table>\n</br></td></tr>")
	HTMLT.write("</table>\n</br></td>")
	
	
def NMIKGB_UGDashboard():
	flag = 0;
	html_new = html_dir_nmi+"/STATUS_"+RELEASE+"_"+ship+"_LLSV3_ST_week2nmi.html";
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
	HTMLT.write("<tr align=\"center\"><td><b><font size=\"4\">NMI KGB[Upgrade] </b></font>\n<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		deli,loops,passed,fail,test_pass,test_fail,total,x,y = [0]*9
		if path.exists(html_new):
			HTMLNEW = open(html_new,'r')
			lines = HTMLNEW.readlines()
			for line in lines:
				if weekday in line:
					flag = 1
				if flag == 1:
					if "LOOP PASSED" in line and "Blade ug_Test_Status" in line:
						loop = re.search(r'>(\d+/\d+) LOOP PASSED',line).groups()
						passed,loops  = loop[0].split("/")
						fail = int(loops) - int(passed)
					if "Blade ug_Test_Status" in line:
						if "<a href=" in line:
							link = line.split(">")
							link = link[2]
							path1 = link.split("=")
							path1 = path1[1][path1[1].index("/ibw"):-1]
							path1 = "/proj/pduosslegacy/eniqdmt"+path1
							II = open(path1,'r')
							lines1 = II.readlines()
							for line1 in lines1:
								x = 0
								if "Blade ug_Test_Status" in line1 and "Cases Passed" in line1:
									test_cases = re.search(r'>(\d+/\d+) Cases Passed',line1).groups()
									test_pass, total  = test_cases[0].split("/")
									test_pass = int(test_pass)
									total = int(total)
									test_fail = total - test_pass
								if "Blade ug_smoke_Test_Status" in line1 and "Cases Passed" in line1:
									test_cases = re.search(r'>(\d+/\d+) Cases Passed',line1).groups()
									test_pass1, total1  = test_cases[0].split("/")
									test_pass1 = int(test_pass1)
									total1 = int(total1)
									test_pass = test_pass + test_pass1
									total = total + total1
									test_fail1 = total1 - test_pass1
									test_fail = test_fail + test_fail1
									x = 1
								if x:
									break
				if weekday+" END" in line:
					flag = 0
					break
			
			HTMLNEW.close()
		loop_status = str(passed)+"/"+str(fail)
		test_status = str(test_pass)+"/"+str(test_fail)
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+str(loops)+"</td>\n<td>"+loop_status+"</td>\n<td>"+str(total)+"</td>\n<td>"+test_status+"</td>\n</tr>")

	#HTMLT.write("</br></table>\n</br></td>")
	HTMLT.write("</table>\n</br></td>")
						
						
						
def NMIKGB_RBDashboard():
	flag = 0;
	html_new = html_dir_nmi+"/STATUS_"+RELEASE+"_"+ship+"_LLSV3_ST_week2nmi.html";
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
	HTMLT.write("<td><b><font size=\"4\">NMI KGB[Rollback] </b></font>\n<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		deli,loops,passed,fail,test_pass,test_fail,total,x,y = [0]*9
		if path.exists(html_new):
			HTMLNEW = open(html_new,'r')
			lines = HTMLNEW.readlines()
			for line in lines:
				if weekday in line:
					flag = 1
				if flag == 1:
					if "LOOP PASSED" in line and "Blade rb_Test_Status" in line:
						loop = re.search(r'>(\d+/\d+) LOOP PASSED',line).groups()
						passed,loops  = loop[0].split("/")
						fail = int(loops) - int(passed)
					if "Blade rb_Test_Status" in line:
						if "<a href=" in line:
							link = line.split(">")
							link = link[2]
							path1 = link.split("=")
							path1 = path1[1][path1[1].index("/ibw"):-1]
							path1 = "/proj/pduosslegacy/eniqdmt"+path1
							II = open(path1,'r')
							lines1 = II.readlines()
							for line1 in lines1:
								x = 0
								if "Blade rb_Test_Status" in line1 and "Cases Passed" in line1:
									test_cases = re.search(r'>(\d+/\d+) Cases Passed',line1).groups()
									test_pass, total  = test_cases[0].split("/")
									test_pass = int(test_pass)
									total = int(total)
									test_fail = total - test_pass
								if "Blade rb_smoke_Test_Status" in line1 and "Cases Passed" in line1:
									test_cases = re.search(r'>(\d+/\d+) Cases Passed',line1).groups()
									test_pass1, total1  = test_cases[0].split("/")
									test_pass1 = int(test_pass1)
									total1 = int(total1)
									test_pass = test_pass + test_pass1
									total = total + total1
									test_fail1 = total1 - test_pass1
									test_fail = test_fail + test_fail1
									x = 1
								if x:
									break
				if weekday+" END" in line:
					flag = 0
					break
			
			HTMLNEW.close()
		loop_status = str(passed)+"/"+str(fail)
		test_status = str(test_pass)+"/"+str(test_fail)
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+str(loops)+"</td>\n<td>"+loop_status+"</td>\n<td>"+str(total)+"</td>\n<td>"+test_status+"</td>\n</tr>")

	#HTMLT.write("</br></table>\n</br></td></tr>")
	HTMLT.write("</table>\n</br></td>")


def Standalone_PF_KGB_Dashboard():
	flag = 0
	pipeline_details = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/pipeline_details.txt";
	f = open(pipeline_details,'r')
	lines = f.readlines()
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
	HTMLT.write("<tr align=\"center\"><td><b><font size=\"4\">Standalone PF KGB</b></font>\n<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		loops,total = ['0']*2
		loop_status,test_status = ['0/0']*2
		for line in lines:
			if "Standalone PF KGB" in line:
				flag = 1
			if flag and weekday in line:
				det = line.split("::")
				loops = det[1]
				loop_status = det[2]
				total = det[3]
				test_status = det[4]
			if "PF KGB 1" in line:
				flag = 0
			
		
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+loops+"</td>\n<td>"+loop_status+"</td>\n<td>"+total+"</td>\n<td>"+test_status+"</td>\n</tr>")

	HTMLT.write("</br></table>\n</br></td>")
	#HTMLT.write("</table>\n</br></td>")
	

def NMIKGB_RIIDashboard():
	flag = 0;
	html_new = html_dir_nmi+"/STATUS_"+RELEASE+"_"+ship+"_LLSV3_ST_week2nmi.html";
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
	HTMLT.write("<td><b><font size=\"4\">NMI KGB[Rack II] </b></font>\n<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		deli,loops,passed,fail,test_pass,test_fail,total,x,y = [0]*9
		if path.exists(html_new):
			HTMLNEW = open(html_new,'r')
			lines = HTMLNEW.readlines()
			for line in lines:
				if weekday in line:
					flag = 1
				if flag == 1:
					if "LOOP PASSED" in line and "Rackmount ii_Test_Status" in line:
						loop = re.search(r'>(\d+/\d+) LOOP PASSED',line).groups()
						passed,loops  = loop[0].split("/")
						fail = int(loops) - int(passed)
					if "Rackmount ii_Test_Status" in line:
						if "<a href=" in line:
							link = line.split(">")
							link = link[2]
							path1 = link.split("=")
							path1 = path1[1][path1[1].index("/ibw"):-1]
							path1= "/proj/pduosslegacy/eniqdmt"+path1
							II = open(path1,'r')
							lines1 = II.readlines()
							for line1 in lines1:
								x = 0
								if "Rackmount ii_Test_Status" in line1 and "Cases Passed" in line1:
									test_cases = re.search(r'>(\d+/\d+) Cases Passed',line1).groups()
									test_pass, total  = test_cases[0].split("/")
									test_pass = int(test_pass)
									total = int(total)
									test_fail = total - test_pass
								if "Rackmount ii_smoke_Test_Status" in line1 and "Cases Passed" in line1:
									test_cases = re.search(r'>(\d+/\d+) Cases Passed',line1).groups()
									test_pass1, total1  = test_cases[0].split("/")
									test_pass1 = int(test_pass1)
									total1 = int(total1)
									test_pass = test_pass + test_pass1
									total = total + total1
									test_fail1 = total1 - test_pass1
									test_fail = test_fail + test_fail1
									x = 1
								if x:
									break
				if weekday+" END" in line:
					flag = 0
					break
			
			HTMLNEW.close()
		loop_status = str(passed)+"/"+str(fail)
		test_status = str(test_pass)+"/"+str(test_fail)
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+str(loops)+"</td>\n<td>"+loop_status+"</td>\n<td>"+str(total)+"</td>\n<td>"+test_status+"</td>\n</tr>")

	HTMLT.write("</br></table>\n</br></td></tr>")
	#HTMLT.write("</table>\n</br></td>")
	
	
def NMIKGB_MBDashboard():
	flag = 0;
	html_new = html_dir_nmi+"/STATUS_"+RELEASE+"_"+ship+"_LLSV3_SM_week2nmi.html";
	html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
	HTMLT = open (html_table , 'a')
	HTMLT.write("<tr align=\"center\"><td><b><font size=\"4\">NMI KGB[MB II] </b></font>\n<table border=\"3\" style=\"width:100\">\n")
	HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>DAY</th>\n<th>NUMBER OF LOOPS RUN</th>\n<th>LOOP STATUS:PASS VS FAIL</th>\n<th>NUMBER OF TEST CASES RUN</th>\n<th>TESTCASE:PASS VS FAIL</th>\n</tr>")
	for weekday in wday:
		deli,loops,passed,fail,test_pass,test_fail,total = [0]*7
		cord_total, cord_smoke_total, eng_smoke_total, eng_total, read1_total, read1_smoke_total, read2_smoke_total, read2_total = [0] * 8
		cord_test_pass, cord_test_smoke_pass, eng_test_pass, eng_test_smoke_pass, read1_test_pass, read1_test_smoke_pass, read2_test_pass, read2_test_smoke_pass = [0] * 8
		cord_test_fail, cord_test_smoke_fail, eng_test_fail, eng_test_smoke_fail, read1_test_fail, read1_test_smoke_fail, read2_test_fail, read2_test_smoke_fail = [0] * 8
		if path.exists(html_new):
			HTMLNEW = open(html_new,'r')
			lines = HTMLNEW.readlines()
			for line in lines:
				if weekday in line:
					flag = 1
				if flag == 1:
					if "COORDINATOR Blade ii_Test_Status" in line and "Not Executed" not in line:
						loops = loops + 1
					if "COORDINATOR Blade ii_Test_Status" in line and ('<td bgcolor="#04B45F"' in line or '<td bgcolor="orange"' in line):
						passed = passed + 1
					if "COORDINATOR Blade ii_Test_Status" in line and '<td bgcolor="red"' in line:
						fail = fail + 1
					if "COORDINATOR Blade ii_Test_Status" in line and "Cases Passed" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						cord_test_pass, cord_total  = test_cases[0].split("/")
						cord_test_pass = int(cord_test_pass)
						cord_total = int(cord_total)
						cord_test_fail = cord_total - cord_test_pass
					if "COORDINATOR Blade ii_smoke_Test_Status" in line and "Cases Passed" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						cord_test_smoke_pass, cord_smoke_total  = test_cases[0].split("/")
						cord_test_smoke_pass = int(cord_test_smoke_pass)
						cord_smoke_total = int(cord_smoke_total)
						cord_test_smoke_fail = cord_smoke_total - cord_test_smoke_pass
					
					if "ENGINE Blade ii_Test_Status" in line and "Cases Passed" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						eng_test_pass, eng_total  = test_cases[0].split("/")
						eng_test_pass = int(eng_test_pass)
						eng_total = int(eng_total)
						eng_test_fail = eng_total - eng_test_pass
					if "ENGINE Blade ii_smoke_Test_Status" in line and "Cases Passed" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						eng_test_smoke_pass, eng_smoke_total  = test_cases[0].split("/")
						eng_test_smoke_pass = int(eng_test_smoke_pass)
						eng_smoke_total = int(eng_smoke_total)
						eng_test_smoke_fail = eng_smoke_total - eng_test_smoke_pass
					if "READER1 Blade ii_Test_Status" in line and "Cases Passed" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						read1_test_pass, read1_total  = test_cases[0].split("/")
						read1_test_pass = int(read1_test_pass)
						read1_total = int(read1_total)
						read1_test_fail = read1_total - read1_test_pass
					if "READER1 Blade ii_smoke_Test_Status" in line and "Cases Passed" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						read1_test_smoke_pass, read1_smoke_total  = test_cases[0].split("/")
						read1_test_smoke_pass = int(read1_test_smoke_pass)
						read1_smoke_total = int(read1_smoke_total)
						read1_test_smoke_fail = read1_smoke_total - read1_test_smoke_pass
					if "READER2 Blade ii_Test_Status" in line and "Cases Passed" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						read2_test_pass, read2_total  = test_cases[0].split("/")
						read2_test_pass = int(read2_test_pass)
						read2_total = int(read2_total)
						read2_test_fail = read2_total - read2_test_pass
					if "READER2 Blade ii_smoke_Test_Status" in line and "Cases Passed" in line:
						test_cases = re.search(r'>(\d+/\d+) Cases Passed',line).groups()
						read2_test_smoke_pass, read2_smoke_total  = test_cases[0].split("/")
						read2_test_smoke_pass = int(read2_test_smoke_pass)
						read2_smoke_total = int(read2_smoke_total)
						read2_test_smoke_fail = read2_smoke_total - read2_test_smoke_pass
				if weekday+" END" in line:
					flag = 0
					break
			HTMLNEW.close()
		total = cord_total + cord_smoke_total + eng_smoke_total + eng_total + read1_total + read1_smoke_total + read2_smoke_total + read2_total;
		test_pass = cord_test_pass + cord_test_smoke_pass + eng_test_pass + eng_test_smoke_pass + read1_test_pass +read1_test_smoke_pass + read2_test_pass + read2_test_smoke_pass;
		test_fail = cord_test_fail + cord_test_smoke_fail + eng_test_fail + eng_test_smoke_fail + read1_test_fail +read1_test_smoke_fail + read2_test_fail + read2_test_smoke_fail;	
					
		loop_status = str(passed)+"/"+str(fail)
		test_status = str(test_pass)+"/"+str(test_fail)
		HTMLT.write("<tr align=\"center\">\n<td bgcolor=\"#98AFC7\"><b>"+weekday+"</b></td>\n<td>"+str(loops)+"</td>\n<td>"+loop_status+"</td>\n<td>"+str(total)+"</td>\n<td>"+test_status+"</td>\n</tr>")

	#HTMLT.write("</br></table>\n</br></td></tr></table>\n")				
	HTMLT.write("</table>\n</br></td>")
	#HTMLT.write("</body>\n</html>")
	HTMLT.close()
	
html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
HTMLT = open (html_table , 'w')
HTMLT.write("<html>\n<head><center><h1>Weekly CI Dashboard</h1></center></head>\n<body>")

HTMLT.write("<h4><font color='red'>NOTE: The following runs are based on the plan shared by SoS for the fortnight</font></h4>")

HTMLT.write("<h2>Radiator Pages</h2>")
url = "https://eniqdmt.seli.wh.rnd.internal.ericsson.com/kgb_radiator_"+ship+".html"
print(url)
link = '<h3><a href="' + url +'">KGB</a></h3>'
HTMLT.write(link)

url = "https://eniqdmt.seli.wh.rnd.internal.ericsson.com/cdb_radiator_"+ship+".html"
print(url)
link = '<h3><a href="' + url +'">CDB II</a></h3>'
HTMLT.write(link)

url = "https://eniqdmt.seli.wh.rnd.internal.ericsson.com/cdb_upgrade_radiator_"+ship+".html"
print(url)
link = '<h3><a href="' + url +'">CDB Upgrade</a></h3>'
HTMLT.write(link)

#HTMLT.write("<a href="url">CDB II</a>")
#HTMLT.write("<a href="url">CDB Upgrade</a>")
HTMLT.write("<h2>Customer Deployable Baseline (CDB)</h2>")
HTMLT.write("<table cellspacing=\"18\">")
HTMLT.close()

#II_Dashboard()
#MBII_Dashboard()
RackII_Dashboard()
VappII_Dashboard()
#RackII_Dashboard()
#RackUpgrade_Dashboard()
#Mb_Ug_Dashboard()
#RackUpgrade_Dashboard()
SB_UG_Dashboard()
VappFFU_Dashboard()
#VappII_Dashboard()
RackUpgrade_Dashboard()
Build_Dashboard()
PFKGB_Dashboard()
TPKGB_Dashboard()
InfraKGB_Dashboard()
NMIKGB_IIDashboard()
NMIKGB_UGDashboard()
NMIKGB_RBDashboard()
#Standalone_PF_KGB_Dashboard()
#NMIKGB_RIIDashboard()
NMIKGB_MBDashboard()

html_table = "/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/test.html";
HTMLT = open (html_table , 'a')
HTMLT.write("</table>\n</body>\n</html>")
HTMLT.close()
