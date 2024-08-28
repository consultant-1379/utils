import os
import subprocess

jenkins = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/tp1'
os.chdir("/vobs/eniq/delivery/tp")
x=subprocess.Popen('ls | grep _etl', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
list.remove('udm_etl')
list.remove('ipprobe_etl')
list.remove('erbs_etl')
list.remove('erbsg2_etl')
os.system('mkdir -p /home/eniqdmt/zsampri/property_files')
for etls in list:
	os.chdir("/vobs/eniq/delivery/tp/"+etls)
	if (os.path.isdir("FD")):
		x=subprocess.Popen('find FD -type f', stdout=subprocess.PIPE, shell=True)
		out,err = x.communicate()
		out = out.strip()
		list1 = out.split("\n")
		for dir in list1:
            		pkgs = dir[dir.rindex('/')+1:]
            		pkg = pkgs[:pkgs.index('.')]
            		path = dir[0:dir.rindex('/')]
            		if 'Manual' in dir:
               			dir = 'FD/Manual\ Modification/'+pkgs
            		if 'Manual' in path:
                		path = 'FD/Manual\ Modification/'
            		x=subprocess.Popen('/opt/rational/clearcase/bin/cleartool desc '+dir, stdout=subprocess.PIPE, shell=True)
			out,err = x.communicate()
			out = out.strip()
           		f = open('/home/eniqdmt/zsampri/property_files/'+pkgs+'_properties','w')
            		f.write(out)
            		f.close()
            		os.system('cp /home/eniqdmt/zsampri/property_files/'+pkgs+'_properties '+jenkins+'/'+etls+'/'+path)
            		os.system('rm -rf /home/eniqdmt/zsampri/property_files/'+pkgs+'_properties')
