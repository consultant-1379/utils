import os
import sys
import subprocess
import requests
# quality profile key for Platform_sonar AXHkCNcBT9w2Oq_MRdQo

#######################################
###Function to check the branch
#######################################

def check_branch(projects,branch):
    for project in projects:
        headers = {
            'authority': 'sonarqube.lmera.ericsson.se',
            'accept': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
            'x-xsrf-token': 'bqkk43b4oq0r5tgnqog29qdjee',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://sonarqube.lmera.ericsson.se/dashboard?id='+project,
            'accept-language': 'en-US,en;q=0.9',
            'cookie': '_ga=GA1.2.2146927517.1608016603; _fbp=fb.1.1608016603445.191654112; _rdt_uuid=1608016603393.9773df9d-9a68-43c0-8180-84d2ef31231a; XSRF-TOKEN=bqkk43b4oq0r5tgnqog29qdjee; JWT-SESSION=eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJBWGhKb2FVM0ZXSXlNMlp1NDQ0WCIsInN1YiI6ImVzamthZG0xMDAiLCJpYXQiOjE2MTYxNDMwMzMsImV4cCI6MTYxNjQwMzIxMiwibGFzdFJlZnJlc2hUaW1lIjoxNjE2MTQzMDMzNjU1LCJ4c3JmVG9rZW4iOiJicWtrNDNiNG9xMHI1dGducW9nMjlxZGplZSJ9.ZwVgQ8hqyBil4md0Mn54uEd2nJVcUnJWJKdmqI4EG2I',
            }
        response = requests.get('https://sonarqube.lmera.ericsson.se/api/project_branches/list?project='+project, headers=headers, auth=('113e5fae4d562c6b79bca47a56870206c2cff446', ''))
        job_contents = response.content
        job = job_contents.split("}]")
        f = 0
        for line in job:
            if(branch in line):
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
        HTMLT.write("<tr bgcolor=\"#98AFC7\">\n<th>Team</th>\n<th>Sl.No</th>\n<th>Module</th>\n<th colspan='5' style='border-right: 5px solid #000000'>New_Code</th>\n<b></b><th  colspan='5'>Overall_Code</th>\n</tr>\n")
        HTMLT.write("<tr align=\"center\">\n<th></th><th></th><th></th><th>Coverage</th><th>Duplications</th><th>Bugs</th><th>Vulnerabilities</th><th style='border-right: 5px solid #000000'>Code Smells</th><th>Coverage</th><th>Duplications</th><th>Bugs</th><th>Vulnerabilities</th><th>Code Smells</th>\n</tr>")
        f1 = 1
    
    HTMLT.write("<tr align=\"center\">\n<td rowspan='"+str(len(projects))+"'>"+journey_table_name+"</td>\n")
    HTMLT.close()
    flag = 0
    for project, branch in projects.items():
        print("Gathering the information of "+project)
        headers = {
            'authority': 'sonarqube.lmera.ericsson.se',
            'accept': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
            'x-xsrf-token': 'bqkk43b4oq0r5tgnqog29qdjee',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://sonarqube.lmera.ericsson.se/dashboard?id='+project,
            'accept-language': 'en-US,en;q=0.9',
            'cookie': '_ga=GA1.2.2146927517.1608016603; _fbp=fb.1.1608016603445.191654112; _rdt_uuid=1608016603393.9773df9d-9a68-43c0-8180-84d2ef31231a; XSRF-TOKEN=bqkk43b4oq0r5tgnqog29qdjee; JWT-SESSION=eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJBWGhKb2FVM0ZXSXlNMlp1NDQ0WCIsInN1YiI6ImVzamthZG0xMDAiLCJpYXQiOjE2MTYxNDMwMzMsImV4cCI6MTYxNjQwMzIxMiwibGFzdFJlZnJlc2hUaW1lIjoxNjE2MTQzMDMzNjU1LCJ4c3JmVG9rZW4iOiJicWtrNDNiNG9xMHI1dGducW9nMjlxZGplZSJ9.ZwVgQ8hqyBil4md0Mn54uEd2nJVcUnJWJKdmqI4EG2I',
        }
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
        response = requests.get('https://sonarqube.lmera.ericsson.se/api/measures/search_history', headers=headers, params=params, auth=('113e5fae4d562c6b79bca47a56870206c2cff446', ''))
        job_contents = response.content
        job = job_contents.split("}]")
        
        ###New Code Metrics API#################
        new_response = requests.get('https://sonarqube.lmera.ericsson.se/api/measures/component', headers=headers, params=new_params, auth=('113e5fae4d562c6b79bca47a56870206c2cff446', ''))
        new_job_contents = new_response.content
        new_job = new_job_contents.split("}]")
        
        ##############       
        new_coverage='-'
        status['new_coverage'] = 'ffffff'
        
        coverage='-'
        status['coverage'] = 'ffffff'
         
        new_duplicated='-'
        status['new_duplicated'] = 'ffffff'
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
                  length = len(line.split(":")) - 1
                  coverage = (line.split(":")[length]).strip('""')
                  if(int(float(coverage))<80):
                      status['coverage'] = 'ff751a'
                  else:
                      status['coverage'] = '#a5ff5c'
                  if(project == 'sonarqube-scanner-helpset_stats'):
                      coverage='-'
                      status['coverage'] = 'fffffff'  
           
            if '"metric":"duplicated_lines_density"' in line:
                length = len(line.split(":")) - 1
                duplicated = (line.split(":")[length]).strip('""')
                if(int(float(duplicated))>0):
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
        #New Code Metrics
        #################
        
        for line in new_job: 
            if '"metric":"new_duplicated_lines_density"' in line:
                length = len(line.split(":")) - 2
                initial = line.split(":")[length]
                final = (initial.split(","))
                new_duplicated = (final[0]).strip('""')
                new_duplicated = str(round(float(new_duplicated),1))
                if(int(float(new_duplicated))>0):
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
                if(int(float(new_bugs))>0):
                    status['new_bugs'] = 'ff751a'
                else:
                    status['new_bugs'] = '#a5ff5c'
            
            if '"metric":"new_vulnerabilities"' in line:
                length = len(line.split(":")) - 2
                initial = line.split(":")[length]
                final = (initial.split(","))
                new_vulnerability = (final[0]).strip('""') 
                if(int(float(new_vulnerability))>0):
                    status['new_vulnerability'] = 'ff751a'
                else:
                    status['new_vulnerability'] = '#a5ff5c'
            
            if '"metric":"new_code_smells"' in line:
                length = len(line.split(":")) - 2
                initial = line.split(":")[length]
                final = (initial.split(","))
                new_code_smells = (final[0]).strip('""')
                if(int(float(new_code_smells))>0):
                    status['new_code_smells'] = 'ff751a'
                else:
                    status['new_code_smells'] = '#a5ff5c' 
                                      
            if '"metric":"new_coverage"' in line:
                  length = len(line.split(":")) - 2
                  initial = line.split(":")[length]
                  final = (initial.split(","))
                  new_coverage = (final[0]).strip('""')
                  new_coverage= str(round(float(new_coverage),1))
                  if(int(float(new_coverage))< 80):
                      status['new_coverage'] = 'ff751a'
                      new_coverage= new_coverage+"%"
                  else:
                      status['new_coverage'] = '#a5ff5c'
                      new_coverage= new_coverage+"%" 
        
        #####################################################              
        
        html_table = "sonar.html";
        HTMLT = open (html_table , 'a')
        url = "https://sonarqube.lmera.ericsson.se/dashboard?id="+project
        
        if(flag != 1):
            HTMLT.write("<td style='text-align:center;'>"+str(num)+"</td>\n<td style='text-align:center;color:black'><b><a href=" + url +">"+project.replace('sonarqube-scanner-','')+"</a></b></td>\n<td style='text-align:center;' bgcolor= '"+status['new_coverage']+"'>"+new_coverage+"</td>\n<td style='text-align:center;' bgcolor= '"+status['new_duplicated']+"'>"+new_duplicated+"</td>\n<td style='text-align:center;' bgcolor= '"+status['new_bugs']+"'>"+new_bugs+"</td>\n<td style='text-align:center;' bgcolor= '"+status['new_vulnerability']+"'>"+new_vulnerability+"</td>\n<td style='text-align:center;border-right: 5px solid #000000' bgcolor= '"+status['new_code_smells']+"'>"+new_code_smells+"</td>\n<td style='text-align:center;' bgcolor= '"+status['coverage']+"'>"+coverage+"%</td>\n<td style='text-align:center;' bgcolor= '"+status['duplicated']+"'>"+duplicated+"%</td>\n<td style='text-align:center;' bgcolor= '"+status['bug']+"'>"+bug+"</td>\n<td style='text-align:center;' bgcolor= '"+status['vulnerability']+"'>"+vulnerability+"</td>\n<td style='text-align:center;' bgcolor= '"+status['code_smell']+"'>"+code_smell+"</td>\n</tr>")
            
            num = num + 1
        
        else:
            HTMLT.write("<td style='text-align:center;'>"+str(num)+"</td>\n<td style='text-align:center;color:black'><b><a href=" + url +">"+project.replace('sonarqube-scanner-','')+"</a></b></td>\n<td style='text-align:center;' bgcolor= '"+status['new_coverage']+"'>"+new_coverage+"%</td>\n<td style='text-align:center;' bgcolor= '"+status['new_duplicated']+"'>"+new_duplicated+"%</td>\n<td style='text-align:center;' bgcolor= '"+status['new_bugs']+"'>"+new_bugs+"</td>\n<td style='text-align:center;' bgcolor= '"+status['new_vulnerability']+"'>"+new_vulnerability+"</td>\n<td style='text-align:center;' bgcolor= '"+status['new_code_smells']+"'>"+new_code_smells+"</td>\n<td style='text-align:center;' bgcolor= '"+status['coverage']+"'>"+coverage+"%</td>\n<td style='text-align:center;' bgcolor= '"+status['duplicated']+"'>"+duplicated+"%</td>\n<td style='text-align:center;' bgcolor= '"+status['bug']+"'>"+bug+"</td>\n<td style='text-align:center;' bgcolor= '"+status['vulnerability']+"'>"+vulnerability+"</td>\n<td style='text-align:center;' bgcolor= '"+status['code_smell']+"'>"+code_smell+"</td>\n</tr>")
        HTMLT.close()
        print("Information is gathered for "+project)

