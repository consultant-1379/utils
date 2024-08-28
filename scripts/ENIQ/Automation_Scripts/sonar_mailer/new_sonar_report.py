import os
import sys
import subprocess
import requests

#auth key for new sonar
token='348ca88404be28f388a16026cb62a1c082f6911e'


# quality profile key for Platform_sonar AXHkCNcBT9w2Oq_MRdQo

#######################################
###Function to check the branch
#######################################
def check_branch(projects,branch):
    for project in projects:
        response = requests.get('https://codeanalyzer2.internal.ericsson.com/api/project_branches/list?project='+project,  auth=('348ca88404be28f388a16026cb62a1c082f6911e', ''))
        job_contents = response.content
        job = job_contents.split("}]")
        f = 0
        v = '"'+branch+'"'
        for line in job:
            if(v in line):
                yes_branch.append(project)
                final_dict[project] = branch               
                f = 1
                break
        if(f == 0):
            no_branch.append(project)
    return(len(no_branch))

###################################################
###Function to create the table   
###################################################
 
def create_table(projects,journey_table_name):
    html_table = "sonar.html";    
    global f1
    global num
    num = 1
    HTMLT = open (html_table , 'a')
    if(f1 != 1): 
        
        
        HTMLT.write("<center><table style=\"width:100\">\n")
        HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>Team</th>\n<th>Sl.No</th>\n<th>Module</th>\n<th colspan='6' style='border-right: 5px solid #000000'>New_Code</th>\n<b></b><th  colspan='5'>Overall_Code</th>\n</tr>\n")
        HTMLT.write("<tr align=\"center\">\n<th></th><th></th><th></th><th>Coverage</th><th>Duplications</th><th>Bugs</th><th>Vulnerabilities</th><th>Code Smells</th><th style='border-right: 5px solid #000000'>Quality Gate Status</th><th>Coverage</th><th>Duplications</th><th>Bugs</th><th>Vulnerabilities</th><th>Code Smells</th>\n</tr>")
        f1 = 1
    
    HTMLT.write("<tr align=\"center\">\n<td rowspan='"+str(len(projects))+"'>"+journey_table_name+"</td>\n")
    HTMLT.close()
    flag = 0
    for project, branch in projects.items():
        print("Gathering the information of "+project)

        params = (
            ('branch', branch),
            ('component', project),
            ('metrics', 'bugs,vulnerabilities,sqale_index,duplicated_lines_density,ncloc,coverage,code_smells'),
            ('ps', '1000'),
        )
        new_params = (
            ('branch', branch),
            ('component', project),
            ('metricKeys', 'new_bugs,new_vulnerabilities,new_code_smells,new_coverage,new_duplicated_lines_density'),
            ('ps', '1000'),
        )
            
       
        
        status = {}
        
        ###Overall Code Metrics API############
        response = requests.get('https://codeanalyzer2.internal.ericsson.com/api/measures/search_history', params=params, auth=('348ca88404be28f388a16026cb62a1c082f6911e', ''))
        job_contents = response.content
        job = job_contents.split("}]")
        
        #print (job_contents)
        print ('\n')
        
        ###New Code Metrics API#################
        new_response = requests.get('https://codeanalyzer2.internal.ericsson.com/api/measures/component', params=new_params, auth=('348ca88404be28f388a16026cb62a1c082f6911e', ''))
        new_job_contents = new_response.content
        new_job = new_job_contents.split("}]")
        
        #print (new_job_contents)
        print ("\n\n")
        
        ###New Code Metrics Build status API#################
        response_build = requests.get('https://codeanalyzer2.internal.ericsson.com/api/qualitygates/project_status?projectKey='+project+'&branch='+branch, auth=('348ca88404be28f388a16026cb62a1c082f6911e', ''))
        new_build_contents = response_build.content
        #print(new_build_contents)
        new_build = new_build_contents.split("}]")
        
        #print (new_build)
        print ("\n\n")
       
        
        
        
        ##############  
        
        
        
        ###########New metrics declaration#####
        
        new_bugs = 'NNC'
        status['new_bugs'] = 'ffffff'
       
        
        new_code_smells = 'NNC'
        status['new_code_smells'] = 'ffffff'
        
        new_vulnerability = 'NNC'
        status['new_vulnerability'] = 'ffffff'
             
        new_coverage='NNC'
        #status['new_coverage'] = '#a5ff5c'
        status['new_coverage'] = 'ffffff'
        flagNew_Coverage = 0
        
        new_build_status = 'NNC'
        status['new_build_status'] = 'ffffff'
       
        
        coverage='0'
        #status['coverage'] = '#a5ff5c'
        status['coverage'] = '#ffffff'
         
        new_duplicated='NNC'
        #status['new_duplicated'] = '#a5ff5c'
        status['new_duplicated'] = '#ffffff'
        flagNew_Duplicated = 0
        ###############
        
        #####################
        #Overall Code Metrics
        #####################
        for line in job:
            if '"metric":"vulnerabilities"' in line:
                length = len(line.split(":")) - 1
                vulnerability = (line.split(":")[length]).strip('""')
                
                if(int(float(vulnerability))>0):
                    status['vulnerability'] = 'ff751a'
                   
                else:
                    status['vulnerability'] = '#a5ff5c'
                    
            
                
            if '"metric":"coverage"' in line:
                      #print (line)
                      length = len(line.split(":")) - 1
                      coverage = (line.split(":")[length]).strip('""')
                      if '+' in coverage:
                        print (" + in coverage")
                        coverage = '0.0'
                      #print (coverage)
                      if(int(float(coverage))<80):
                          status['coverage'] = 'ff751a'
                          coverage= coverage+"%"
                      else:
                          status['coverage'] = '#a5ff5c'
                          coverage= coverage+"%"
                      if(project == 'sonarqube-scanner-helpset_stats'):
                          coverage='NA'
                          status['coverage'] = '#a5ff5cf'  
           
            if '"metric":"duplicated_lines_density"' in line:
                length = len(line.split(":")) - 1
                duplicated = (line.split(":")[length]).strip('""')
                if(float(duplicated)>3):
                    status['duplicated'] = 'ff751a'
                else:
                    status['duplicated'] = '#a5ff5c'
            
            if '"metric":"bugs"' in line:
                length = len(line.split(":")) - 1
                bug = (line.split(":")[length]).strip('""')
                if(int(float(bug))>0):
                    status['bug'] = 'ff751a'
                else:
                    status['bug'] = '#a5ff5c'
            
            if '"metric":"code_smells"' in line:
                length = len(line.split(":")) - 1
                code_smell = (line.split(":")[length]).strip('""')
                if(int(float(code_smell))>0):
                    status['code_smell'] = 'ff751a'
                else:
                    status['code_smell'] = '#a5ff5c'
                    
        #################
        #New Code Build Metrics
        #################           
        for line in new_build:
            if '"projectStatus":{"status"' in line: 
                initial = line.split(":")[2]
                final = (initial.split(","))
                new_build_status = (final[0]).strip('""')
                if(new_build_status=='OK'):
                    new_build_status='Passed'
                    print('build'+ new_build_status)
                    status['new_build_status'] = '#a5ff5c'
                    
                if(new_build_status=='ERROR'):
                    new_build_status='Failed'
                    print('build'+ new_build_status)
                    status['new_build_status'] = '#ff0000'                                
                
                    
        #################
        #New Code Metrics
        ################# 
        
        for line in new_job: 
            if '"metric":"new_duplicated_lines_density"' in line:
                flagNew_Duplicated = 1
                length = len(line.split(":")) - 2
                initial = line.split(":")[length]
                final = (initial.split(","))
                new_duplicated = (final[0]).strip('""')
                new_duplicated = str(round(float(new_duplicated),1))
                print('new duplicated are '+new_duplicated)
                if(float(new_duplicated)>3):
                    status['new_duplicated'] = 'ff751a'
                    new_duplicated = new_duplicated+"%"
                else:
                    status['new_duplicated'] = '#a5ff5c'
                    new_duplicated = new_duplicated+"%"
            
            if '"metric":"new_bugs"' in line:
                length = len(line.split(":")) - 2
                initial = line.split(":")[length]
                final = (initial.split(","))
                new_bugs = (final[0]).strip('""')
                print ('new bugs are '+new_bugs)
                if(int(float(new_bugs))>0):
                    status['new_bugs'] = 'ff751a'
                else:
                    status['new_bugs'] = '#a5ff5c'
            
            if '"metric":"new_vulnerabilities"' in line:
                length = len(line.split(":")) - 2
                initial = line.split(":")[length]
                final = (initial.split(","))
                new_vulnerability = (final[0]).strip('""') 
                print('new vulunerabilities are '+new_vulnerability)
                if(int(float(new_vulnerability))>0):
                    status['new_vulnerability'] = 'ff751a'
                else:
                    status['new_vulnerability'] = '#a5ff5c'
            
            if '"metric":"new_code_smells"' in line:
                length = len(line.split(":")) - 2
                initial = line.split(":")[length]
                final = (initial.split(","))
                new_code_smells = (final[0]).strip('""')
                print('new code smells are '+new_code_smells)
                if(int(float(new_code_smells))>0):
                    status['new_code_smells'] = 'ff751a'
                   
                else:
                    status['new_code_smells'] = '#a5ff5c' 
                   
                                      
                            
            if '"metric":"new_coverage"' in line :
                flagNew_Coverage = 1
                length = len(line.split(":")) - 2
                initial = line.split(":")[length]
                final = (initial.split(","))
                new_coverage = (final[0]).strip('""')
                print('new coverage is '+new_coverage)
                new_coverage= str(round(float(new_coverage),1))
                if(int(float(new_coverage))< 80):
                    status['new_coverage'] = 'ff751a'
                    new_coverage= new_coverage+"%"
                else:
                    status['new_coverage'] = '#a5ff5c'
                    new_coverage= new_coverage+"%" 
                if(project == 'sonarqube-scanner-helpset_stats'):
                   new_coverage='NA'
                   #status['coverage'] = '#a5ff5cf'
                   status['coverage'] = '#ffffff'
        
        ##################################################### 
        if (flagNew_Duplicated == 0):
            if (  (new_code_smells =='0') and (new_bugs == '0') and (new_vulnerability =='0') ):
              print ('nnc for new duplications')
            
            else:
              new_duplicated = '0.0%'
              status['new_duplicated'] = '#a5ff5c'
        if (flagNew_Coverage == 0):
            
            #print (new_duplicated == '0.0%')
            #print (new_code_smells =='0')
            #print (new_bugs == '0')
            #print (new_vulnerability =='0')
            if ( (new_duplicated == 'NNC') and (new_code_smells =='0') and (new_bugs == '0') and (new_vulnerability =='0') ):
              print('all metrics zero')
              new_code_smells = 'NNC'
              new_bugs = 'NNC'
              new_vulnerability = 'NNC'
              status['new_bugs'] = 'ffffff'
              status['new_code_smells'] = 'ffffff'
              status['new_vulnerability'] = 'ffffff'
              
            else:
              #new_coverage='0.0%'
              #status['new_coverage'] = 'ff751a'
              new_coverage = '0.0'
              status['new_coverage'] = 'ff751a'
              print ("all metrics are not zero")
            if(project == 'sonarqube-scanner-helpset_stats'):
              new_coverage='NA'
              status['new_coverage'] = '#ffffff'
        if (new_bugs == 'NNC'):
          new_coverage = 'NNC'
          new_duplicated = 'NNC'
          status['new_coverage'] = '#ffffff'
          status['new_duplicated'] = '#ffffff'
          
        if ( (new_duplicated == 'NNC') and (new_code_smells =='NNC') and (new_bugs == 'NNC') and (new_vulnerability =='NNC') and (new_coverage == 'NNC') ):
          new_build_status = 'NNC'
          status['new_build_status'] = 'ffffff'
          
          
        ##############################################################
        html_table = "sonar.html";
        HTMLT = open (html_table , 'a')
		
        url = "https://codeanalyzer2.internal.ericsson.com/dashboard?branch="+branch+"&id="+project
        
        if(flag != 1):
            HTMLT.write("<td style='text-align:center;'>"+str(num)+"</td>\n<td style='text-align:center;color:black'><b><a href=" + url +">"+(project.replace('sonarqube-scanner-','')).replace('Eniq_BO_','')+"</a></b></td>\n<td style='text-align:center;' bgcolor= '"+status['new_coverage']+"'>"+new_coverage+"</td>\n<td style='text-align:center;' bgcolor= '"+status['new_duplicated']+"'>"+new_duplicated+"</td>\n<td style='text-align:center;' bgcolor= '"+status['new_bugs']+"'>"+new_bugs+"</td>\n<td style='text-align:center;' bgcolor= '"+status['new_vulnerability']+"'>"+new_vulnerability+"</td>\n<td style='text-align:center;' bgcolor= '"+status['new_code_smells']+"'>"+new_code_smells+"</td>\n<td style='text-align:center;border-right: 5px solid #000000' bgcolor= '"+status['new_build_status']+"'>"+new_build_status+"</td>\n<td style='text-align:center;' bgcolor= '"+status['coverage']+"'>"+coverage+"</td>\n<td style='text-align:center;' bgcolor= '"+status['duplicated']+"'>"+duplicated+"%</td>\n<td style='text-align:center;' bgcolor= '"+status['bug']+"'>"+bug+"</td>\n<td style='text-align:center;' bgcolor= '"+status['vulnerability']+"'>"+vulnerability+"</td>\n<td style='text-align:center;' bgcolor= '"+status['code_smell']+"'>"+code_smell+"</td>\n</tr>")
            
            num = num + 1
        
        else:
            HTMLT.write("<td style='text-align:center;'>"+str(num)+"</td>\n<td style='text-align:center;color:black'><b><a href=" + url +">"+project.replace('sonarqube-scanner-','')+"</a></b></td>\n<td style='text-align:center;' bgcolor= '"+status['new_coverage']+"'>"+new_coverage+"%</td>\n<td style='text-align:center;' bgcolor= '"+status['new_duplicated']+"'>"+new_duplicated+"%</td>\n<td style='text-align:center;' bgcolor= '"+status['new_bugs']+"'>"+new_bugs+"</td>\n<td style='text-align:center;' bgcolor= '"+status['new_vulnerability']+"'>"+new_vulnerability+"</td>\n<td style='text-align:center;' bgcolor= '"+status['new_code_smells']+"'>"+new_code_smells+"</td>\n<td style='text-align:center;' bgcolor= '"+status['new_build_status']+"'>"+new_build_status+"</td><td style='text-align:center;' bgcolor= '"+status['coverage']+"'>"+coverage+"</td>\n<td style='text-align:center;' bgcolor= '"+status['duplicated']+"'>"+duplicated+"%</td>\n<td style='text-align:center;' bgcolor= '"+status['bug']+"'>"+bug+"</td>\n<td style='text-align:center;' bgcolor= '"+status['vulnerability']+"'>"+vulnerability+"</td>\n<td style='text-align:center;' bgcolor= '"+status['code_smell']+"'>"+code_smell+"</td>\n</tr>")
        HTMLT.close()
        print("Information is gathered for "+project)

