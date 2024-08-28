import os
import subprocess

jenkins = '/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/git_work/tp'
os.chdir("/vobs/eniq/delivery/tp")
x=subprocess.Popen('ls | grep dim', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
for etls in list:
        os.chdir("/vobs/eniq/delivery/tp/"+etls)
        x=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
        out,err = x.communicate()
        out = out.strip()
        list1 = out.split("\n")
        if 'FD' in list1:
                list1.remove('FD')
        for dir in list1:
                x=subprocess.Popen('/opt/rational/clearcase/bin/cleartool desc '+dir, stdout=subprocess.PIPE, shell=True)
                out,err = x.communicate()
                out = out.strip()
                f = open('/home/eniqdmt/zsampri/property_files/'+dir+'_properties','w')
                f.write(out)
                f.close()
                os.system('cp /home/eniqdmt/zsampri/property_files/'+dir+'_properties '+jenkins+'/'+etls)
                os.system('rm -rf /home/eniqdmt/zsampri/property_files/'+dir+'_properties')

