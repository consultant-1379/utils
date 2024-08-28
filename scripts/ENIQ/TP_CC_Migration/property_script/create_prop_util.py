import os
import subprocess

jenkins = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/tp'
os.chdir("/vobs/eniq/delivery/tp/")
x=subprocess.Popen('find util -type f', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list1 = out.split("\n")
for dir in list1:
        pkgs = dir[dir.rindex('/')+1:]
        pkg = pkgs[:pkgs.index('.')]
        path = dir[0:dir.rindex('/')]
        x=subprocess.Popen('/opt/rational/clearcase/bin/cleartool desc '+dir, stdout=subprocess.PIPE, shell=True)
	out,err = x.communicate()
	out = out.strip()
        f = open('/home/eniqdmt/zsampri/property_files/'+pkgs+'_properties','w')
        f.write(out)
        f.close()
        os.system('cp /home/eniqdmt/zsampri/property_files/'+pkgs+'_properties '+jenkins+'/'+path)
        os.system('rm -rf /home/eniqdmt/zsampri/property_files/'+pkgs+'_properties')
