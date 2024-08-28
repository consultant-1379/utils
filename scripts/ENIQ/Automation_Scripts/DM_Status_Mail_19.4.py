#!/proj/ciexadm200/tools/python-2.7.8/bin/python
# -*- coding: utf-8 -*-
'''
Created on Mar 20, 2019

@author: zsxxhem
'''

import pexpect
import os
from datetime import timedelta, datetime, date
from jenkins import Jenkins
import base64
import re
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict


class getBuildStatus:
    
    def __init__(self):
        self.Shipment = os.environ['Shipment']
        self.Release = os.environ['Release']
        self.previous_ship = os.environ['Previous_Shipment']
        
        self.Previous_Date = datetime.today() - timedelta(days=1)
        if datetime.today().strftime("%a") == "Mon":
            self.Previous_Date = datetime.today() - timedelta(days=3)
        self.alphaNum = {'1':"A.1", '2':"B", '3':"B.1", '4':"C", '5':"C.1", '6':"D"}
        self.jenkinPwd = base64.b64decode("TmFwbGVzITA1MTI=")
        self.jenkinUrl = "https://fem167-eiffel004.lmera.ericsson.se:8443/jenkins/"
        self.checkin = {}; self.catalog = {}
        self.date = self.rack_html_status = ""
        self.fdm_status = self.feature_status = self.onm_status = self.rack_ii_status = self.blade_ii_status = self.multiblade_ii_status = self.vApp_ii_status = ''
        self.blade_upgrade_status = self.vApp_upgrade_status = self.vApp_ii_name = self.vApp_upgrade_name = ''
        self.footer = "</table></body></html>\n"
        self.checkin_header = "<html><head><title>Delivery Details</title></head>\n<body><table bordercolor=\"#696969\" border=\"1\" cellspacing=\"0\" rules=\"all\" cellpadding=\"2\"><tr bgcolor=\"lightskyblue\"><th><b>Package Name</th><th><b>Delivered By</th></tr>\n"
        self.status_details = {"Success" : "Completed", "Failure" : "Failed", "Not Run" : "Not Run", "Ongoing" : "Ongoing", "Aborted": "Aborted"}
        self.loginPage = "https://atvphspp17.athtem.eei.ericsson.se/Users/login"
        self.catalogList = "https://atvphspp17.athtem.eei.ericsson.se/vappTemplates/index/catalog_name:ASSURE-ES-CIExecution/org_id:urn%3Avcloud%3Aorg%3A14bdd9f8-12cc-49ae-82a1-69c953ecb175" 
        self.payload = {'User[username]': 'statsjenki', 'User[password]': base64.b64decode("QXByaWxAMjAxOQ==")}
        
    def printHeading(self, buildName, status, syBar="-"):
        print syBar*100
        print "{} (LINUX) - {}".format(buildName, status).center(100)
        print syBar*100
        
    def searchDate(self, val):
        q = re.compile("[A-Z]\w{2}\s+\d+")
        op = q.search(val)
        
        if op != None:
            return op.group(0)
        else:
            return " "
    
    def checkJenkinsJob(self, jobName):
        page = Jenkins(self.jenkinUrl,  username="esjkadm100", password=self.jenkinPwd)
        buildStatus = page.get_build_info(jobName, page.get_job_info(jobName)['nextBuildNumber'] - 1 )
        if buildStatus['building']:
            return 'Ongoing'
        elif (self.Previous_Date.strftime("%b-%d") == date.fromtimestamp(int(str(buildStatus['timestamp'])[:-3])).strftime("%b-%d")) or (datetime.today().strftime("%b-%d") == date.fromtimestamp(int(str(buildStatus['timestamp'])[:-3])).strftime("%b-%d")):
            return buildStatus['result'].title()
        else:
            return "Not Run"
            
    def verifyDate(self, bType, CmdOP, build=True):
        try:
            if build:
                output = [line for line in CmdOP.split("\n") if line.startswith("drwx")]
            else:
                output = [line for line in CmdOP.split("\n") if line.startswith("-rw")]
                
            fdm_date = {self.searchDate(i).split(" ")[0] + "-" + self.searchDate(i).split(" ")[-1].zfill(2) for i in output}
            
            dateCheck = list(fdm_date)
            
            if self.Previous_Date.strftime("%b-%d") in dateCheck:
                if self.date == "":
                    self.date = self.searchDate(output[0])
                self.printHeading(bType, "PASS")
                return "Completed"
            else:
                echo = "FAIL -> Last Cached Date : " + str(dateCheck)
                self.printHeading(bType, echo)
                return "Failed"
        except Exception as error:
            print CmdOP
            print "EXCEPTION ERROR : " + str(error)
            
    def checkMWSBuildStatus(self):
        try:
            self.printHeading("FDM BUILD", "Checking Cached Content...!!")
            FDM_Build = "/JUMP/ENIQ_STATS/ENIQ_STATS/" + str(self.Shipment) + "/eniq_base_sw/"
        
            child = pexpect.spawn('ssh root@10.45.192.153')
            child.expect('#', timeout=20)
        
            cmd = "ls -lh " + str(FDM_Build)
            child.sendline(cmd)
            child.expect ('#', timeout=20)
        
            fdmStatus = self.checkJenkinsJob("ENIQ_BUILD_LINUX_ISO_S19.4")
            if fdmStatus == "Success":
                self.fdm_status = self.verifyDate("FDM BUILD", child.before)
            else:
                self.fdm_status = self.status_details[fdmStatus]
                
            self.printHeading("ONM BUILD", "Checking Cached Content...!!")
        
            Onm_Shipment = self.Shipment.split("_")[0]
            Onm_Media = self.Release.split("_S")[1].replace(".","_")
            ONM_Build = "/JUMP/OM_LINUX_MEDIA/OM_LINUX_0" + Onm_Media + "/" + Onm_Shipment + "/om_linux/"
        
            cmd = "ls -lh " + str(ONM_Build)
            child.sendline(cmd)
            child.expect ('#', timeout=20)
        
            infraStatus = self.checkJenkinsJob("ENIQ_BUILD_LINUX_ISO_I19.4")
            if infraStatus == "Success":
                self.onm_status = self.verifyDate("ONM BUILD", child.before)
            else:
                self.onm_status = self.status_details[infraStatus]
        
            self.printHeading("Feature BUILD", "Checking Cached Content...!!")
        
            Feature_Build = "/JUMP/ENIQ_STATS/ENIQ_STATS/Features_" + self.Shipment.split(".")[0] + self.alphaNum[self.Shipment.split(".")[1]] + "_" + self.Shipment + "/"
        
            cmd = "ls -lh " + str(Feature_Build)
            child.sendline(cmd)
            child.expect ('#', timeout=20)
        
            featureStatus = self.checkJenkinsJob("19A.1(19.1)FDM DELTA FEATURE BUILD(TP,KPI,PARSER)")
            if featureStatus == "Success":
                self.feature_status = self.verifyDate("Feature BUILD", child.before)
            else:
                self.feature_status = self.status_details[featureStatus]
                
            child.close()
        except pexpect.exceptions.TIMEOUT:
            print "Unable to Connect to MWS!!."
        except Exception as error:
            print "EXCEPTION ERROR : " + str(error)

    def getLatestCatalog(self):
        try:
            nmiFlag = infraFlag = cdbFlag = False
            cdbCatalog = nmiCatalog = infraCatalog = ''
            
            with requests.Session() as session:
                session.post(self.loginPage, data=self.payload)
                page = session.get(self.catalogList)
                soup = BeautifulSoup(page.text, 'html.parser')
                #print soup.prettify()
                for line in soup.find_all('a'):
                    line = str(line)
                    if "Linux_CDB" in line and cdbFlag == False:
                        cdbFlag = True
                        cdbCatalog = line
            
                    elif "Linux_Infra" in line and infraFlag == False:
                        infraFlag = True
                        infraCatalog = line
                        
                    elif "Linux_NMI" in line and nmiFlag == False:
                        nmiFlag = True
                        nmiCatalog = line
                        
                    if nmiFlag and infraFlag and cdbFlag:
                        break
                    
                self.catalog ["RHEL + INFRA"] = str(infraCatalog.split(">")[1].split("<")[0])
                self.catalog ["RHEL + INFRA + NMI"] = str(nmiCatalog.split(">")[1].split("<")[0])
                self.catalog ["Full ENIQ - "] = str(cdbCatalog.split(">")[1].split("<")[0])
                
                print "-O-"*30
                print "Linux_CDB : " + self.catalog ["Full ENIQ - "]
                print "Linux_Infra : " + self.catalog ["RHEL + INFRA"]
                print "Linux_NMI : " + self.catalog ["RHEL + INFRA + NMI"]
                print "-O-"*30
        except Exception as error:
            print "EXCEPTION ERROR : " + str(error)

    def checkServer_II(self, server, job, outline, isVapp = False):
        try:
            statusFlag = False
                        
            self.status = self.checkJenkinsJob(job)
            if self.status == "Success":
                if isVapp:
                    serverName = self.get_vAppName(job)
                    serverLog = 'eniqs'
                    ship = self.Shipment
                    
                    cmd = "ssh -p 2251 root@" + serverName
                else:
                    serverName = serverIp = serverLog = server
                    if serverName == "ieatrcx6575":
                        if self.Previous_Date.strftime("%a") == "Thu":
                            ship = self.previous_ship
                        else:
                            ship = self.Shipment
                    else:
                        ship = self.Shipment
                    cmd = "ssh root@" + serverIp
                    
                self.printHeading("Initial Install", serverName + "...!!", syBar=outline)
                child = pexpect.spawn('ssh eniqdmt@selid1t007')
                child.expect('~', timeout=20)
                
                child.sendline(cmd)
                child.expect ('assword:', timeout=20)
                child.sendline("shroot12")
                child.expect ('#', timeout=20)
                
                
                cmd = "cat /eniq/local_logs/installation/{}_install.log | grep \"ENIQ SW successfully installed\"".format(serverLog)
                child.sendline(cmd)
                child.expect ('#', timeout=20)
                
                if "ENIQ SW successfully installed" in child.before.split("\n")[-2] and "grep" not in child.before.split("\n")[-2]:
                    statusFlag = True
                
                cmd = "cat /eniq/local_logs/installation/{}_install.log | grep ERROR".format(serverLog)
                child.sendline(cmd)
                child.expect ('#', timeout=20)
                
                if "ERROR" in child.before.split("\n")[-2] and "grep" not in child.before.split("\n")[-2]:
                    statusFlag = False
                    self.status = "Failure"
                
                child.sendline("cat /eniq/admin/version/*")
                child.expect ('#', timeout=20)
                
                if statusFlag:
                    if ship in child.before:
                        echo = "{} - Successfully Installed ".format(serverName, ship)
                        print echo.center(100)
                    else:
                        self.status = "Failure"
                        echo = "{} - Failed to Install {}".format(serverName, ship)
                        print echo.center(100)
                        installShip = child.before.split("Shipment_")[-1].split(" ")[0]
                        echo = "{} - Installed Shipment {} - Expected to be installed {}".format(serverName, installShip, ship)
                        print echo.center(100)
                else:
                    self.status = "Failure"
                    echo = "{} - Failed to Install {}".format(serverName, ship)
                    print echo.center(100)
                self.printHeading("Initial Install", "{} - {}".format(serverName, self.status), syBar=outline)
                child.close()
            else:
                self.printHeading("Initial Install", "{} - {}".format(server, self.status), syBar=outline)
        except pexpect.exceptions.TIMEOUT:
            print "Unable to Connect to {}!!.".format(server)
            
    def checkServer_Upgrade(self, server, job, outline, isVapp = False):
        try:
            statusFlag = False
            logDate = self.Previous_Date.strftime("%Y-%b-%d")
            if isVapp: self.vAppName = self.get_vAppName(job)
            
            self.status = self.checkJenkinsJob(job)
            if self.status == "Success":
                if isVapp:
                    serverName = self.get_vAppName(job)
                    cmd = "ssh -p 2251 root@" + serverName
                    updateShip = "19.2.12"
                else:
                    serverName = server
                    cmd = "ssh root@" + serverIp
                    updateShip = self.previous_ship
                    
                self.printHeading("Upgrade from 19.2.12", serverName + "...!!", syBar=outline)
                
                child = pexpect.spawn('ssh eniqdmt@selid1t007')
                child.expect('~', timeout=20)
                
                child.sendline(cmd)
                child.expect ('assword:', timeout=20)
                child.sendline("shroot12")
                child.expect ('#', timeout=20)
                cmd = "cat /eniq/local_logs/upgrade/{}_upgrade_eniq_sw.log | grep \"Completed upgrade Procedure\"".format(logDate)
                child.sendline(cmd)
                child.expect ('#', timeout=20)
                
                if "Completed upgrade Procedure" in child.before.split("\n")[-2] and "grep" not in child.before.split("\n")[-2]:
                    statusFlag = True
                
                cmd = "cat /eniq/local_logs/upgrade/{}_upgrade_eniq_sw.log | grep ERROR".format(logDate)
                child.sendline(cmd)
                child.expect ('#', timeout=20)
                
                if "ERROR" in child.before.split("\n")[-2] and "grep" not in child.before.split("\n")[-2]:
                    statusFlag = False
                    self.status = "Failure"
                
                child.sendline("cat /eniq/admin/version/*")
                child.expect ('#', timeout=20)
                
                if statusFlag:
                    if self.Shipment in child.before and updateShip in child.before:
                        echo = "{} - Successfully Upgraded from {} to {}".format(serverName, updateShip, self.Shipment)
                        print echo.center(100)
                    else:
                        self.status = "Failure"
                        echo = "{} - Failed to Upgrade from {} to {}".format(serverName, updateShip, self.Shipment)
                        print echo.center(100)
                        ship = child.before.split("Shipment_")[-2].split(" ")[0]
                        echo = "{} - Upgraded Shipment {} - Expected to be upgraded to {}".format(serverName, ship, self.Shipment)
                        print echo.center(100)
                else:
                    self.status = "Failure"
                    echo = "{} - Failed to Upgrade from {} to {}".format(serverName, updateShip, self.Shipment)
                    print echo.center(100)
                self.printHeading("Upgrade from 19.2.12", "{} - {}".format(serverName, self.status), syBar=outline)
                child.close()
            else:
                self.printHeading("Upgrade from 19.2.12", "{} - {}".format(server, self.status), syBar=outline)
        except pexpect.exceptions.TIMEOUT:
            print "Unable to Connect to {}!!.".format(server)
            
    def get_vAppName(self, job):
        try:
            page = Jenkins(self.jenkinUrl,  username="esjkadm100", password=self.jenkinPwd)
            buildStatus = page.get_build_info(job, page.get_job_info(job)['nextBuildNumber'] - 1 )
            node = page.get_node_config(buildStatus["builtOn"])
            
            match = re.compile("hostname>(atvts\d{4})<")
            name = match.search(node)
            
            return name.group(1)
        except Exception as error:
            print "EXCEPTION ERROR : " + str(error)
    
    def vApp_II(self, outline):
        try:
            infraStatus = self.checkJenkinsJob("ES_CDB_Vapp_II_Infra")
            nmiStatus = self.checkJenkinsJob("ES_CDB_Vapp_NMI")
            
            self.vAppName = self.get_vAppName("ES_CDB_Vapp_II_Infra")
            if infraStatus == "Success":
                if nmiStatus == "Success":
                    self.checkServer_II("vApp", "ES_CDB_Vapp_II", outline, isVapp=True)
                    print "vApp Name - {}".format(self.vAppName).center(100)
                else:
                    self.status = nmiStatus
            else:
                self.status = infraStatus
        except Exception as error:
            print "EXCEPTION ERROR : " + str(error)
            
    def multiBlade_II(self, outline):
        try:
            self.checkServer_II("ieatrcxb6506", "ES_LINUX_M_BLADE_II", outline)
            if self.status == "Success":
                self.checkServer_II("ieatrcxb6507", "ES_LINUX_M_BLADE_ENGINE_II", outline)
                if self.status == "Success":
                    self.checkServer_II("ieatrcxb6508", "ES_LINUX_M_BLADE_READER1_II", outline)
                    if self.status == "Success":
                        self.checkServer_II("ieatrcxb6509", "ES_LINUX_M_BLADE_READER2_II", outline)
        except Exception as error:
            print "EXCEPTION ERROR : " + str(error)
    
    def getDeliveryInfo(self, outline):
        try:
            self.printHeading("Packages delivered for", self.Shipment +" on " + self.Previous_Date.strftime("%d %b %Y"), syBar=outline)
        
            child = pexpect.spawn('ssh eniqdmt@selid1t007')
            child.expect('>', timeout=20)
            
            cmd = "ct setview eniq_bld_ENIQ_S19.4_{}".format(self.Shipment)
            child.sendline(cmd)
            child.expect ('>', timeout=20)
        
            child.sendline("cd /vobs/dm_eniq/AT_delivery/container/")
            child.expect ('>', timeout=20)
        
            cmd = "ls -l | grep \"" + self.date + "\""
            child.sendline(cmd)
            child.expect ('>', timeout=20)
        
            for line in [i.split(" ")[-1].strip() for i in child.before.split("\n") if i.startswith("-r")]:
                self.checkin[line.strip("*")] = ""
            
            for key in self.checkin.keys():
                ctCmd = "ct desc " + key
                child.sendline(ctCmd)
                child.expect ('>', timeout=20)
                
                build_ship = [i.strip().upper() for i in child.before.split("\n") if "BaseLine" in i]
                #print build_ship
                if self.Shipment.upper() in build_ship[0]:
                    name = [i.split("by")[-1].split("(")[0].strip() for i in child.before.split("\n") if "created" in i]
                    self.checkin[key] = name[0].title()
            child.close()
        
            for k,v in self.checkin.items():
                if v != "":
                    echo = " {} - {} ".format(k,v)
                    print "|" + echo.center(98) + "|"
            print "-"*100
        except pexpect.exceptions.TIMEOUT:
            print "Unable to Connect to MWS...!!"
            
    def generateDeliverHTMLPage(self):
        row = ''
        for key, val in self.checkin.items():
            if val != "":
                row+="<tr><td><b>"+ key +"</td><td><b>" + val + "</td></tr>\n";
        
        html = self.checkin_header + row + self.footer
        with open ("/var/tmp/deliver_status_19_4.html", 'w') as htmFile:htmFile.write(html)
        
    def generateCatalogHTMLPage(self):
        row = "<html><head><title>Catalog Details</title></head>\n<body><table bordercolor=\"#696969\" border=\"1\" cellspacing=\"0\" rules=\"all\" cellpadding=\"2\"><tr bgcolor=\"plum\"><th><b>Category</th><th><b>Catalog</th><th><b>Template</th><th><b>URL</th></tr>\n"
        for key, val in self.catalog.items():
            if key == "Full ENIQ - ":
                row += "<tr><th><font color=\"royalblue\"><b>" + key + str(val.split("_")[2]) + "</th><th><font color=\"royalblue\"><b>ASSURE-ES-CIExecution</th><th><font color=\"royalblue\"><b>" + val + "</th><th rowspan=\"3\"><font color=\"royalblue\"><b>atvphspp17.athtem.eei.ericsson.se</th></tr>"
            else:
                row += "<tr><th><font color=\"royalblue\"><b>" + key + "</th><th><font color=\"royalblue\"><b>ASSURE-ES-CIExecution</th><th><font color=\"royalblue\"><b>" + val + "</th></tr>"
        html = row + self.footer
        with open ("/var/tmp/catalog_details_19_4.html", 'w') as htmFile:htmFile.write(html)    
        
    def generateBuildHTMLPage(self):
        build_header = "<html><head><title>Build Status Details</title></head>\n \
              <body><table bordercolor=\"#696969\" border=\"1\" rules=\"all\" cellspacing=\"0\" cellpadding=\"2\"> \
            <tr bgcolor=\"wheat\"> <td width=\"64\"><b>ENIQ Stats</b></td><td><b>{}</b></td><td><b>SERVER NAME</b></td><td><b>STATUS</b></td><td><b>RTStatus</b></td><td width=\"94\"><b>RT Log Verification (Design)</b></td><td><b>JIRA</b></td><td width=\"94\"><b>Assigned to / Comments</b></td></tr>".format(self.Shipment)
            
        build_tail = "</table></body></html>"
        
        build_body = "<tr> <td colspan=\"2\"> <b><center>FDM Build - Linux</center></b> </td> <td> </td> <td> <b>{1}</b> </td> <td> </td> <td> </td> <td> </td> <td> </td> </tr> \
            <tr> <td colspan=\"2\"> <b><center>Infra Build - Linux</center></b> </td> <td> </td> <td> <b>{2}</b> </td> <td> </td> <td> </td> <td> </td> <td> </td> </tr> \
            <tr> <td colspan=\"2\"> <b><center>FDM Feature Build</center></b> </td> <td> </td> <td> <b>{3}</b> </td> <td> </td> <td> </td> <td> </td> <td> </td> \
            </tr>".format(self.Shipment, self.fdm_status, self.onm_status, self.feature_status)#, self.vApp_ii_name, self.vApp_ii_status, self.blade_ii_status, self.multiblade_ii_status, self.rack_ii_status, self.vApp_upgrade_name, self.vApp_upgrade_status, self.blade_upgrade_status, self.previous_ship, self.rack_html_status)

        build_body = build_body.replace("<b>Completed</b>", "<b><font color=\"darkgreen\">Completed</b>")
        build_body = build_body.replace("<b>Ongoing</b>", "<b><font color=\"blue\">Ongoing</b>")
        build_body = build_body.replace("<b>Failed</b>", "<b><font color=\"red\">Failed</b>")
        build_body = build_body.replace("<b>Not Run</b>", "<b><font color=\"orange\">Not Run</b>")
        build_body = build_body.replace("<b>Aborted</b>", "<b><font color=\"maroon\">Aborted</b>")
        html = build_header + build_body + build_tail
        with open ("/var/tmp/build_status_result_19_4.html", 'w') as htmFile:htmFile.write(html)

