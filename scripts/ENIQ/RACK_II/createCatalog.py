# ************************************************************************
# Author: Suresh Jaganathan                                              *
# Description: This script will                                          *
#                   * Stop the vApp                                      *
#                   * Reduce ossmaster memory                            *
#                   * Add to catalog and check sync status               *
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

username = 'ociadm100'
password = 'Wiproci321'
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

cloudDetails = {'OSSRC-CI-CDB-UG': {'cloudArea': 'urn:vcloud:orgvdc:ea073353-3f2f-46ad-a299-b931c2f54156',
                                    'sppPortal': 'atvcloud3'},
                'CI-Execution-OSSRC': {'cloudArea': 'urn%3Avcloud%3Aorgvdc%3Ab9628a68-ef3a-44d2-92eb-b929a0426557',
                                       'sppPortal': 'atvcloud3'},
                'OSSRC-CI-Exec-POD-B': {'cloudArea': 'urn%3Avcloud%3Aorgvdc%3A1eeb656f-5184-4677-a23e-d73b121678aa',
                                        'sppPortal': 'atvpbspp11'},
                'OSSRC-CI-Exec-POD-F': {'cloudArea': 'urn%3Avcloud%3Aorgvdc%3Affecbb33-0cef-4244-b985-a335e3108135',
                                        'sppPortal': 'atvpfspp15'},
                'OSSRC-CI_Execution': {'cloudArea': 'urn%3Avcloud%3Aorgvdc%3Ab29490a4-cc80-4178-ac9d-9768ec7d4fdf',
                                        'sppPortal': 'atvpjspp19'}, }
catalogDetails = {'OSSRC-CI-CDB-UG': {'cloudArea': 'urn%3Avcloud%3Aorg%3A1f5de637-01fc-4ba4-bc4d-e48abe37f8ab'},
                  'CI-Execution-OSSRC': {'cloudArea': 'urn%3Avcloud%3Aorg%3Acd2a9a08-2676-497a-a7b4-8f738bc37abb'},
                  'OSSRC-CI-Exec-POD-B': {'cloudArea': 'urn%3Avcloud%3Aorg%3Aa9f9797f-eb10-4594-a902-1b217240d27d'},
                  'OSSRC-CI-Exec-POD-F': {'cloudArea': 'urn%3Avcloud%3Aorg%3A28d283f4-8788-4eeb-b645-181e0c22a1c8'},
	          'OSSRC-CI-Exec-POD-F-PLM': {'cloudArea': 'urn%3Avcloud%3Aorg%3A0581dcde-8aad-4a6f-8f0b-75d600583685'},		
                  'OSSRC-CI_Execution': {'cloudArea':'urn%3Avcloud%3Aorg%3Af744e55e-f6a1-41ba-bdb6-fa75bb8de420'}, }

