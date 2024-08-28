import os
import subprocess

jenkins = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/tp1'
os.chdir("/vobs/eniq/delivery/tp/")
x=subprocess.Popen('ls | grep ml_hc_e_interface', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
#list.remove('ipran_interface')
for pkgs in list:
	os.chdir("/vobs/eniq/delivery/tp/"+pkgs)
	x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
	out,err = x.communicate()
	out = out.strip()
	list1 = out.split('\n')
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
