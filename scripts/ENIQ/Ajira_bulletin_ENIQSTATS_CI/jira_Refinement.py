import os
import sys
import json
import time
import datetime
import utils
from jira import JIRA

#Read config file
if sys.platform == "win32":
    path = ".."
else:
    path = "scripts"
sys.path.append(path + '/lib')
import requests
from requests.auth import HTTPBasicAuth
import ConfigParser
#Read config file
config = ConfigParser.ConfigParser()
config.read('scripts/etc/config_jira_Refinement.cfg')

#html file formation
textEnd = config.get('email', 'textEnd')
tableStart = config.get('email', 'tableStart')
tab1 = config.get('email', 'tab1')
tab2 = config.get('email', 'tab2')
tab3 = config.get('email', 'tab3')
tab4 = config.get('email', 'tab4')
tab5 = config.get('email', 'tab5')
tab6 = config.get('email', 'tab6')
tabEnd1 = config.get('email', 'tabEnd1')
content = config.get('email', 'content')

#script start to manipulate the jira input outputs
proxy = {
    "http": "",
   "https": "",
    }
jiraUrl="https://jira-oss.seli.wh.rnd.internal.ericsson.com/rest/api/2/search?"

#jqlQuery='jql=project%20=%20EQEV%20AND%20issuetype%20=%20MR%20AND%20labels%20=%20ENIQ-ReadyForRefinement'
jqlQuery='jql=project = EQEV AND issuetype = MR AND status not in (Closed, "MR Cancelled") AND labels = ENIQ-ReadyForRefinement'

headers = {'Content-Type': 'application/json'}
getData=requests.get(str(jiraUrl)+str(jqlQuery) ,auth=HTTPBasicAuth('statsjenki','Oct#2023'),headers=headers,proxies=proxy)
jsonData=json.loads(getData.text)

print("Total Issues : " , jsonData['total'])
total = jsonData['total']

if total != 0 :
	print("Total issue is not 0")
	#start writing html
	emailHeader = open("scripts/etc/mailHeader_jira_Refinement.txt", 'r')
	emailReport = open("scripts/etc/mailReport_jira_Refinement.html", 'w')
	emailReport.write(str(emailHeader.read()))

	emailReport.write(str(tableStart))
	
	for data in jsonData['issues']:
			try:
					if data['fields']['assignee'] is None:
							assignee = "Unassigned"
					else:
							assignee = str(data['fields']['assignee']['displayName']).strip()

					creationDate = str(data['fields']['created']).strip()[:10]
					create = datetime.datetime.strptime(creationDate, "%Y-%m-%d").date()
					currentDate = datetime.datetime.utcnow()
					currentDate1 = currentDate.strftime("%Y-%m-%d")
					current = datetime.datetime.strptime(currentDate1, "%Y-%m-%d").date()
					ticketDays = abs((current - create).days)
					key = data['key']
					linkUrl = "https://jira-oss.seli.wh.rnd.internal.ericsson.com/browse/" + key

					if not data['fields']['components']:
							components = "None"
					else:
							comp = data['fields']['components']
							compo = [li[u'name'] for li in comp]
							compon = [str(x) for x in compo]
							components = ",".join(compon)
							#print components
					if not data['fields']['labels']:
							labels = "None"
					else:
							lab = data['fields']['labels']
							label = [str(l) for l in lab]
							labels = ",".join(label)
							#print labels
					if not data['fields']['fixVersions']:
							fixVersion = "None"
					else:
							fixV = data['fields']['fixVersions']
							fixVer = [li[u'name'] for li in fixV]
							fixVers = [str(l) for l in fixVer]
							fixVersion = ",".join(fixVers)
							#print fixVersion


					###writing data in html file####
					emailReport.write(str(tab1))
					emailReport.write(str(data['fields']['issuetype']['name']))
					emailReport.write(str(tab2))
					emailReport.write("<a href =" + str(linkUrl) + ">" + str(key) + "</a>")
					#emailReport.write(str(data['key']))
					emailReport.write(str(tab3))
					emailReport.write(str(data['fields']['summary']))
					emailReport.write(str(tab4))
					emailReport.write(str(data['fields']['status']['name']))
					emailReport.write(str(tab5))
					emailReport.write(str(assignee))

					
					####for taking last comment####
					jira = JIRA(basic_auth=('statsjenki',"Apr#2024"), options={'server':'http://jira-oss.seli.wh.rnd.internal.ericsson.com'})
					IssueNo = (str(key))
					comments_id=jira.comments(IssueNo)
					a=int(0)
					for i in comments_id:
						if int(i.id)>a:
							a=int(i.id)
					lastComment = jira.comment(IssueNo,a).body
					print(type(lastComment))
					lastComment = lastComment.encode('utf-8','ignore')
					emailReport.write(str(tab6))
					emailReport.write(str(lastComment))
					emailReport.write(str(tabEnd1))
			except Exception as e:
					print(" Error in printing jira information")
					print(e)
					exit(1)
	emailReport.write(str(content))

elif total == 0:
		print("Total issue is 0")
		emailReport = open("scripts/etc/mailReport_jira_Refinement.html", 'w')
		emailReport.write("Hi All,<br><br>No MR for discussion this Week.<br><br><b>Regards,<br>Technical Management Scope Team<br>ENIQ_S</b>")
