import os
import datetime
import sys
from  config_19_4 import *
import subprocess

vobs_dir = "/vobs/dm_eniq/AT_delivery/container"
infra_dir = "/vobs/dm_eniq/AT_delivery/infra_container"
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
day_no = datetime.datetime.today().weekday()
weekday = weekdays[day_no]
today = datetime.datetime.now().strftime ("%d-%m-%Y")
today1 = datetime.datetime.now().strftime ("%b %d")
today2 = datetime.datetime.now().strftime ("%d-%b-%y")
year = int(datetime.datetime.now().strftime ("%Y"))
month = int(datetime.datetime.now().strftime ("%m"))
day = int(datetime.datetime.now().strftime ("%d"))
if len(str(day)) == 1:
	 today1 = datetime.datetime.now().strftime ("%b  ")+str(day)
else:
	 today1 = datetime.datetime.now().strftime ("%b ")+str(day)
# today = '16-02-2020'
# today1 = "Feb 16"
# today2 = "16-Feb-20"
# week = datetime.date(2020,2,16).isocalendar()[1]
week = datetime.date(year,month,day).isocalendar()[1]
check_dir = "/vobs/eniq/delivery/"
nmi_dir = "/vobs/nfd_eniq/"
nmi_paths = ["install", "Packages_INC","NASd","bootstrap","sentinel","sql_anywhere","sybase_iq"]

today1 =  "'"+today1+"'"
pf_pkgs = []
techpacks = []
reports = []
nmi_deliveries = []

def checkins_count(name):
	checkins = str(os.popen("cleartool lshistory  -since "+today2+" -fmt '\"%Nd\" \"%u\" \"%En\" \"%Vn\" \"%e\" \"%o\" \n%c\n' -nco " + check_dir + name).read())
	return checkins.count('checkin')

def nmi_checkins_count(name):
	checkins = str(os.popen("cleartool lshistory  -since "+today2+" -fmt '\"%Nd\" \"%u\" \"%En\" \"%Vn\" \"%e\" \"%o\" \n%c\n' -nco " + nmi_dir + name).read())
	return checkins.count('checkin')
	
def infra_checkins_count():
	os.chdir('/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/infra_spartan_19_4/infra_spartan')
	p = subprocess.Popen("git rev-list --since=%s origin/%s | wc -l" %(today2,sys.argv[1]), stdout=subprocess.PIPE, shell=True)
	count = p.stdout.read().strip()
	return int(count)

def integrate(template):

	f = open (template,'r')
	contents = f.readlines()
	f.close()

	for index,line in enumerate(contents):
		if "Date Start" in line:
			contents[index+1] = "labels: ["+ ",".join([ "'" + str(x) + "'" for x in date ]) +"],\n"
		elif "Techpack_data Start" in line:
			contents[index+1] = "data: ["+ ",".join([str(x) for x in tp_data]) +"],\n"
		elif "Platform_data Start" in line:
			contents[index+1] = "data: ["+ ",".join([str(x) for x in pf_data]) +"],\n"
		elif "Infra_data Start" in line:
			contents[index+1] = "data: ["+ ",".join([str(x) for x in infra_data]) +"],\n"
		elif "Kpi_data Start" in line:
			contents[index+1] = "data: ["+ ",".join([str(x) for x in kpi_data]) +"],\n"
		elif "Nmi_data Start" in line:
			contents[index+1] = "data: ["+ ",".join([str(x) for x in nmi_data]) +"],\n"
			
		elif "Techpack_checkin Start" in line :
			contents[index+1] = "data: ["+ ",".join([str(x) for x in tp_checkins_data]) +"],\n"
		elif "Platform_checkin Start" in line :
			contents[index+1] = "data: ["+ ",".join([str(x) for x in pf_checkins_data]) +"],\n"
		elif  "Kpi_checkin Start" in line :
			contents[index+1] = "data: ["+ ",".join([str(x) for x in kpi_checkins_data]) +"],\n"
		elif "Week no" in line:
			contents[index] = '<h2 align="center"> Metrics for Week '+ str(week) +'</h2> <!-- Week no --> \n'
		elif "Nmi_checkin Start" in line:
			contents[index+1] = "data: ["+ ",".join([str(x) for x in nmi_checkins_data]) +"],\n"
		elif "Team links" in line:
			contents[index] = '<div style="float:right; padding-top:80px;"><font size="4"><a href="http://eniqdmt.lmera.ericsson.se/teamwise_commits_'+sys.argv[1]+'.html"> For Team-wise Commits Click Here </a> </br> </br><a href="http://eniqdmt.lmera.ericsson.se/teamwise_deliveries_'+sys.argv[1]+'.html"> For Team-wise Deliveries Click Here</a></font></div><!-- Team links -->'
		elif "Main Page link" in line:
			contents[index] = '<a href="http://eniqdmt.lmera.ericsson.se/overall_metrics_'+sys.argv[1]+'.html"> Back to Main Page </a> <!-- Main Page link -->'
		elif "Shipment" in line:
			contents[index] = '<h2 align="center"> '+sys.argv[1]+' </h2>  <!-- Shipment -->'
		elif "Infra_checkin Start" in line:
			contents[index+1] = "data: ["+ ",".join([str(x) for x in infra_checkins_data]) +"],\n"
			
	f = open (template,'w+')			
	f.writelines(contents)
	f.close()
	
