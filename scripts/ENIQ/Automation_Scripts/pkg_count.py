import os
import subprocess
import re
import sys
import requests
import base64
#from bs4 import BeautifulSoup
import random
from datetime import datetime, timedelta, date
import calendar

ship = sys.argv[1]
rels = "ENIQ_S"+ship.split('.')[0]+"."+ship.split('.')[1]
reli = "ENIQ_I"+ship.split('.')[0]+"."+ship.split('.')[1]
shipi = ship.split('_')[0]
#ship = "21.2.6_Linux"
# today1 = "Jun 17"
# today = "17/06"
delv=0
days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
yesterday = date.today() - timedelta(days=1)
mont = yesterday.strftime("%b")
today1 = yesterday.strftime("%b %d")
today = yesterday.strftime("%d/%m")
year = int(yesterday.strftime("%y"))
mon = int(yesterday.strftime("%m"))
day = int(yesterday.strftime("%d"))
day_week = days[calendar.weekday(year,mon,day)]

#os.chdir("/vobs/dm_eniq/AT_delivery/container")
if day_week == "Monday":
        f = open("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/package_details.txt",'w')
else:
        f = open("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/metrics/package_details.txt",'a')
x=subprocess.Popen('ls -ltr /view/eniq_delta_bld_'+rels+'_'+ship+'/vobs/dm_eniq/AT_delivery/container/ | grep -v directory | grep '+mont, stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
if len(list) > 0 and out != '':
	for line in list:
        	pkgs = line.split(' ')
        	if pkgs[len(pkgs)-3] == str(day):
                	pkg = pkgs[len(pkgs)-1]
                	x=subprocess.Popen('/opt/rational/clearcase/bin/cleartool desc /view/eniq_delta_bld_'+rels+'_'+ship+'/vobs/dm_eniq/AT_delivery/container/'+pkg+' | grep -i BaseLine', stdout=subprocess.PIPE, shell=True)
                	out,err = x.communicate()
                	out = out.strip()
                	if ship.lower() in out:
                        	delv += 1;
#os.chdir("/vobs/dm_eniq/AT_delivery/infra_container")
x=subprocess.Popen('ls -ltr /view/eniq_bld_'+reli+'_'+shipi+'/vobs/dm_eniq/AT_delivery/infra_container/ | grep -v directory | grep '+mont, stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list1 = out.split('\n')
if len(list1) > 0 and out != '':
	for line in list:
        	pkgs = line.split(' ')
        	if pkgs[len(pkgs)-3] == str(day):
                	pkg = pkgs[len(pkgs)-1]
                	x=subprocess.Popen('/opt/rational/clearcase/bin/cleartool desc /view/eniq_bld_'+reli+'_'+shipi+'/vobs/dm_eniq/AT_delivery/infra_container/'+pkg+' | grep -i BaseLine', stdout=subprocess.PIPE, shell=True)
                	out,err = x.communicate()
                	out = out.strip()
                	if shipi.lower() in out:
                        	delv += 1;
print("Now of packages delivered on "+str(mont)+" "+str(day)+" : "+str(delv))
f.write(day_week+"::"+str(delv)+'\n')
f.close()
