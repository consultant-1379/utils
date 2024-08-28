import os
import subprocess

name = 'ENIQ_Feature_Files_Linux'  
jenkins = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/' 
vobs = "/vobs/eniq/delivery/tp/"+name
os.chdir('/vobs/eniq/delivery/tp')
x=subprocess.Popen('ls -p '+name+'| grep -v /', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list1 = out.split('\n')
num = list(range(1000))
os.system('mkdir /home/eniqdmt/zsampri/property_files/')
for dir in list1:
        for n in num:
                if (os.path.isfile(vobs+'/'+dir+'@@/main/'+str(n))):
                        os.system('mkdir /home/eniqdmt/zsampri/property_files/'+dir+'_'+str(n))
                        os.system('scp '+vobs+'/'+dir+'@@/main/'+str(n)+' /home/eniqdmt/zsampri/property_files/'+dir+'_'+str(n))
			os.chdir('/home/eniqdmt/zsampri/property_files/'+dir+'_'+str(n))
			os.system('mv '+str(n)+' '+dir)
	#f = open('/home/eniqdmt/zsampri/property_files/'+dir+'_properties','a')
	for n in num:
		if (os.path.isfile(vobs+'/'+dir+'@@/main/'+str(n))):
			f = open('/home/eniqdmt/zsampri/property_files/'+dir+'_'+str(n)+'/'+dir+'_properties','a')
			x=subprocess.Popen('/opt/rational/clearcase/bin/cleartool desc '+vobs+'/'+dir+'@@/main/'+str(n), stdout=subprocess.PIPE, shell=True)
			out,err = x.communicate()
			out = out.strip()
			f.write(out)
			f.write("\n")
			f.write("\n")
	f.close()
#os.system('scp -r /home/eniqdmt/zsampri/property_files esjkadm100@seliiuapp00512:'+jenkins)
#os.system('rm -rf /home/eniqdmt/zsampri/property_files')
