import os
import sys
import json
import time
import datetime
import utils
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
config.read('scripts/etc/config_jira_Wizzards.cfg')

#html file formation
textEnd = config.get('email', 'textEnd')
tableStart = config.get('email', 'tableStart')
tab1 = config.get('email', 'tab1')
tab2 = config.get('email', 'tab2')
tab3 = config.get('email', 'tab3')
tab4 = config.get('email', 'tab4')
tab5 = config.get('email', 'tab5')
tab6 = config.get('email', 'tab6')
tab7 = config.get('email', 'tab7')
tab8 = config.get('email', 'tab8')
tab9 = config.get('email', 'tab9')
tab10 = config.get('email', 'tab10')
tabEnd1 = config.get('email', 'tabEnd1')

tab11 = config.get('email', 'tab11')
tab12 = config.get('email', 'tab12')
tab13 = config.get('email', 'tab13')
tab14 = config.get('email', 'tab14')
tab15 = config.get('email', 'tab15')
tab16 = config.get('email', 'tab16')
tab17 = config.get('email', 'tab17')
tab18 = config.get('email', 'tab18')
tab19 = config.get('email', 'tab19')
tab20 = config.get('email', 'tab20')
tabEnd2 = config.get('email', 'tabEnd2')

tab21 = config.get('email', 'tab21')
tab22 = config.get('email', 'tab22')
tab23 = config.get('email', 'tab23')
tab24 = config.get('email', 'tab24')
tab25 = config.get('email', 'tab25')
tab26 = config.get('email', 'tab26')
tab27 = config.get('email', 'tab27')
tab28 = config.get('email', 'tab28')
tab29 = config.get('email', 'tab29')
tab30 = config.get('email', 'tab30')
tabEnd3 = config.get('email', 'tabEnd3')
content = config.get('email', 'content')

#start writing html
emailHeader = open("scripts/etc/mailHeader_jira_Wizzards.txt", 'r')
emailReport = open("scripts/etc/mailReport_jira_Wizzards.html", 'w')
emailReport.write(str(emailHeader.read()))

#script start to manipulate the jira input outputs
proxy = {
    "http": "",
   "https": "",
    }
#jiraUrl="http://jira-nam.lmera.ericsson.se/rest/api/2/search?"
jiraUrl="https://jira-oss.seli.wh.rnd.internal.ericsson.com/rest/api/2/search?"

jqlQuery='jql=project%20%3D%20EQEV%20AND%20status%20in%20(Open%2C%20%22In%20Progress%22%2C%20Reopened%2C%20Resolved%2C%20Blocked%2C%20Committed%2C%20Review%2C%20Test%2C%20%22Ready%20for%20Review%22%2C%20%22On%20Hold%22%2C%20%22For%20Review%22%2C%20%22Test%2FReview%22%2C%20Delivered%2C%20EPICS%2C%20%22Proposed%20Replan%22%2C%20%22Code%20Review%22%2C%20%22Design%20Activity%22%2C%20%22CA%20Completed%22%2C%20%22Scoping%20planning%22%2C%20%22To%20be%20Planned%22%2C%20%22Review%2FTest%22%2C%20%22In%20CA%22%2C%20%22Development%20In%20Progress%22%2C%20%22Development%20Done%22%2C%20%22Pre%20Pre%20Study%20Queue%22%2C%20%22Pre%20Pre%20Study%20Done%22%2C%20%22Pre%20Pre%20Study%20Halted%22%2C%20%22MR%20Cancelled%22%2C%20%22RV%20In%20Progress%22%2C%20%22RV%20Done%22%2C%20%22RV%20Blocked%22%2C%20%22RV%20Halted%22%2C%20%22Dev%20pre%20RV%20Done%22%2C%20%22Development%20Blocked%22%2C%20%22Development%20Halted%22%2C%20%22Release%20Blocked%22%2C%20%22Release%20Halted%22%2C%20%22Release%20In%20Progress%22%2C%20%22Release%20Done%22%2C%20%22Development%20Cancelled%22%2C%20%22Release%20Cancelled%22%2C%20%22Pre%20Pre%20Study%20Cancelled%22%2C%20%22Ready%20for%20RV%22%2C%20%22RV%20Cancelled%22%2C%20%22Review%5C%5CTest%22%2C%20%22Pre-study%20Queue%22%2C%20%22Pre-study%20In%20Progress%22%2C%20%22Pre-study%20Done%22%2C%20%22Pre-study%20Blocked%22%2C%20%22Pre-study%20Halted%22%2C%20%22Pre-study%20Cancelled%22%2C%20DevelopmentQueue%2C%20%22QS%20In%20Progress%22%2C%20%22QS%20Done%22%2C%20%22SA%20In%20Progress%22%2C%20%22SA%20Done%22%2C%20%22Acceptance%20In%20Progress%22%2C%20Candidate%2C%20%22Refinement%20In%20Progress%22%2C%20%22Refinement%20Halted%22%2C%20%22Refinement%20Done%22%2C%20%22CA%20Open%22%2C%20%22Pre-PreStudy%20Open%22%2C%20%22Pre-PreStudy%20In%20Progress%22%2C%20%22Pre-PreStudy%20On%20Hold%22%2C%20%22Pre-PreStudy%20Done%22%2C%20%22PreStudy%20Open%22%2C%20%22PreStudy%20In%20Progress%22%2C%20%22PreStudy%20On%20Hold%22%2C%20%22Pre%20Prestudy%20In%20Progress%22%2C%20%22Pre%20Prestudy%20Blocked%22%2C%20%22Release%20Queue%22)%20AND%20component%20%3D%20Wizzards&maxResults=500'

