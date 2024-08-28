import os
import subprocess

name = 'CXC'  
jenkins = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/tp/'+name 
vobs="/vobs/eniq/delivery/tp/"+name
os.chdir('/vobs/eniq/delivery/tp/')
x=subprocess.Popen('ls -p '+name+'| grep -v /', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list1 = out.split('\n')
num = list(range(100))
os.system('mkdir /home/eniqdmt/zsampri/property_files/')
for dir in list1:
	f = open('/home/eniqdmt/zsampri/property_files/'+dir+'_properties','a')
	for n in num:
		if (os.path.isfile(vobs+'/'+dir+'@@/main/'+str(n))):
			x=subprocess.Popen('/opt/rational/clearcase/bin/cleartool desc '+vobs+'/'+dir+'@@/main/'+str(n), stdout=subprocess.PIPE, shell=True)
			out,err = x.communicate()
			out = out.strip()
			f.write(out)
			f.write("\n")
			f.write("\n")
	f.close()
os.system('scp /home/eniqdmt/zsampri/property_files/* esjkadm100@seliiuapp00512:'+jenkins)
os.system('rm -rf /home/eniqdmt/zsampri/property_files')