#####################################
####Main
#####################################    

#platform =['sonarqube-scanner-export']
platform = ['sonarqube-scanner-3GPP32435','sonarqube-scanner-3GPP32435BCS','sonarqube-scanner-3GPP32435DYN','sonarqube-scanner-adminui','sonarqube-scanner-alarm_module','sonarqube-scanner-alarmcfg','sonarqube-scanner-ascii','sonarqube-scanner-asn1','sonarqube-scanner-BCDParser','sonarqube-scanner-busyhourcfg','sonarqube-scanner-ct','sonarqube-scanner-common','sonarqube-scanner-csexport','sonarqube-scanner-dwhmanager','sonarqube-scanner-ebs','sonarqube-scanner-ebsmanager','sonarqube-scanner-engine','sonarqube-scanner-export','sonarqube-scanner-installer','sonarqube-scanner-json','sonarqube-scanner-licensing','sonarqube-scanner-mdc','sonarqube-scanner-mdc_ccn','sonarqube-scanner-mdc_dyn','sonarqube-scanner-mdc_pc','sonarqube-scanner-mrr','sonarqube-scanner-minilink','sonarqube-scanner-monitoring','sonarqube-scanner-nossdb','sonarqube-scanner-parser','sonarqube-scanner-redback','sonarqube-scanner-repository','sonarqube-scanner-sasn','sonarqube-scanner-scheduler','sonarqube-scanner-stfiop','sonarqube-scanner-symboliclinkcreator','sonarqube-scanner-twampm','sonarqube-scanner-twamppt','sonarqube-scanner-twampst','sonarqube-scanner-uncompress','sonarqube-scanner-volte','sonarqube-scanner-diskmanager','sonarqube-scanner-helpset_stats']