#####################################
####Main
#####################################    

platform = ['sonarqube-scanner-3GPP32435','sonarqube-scanner-3GPP32435BCS','sonarqube-scanner-3GPP32435DYN','sonarqube-scanner-adminui','sonarqube-scanner-alarm_module','sonarqube-scanner-alarmcfg','sonarqube-scanner-ascii','sonarqube-scanner-asn1','sonarqube-scanner-BCDParser','sonarqube-scanner-busyhourcfg','sonarqube-scanner-ct','sonarqube-scanner-common','sonarqube-scanner-csexport','sonarqube-scanner-dwhmanager','sonarqube-scanner-Eascii','sonarqube-scanner-ebs','sonarqube-scanner-ebsmanager','sonarqube-scanner-engine','sonarqube-scanner-export','sonarqube-scanner-information_store_parser','sonarqube-scanner-installer','sonarqube-scanner-json','sonarqube-scanner-kpiparser','sonarqube-scanner-licensing','sonarqube-scanner-mdc','sonarqube-scanner-mdc_ccn','sonarqube-scanner-mdc_dyn','sonarqube-scanner-mdc_pc','sonarqube-scanner-mrr','sonarqube-scanner-mediation','sonarqube-scanner-minilink','sonarqube-scanner-monitoring','sonarqube-scanner-nossdb','sonarqube-scanner-parser','sonarqube-scanner-redback','sonarqube-scanner-repository','sonarqube-scanner-sasn','sonarqube-scanner-scheduler','sonarqube-scanner-stfiop','sonarqube-scanner-symboliclinkcreator','sonarqube-scanner-twampm','sonarqube-scanner-twamppt','sonarqube-scanner-twampst','sonarqube-scanner-uncompress','sonarqube-scanner-volte','sonarqube-scanner-diskmanager','sonarqube-scanner-helpset_stats']