def postCDB(datacenter, slave, memory, memory1, memory2, oms_memory, addCatalog, catalogName):
    emailReport = open("emailReport.html", 'w')
    if datacenter == "PODB":
        datacenter = "OSSRC-CI-Exec-POD-B"
    if datacenter == "PODF":
        datacenter = "OSSRC-CI-Exec-POD-F"
    if datacenter == "PODJ":
	datacenter = "OSSRC-CI_Execution"
    if datacenter not in cloudDetails:
        print "Invalid Data Center used " + str(datacenter)
        print "Please select either OSSRC-CI-CDB-UG or CI-Execution-OSSRC or contact CI Infra"
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
    cloudUrl = 'https://' + str(username) + ':' + str(password) + '@' + str(
    sppPortal) + '.athtem.eei.ericsson.se/Vms/vapp_index_api/vapp_id:' + str(vappId) + '/orgvdc_id:' + \
         cloudDetails[cloudArea]['cloudArea'] + '/.xml'
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
            vmMemory = vms.find('memory_mb').text

    os.remove("vmList.xml")
    if (int(vmMemory) >= 23552):
        try:
            print vmId
        except:
            print "Slave " + str(slave) + " not having netsim vm"
            sys.exit(2)
        cloudUrl = 'https://' + str(sppPortal) + '.athtem.eei.ericsson.se/Vms/set_memory_mb/vm_id:' + str(
            vmId) + '/vapp_id:' + str(
            vappId) + '/orgvdc_id:' + cloudDetails[cloudArea]['cloudArea'] + '/memory_mb:' + str(memory1)
        vAppUrl = 'curl -s -u ' + str(username) + ':' + str(
            password) + ' --insecure --cookie-jar ./somefile https://' + str(
            sppPortal) + '.athtem.eei.ericsson.se/Vapps/stop_vapp_api/vapp_id:' + str(
            vappId) + '/.xml -m 4800'
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
        print "Setting NETSIM memory size to " + str(memory1)
        redMemUrl = 'curl -s -u ' + str(username) + ':' + str(password) + ' -k --cookie ./somefile ' + str(cloudUrl)
        reduceOutput = os.popen(redMemUrl).read()

    #to reduce memory of ossmaster

    cloudUrl = 'https://' + str(username) + ':' + str(password) + '@' + str(
        sppPortal) + '.athtem.eei.ericsson.se/Vms/vapp_index_api/vapp_id:' + str(vappId) + '/orgvdc_id:' + \
               cloudDetails[cloudArea]['cloudArea'] + '/.xml'
    urllib.urlretrieve(str(cloudUrl), "vmList.xml")
    document = ElementTree.parse("vmList.xml")
    for vms in document.findall('vms'):
        if vms.find('name').text == 'master_ossmaster':
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
    try:
        print vmId
    except:
        print "Slave " + str(slave) + " not having ossmaster vm"
        sys.exit(2)
    cloudUrl = 'https://' + str(sppPortal) + '.athtem.eei.ericsson.se/Vms/set_memory_mb/vm_id:' + str(
        vmId) + '/vapp_id:' + str(
        vappId) + '/orgvdc_id:' + cloudDetails[cloudArea]['cloudArea'] + '/memory_mb:' + str(memory)
    vAppUrl = 'curl -s -u ' + str(username) + ':' + str(
        password) + ' --insecure --cookie-jar ./somefile https://' + str(
        sppPortal) + '.athtem.eei.ericsson.se/Vapps/stop_vapp_api/vapp_id:' + str(
        vappId) + '/.xml -m 4800'
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
    print "Setting OSSMASTER memory size to " + str(memory)
    redMemUrl = 'curl -s -u ' + str(username) + ':' + str(password) + ' -k --cookie ./somefile ' + str(cloudUrl)
    reduceOutput = os.popen(redMemUrl).read()

    #for changing memory of UAS CIS-28000
    cloudUrl = 'https://' + str(username) + ':' + str(password) + '@' + str(
    sppPortal) + '.athtem.eei.ericsson.se/Vms/vapp_index_api/vapp_id:' + str(vappId) + '/orgvdc_id:' + \
         cloudDetails[cloudArea]['cloudArea'] + '/.xml'
    urllib.urlretrieve(str(cloudUrl), "vmList.xml")
    document = ElementTree.parse("vmList.xml")
    for vms in document.findall('vms'):
        if vms.find('name').text == 'master_uas1':
            print vms.find('name').text
            status = vms.find('status').text
            print status
            vmId = vms.find('vm_id').text
            if (str(status) == 'POWERED_ON'):
                print 'The vApp must be in the POWERED_OFF state to change cpu or memory on one of its VMs'
                vmStatus = "ON"
            elif (str(status) == 'POWERED_OFF'):
                vmStatus = "OFF"
            vmMemory = vms.find('memory_mb').text

    os.remove("vmList.xml")
    if (int(vmMemory) <= 9216):
        try:
            print vmId
        except:
            print "Slave " + str(slave) + " not having uas vm"
            sys.exit(2)
        cloudUrl = 'https://' + str(sppPortal) + '.athtem.eei.ericsson.se/Vms/set_memory_mb/vm_id:' + str(
            vmId) + '/vapp_id:' + str(
            vappId) + '/orgvdc_id:' + cloudDetails[cloudArea]['cloudArea'] + '/memory_mb:' + str(memory2)
        vAppUrl = 'curl -s -u ' + str(username) + ':' + str(
            password) + ' --insecure --cookie-jar ./somefile https://' + str(
            sppPortal) + '.athtem.eei.ericsson.se/Vapps/stop_vapp_api/vapp_id:' + str(
            vappId) + '/.xml -m 4800'
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
        print "Setting UAS memory size to " + str(memory2)
        redMemUrl = 'curl -s -u ' + str(username) + ':' + str(password) + ' -k --cookie ./somefile ' + str(cloudUrl)
        reduceOutput = os.popen(redMemUrl).read()

    #for changing memory of OMSAS
    cloudUrl = 'https://' + str(username) + ':' + str(password) + '@' + str(
    sppPortal) + '.athtem.eei.ericsson.se/Vms/vapp_index_api/vapp_id:' + str(vappId) + '/orgvdc_id:' + \
         cloudDetails[cloudArea]['cloudArea'] + '/.xml'
    urllib.urlretrieve(str(cloudUrl), "vmList.xml")
    document = ElementTree.parse("vmList.xml")
    for vms in document.findall('vms'):
        if vms.find('name').text == 'master_omsas':
            print vms.find('name').text
            status = vms.find('status').text
            print status
            vmId = vms.find('vm_id').text
            if (str(status) == 'POWERED_ON'):
                print 'The vApp must be in the POWERED_OFF state to change cpu or memory on one of its VMs'
                vmStatus = "ON"
            elif (str(status) == 'POWERED_OFF'):
                vmStatus = "OFF"
            vmMemory = vms.find('memory_mb').text

    os.remove("vmList.xml")
    if (int(vmMemory) >= 3072):
        try:
            print vmId
        except:
            print "Slave " + str(slave) + " not having omsas vm"
            sys.exit(2)
        cloudUrl = 'https://' + str(sppPortal) + '.athtem.eei.ericsson.se/Vms/set_memory_mb/vm_id:' + str(
            vmId) + '/vapp_id:' + str(
            vappId) + '/orgvdc_id:' + cloudDetails[cloudArea]['cloudArea'] + '/memory_mb:' + str(oms_memory)
        vAppUrl = 'curl -s -u ' + str(username) + ':' + str(
            password) + ' --insecure --cookie-jar ./somefile https://' + str(
            sppPortal) + '.athtem.eei.ericsson.se/Vapps/stop_vapp_api/vapp_id:' + str(
            vappId) + '/.xml -m 4800'
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
        print "Setting OMSAS memory size to " + str(oms_memory)
        redMemUrl = 'curl -s -u ' + str(username) + ':' + str(password) + ' -k --cookie ./somefile ' + str(cloudUrl)
        reduceOutput = os.popen(redMemUrl).read()

    #for changing memory of OMSRVM
    cloudUrl = 'https://' + str(username) + ':' + str(password) + '@' + str(
    sppPortal) + '.athtem.eei.ericsson.se/Vms/vapp_index_api/vapp_id:' + str(vappId) + '/orgvdc_id:' + \
         cloudDetails[cloudArea]['cloudArea'] + '/.xml'
    urllib.urlretrieve(str(cloudUrl), "vmList.xml")
    document = ElementTree.parse("vmList.xml")
    for vms in document.findall('vms'):
        if vms.find('name').text == 'master_omsrvm':
            print vms.find('name').text
            status = vms.find('status').text
            print status
            vmId = vms.find('vm_id').text
            if (str(status) == 'POWERED_ON'):
                print 'The vApp must be in the POWERED_OFF state to change cpu or memory on one of its VMs'
                vmStatus = "ON"
            elif (str(status) == 'POWERED_OFF'):
                vmStatus = "OFF"
            vmMemory = vms.find('memory_mb').text

    os.remove("vmList.xml")
    if (int(vmMemory) >= 3072):
        try:
            print vmId
        except:
            print "Slave " + str(slave) + " not having omsrvm vm"
            sys.exit(2)
        cloudUrl = 'https://' + str(sppPortal) + '.athtem.eei.ericsson.se/Vms/set_memory_mb/vm_id:' + str(
            vmId) + '/vapp_id:' + str(
            vappId) + '/orgvdc_id:' + cloudDetails[cloudArea]['cloudArea'] + '/memory_mb:' + str(oms_memory)
        vAppUrl = 'curl -s -u ' + str(username) + ':' + str(
            password) + ' --insecure --cookie-jar ./somefile https://' + str(
            sppPortal) + '.athtem.eei.ericsson.se/Vapps/stop_vapp_api/vapp_id:' + str(
            vappId) + '/.xml -m 4800'
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
        print "Setting OMSRVM memory size to " + str(oms_memory)
        redMemUrl = 'curl -s -u ' + str(username) + ':' + str(password) + ' -k --cookie ./somefile ' + str(cloudUrl)
        reduceOutput = os.popen(redMemUrl).read()

    #for changing memory of OMSRVS
    cloudUrl = 'https://' + str(username) + ':' + str(password) + '@' + str(
    sppPortal) + '.athtem.eei.ericsson.se/Vms/vapp_index_api/vapp_id:' + str(vappId) + '/orgvdc_id:' + \
         cloudDetails[cloudArea]['cloudArea'] + '/.xml'
    urllib.urlretrieve(str(cloudUrl), "vmList.xml")
    document = ElementTree.parse("vmList.xml")
    for vms in document.findall('vms'):
        if vms.find('name').text == 'master_omsrvs':
            print vms.find('name').text
            status = vms.find('status').text
            print status
            vmId = vms.find('vm_id').text
            if (str(status) == 'POWERED_ON'):
                print 'The vApp must be in the POWERED_OFF state to change cpu or memory on one of its VMs'
                vmStatus = "ON"
            elif (str(status) == 'POWERED_OFF'):
                vmStatus = "OFF"
            vmMemory = vms.find('memory_mb').text

    os.remove("vmList.xml")
    if (int(vmMemory) >= 3072):
        try:
            print vmId
        except:
            print "Slave " + str(slave) + " not having omsrvs vm"
            sys.exit(2)
        cloudUrl = 'https://' + str(sppPortal) + '.athtem.eei.ericsson.se/Vms/set_memory_mb/vm_id:' + str(
            vmId) + '/vapp_id:' + str(
            vappId) + '/orgvdc_id:' + cloudDetails[cloudArea]['cloudArea'] + '/memory_mb:' + str(oms_memory)
        vAppUrl = 'curl -s -u ' + str(username) + ':' + str(
            password) + ' --insecure --cookie-jar ./somefile https://' + str(
            sppPortal) + '.athtem.eei.ericsson.se/Vapps/stop_vapp_api/vapp_id:' + str(
            vappId) + '/.xml -m 4800'
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
        print "Setting OMSRVS memory size to " + str(oms_memory)
        redMemUrl = 'curl -s -u ' + str(username) + ':' + str(password) + ' -k --cookie ./somefile ' + str(cloudUrl)
        reduceOutput = os.popen(redMemUrl).read()
    
    if catalogArea == "OSSRC-CI-Exec-POD-F-PLM":
       cloudArea = "OSSRC-CI-Exec-POD-F-PLM"

    if (addCatalog == "True"):
        print "Adding vApp to Catalog"
        timeStamp = datetime.now().strftime("%Y.%m.%d_%I.%M.%S")
        addCatalogUrl = 'curl -s -u ' + str(username) + ':' + str(
            password) + ' --insecure ' + 'https://' + str(
            sppPortal) + '.athtem.eei.ericsson.se/Vapps/add_to_catalog_api/vapp_id:' + vappId + '/dest_catalog_name:' + str(
            cloudArea) + '/new_vapp_template_name:' + str(catalogName) + '_' + str(timeStamp) + '/.xml -m 1800'
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
            if sppPortal is "atvcloud3":
                syncArea = syncArea1
                syncStatus = syncStatus1
            elif sppPortal is "atvspp2":
                syncArea = syncArea2
                syncStatus = syncStatus2
            elif sppPortal is "atvpjspp19":
		print "No clusters present in PODJ cloud area"
	    else:
                syncArea = syncArea3
                syncStatus = syncStatus3
            if catalogArea == "OSSRC-CI-Exec-POD-F-PLM":
                syncArea = syncArea4
                syncStatus = syncStatus4

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
            if datacenter == "OSSRC-CI_Execution":
                emailReport.write("<h3>Post CDB Task Result</h3>")
                emailReport.write("<br>===================<br>")
                emailReport.write(
                "vApp Name  : " + str(slave) + " is added successfully to the cloud area " + str(cloudArea))
                emailReport.write("<br>Catalog name : " + str(catalogName) + "<br><br>")
                emailReport.write("<br><br> Regards, <br> CI Infrastructure Team")
                emailReport.close()
            else:
            	print "Checking sync status across clusters after the wait period of one hour"
            	time.sleep(3600)
            	cloudUrl = 'https://' + str(username) + ':' + str(password) + '@' + str(sppPortal) + '.athtem.eei.ericsson.se/Vapps/index_api/orgvdc_id:'
            	while 'UNRESOLVED' in syncStatus.values():
                	for area in sorted(syncArea):
                    		# New Changes for CIS-16758
                    		if syncStatus[area] != "NA":
                        		urllib.urlretrieve(str(cloudUrl) + str(syncArea[area]) + '/.xml', "vappList.xml")
                        		document = ElementTree.parse("vappList.xml")
                        		for vApps in document.findall('vapps'):
                            			# clusters doesn't have vApps means it will do the following
                            			name = vApps.find('name')
                            			if name is None:
                                			syncStatus[area] = "NA"
                                			syncTime[area] = "NA"
                                			print "No vApp present in " + area
                                			continue
                            			# clusters contains vApps then it will do the following
                            			if catalogName in vApps.find('name').text:
                                			if syncStatus[area] == "UNRESOLVED":
                                    				syncStatus[area] = vApps.find('status').text
                                    				startTime = (vApps.find('creation_date').text).split("+")[0]
                                    				currentTime = datetime.now()
                                    				currentTime1 = currentTime - timedelta(minutes=60)  # 1 hour mismatch bcz of athlone time
                                    				syncStartTime = datetime.strptime(startTime, "%Y-%m-%dT%H:%M:%S.%f")
                                    				duration = currentTime1 - syncStartTime
                                    				creationTime = datetime.strptime(str(duration), "%H:%M:%S.%f").strftime("%H:%M:%S")
                                    				syncTime[area] = creationTime
                                    				print "Sync for " + str(catalogName) + " completed with status " + syncStatus[area] + " in the " + area + " in duration of " + str(creationTime)
                    		if 'UNRESOLVED' in syncStatus.values():
                        		time.sleep(300)
            	emailReport.write("<h3>Post CDB Task Result</h3>")
            	emailReport.write("<br>===================<br>")
            	emailReport.write("vApp Name  : " + str(slave) + " is added successfully to the cloud area " + str(cloudArea))
            	emailReport.write("<br>Please find the sync status for " + str(catalogName) + "<br><br>")
            	for status in syncStatus:
                	emailReport.write(status + " :\t" + syncStatus[status] + "\t" + syncTime[status] + "<br>")
            	emailReport.write("<br><br> Regards, <br> CI Infrastructure Team")
            	emailReport.close()

