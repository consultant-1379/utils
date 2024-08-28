import re
import requests
import base64
from bs4 import BeautifulSoup
import sys


def build_results(jenkins_link,ship1,ship2):
	pwd = base64.b64decode("TmFwbGVzITA1MTI=")
	page = requests.get(jenkins_link, auth=('esjkadm100', pwd))
	soup = BeautifulSoup(page.content, 'html.parser')
	contents = soup.prettify()
	lines = contents.split("\n")
	total_count1,total_count2,succ_count2,succ_count1 = 0,0,0,0
	for index,line in enumerate(lines):
		if month in line:
			if 'tooltip="Failed &gt; Console Output"' in lines[index-9] or 'tooltip="Success &gt; Console Output"' in lines[index-9]:
				console_link = re.search(r'href="(.+)"', lines[index-10]).groups()[0]
				console_link = "https://fem167-eiffel004.lmera.ericsson.se:8443"+console_link
				job_page = requests.get(console_link, auth=('esjkadm100', pwd))
				job_contents = job_page.content
				job_lines = job_contents.split("\n")
				for line1 in job_lines:
					if ship1 in line1:
						total_count1 = total_count1 + 1
						break
					elif ship2 in line1:
						total_count2 = total_count2 + 1
						break

	for index,line in enumerate(lines):
		if month in line:
			if 'tooltip="Success &gt; Console Output"' in lines[index-9]:
				console_link = re.search(r'href="(.+)"', lines[index-10]).groups()[0]
				console_link = "https://fem167-eiffel004.lmera.ericsson.se:8443"+console_link
				job_page = requests.get(console_link, auth=('esjkadm100', pwd))
				job_contents = job_page.content
				job_lines = job_contents.split("\n")
				for line1 in job_lines:
					if ship1 in line1:
						succ_count1 = succ_count1 + 1
						break
					elif ship2 in line1:
						succ_count2 = succ_count2 + 1
						break
	return total_count1,total_count2,succ_count1,succ_count2
	

def build_results_ship3(jenkins_link,ship1):
	pwd = base64.b64decode("TmFwbGVzITA1MTI=")
	page = requests.get(jenkins_link, auth=('esjkadm100', pwd))
	soup = BeautifulSoup(page.content, 'html.parser')
	contents = soup.prettify()
	lines = contents.split("\n")
	total_count1,total_count2,succ_count2,succ_count1 = 0,0,0,0
	for index,line in enumerate(lines):
		if month in line:
			if 'tooltip="Aborted &gt; Console Output"' not in lines[index-9]:
				console_link = re.search(r'href="(.+)"', lines[index-10]).groups()[0]
				console_link = "https://fem167-eiffel004.lmera.ericsson.se:8443"+console_link
				job_page = requests.get(console_link, auth=('esjkadm100', pwd))
				job_contents = job_page.content
				job_lines = job_contents.split("\n")
				for line1 in job_lines:
					if ship1 in line1:
						total_count1 = total_count1 + 1
						break

	for index,line in enumerate(lines):
		if month in line:
			if 'tooltip="Success &gt; Console Output"' in lines[index-9]:
				console_link = re.search(r'href="(.+)"', lines[index-10]).groups()[0]
				console_link = "https://fem167-eiffel004.lmera.ericsson.se:8443"+console_link
				job_page = requests.get(console_link, auth=('esjkadm100', pwd))
				job_contents = job_page.content
				job_lines = job_contents.split("\n")
				for line1 in job_lines:
					if ship1 in line1:
						succ_count1 = succ_count1 + 1
						break
	return total_count1,succ_count1

	
try:
	month = sys.argv[1]
	s1_19_4 = sys.argv[2]
	s2_19_4 = sys.argv[3]
	s1_20_2 = sys.argv[4]
	s2_20_2 = sys.argv[5]
	s1_20_4 = sys.argv[6]
	s2_20_4 = sys.argv[7]


	#If there is a third sprint, uncomment the below lines
	# s3_19_2 = sys.argv[10]
	# s3_19_4 = sys.argv[11]
	# s3_20_2 = sys.argv[12]
	# s3_18_2 = sys.argv[13]