infra = [ 'ENIQ_Infra_Spartan']

security =  [ 'ENIQ_Security_Spartan']

#nmi = ['nmiinstall','nmiNASd','nmibootstrap']
nmi = ['nmiNASd','nmibootstrap']

netan = ['network-analytics-pm-explorer','network-analytics-pm-alarming','network-analytics-nr-kpi-dashboard','network-analytics-pm-data','network-analytics-energy-report','network-analytics-volte','network-analytics-RNO-MRR','network-analytics-ran-performance-overview','network-analytics-IMS-Capacity','Network-Analytics-Uplink-Interference','network-analytics-NR-and-LTE-Timing-Advance','Transport-MINI-LINK-Performance']

netan_platform = ['ENIQ_network-analytics-utilities','ENIQ_network_analytics_server']

netan_parsers = ['sonarqube-scanner-kpiparser', 'sonarqube-scanner-information_store_parser' ]

ocs = ['Eniq_BO_OCS']

bo = ['Eniq_BO_EBID']

ddc = [ 'ENIQ_DDC']






f1 = 0
f2 = 0
html_table = "sonar.html";
html_table1 = "temp.html";
HTMLT = open (html_table , 'w')
HTMLT.write("<html>\n<head><style>table {border-collapse: collapse;} td, th {border: 1px solid #000000;text-align: center;}</style><center><h2>pEniq SonarQube Analysis Report</h2></center></head>\n<body>")
HTMLT.write("<table align=\"center\"><tr style=\"background-color:##a5ff5c\"><td>\"NNC\"</td><td>No New Code to analyse</td></tr><tr style=\"background-color:#ff751a\"><td>Amber</td><td>  Did not meet the Gating criteria  </td></tr ><tr style=\"background-color:#a5ff5c\"><td>Green</td><td>Met the Gating criteria</td></tr></table>")
HTMLT.write("<br>")
HTMLT.write("")
HTMLT.close()
HTMLT = open (html_table1 , 'w')
HTMLT.close()
fp1 = open("branch.txt",'r')
l1 = fp1.readlines()
fp1.close()
length = len(l1)

