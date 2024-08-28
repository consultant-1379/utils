import os
import subprocess

jenkins = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/tp1'
os.chdir("/vobs/eniq/delivery/tp")
x=subprocess.Popen('ls | grep ipprobe_etl', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
#list.remove("ipprobe_etl")
#list.remove("iptransport_etl")
#list.remove("udm_etl")
#list.remove("erbsg2_etl")
#list.remove('erbs_etl')
#list.remove("Manual Modifications")
for etls in list:
	os.chdir("/vobs/eniq/delivery/tp/"+etls)
	if (os.path.isdir("FD")):
	    x=subprocess.Popen('find TWAMP_doc.mkelem -type f', stdout=subprocess.PIPE, shell=True)
	    out,err = x.communicate()
	    out = out.strip()
	    list1 = out.split("\n")
	    for dir in list1:
            	pkgs = dir[dir.rindex('/')+1:]
            	pkg = pkgs[:pkgs.index('.')]
            	path = dir[0:dir.rindex('/')]
            	if 'EIN_team_doc_for_configuring_IPPROBE' in dir:
               		dir = 'TWAMP_doc.mkelem/EIN_team_doc_for_configuring_IPPROBE/'+pkgs
            	if 'EIN_team_doc_for_configuring_IPPROBE' in path:
                	path = 'TWAMP_doc.mkelem/EIN_team_doc_for_configuring_IPPROBE/'
                if 'ENIQ_test_doc' in dir:
                        dir = 'TWAMP_doc.mkelem/ENIQ_test_doc/'+pkgs
                if 'ENIQ_test_doc' in path:
                        path = 'TWAMP_doc.mkelem/ENIQ_test_doc/'
                if 'OSS_RC_Doc' in dir:
                        dir = 'TWAMP_doc.mkelem/OSS_RC_Doc/'+pkgs
                if 'OSS_RC_Doc' in path:
                        path = 'TWAMP_doc.mkelem/OSS_RC_Doc/'
                if 'TWAMP_documentation' in dir:
                        dir = 'TWAMP_doc.mkelem/TWAMP_documentation/'+pkgs
                if 'TWAMP_documentation' in path:
                        path = 'TWAMP_doc.mkelem/TWAMP_documentation/'
                if 'TWAMP_simulator' in dir:
                        dir = 'TWAMP_doc.mkelem/TWAMP_simulator/'+pkgs
                if 'TWAMP_simulator' in path:
                        path = 'TWAMP_doc.mkelem/TWAMP_simulator/'
                if 'TWAMP_Proper_simulated_files' in dir:
                        dir = 'TWAMP_doc.mkelem/TWAMP_Proper_simulated_files/'+pkgs
                if 'TWAMP_Proper_simulated_files' in path:
                        path = 'TWAMP_doc.mkelem/TWAMP_Proper_simulated_files/'
            	x=subprocess.Popen('/opt/rational/clearcase/bin/cleartool desc '+dir, stdout=subprocess.PIPE, shell=True)
	    	out,err = x.communicate()
	    	out = out.strip()
            	f = open('/home/eniqdmt/zsampri/property_files/'+pkgs+'_properties','w')
            	f.write(out)
            	f.close()
            	os.system('cp /home/eniqdmt/zsampri/property_files/'+pkgs+'_properties '+jenkins+'/'+etls+'/'+path)
            	os.system('rm -rf /home/eniqdmt/zsampri/property_files/'+pkgs+'_properties')
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
	