except Exception as e:
	print "Invalid arguments"


		
ES20_2_job_link = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/view/Linux_Builds/job/ENIQ_BUILD_LINUX_ISO_S20.2"
ES20_s1_total,ES20_s2_total,ES20_s1_succ,ES20_s2_succ=build_results(ES20_2_job_link,s1_20_2,s2_20_2)
ES19_4_job_link = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/view/Linux_Builds/job/ENIQ_BUILD_LINUX_ISO_S19.4"
ES19_4_s1_total,ES19_4_s2_total,ES19_4_s1_succ,ES19_4_s2_succ=build_results(ES19_4_job_link,s1_19_4,s2_19_4)
ES20_4_job_link = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/view/Linux_Builds/job/ENIQ_BUILD_LINUX_ISO_S20.4"
ES20_4_s1_total,ES20_4_s2_total,ES20_4_s1_succ,ES20_4_s2_succ=build_results(ES20_4_job_link,s1_20_4,s2_20_4)


EI20_2_job_link = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/view/Linux_Builds/job/ENIQ_BUILD_LINUX_ISO_I20.2"
EI20_s1_total,EI20_s2_total,EI20_s1_succ,EI20_s2_succ=build_results(EI20_2_job_link,s1_20_2,s2_20_2)
EI19_4_job_link = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/view/Linux_Builds/job/ENIQ_BUILD_LINUX_ISO_I19.4"
EI19_4_s1_total,EI19_4_s2_total,EI19_4_s1_succ,EI19_4_s2_succ=build_results(EI19_4_job_link,s1_19_4,s2_19_4)
EI20_4_job_link = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/view/Linux_Builds/job/ENIQ_BUILD_LINUX_ISO_I20.4"
EI20_4_s1_total,EI20_4_s2_total,EI20_4_s1_succ,EI20_4_s2_succ=build_results(EI20_4_job_link,s1_20_4,s2_20_4)

#If there is a third sprint, uncomment the below lines
# ES19_2_s3_total,ES19_2_s3_succ=build_results_ship3(ES19_2_job_link,s3_19_2)
# ES20_s3_total,ES20_s3_succ=build_results_ship3(ES20_2_job_link,s3_20_2)
# ES19_4_s3_total,ES19_4_s3_succ=build_results_ship3(ES19_4_job_link,s3_19_4)
# ES18_2_s3_total,ES18_2_s3_succ=build_results_ship3(ES18_2_job_link,s3_18_2)
# EI19_2_s3_total,EI19_2_s3_succ=build_results_ship3(EI19_2_job_link,s3_19_2)
# EI20_s3_total,EI20_s3_succ=build_results_ship3(EI20_2_job_link,s3_20_2)
# EI19_4_s3_total,EI19_4_s3_succ=build_results_ship3(EI19_4_job_link,s3_19_4)


f = open('/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/builds_report.html','w')
f.write("<html>\n<body>\n")
f.write("<table border=\"3\"><b><th colspan=\"2\">Sprint</th><th>Total Builds</th><th>Successful Builds</th></b>\n")

## uncomment the below lines if third sprint is there
# f.write("<tr><td rowspan=\"2\">"+s2_19_3+"</td><td>ENIQ_STATS</td><td>"+str(ES19_2_s3_total)+"</td><td>"+str(ES19_2_s3_succ)+"</td></tr>")
# f.write("<tr><td>INFRA</td><td>"+str(EI19_2_s3_total)+"</td><td>"+str(EI19_2_s3_succ)+"</td></tr>")
##