###############################################################################
############################################################################

"""

this comment section is used for testing
###################################################
###For testing
###################################################
no_branch = []
yes_branch = []
no_branch1 = nmi
final_dict = {}
for i in range(length):        
    no_branch = []
    yes_branch = []
    l = check_branch(no_branch1,l1[i].strip())
    no_branch1 = []
    no_branch1 = no_branch

create_table(final_dict,"help")

#################################################################################
#################################################################################
"""



###################################################
###For Security_Spartan
###################################################
no_branch = []
yes_branch = []
no_branch1 = security
final_dict = {}
for i in range(length):        
    no_branch = []
    yes_branch = []
    l = check_branch(no_branch1,l1[i].strip())
    no_branch1 = []
    no_branch1 = no_branch

create_table(final_dict,"Security_Spartan")


###################################################
###For Infra_Spartan
###################################################
no_branch = []
yes_branch = []
no_branch1 = infra
final_dict = {}
for i in range(length):        
    no_branch = []
    yes_branch = []
    l = check_branch(no_branch1,l1[i].strip())
    no_branch1 = []
    no_branch1 = no_branch

create_table(final_dict,"Infra_Spartan")


###################################################
###For NMI
###################################################
no_branch = []
yes_branch = []
no_branch1 = nmi
final_dict = {}
for i in range(length):        
    no_branch = []
    yes_branch = []
    l = check_branch(no_branch1,l1[i].strip())
    no_branch1 = []
    no_branch1 = no_branch

