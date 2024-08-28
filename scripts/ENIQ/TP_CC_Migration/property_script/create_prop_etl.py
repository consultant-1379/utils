import os
import subprocess

jenkins = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/tp1'
os.chdir("/vobs/eniq/delivery/tp/")
x=subprocess.Popen('ls | grep _etl', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
list.remove('udm_etl')
list.remove('ipprobe_etl')
list.remove('erbs_etl')
list.remove('erbsg2_etl')
for pkgs in list:
	os.chdir("/vobs/eniq/delivery/tp/"+pkgs)
	os.system('mkdir -p /home/eniqdmt/zsampri/property_files')
	x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
	out,err = x.communicate()
	out = out.strip()
	list1 = out.split('\n')
        if 'FD' in list1:
                list1.remove('FD')
	for dir in list1:
		x=subprocess.Popen('/opt/rational/clearcase/bin/cleartool desc '+dir, stdout=subprocess.PIPE, shell=True)
                out,err = x.communicate()
                out = out.strip()
		#dir = dir[:dir.index('.')]
       		f = open('/home/eniqdmt/zsampri/property_files/'+dir+'_properties','w')
       		f.write(out)
       		f.close()
       		os.system('cp /home/eniqdmt/zsampri/property_files/'+dir+'_properties '+jenkins+'/'+pkgs)
       		os.system('rm -rf /home/eniqdmt/zsampri/property_files/'+dir+'_properties')