f.write("<tr><td rowspan=\"2\">"+s1_19_4+"</td><td>ENIQ_STATS</td><td>"+str(ES19_4_s1_total)+"</td><td>"+str(ES19_4_s1_succ)+"</td></tr>\n")
f.write("<tr><td>INFRA</td><td>"+str(EI19_4_s1_total)+"</td><td>"+str(EI19_4_s1_succ)+"</td></tr>\n")
f.write("<tr><td rowspan=\"2\">"+s2_19_4+"</td><td>ENIQ_STATS</td><td>"+str(ES19_4_s2_total)+"</td><td>"+str(ES19_4_s2_succ)+"</td></tr>\n")
f.write("<tr><td>INFRA</td><td>"+str(EI19_4_s2_total)+"</td><td>"+str(EI19_4_s2_succ)+"</td></tr>\n")

## uncomment the below lines if third sprint is there
# f.write("<tr><td rowspan=\"2\">"+s3_19_4+"</td><td>ENIQ_STATS</td><td>"+str(ES19_4_s3_total)+"</td><td>"+str(ES19_4_s3_succ)+"</td></tr>")
# f.write("<tr><td>INFRA</td><td>"+str(EI19_4_s3_total)+"</td><td>"+str(EI19_4_s3_succ)+"</td></tr>")
##

f.write("<tr><td rowspan=\"2\">"+s1_20_2+"</td><td>ENIQ_STATS</td><td>"+str(ES20_s1_total)+"</td><td>"+str(ES20_s1_succ)+"</td></tr>\n")
f.write("<tr><td>INFRA</td><td>"+str(EI20_s1_total)+"</td><td>"+str(EI20_s1_succ)+"</td></tr>")
f.write("<tr><td rowspan=\"2\">"+s2_20_2+"</td><td>ENIQ_STATS</td><td>"+str(ES20_s2_total)+"</td><td>"+str(ES20_s2_succ)+"</td></tr>\n")
f.write("<tr><td>INFRA</td><td>"+str(EI20_s2_total)+"</td><td>"+str(EI20_s2_succ)+"</td></tr>")

## uncomment the below lines if third sprint is there
# f.write("<tr><td rowspan=\"2\">"+s3_20_2+"</td><td>ENIQ_STATS</td><td>"+str(ES20_s3_total)+"</td><td>"+str(ES20_s3_succ)+"</td></tr>")
# f.write("<tr><td>INFRA</td><td>"+str(EI20_s3_total)+"</td><td>"+str(EI20_s3_succ)+"</td></tr>")
##

f.write("<tr><td rowspan=\"2\">"+s1_20_4+"</td><td>ENIQ_STATS</td><td>"+str(ES20_4_s1_total)+"</td><td>"+str(ES20_4_s1_succ)+"</td></tr>\n")
f.write("<tr><td>INFRA</td><td>"+str(EI20_4_s1_total)+"</td><td>"+str(EI20_4_s1_succ)+"</td></tr>")
f.write("<tr><td rowspan=\"2\">"+s2_20_4+"</td><td>ENIQ_STATS</td><td>"+str(ES20_4_s2_total)+"</td><td>"+str(ES20_4_s2_succ)+"</td></tr>\n")
f.write("<tr><td>INFRA</td><td>"+str(EI20_4_s2_total)+"</td><td>"+str(EI20_4_s2_succ)+"</td></tr>")

# f.write("<tr><td colspan = \"2\">"+s1_18_2+"</td><td>"+str(ES18_2_s1_total)+"</td><td>"+str(ES18_2_s1_succ)+"</td></tr>\n")
# f.write("<tr><td colspan = \"2\">"+s2_18_2+"</td><td>"+str(ES18_2_s2_total)+"</td><td>"+str(ES18_2_s2_succ)+"</td></tr>\n")

## uncomment the below lines if third sprint is there
# f.write("<tr><td colspan = \"2\">"+s3_18_2+"</td><td>"+str(ES18_2_s3_total)+"</td><td>"+str(ES18_2_s3_succ)+"</td></tr>")
##

f.write("</table></body></html>")