if __name__ == "__main__":
    buildStatus = getBuildStatus()
    buildStatus.checkMWSBuildStatus()
    
    #===========================================================================
    # if buildStatus.Previous_Date.strftime("%a") == "Thu":
    #     print "!!..RACK Initial Install on Previous Shipment..!!".center(100)
    #     rackName = buildStatus.checkServer_II("ieatrcx6575", "ES_LINUX_RACK_II", "*")
    #     buildStatus.rack_ii_status = buildStatus.status_details[buildStatus.status]
    #     buildStatus.rack_html_status = "Initial Install <font color=\"blue\">[{}]".format(self.previous_ship)
    # elif buildStatus.Previous_Date.strftime("%a") == "Fri":
    #     print "!!..RACK Upgrade..!!".center(100)
    #     rackName = buildStatus.checkServer_II("ieatrcx6575", "ES_LINUX_RACK_II", "*")
    #     buildStatus.rack_ii_status = buildStatus.status_details[buildStatus.status]
    #     buildStatus.rack_html_status = "Upgrade <font color=\"blue\">[{} -> {}]".format(self.previous_ship, self.Shipment)
    # else:
    #     print "!!..RACK Initial Install..!!".center(100)
    #     rackName = buildStatus.checkServer_II("ieatrcx6575", "ES_LINUX_RACK_II", "*")
    #     buildStatus.rack_ii_status = buildStatus.status_details[buildStatus.status]
    #     buildStatus.rack_html_status = "Initial Install <font color=\"blue\">[{}]".format(self.Shipment)
    # 
    # print "!!..BLADE Initial Install..!!".center(100)
    # bladeName = buildStatus.checkServer_II("ieatrcxb6105", "ES_LINUX_BLADE_II_ieatrcxb6105", "=")
    # buildStatus.blade_ii_status = buildStatus.status_details[buildStatus.status]
    # 
    # print "!!..vApp Initial Install..!!".center(100)
    # buildStatus.vApp_II("-")
    # buildStatus.vApp_ii_status = buildStatus.status_details[buildStatus.status]
    # buildStatus.vApp_ii_name = buildStatus.vAppName
    # 
    # print "!!..MULTIBLADE Initial Install..!!".center(100)
    # buildStatus.multiBlade_II("^")
    # buildStatus.multiblade_ii_status = buildStatus.status_details[buildStatus.status]
    # 
    # print "!!..vApp Upgrade..!!".center(100)
    # buildStatus.checkServer_Upgrade("eniqs", "Linux_upgrade", "~", isVapp = True)
    # buildStatus.vApp_upgrade_status = buildStatus.status_details[buildStatus.status]
    # buildStatus.vApp_upgrade_name = buildStatus.vAppName
    # 
    # print "!!..Physical Server Upgrade..!!".center(100)
    # buildStatus.checkServer_Upgrade("ieatrcxb6104", "CDB_Linux_RHEL_SB_UG","#")
    # buildStatus.blade_upgrade_status = buildStatus.status_details[buildStatus.status]
    #===========================================================================
    
    buildStatus.getDeliveryInfo("+")
    #buildStatus.getLatestCatalog()
    
    buildStatus.generateBuildHTMLPage()
    #buildStatus.generateCatalogHTMLPage()
    buildStatus.generateDeliverHTMLPage()


