import os
import subprocess
import re

os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/property_files/")
x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')

for etls in list:
        os.chdir("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/property_files/"+etls)
        x=subprocess.Popen('ls | grep properti', stdout=subprocess.PIPE, shell=True)
        out,err = x.communicate()
        out = out.strip()
        list1 = out.split("\n")
        for dir in list1:
		try : 
        		x=subprocess.Popen('cat '+dir+' | grep BaseLine', stdout=subprocess.PIPE, shell=True)
       			out,err = x.communicate()
	        	out = out.strip()
			txts = out.split('\"')
			txt = txts[1]
			rel = txt[6:10]
			ship = txt[10:]
			print rel
			print ship
		except Exception:
			print "Exception"
