import os
import sys
import subprocess

######storing command line arguments in variable########
if len(sys.argv) >= 6:
	zid = sys.argv[1]
        product = sys.argv[2]
        sprint = sys.argv[3]
        release = sys.argv[4]
        rstate = sys.argv[5]
else:
        zid = sys.argv[1]
        product = sys.argv[2]
        branch = sys.argv[3]

#path = "/home/eniqdmt/nmi_git_clone/"+product
os.system("rm -rf /var/tmp/nmi_git/*");
os.chdir("/var/tmp/nmi_git")
os.system("mkdir -p /var/tmp/nmi_git/output/")
os.system("cp /vobs/nfd_eniq/buildit_migration /var/tmp/nmi_git/")

if(product == "sql_anywhere"):
		os.system("curl -O https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/eniq_nmi/"+product+"/"+release+"/"+sprint+"/"+rstate+"/sql_anywhere.tar.gz")
		os.system("tar -xvf sql_anywhere.tar.gz")  
elif(product == "sybase_iq"):
		os.system("curl -O https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/eniq_nmi/"+product+"/"+release+"/"+sprint+"/"+rstate+"/sybase_iq.tar.gz")
		os.system("tar -xvf sybase_iq.tar.gz") 
else:	
		#os.chdir("/home/eniqdmt/")
		os.system("git clone ssh://esjkadm100@gerrit.ericsson.se:29418/OSS/ENIQ-CR-Parent/com.ericsson.eniq.stats.nmi/"+product+" && scp -p -P 29418 esjkadm100@gerrit.ericsson.se:hooks/commit-msg "+product+"/.git/hooks/")
		os.chdir(product)
		os.system("git checkout "+branch)
		#os.system("cp -r /home/eniqdmt/"+product+" /home/eniqdmt/nmi_git_clone")

########removing hidden .git files##########
#os.chdir(path)
#x=subprocess.Popen('find . | grep git', stdout=subprocess.PIPE, shell=True)
#out,err = x.communicate()
#out = out.strip()
#list = out.split('\n')
#print (list)
#for i in list:
        #os.system("rm -rf "+i)
