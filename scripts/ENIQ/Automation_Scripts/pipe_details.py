import requests
import getpass
import datetime
import base64

pwd = base64.b64decode("TmFwbGVzITA1MTI=")
page_list = {"https://fem156-eiffel004.lmera.ericsson.se:8443/jenkins/view/PF_KGB/":3, "https://fem160-eiffel004.lmera.ericsson.se:8443/jenkins/view/ES_KGB/":3, 			"https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/view/VCDB_LINUX_II_Pipeline/":8, "https://fem156-eiffel004.lmera.ericsson.se:8443/jenkins/view/INFRA_KGB_Pipeline/":6}

with open ('/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/PIPE/pipeline_details.txt', 'w') as newFile:
	newFile.write("|" + "DAY".center(15) + "|" + "NUMBER OF LOOPS RUN".center(30) + "|" + "LOOP STATUS:PASS VS FAIL".center(30) + "|" + "NUMBER OF TEST CASES RUN".center(30) + "|" + "TESTCASE:PASS VS FAIL".center(30) + "|\n")

month_dict = {"Jan":1,"Feb":2,"Mar":3,"Apr":4, "May":5, "Jun":6, "Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}

def getDate(line, tmp):
	date = line.split("\"startDate\":")[1].split(",\"")[0].split("\"")[1]
	#print date
	year = int(date.split(",")[1].strip())
	month = month_dict[date.split(",")[0].split(" ")[0].strip()]
	day = int(date.split(",")[0].split(" ")[1].strip())
	if (day < today.day) and (today.month == month):
		point = True
	elif (day > today.day) and (today.month != month):
		point = True
	else:
		point = False
	
	dayofweek = datetime.date(year, month, day).strftime("%A")
	if tmp == '':
		tmp = dayofweek
	return dayofweek, point, tmp
		
for pageLink in page_list.keys():
	try:
		page = requests.get(pageLink, auth=('esjkadm100', pwd))
		jobInfo = page_list[pageLink]
		jobName = pageLink.split("/")[-2]
		contents = page.content

		jobCount = 1
		loopCount = passCount = failCount = 0
		days = [];tmp = '';startDate='';row='';lastDay=''
		passFailFlag = False; point = False
		pipeLineResult = {}
		today = datetime.datetime.today() - datetime.timedelta(days=7)

		with open ('/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/PIPE/tmp.txt', 'w+') as newFile:
			newFile.write(contents)

		with open ('/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/PIPE/tmp.txt', 'r+') as newFile:
			for line in newFile.readlines():
				if ("displayName" in line) and ("startDate" in line):
					
					#print startDate, tmp
					if "SUCCESS" in line:
						passFailFlag = True
					else:
						passFailFlag = False
						
					if jobCount == 1:
						day, breakPoint, tmp = getDate(line, tmp)
						#print tmp, day, lastDay
						if lastDay != day and lastDay != '':
							row =  lastDay + "::" + str(loopCount) + "::" + (str(passCount)+"/" + str(failCount)) + "::\n" + row
							loopCount = passCount = failCount = 0
						if breakPoint:
							break
						lastDay = day
					elif jobCount == jobInfo:
						if passFailFlag: passCount+=1
						else: failCount+=1
						loopCount+=1
						jobCount = 0
						pipeLineResult[day] = pipeLineResult.get(day, 0) + 1
						
					jobCount+=1

		#print pipeLineResult
		with open ('/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/PIPE/pipeline_details.txt', 'a+') as newFile:
			newFile.write("\n***"+jobName+"***\n\n")
			newFile.write(row)
			newFile.write("\n***"+jobName+"END***\n\n")
	except Exception as error:
		print "ERROR : " + str(error)
		print "Please check your input!!"


