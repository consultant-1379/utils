#************************************************************************
#            Author: ENIQ-CI-INFRA                                                    *
#            Description: Logic script to define the environment        *
#                         variables and testware                        *
#                                                                       *
#************************************************************************

import socket
import os
import urllib2
import urllib
import sys
import ConfigParser
import logging
import ntpath
import utils
if sys.platform == "win32":
    path = ".."
else:
    path = "scripts"
sys.path.append(path + '/lib')
from xmlMod.etree import ElementTree as xml
from xmlMod.etree import ElementPath as xmlPath
xml.register_namespace('','http://maven.apache.org/POM/4.0.0')
myname = ntpath.basename(__file__).split('.')[0]
module_logger = logging.getLogger(myname)
config = ConfigParser.ConfigParser()
config.read(path + '/etc/config.cfg')
#defaultMail = config.get('Jenkins','defaultRecipients')
from utils import generateErrorMsg


def genEnvVar():
    try:
        global module_logger
        calledFrom = ntpath.basename(module_logger.findCaller()[0]).split('.')[0]
        if ntpath.basename(module_logger.findCaller()[0]).split('.')[0] != myname:
            module_logger = logging.getLogger(ntpath.basename(module_logger.findCaller()[0]).split('.')[0] + "." + myname)
        module_logger.info("Execution of Logic script started")
        machine = socket.gethostbyaddr(socket.gethostname())
        module_logger.info("Slave Name = " + str(machine[0]))
        module_logger.info("Slave IP = " + str(machine[2][0]))
        envList = os.environ
        '''
        If V2 (CDB2) job, scheduler file should be ossrc_scheduler1 and for others ossrc_scheduler by default. This can be
                overridden by schedulerFile variable
        '''
        jobName = str(envList["JOB_NAME"])
        #drop = str(envList['drop'])
        buildTag = str(envList['BUILD_TAG'])
        manualVer = "1.0.28"
        testwarePLM = {}
        # if drop is not defined, set it to None
        if "drop" not in envList:
            drop = "16.0.7" #Given some default val
        else:
            drop = str(envList['drop'])
        if "Cloud_CDB_Auto_Deployment_2" in envList["JOB_NAME"]:
            cdb_schedule = "eniq_schedule.xml"
        else:
            cdb_schedule = "eniq_schedule.xml"
        # if scheduler file is defined, assign its value
        if "schedulerFile" in envList:
            cdb_schedule = envList['schedulerFile']
        # if deployPackage is not defined, set it to None
        if "deployPackage" not in envList:
            deployPackage = None
        else:
            deployPackage = str(envList['deployPackage'])
        # if scheduleVersion is not defined, set it to RELEASE. This can be used to run snapshot version
        if "scheduleVersion" not in envList:
            scheduleVersion = "RELEASE"
        else:
            scheduleVersion = str(envList['scheduleVersion'])
        # if phase is not defined, set it to KGB
        if "phase" not in envList:
            phase = "KGB"
        else:
            phase = str(envList['phase'])
        # Setting product to OSS-RC as default
        if "product" not in envList:
            product = "ENIQ-STATS"
        else:
            product = str(envList['product'])
        # Exiting if ISO No if not defined.
        if "isoNo" not in envList:
            isoNo = deployPackage.split("::")[0].upper()
            #===================================================================
            # module_logger.debug("ISONo variable is not set. Exiting generating environment variable")
            # module_logger.info("Something went wrong in generating environment variables.Please contact CI Dev Infra team")
            # #generateErrorMsg()
            # sys.exit(2)
            #===================================================================
        else:
            isoNo = str(envList['isoNo'])
        #hardcoded for CDB3 job to do install only
        if "Cloud_CDB_Auto_Deployment_3" in envList["JOB_NAME"]:
            cdb_schedule = "cdb_install_only.xml"
        #if "EMAIL" in envList:
        #    module_logger.info("Updating EMAIl ID for default recipients")
        #    newEmail = envList['EMAIL'] + ", " + str(defaultMail)
        #    module_logger.info("Updated Email List : " + newEmail)
        module_logger.info("schedulerVersion = " + str(scheduleVersion))
        module_logger.info("Scheduler File = " + str(cdb_schedule))
        module_logger.info("Drop =" + str(drop))
        if 'EMAIL' in envList:
            module_logger.info("Email = " + envList['EMAIL'])
        #Temp File to store the environment variables
        tempFile = open('/tmp/' + str(buildTag),'wb' )
        if "15.2." in str(drop):
		AOM_NUMBER = "AOM 901 122"
	elif "16.2." in str(drop):
		AOM_NUMBER = "AOM 901 133"
	elif "17.2." in str(drop):
		AOM_NUMBER = "AOM 901 155"
	else:
		aomNumber = urllib2.urlopen("https://cifwk-oss.lmera.ericsson.se/getAOMRstate/?product=" + str(product) + "&drop=" + str(drop)).read()
        	AOM_NUMBER = aomNumber.split(" ")[0]
        tempFile.write("AOM_NUMBER=" + str(AOM_NUMBER)+"\n")
        if "EU_LEVEL" in envList:
            tempFile.write("EU_LEVEL=" + str(envList['EU_LEVEL'])+"\n")
        vAppName = str(machine[0])
        tempFile.write("vAppName="+str(vAppName)+"\n")
        if os.path.isfile("pom.xml"):
          os.remove("pom.xml")
        if scheduleVersion == "RELEASE":
            module_logger.info("Retrieving maven dependency com.ericsson.eniq.stats.ci:eniq_taf_scheduler:RELEASE")
            tmpData = urllib.urlretrieve("https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/eniq/stats/ci/eniq_taf_scheduler/maven-metadata.xml","tmpPom.xml")
            document = xml.parse("tmpPom.xml")
            tafVer = str([i.text for i in document.findall('versioning/release')][0])
        else:
            tafVer = str(scheduleVersion)
        module_logger.info("TAF Scheduler version = " + str(tafVer))
        module_logger.info("Retrieving maven dependency com.ericsson.cifwk.taf:taf-run-maven-plugin:RELEASE")
        tmpData = urllib.urlretrieve("https://arm104-eiffel004.lmera.ericsson.se:8443/nexus/content/repositories/releases/com/ericsson/cifwk/taf/taf-run-maven-plugin/maven-metadata.xml","tmpPom.xml")
        document = xml.parse("tmpPom.xml")
        runVer = str([i.text for i in document.findall('versioning/release')][0])
        module_logger.info("TAF taf-run-maven-plugin version = " + str(runVer))
        module_logger.info("Manual Version = " + str(manualVer))
        drops = drop.split('::')
        try:
            isoVer = drops[1]
        except IndexError:
            isoVer = urllib2.urlopen("https://cifwk-oss.lmera.ericsson.se/getlatestisover/?drop=" + str(drops[0]) + "&product=" + str(product)).read()
        module_logger.info("ISO Version = " + str(isoVer))
        tempFile.write("isoVer="+str(isoVer)+"\n")
        if "KGB" in phase:
            module_logger.info("deployPackage = " + str(deployPackage))
            #Configuration for multiple KGB
            packageList = deployPackage.split('||')
            gavs = ""
            for packageTemp in packageList:
                package = packageTemp.split('::')[0]
                packageVersion = packageTemp.split('::')[1]
                tempData = urllib2.urlopen('https://cifwk-oss.lmera.ericsson.se/dmt/getLatestPackageObj/?package=' + str(package) + '&version=' + str(packageVersion))
                gavInfo = tempData.read()
                ver = gavInfo.split('::')[0]
                groupId = gavInfo.split('::')[1]
                module_logger.info("Package :" + str(package) +  ", Group ID :" + str(groupId) + ", Version : " + str(ver))
                gavs = gavs + "#" + str(package) + "::" + str(gavInfo)
            #Writing the variables to temp file
            tempFile.write("gavs=" + str(gavs)+"\n")
            module_logger.info("GAVs = " + str(gavs))
            module_logger.info("Retrieving testware for package list : ${packageList}")
            testwareTmp = urllib2.urlopen("https://cifwk-oss.lmera.ericsson.se/testware/getmapping/?packagelist=" + str(" ".join(packageList)))
            testware = str(testwareTmp.read())
            pomUrl = "https://cifwk-oss.lmera.ericsson.se/testware/createpom/?packagelist=" + str(" ".join(packageList)) + "&pomversion=2.0.2&scheduleversion=" + str(tafVer) + "&manualversion=" + str(manualVer) + "&tafrunversion=" + str(runVer) +"&schedulegroup=com.ericsson.eniq.stats.ci&scheduleartifact=eniq_taf_scheduler&schedulename=" + str(cdb_schedule)
        else:
            testwareTmp = urllib2.urlopen("https://cifwk-oss.lmera.ericsson.se/testware/getmapping/?product=" + str(product) + "&isoartifact=" + str(isoNo) + "&isoversion=" + str(isoVer))
            testware = str(testwareTmp.read())
            pomUrl="https://cifwk-oss.lmera.ericsson.se/testware/createpom/?isoartifact=" + str(isoNo) + "&isoversion=" + str(isoVer) + "&pomversion=2.0.2&scheduleversion=" + str(tafVer) + "&manualversion=" + str(manualVer) + "&tafrunversion=" + str(runVer) + "&schedulegroup=com.ericsson.eniq.stats.ci&scheduleartifact=eniq_taf_scheduler&schedulename=" + str(cdb_schedule)
        module_logger.info("Testware = " + testware)
        tempFile.write("testware="+testware+"\n")
        if "PLM_GA_URL" in envList:
            pomUrl = envList['PLM_GA_URL']
            module_logger.info("POM URL = " + str(pomUrl))
            tmpPom = urllib2.urlopen(pomUrl)
            f = open("testPom.xml","w")
            f.write(tmpPom.read())
            f.close()
            pomFile = xml.parse("testPom.xml")
            root = pomFile.getroot()
            try:
                PLM_Testware = envList['PLM_Testware']
                module_logger.info("Testware [Group ID:Version] to be updated = " + PLM_Testware)
                testwarePLM = {}
                testList = PLM_Testware.split('||')
                for testTmp in testList:
                    testCase = testTmp.split('::')[0]
                    testCaseVer = testTmp.split('::')[1]
                    testwarePLM[testCase] = testCaseVer
                    for scheduler in root.findall('*//{http://maven.apache.org/POM/4.0.0}artifactItems'):
                        for artifact in scheduler.findall('./{http://maven.apache.org/POM/4.0.0}artifactItem'):
                            if str(artifact.find('{http://maven.apache.org/POM/4.0.0}groupId').text) == testCase:
                                artifact.find('{http://maven.apache.org/POM/4.0.0}version').text = testwarePLM[testCase]
            except:
                module_logger.info("No testware to be changed.")

            for scheduler in root.findall('*//{http://maven.apache.org/POM/4.0.0}schedule'):
                scheduler.find('./{http://maven.apache.org/POM/4.0.0}schedule_name').text = str(cdb_schedule)
                for artifact in scheduler.findall('./{http://maven.apache.org/POM/4.0.0}artifactItem'):
                    artifact.find('{http://maven.apache.org/POM/4.0.0}version').text = str(scheduleVersion)
            pomFile.write('pom.xml')
        else:
            module_logger.info("POM URL = " + str(pomUrl))
            tmpPom = urllib2.urlopen(pomUrl)
            f = open("pom.xml","w")
            f.write(tmpPom.read())
            f.close()

        f = open("pom.xml","r")
        module_logger.info(f.read())
        f.close()
        module_logger.info("Cleaning temporary files:")
        if os.path.isfile("tmpPom.xml"):
            os.remove("tmpPom.xml")
        if os.path.isfile("testPom.xml"):
            os.remove("testPom.xml")
        module_logger.info("Execution of Logic script completed.")
    except Exception as e:
        print e
        message = utils.PrintException()
        module_logger.debug("Error in generating envionrment variables: " + message + str(e))
        module_logger.info("hing went wrong in generating environment variables.Please contact CI Dev Infra team")
        #generateErrorMsg()
        sys.exit(2)

def main():
    module_logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('ci_dev_infra.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    module_logger.addHandler(ch)
    module_logger.addHandler(fh)
    genEnvVar()
if __name__ == '__main__':
    main()









