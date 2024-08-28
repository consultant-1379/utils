#************************************************************************
#            Author: Priyanka Samikannu                                 *
#            Description: Logic script to get JIRA count and details    *
#                         which is on CI JIRA Board                     *
#                                                                       *
#************************************************************************

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
config = ConfigParser.ConfigParser()
config.read('scripts/etc/config_jira_Eniq.cfg')

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
tabEnd1 = config.get('email', 'tabEnd1')

tab11 = config.get('email', 'tab11')
tab12 = config.get('email', 'tab12')
tab13 = config.get('email', 'tab13')
tab14 = config.get('email', 'tab14')
tab15 = config.get('email', 'tab15')
tab16 = config.get('email', 'tab16')
tab17 = config.get('email', 'tab17')
tabEnd2 = config.get('email', 'tabEnd2')

tab21 = config.get('email', 'tab21')
tab22 = config.get('email', 'tab22')
tab23 = config.get('email', 'tab23')
tab24 = config.get('email', 'tab24')
tab25 = config.get('email', 'tab25')
tab26 = config.get('email', 'tab26')
tab27 = config.get('email', 'tab27')
tabEnd3 = config.get('email', 'tabEnd3')
content = config.get('email', 'content')

#start writing html
emailHeader = open("scripts/etc/mailHeader_jira_eniq.txt", 'r')
emailReport = open("scripts/etc/mailReport_jira.html", 'w')
emailReport.write(str(emailHeader.read()))

#script start to manipulate the jira input outputs
proxy = {
    "http": "",
   "https": "",
    }
jiraUrl="https://jira-oss.seli.wh.rnd.internal.ericsson.com/rest/api/2/search?"

jqlQuery='jql=project%20%3D%20CIS%20AND%20component%20%3D%20%22CI%20Infra%20%2F%20CI%20Fwk%22%20AND%20%22Your%20PDG%2FArea%22%20%3D%20%22ENIQ%20Stats%22%20AND%20%22CI%20Support%22%20%3D%201%20AND%20%22CI%20Sub-Area%22%20%3D%20Infra%20AND%20status%20not%20in%20(Closed%2C%20Resolved%2C%20%22On%20Hold%22)'
#jqlQuery='jql=project%20%3D%20CIS%20AND%20component%20%3D%20%22CI%20Infra%20%2F%20CI%20Fwk%22%20AND%20%22Your%20PDG%2FArea%22%20%3D%20%22ENIQ%20Stats%22%20AND%20%22CI%20Support%22%20%3D%201%20AND%20%22CI%20Sub-Area%22%20%3D%20Infra%20AND%20status%20in%20(Open%2C%20%22In%20Progress%22%2C%20Reopened%2C%20Blocked%2C%20Review%2C%20Parked%2C%20%22Review%2FTesting%22%2C%20%22Ready%20to%20take%22%2C%20%22Waiting%20for%22)'
headers = {'Content-Type': 'application/json'}
getData=requests.get(str(jiraUrl)+str(jqlQuery) ,auth=HTTPBasicAuth('statsjenki','2020#Oct'),headers=headers,proxies=proxy)
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
                linkUrl = "http://jira-nam.lmera.ericsson.se/browse/" + key
                if (ticketDays > 45):
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
                        emailReport.write(str(creationDate))
                        emailReport.write(str(tab6))
                        emailReport.write(str(ticketDays))
                        emailReport.write(str(tab7))
                        emailReport.write(str(assignee))
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
                linkUrl = "http://jira-nam.lmera.ericsson.se/browse/" + key
                if (ticketDays > 20 and ticketDays <= 45 ):
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
                        emailReport.write(str(creationDate))
                        emailReport.write(str(tab16))
                        emailReport.write(str(ticketDays))
                        emailReport.write(str(tab17))
                        emailReport.write(str(assignee))
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
                linkUrl = "http://jira-nam.lmera.ericsson.se/browse/" + key
                if (ticketDays <= 20 ):
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
                        emailReport.write(str(creationDate))
                        emailReport.write(str(tab26))
                        emailReport.write(str(ticketDays))
                        emailReport.write(str(tab27))
                        emailReport.write(str(assignee))
                        emailReport.write(str(tabEnd3))

        except:
                print " Error in printing jira information"
                continue

emailReport.write(str(content))