infra = [ 'ENIQ_Infra_Spartan']

security =  [ 'ENIQ_Security_Spartan']

nmi = ['nmiinstall']


f1 = 0
f2 = 0
html_table = "sonar.html";
html_table1 = "temp.html";
HTMLT = open (html_table , 'w')
HTMLT.write("<html>\n<head><style>table {border-collapse: collapse;} td, th {border: 1px solid #000000;text-align: center;}</style><center><h2>pEniq SonarQube Analysis Report</h2></center></head>\n<body>")
HTMLT.write("<table align=\"center\"><tr style=\"background-color:#FFFFFF\"><td>\"-\"</td><td>No New Code to analyse</td></tr><tr style=\"background-color:#ff751a\"><td>Amber</td><td>  Did not meet the Gating criteria  </td></tr ><tr style=\"background-color:#a5ff5c\"><td>Green</td><td>Met the Gating criteria</td></tr></table>")
HTMLT.write("<br>")
HTMLT.write("")
HTMLT.close()
HTMLT = open (html_table1 , 'w')
HTMLT.close()
fp1 = open("branch.txt",'r')
l1 = fp1.readlines()
fp1.close()
length = len(l1)




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

        
HTMLT = open (html_table1 , 'r')
contents = HTMLT.readlines()
HTMLT.close()
HTMLT = open (html_table , 'a')
if(f1 != 0):
    HTMLT.write("</center></table>\n")
HTMLT.writelines(contents)
HTMLT.close()
os.system("rm -rf "+html_table1)
