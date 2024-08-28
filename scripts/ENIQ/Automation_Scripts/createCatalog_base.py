# ************************************************************************
# Author: Priyanka Samikannu                                             *
# Description: This script will                                          *
#                   * Stop the vApp                                      *
#                   * Add to catalog					                 *
# ************************************************************************

import urllib
from xml.etree import ElementTree
import optparse
from datetime import datetime, timedelta
import sys
import os
from re import search
import time
import logging

username = 'statsjenki'
password = 'Oct@2019'
cloudArea = ""
vmStatus = ""
sppPortal = ""
#Improvement in catalog creation in PODF-PLM 
catalogArea =str(os.getenv('catalogArea'))
syncArea1 = {'Cluster 1': "urn%3Avcloud%3Aorgvdc%3A7d1493f4-7655-4546-b716-1fb8cb53bf43",
             'Cluster 2': "urn%3Avcloud%3Aorgvdc%3A92edd3f6-f0e0-42ad-94fc-48b0e74d1e12",
             'Cluster 3': "urn%3Avcloud%3Aorgvdc%3A3b443720-5835-43e9-9332-f90faf04c6fb",
             'Cluster 4': "urn%3Avcloud%3Aorgvdc%3Aba4102fd-91d5-4ca4-95be-45e33cc59741",
             'Cluster 5': "urn%3Avcloud%3Aorgvdc%3A63ba9a73-0080-4c3a-b9d9-043bc4dcaa7a",
             'Cluster 6': "urn%3Avcloud%3Aorgvdc%3Abeacbb60-f14d-4b6a-8e00-5b4383a11823"}

syncArea2 = {'Cluster 2': "urn%3Avcloud%3Aorgvdc%3A0d005f3c-670c-491f-bdcf-e953c62040b2",
             'Cluster 3': "urn%3Avcloud%3Aorgvdc%3A901a2b1c-724e-4161-9a71-1c35a73a620c",
             'Cluster 4': "urn%3Avcloud%3Aorgvdc%3Ad0579c85-4c42-4f8f-9eaa-87027b5393de",
             'Cluster 5': "urn%3Avcloud%3Aorgvdc%3A303758c5-40de-4028-b74d-d0fa6b6ba5a8"}

syncArea3 = {'Cluster 2': "urn%3Avcloud%3Aorgvdc%3A73015ce9-899e-4f12-90a5-d3dfe021f709"}

syncArea4 = {'Cluster 3': "urn%3Avcloud%3Aorgvdc%3A846d6675-ae96-45cd-9dc0-98a623bc1348",
             'Cluster 4': "urn%3Avcloud%3Aorgvdc%3A66643bd6-a817-488a-87b5-7ed3ad253a3a"}

syncStatus1 = {'Cluster 1': "UNRESOLVED",
               'Cluster 2': "UNRESOLVED",
               'Cluster 3': "UNRESOLVED",
               'Cluster 4': "UNRESOLVED",
               'Cluster 5': "UNRESOLVED",
               'Cluster 6': "UNRESOLVED"}

syncStatus2 = {'Cluster 2': "UNRESOLVED",
               'Cluster 3': "UNRESOLVED",
               'Cluster 4': "UNRESOLVED",
               'Cluster 5': "UNRESOLVED"}

syncStatus3 = {'Cluster 2': "UNRESOLVED"}

syncStatus4 = {'Cluster 3': "UNRESOLVED",
               'Cluster 4': "UNRESOLVED"}
syncTime = {}

logFile = "postCdbTask.log"
logging.basicConfig(filename=logFile, level=logging.INFO, format="%(message)s")
global logger
logger = logging.getLogger(logFile)

cloudDetails = {'ASSURE-ES-CIExecution': {'cloudArea': 'urn%3Avcloud%3Aorgvdc%3Ad77fb2ae-c3c0-418a-b7d3-71665c1f194b','sppPortal': 'atvphspp17'}, }
catalogDetails = {'ASSURE-ES-CIExecution': {'cloudArea':'urn%3Avcloud%3Aorg%3A14bdd9f8-12cc-49ae-82a1-69c953ecb175'}, }