create_table(final_dict,"NMI")




###################################################
###For Platform
###################################################
no_branch = []
yes_branch = []
no_branch1 = platform
final_dict = {}
for i in range(length):        
    no_branch = []
    yes_branch = []
    l = check_branch(no_branch1,l1[i].strip())
    no_branch1 = []
    no_branch1 = no_branch

create_table(final_dict,"Platform")

####################################################

###################################################
###For Netan
###################################################
no_branch = []
yes_branch = []
no_branch1 = netan
final_dict = {}
for i in range(length):        
    no_branch = []
    yes_branch = []
    l = check_branch(no_branch1,l1[i].strip())
    no_branch1 = []
    no_branch1 = no_branch

create_table(final_dict,"NetAn")
####################################################

###################################################
###For NetAn Platform
###################################################
no_branch = []
yes_branch = []
no_branch1 = netan_platform
final_dict = {}
for i in range(length):        
    no_branch = []
    yes_branch = []
    l = check_branch(no_branch1,l1[i].strip())
    no_branch1 = []
    no_branch1 = no_branch

create_table(final_dict,"NetAn_Platform")

####################################################


###################################################
###For NetAn Platform
###################################################
no_branch = []
yes_branch = []
no_branch1 = netan_parsers
final_dict = {}
for i in range(length):        
    no_branch = []
    yes_branch = []
    l = check_branch(no_branch1,l1[i].strip())
    no_branch1 = []
    no_branch1 = no_branch