headers = {'Content-Type': 'application/json'}
getData=requests.get(str(jiraUrl)+str(jqlQuery) ,auth=HTTPBasicAuth('statsjenki','Apr#2024'),headers=headers,proxies=proxy)
jsonData=json.loads(getData.text)

print "Total Issues : " , jsonData['total']
total = jsonData['total']
emailReport.write(str(total))
emailReport.write(str(textEnd))
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
               #         print components
                if not data['fields']['labels']:
                        labels = "None"
                else:
                        lab = data['fields']['labels']
                        label = [str(l) for l in lab]
                        labels = ",".join(label) 
		#         print labels 
                if not data['fields']['fixVersions']:
                        fixVersion = "None"
                else:
                        fixV = data['fields']['fixVersions']
                        fixVer = [li[u'name'] for li in fixV]
                        fixVers = [str(l) for l in fixVer]
                        fixVersion = ",".join(fixVers)
                #print fixVersion

		if (ticketDays > 14):
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
                        emailReport.write(str(components))
			emailReport.write(str(tab6))
                        emailReport.write(str(labels))
			emailReport.write(str(tab7))
                        emailReport.write(str(creationDate))
                        emailReport.write(str(tab8))
                        emailReport.write(str(ticketDays))
                        emailReport.write(str(tab9))
                        emailReport.write(str(assignee))
                        emailReport.write(str(tab10))
                        emailReport.write(str(fixVersion))
                        emailReport.write(str(tabEnd1))

        except:
                print " Error in printing jira information"
                continue

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
               #         print components
                if not data['fields']['labels']:
                        labels = "None"
                else:
                        lab = data['fields']['labels']
                        label = [str(l) for l in lab]
                        labels = ",".join(label)
               #         print labels
                if not data['fields']['fixVersions']:
                        fixVersion = "None"
                else:
                        fixV = data['fields']['fixVersions']
                        fixVer = [li[u'name'] for li in fixV]
                        fixVers = [str(l) for l in fixVer]
                        fixVersion = ",".join(fixVers)
                #print fixVersion


		if (ticketDays > 7 and ticketDays <= 14 ):
                        emailReport.write(str(tab11))
                        emailReport.write(str(data['fields']['issuetype']['name']))
                        emailReport.write(str(tab12))
                        emailReport.write("<a href =" + str(linkUrl) + ">" + str(key) + "</a>")
                        #emailReport.write(str(data['key']))
                        emailReport.write(str(tab13))
                        emailReport.write(str(data['fields']['summary']))
                        emailReport.write(str(tab14))
                        emailReport.write(str(data['fields']['status']['name']))
                        emailReport.write(str(tab15))
                        emailReport.write(str(components))
                        emailReport.write(str(tab16))
                        emailReport.write(str(labels))
                        emailReport.write(str(tab17))
                        emailReport.write(str(creationDate))
                        emailReport.write(str(tab18))
                        emailReport.write(str(ticketDays))
                        emailReport.write(str(tab19))
                        emailReport.write(str(assignee))
                        emailReport.write(str(tab20))
                        emailReport.write(str(fixVersion))
                        emailReport.write(str(tabEnd2))

        except:
                print " Error in printing jira information"
                continue

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
               #         print components
                if not data['fields']['labels']:
                        labels = "None"
                else:
                        lab = data['fields']['labels']
                        label = [str(l) for l in lab]
                        labels = ",".join(label)
               #         print labels	
                if not data['fields']['fixVersions']:
                        fixVersion = "None"
                else:
                        fixV = data['fields']['fixVersions']
                        fixVer = [li[u'name'] for li in fixV]
                        fixVers = [str(l) for l in fixVer]
                        fixVersion = ",".join(fixVers)
                #print fixVersion
	
		if (ticketDays <= 7 ):
                        emailReport.write(str(tab21))
                        emailReport.write(str(data['fields']['issuetype']['name']))
                        emailReport.write(str(tab22))
                        #emailReport.write(str(data['key']))
                        emailReport.write("<a href =" + str(linkUrl) + ">" + str(key) + "</a>")
                        emailReport.write(str(tab23))
                        emailReport.write(str(data['fields']['summary']))
                        emailReport.write(str(tab24))
                        emailReport.write(str(data['fields']['status']['name']))
                        emailReport.write(str(tab25))
                        emailReport.write(str(components))
                        emailReport.write(str(tab26))
                        emailReport.write(str(labels))
                        emailReport.write(str(tab27))
                        emailReport.write(str(creationDate))
                        emailReport.write(str(tab28))
                        emailReport.write(str(ticketDays))
                        emailReport.write(str(tab29))
                        emailReport.write(str(assignee))
                        emailReport.write(str(tab30))
                        emailReport.write(str(fixVersion))
                        emailReport.write(str(tabEnd3))

        except:
                print " Error in printing jira information"
                continue

emailReport.write(str(content))

