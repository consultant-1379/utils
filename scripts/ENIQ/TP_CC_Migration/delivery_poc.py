import os
import subprocess

name = 'DC_E_NR.tpi'  
jenkins = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/' 
vobs = "/vobs/dm_eniq/AT_delivery/container"
os.chdir('/vobs/dm_eniq/AT_delivery/container')
x=subprocess.Popen('ls DC_E_NR.tpi', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list1 = out.split('\n')
num = list(range(100))
os.system('mkdir /home/eniqdmt/zsampri/property_files/')
for dir in list1:
        for n in num:
                if (os.path.isfile(vobs+'/'+dir+'@@/main/'+str(n))):
                        os.system('mkdir /home/eniqdmt/zsampri/property_files/'+str(n))
                        os.system('scp '+vobs+'/'+dir+'@@/main/'+str(n)+' /home/eniqdmt/zsampri/property_files/'+str(n))
			os.chdir('/home/eniqdmt/zsampri/property_files/'+str(n))
			os.system('mv '+str(n)+' DC_E_NR.tpi')
	f = open('/home/eniqdmt/zsampri/property_files/'+dir+'_properties','a')
	for n in num:
		if (os.path.isfile(vobs+'/'+dir+'@@/main/'+str(n))):
			f = open('/home/eniqdmt/zsampri/property_files/'+str(n)+'/'+dir+'_properties','a')
			x=subprocess.Popen('/opt/rational/clearcase/bin/cleartool desc '+vobs+'/'+dir+'@@/main/'+str(n), stdout=subprocess.PIPE, shell=True)
			out,err = x.communicate()
			out = out.strip()
			f.write(out)
			f.write("\n")
			f.write("\n")
	f.close()
#os.system('scp -r /home/eniqdmt/zsampri/property_files esjkadm100@seliiuapp00512:'+jenkins)
#os.system('rm -rf /home/eniqdmt/zsampri/property_files')