create_table(final_dict,"NetAn_Parsers")

####################################################



###################################################
###For OCS
###################################################
no_branch = []
yes_branch = []
no_branch1 = ocs
final_dict = {}
for i in range(length):        
    no_branch = []
    yes_branch = []
    l = check_branch(no_branch1,l1[i].strip())
    no_branch1 = []
    no_branch1 = no_branch

create_table(final_dict,"OCS")

####################################################


###################################################
###For BO
###################################################
no_branch = []
yes_branch = []
no_branch1 = bo
final_dict = {}
for i in range(length):        
    no_branch = []
    yes_branch = []
    l = check_branch(no_branch1,l1[i].strip())
    no_branch1 = []
    no_branch1 = no_branch

create_table(final_dict,"BO")

####################################################


###################################################
###For DDC
###################################################
no_branch = []
yes_branch = []
no_branch1 = ddc
final_dict = {}
for i in range(length):        
    no_branch = []
    yes_branch = []
    l = check_branch(no_branch1,l1[i].strip())
    no_branch1 = []
    no_branch1 = no_branch

create_table(final_dict,"DDC")

####################################################


###################################################
###For Techpacks/KPI
###################################################
html_table = "sonar.html";
HTMLT = open (html_table , 'a')
HTMLT.write("<tr align=\"center\">\n<td rowspan=1>Techpacks/KPI</td>\n")

HTMLT.write("<td style='text-align:center;' colspan=13 >Not Applicable</td>\n")


HTMLT.close()


	

####################################################






######################################
###all modules done###
#############################
        
HTMLT = open (html_table1 , 'r')
contents = HTMLT.readlines()
HTMLT.close()
HTMLT = open (html_table , 'a')
if(f1 != 0):
    HTMLT.write("</center></table>\n")
HTMLT.writelines(contents)
HTMLT.close()
os.system("rm -rf "+html_table1)