pkgs = os.popen("find "+vobs_dir+" -type f -ls | grep "+today1+" | awk '{print $11}'").read()
infra_pkgs = os.popen("find "+infra_dir+" -type f -ls | grep "+today1+" | awk '{print $11}'").read()
pkglist = pkgs.strip().split("\n")
if len(infra_pkgs) is not 0:
	infra_pkgs = infra_pkgs.strip().split("\n") 
for pkg in pkglist:
	ship = os.popen("cleartool desc " +pkg +" | grep BaseLine").read()
	if sys.argv[2] in ship :
		desc = os.popen("cleartool desc " + pkg +" | grep DeSc").read()
		if 'eniq_sw' in desc:
			pf_pkgs.append(pkg)
		if 'eniq_techpacks' in desc:
			techpacks.append(pkg)
		if 'eniq_reports' in desc:
			reports.append(pkg)
		if 'install' in desc or 'applications' in desc or 'bootstrap' in desc:
			nmi_deliveries.append(pkg)
		
tps = len(techpacks)
infra_len = len(infra_pkgs)
pf_len = len(pf_pkgs)
rep_len = len(reports)
nmi_del_len = len(nmi_deliveries)
today_present = False	
tp_checkins = checkins_count('tp')
pf_checkins = checkins_count('plat')
kpi_checkins = checkins_count('kpi')
#infra_checkins = infra_checkins_count()
nmi_checkins = sum([nmi_checkins_count(path) for path in nmi_paths])
total_checkins = tp_checkins + pf_checkins + kpi_checkins

if today in date:
	today_present = True
	tp_data[-1] = tps
	pf_data[-1] = pf_len
	infra_data[-1] = infra_len
	kpi_data[-1] = rep_len
	nmi_data[-1] = nmi_del_len
	tp_checkins_data[-1] = tp_checkins
	pf_checkins_data[-1] = pf_checkins
	kpi_checkins_data[-1] = kpi_checkins
	nmi_checkins_data[-1] = nmi_checkins
	#infra_checkins_data[-1] = infra_checkins

else:
	date.append(str(today))
	tp_data.append( tps )
	pf_data.append (pf_len)
	infra_data.append ( infra_len)
	kpi_data.append (rep_len)
	nmi_data.append(nmi_del_len)
	tp_checkins_data.append(tp_checkins)
	pf_checkins_data.append(pf_checkins)
	kpi_checkins_data.append(kpi_checkins)
	nmi_checkins_data.append(nmi_checkins)
	#infra_checkins_data.append(infra_checkins)
	
if weekday == "Sunday":
	if "WEEK1 END" in date:
		if "WEEK2 END" in date:
			date.append("WEEK3 END")
		else:
			date.append("WEEK2 END")
	else:
		date.append("WEEK1 END")
	tp_data.append(0)
	pf_data.append (0)
	infra_data.append (0)
	kpi_data.append (0)
	nmi_data.append(0)
	tp_checkins_data.append(0)
	pf_checkins_data.append(0)
	kpi_checkins_data.append(0)
	nmi_checkins_data.append(0)
	infra_checkins_data.append(0)


f = open("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/config_19_4.py","w+")
f.write("date=[" + ",".join([ "'" + str(x) + "'" for x in date ]) + "]" + os.linesep)
f.write("tp_data=[" + ",".join([str(x) for x in tp_data ]) + "]" + os.linesep)
f.write("pf_data=[" + ",".join([str(x) for x in pf_data ]) + "]" + os.linesep)
f.write("infra_data=[" + ",".join([str(x) for x in infra_data ]) + "]" + os.linesep)
f.write("kpi_data=[" + ",".join([str(x) for x in kpi_data ]) + "]" + os.linesep)
f.write("nmi_data=["+ ",".join([str(x) for x in nmi_data ]) + "]" + os.linesep)

f.write("tp_checkins_data=[" + ",".join([str(x) for x in tp_checkins_data ]) + "]" + os.linesep)
f.write("pf_checkins_data=[" + ",".join([str(x) for x in pf_checkins_data ]) + "]" + os.linesep)
f.write("kpi_checkins_data=[" + ",".join([str(x) for x in kpi_checkins_data ]) + "]" + os.linesep)
f.write("nmi_checkins_data=[" + ",".join([str(x) for x in nmi_checkins_data ]) + "]" + os.linesep)
f.write("infra_checkins_data=[" + ",".join([str(x) for x in infra_checkins_data ]) + "]" + os.linesep)

f.close()

f = open("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/graph_template_19_4.html",'r')
content = f.read()
f1 = open("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/overall_metrics_"+sys.argv[1]+".html",'w')
f1.write(content)
f.close()
f1.close()

f = open("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/graph_template_team_19_4.html",'r')
content = f.read()
f1 = open("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/teamwise_deliveries_"+sys.argv[1]+".html",'w')
f1.write(content)
f.close()
f1.close()

f = open("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/graph_template_checkins_team_19_4.html",'r')
content = f.read()
f1 = open("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/teamwise_commits_"+sys.argv[1]+".html",'w')
f1.write(content)
f.close()
f1.close()

integrate("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/overall_metrics_"+sys.argv[1]+".html")
integrate("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/teamwise_deliveries_"+sys.argv[1]+".html")
integrate("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/teamwise_commits_"+sys.argv[1]+".html")


