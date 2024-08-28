import os
import subprocess

jenkins = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/tp'
os.chdir("/vobs/eniq/delivery/tp/group_type_e/")
x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
for dir in list:
	x=subprocess.Popen('/opt/rational/clearcase/bin/cleartool desc '+dir, stdout=subprocess.PIPE, shell=True)
        out,err = x.communicate()
        out = out.strip()
	dir = dir[:dir.index('.')]
       	f = open('/home/eniqdmt/zsampri/property_files/'+dir+'.properties','w')
       	f.write(out)
       	f.close()
       	os.system('cp /home/eniqdmt/zsampri/property_files/'+dir+'.properties '+jenkins+'/group_type_e/')
       	os.system('rm -rf /home/eniqdmt/zsampri/property_files/'+dir+'.properties')