def main():
    parser = optparse.OptionParser(
        usage="usage: python %prog -c CI-Execution-OSSRC -s suresh_test -m 65536 -n 23552 -u 9216 -o 3072 -a True -t test_suresh_ossrc_15.2.5EU01_1")
    parser.add_option("-c", "--cloudArea",
                      action="store", type="string", dest="cloudArea", help="Cloud Area the vApp belongs to")
    parser.add_option("-s", "--jenkinsSlave",
                      action="store", type="string", dest="jenkinsSlave", help="Jenkins Slave name")
    parser.add_option("-m", "--memory",
                      action="store", type="string", dest="memory", help="Size of OssMaster VM in MB")
    parser.add_option("-n", "--memory1",
                      action="store", type="string", dest="memory1", help="Size of Netsim VM in MB")
    parser.add_option("-u", "--memory2",
                      action="store", type="string", dest="memory2", help="Size of UAS VM in MB")
    parser.add_option("-o", "--oms_memory",
                      action="store", type="string", dest="oms_memory", help="Size of OMSAS,OMSRVM,OMSRVS VM in MB")    
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
    postCDB(options.cloudArea, options.jenkinsSlave, options.memory, options.memory1, options.memory2, options.oms_memory, options.addToCatalog, options.catalogName)


if __name__ == '__main__':
    main()