def postCDB(datacenter, slave, addCatalog, catalogName):
    emailReport = open("emailReport.html", 'w')
    if datacenter == "PODH":
        datacenter = "ASSURE-ES-CIExecution"
    if datacenter not in cloudDetails:
        print "Invalid Data Center used " + str(datacenter)
        sys.exit(2)
    global sppPortal, cloudArea
    sppPortal = cloudDetails[datacenter]['sppPortal']
    cloudArea = datacenter
    cloudUrl = 'https://' + str(username) + ':' + str(password) + '@' + str(
        sppPortal) + '.athtem.eei.ericsson.se/Vapps/index_api/orgvdc_id:'
    # retrieving the vApps in the cloud area
    print "Retrieving Vapps List"
    print cloudArea
    urllib.urlretrieve(str(cloudUrl) + cloudDetails[cloudArea]['cloudArea'] + '/.xml', "vappList.xml")
    document = ElementTree.parse("vappList.xml")
    for vApps in document.findall('vapps'):
        if vApps.find('name').text == slave:
            vappId = vApps.find('vapp_id').text
    os.remove("vappList.xml")
    if not document.findall('vapps'):
        print "Slave " + str(slave) + " not exists in " + str(datacenter) + " Cloud"
        sys.exit(2)
    # retrieving the vms for the specified vApp
    print "Retrieving Vms List"

    #for changing memory of netsim
    cloudUrl = 'https://' + str(username) + ':' + str(password) + '@' + str(sppPortal) + '.athtem.eei.ericsson.se/Vms/vapp_index_api/vapp_id:' + str(vappId) + '/orgvdc_id:' + \cloudDetails[cloudArea]['cloudArea'] + '/.xml'
    urllib.urlretrieve(str(cloudUrl), "vmList.xml")
    document = ElementTree.parse("vmList.xml")
    for vms in document.findall('vms'):
        if vms.find('name').text == 'master_netsim':
            print vms.find('name').text
            status = vms.find('status').text
            print status
            vmId = vms.find('vm_id').text
            if (str(status) == 'POWERED_ON'):
                print 'The vApp must be in the POWERED_OFF state to change cpu or memory on one of its VMs'
                vmStatus = "ON"
            elif (str(status) == 'POWERED_OFF'):
                vmStatus = "OFF"

    os.remove("vmList.xml")
    cloudUrl = 'https://' + str(sppPortal) + '.athtem.eei.ericsson.se/Vms/set_memory_mb/vm_id:' + str(vmId) + '/vapp_id:' + str(vappId) + '/orgvdc_id:' + cloudDetails[cloudArea]['cloudArea'] + '/memory_mb:' + str(memory1)
        vAppUrl = 'curl -s -u ' + str(username) + ':' + str(password) + ' --insecure --cookie-jar ./somefile https://' + str(sppPortal) + '.athtem.eei.ericsson.se/Vapps/stop_vapp_api/vapp_id:' + str(vappId) + '/.xml'
        # Setting the memory size
        if (str(vmStatus) == "ON"):
            print "Powering off the vApp. This will take sometime. Please dont kill the script"
            stopOutput = os.popen(vAppUrl).read()  # Stop vApp and store cookie
        else:
            print "vApp is already powered off"
            stopOutput = os.popen(vAppUrl).read()  # To get cookie
        successPattern = "vapp sucessfully stopped"
        successStatus = search(successPattern, stopOutput)
        if successStatus:
            print "vApp stopped successfull"
        else:
            print "Problem with stopping the vApp. " + str(stopOutput)
            sys.exit(2)

    if catalogArea == "ASSURE-ES-CIExecution":
       cloudArea = "ASSURE-ES-CIExecution"

    if (addCatalog == "True"):
        print "Adding vApp to Catalog"
        timeStamp = datetime.now().strftime("%Y.%m.%d_%I.%M.%S")
        addCatalogUrl = 'curl -s -u ' + str(username) + ':' + str(password) + ' --insecure ' + 'https://' + str(sppPortal) + '.athtem.eei.ericsson.se/Vapps/add_to_catalog_api/vapp_id:' + vappId + '/dest_catalog_name:' + str(cloudArea) + '/new_vapp_template_name:' + str(catalogName) + '_' + str(timeStamp) + '/.xml'
        addCatalogOutput = os.popen(addCatalogUrl).read()
        print addCatalogOutput
        failurePattern = "error"
        failureStatus = search(failurePattern, addCatalogOutput)
        if failureStatus:
            print "Problem with adding the vApp to catalog" + str(addCatalogOutput)
            emailReport.write("<h3>Post CDB Task for vApp " + str(slave) + " is failed</h3>")
            emailReport.write("<br>===================<br>")
            emailReport.write("<h1> Error Message </h1><br>")
            emailReport.write("<br>" + str(addCatalogOutput))
            sys.exit(2)
        else:
            print "vApp " + str(slave) + " added to catalog successfully"
            catalogId = search('<tempid>(.*)</tempid>', addCatalogOutput).group(1)
            catalogUrl = 'https://' + str(username) + ':' + str(password) + '@' + str(
                sppPortal) + '.athtem.eei.ericsson.se/vappTemplates/index_api/catalog_name:' + str(
                cloudArea) + '/org_id:' + str(catalogDetails[cloudArea]['cloudArea']) + '/.xml'
            urllib.urlretrieve(str(catalogUrl), "catalogList.xml")
            document = ElementTree.parse("catalogList.xml")
            for templates in document.findall('vapptemplates'):
                if catalogId == templates.find('vapptemplate_id').text:
                    catalogName = templates.find('vapptemplate_name').text
            print "Catalog Name is " + str(catalogName)
            
def main():
    parser = optparse.OptionParser(
        usage="usage: python %prog -c ASSURE-ES-CIExecution -s Jenkins_Linux_II_221 -a True -t Linux_CDB_19.2.13.EU7")
    parser.add_option("-c", "--cloudArea",
                      action="store", type="string", dest="cloudArea", help="Cloud Area the vApp belongs to")
    parser.add_option("-s", "--jenkinsSlave",
                      action="store", type="string", dest="jenkinsSlave", help="Jenkins Slave name")
    parser.add_option("-a", "--addToCatalog",
                      action="store", type="string", dest="addToCatalog",
                      help="Add the vApp to Catalog in CloudArea. Value should be True or False")
    parser.add_option("-t", "--catalogName",
                      action="store", type="string", dest="catalogName",
                      help="Catalog Name. This will be appeneded with yyyy.MM.dd_HH.mm.ss")
    (options, args) = parser.parse_args()
    if not options.cloudArea or not options.jenkinsSlave or not options.memory or not options.memory1 or not options.memory2 or not options.oms_memory or not options.addToCatalog or not options.catalogName:
        print "Incorrect arguments"
        parser.print_help()
        quit()
    postCDB(options.cloudArea, options.jenkinsSlave, options.addToCatalog, options.catalogName)


if __name__ == '__main__':
    main()