import os
import sys
import subprocess

jbName = sys.argv[2]
repoName = sys.argv[3]
def cleanup():
        os.chdir("/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+jbName)
        file = open("dependentModule.txt",'r')
        list = file.readlines()
        file.close()
        for i in list:
                os.system("rm -rf "+i)
        os.system("rm -rf dependentModule.txt test "+repoName)
        os.system("rm -rf /proj/eiffel013_config_fem6s11/eiffel_home/slaves/ComputeFarm1/workspace/"+jbName+"/scripts")

build_file_path = sys.argv[1]
os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_172_bkp/"
	
print("/proj/eiffel013_config_fem6s11/tools/ant/bin/ant -buildfile /proj/eiffel013_config_fem6s11/tools/ant_sonar.xml -Dpackage.build.file="+build_file_path+" -Dproject.root=/proj -Dexclude_files='dep_arch/**,build/**,src/**,doc/**,test/**,jar/**,template/**,.classpath,.project' -Dlogname=zmudshu")

os.system("/proj/eiffel013_config_fem6s11/tools/ant/bin/ant -buildfile /proj/eiffel013_config_fem6s11/tools/ant_sonar.xml -Dpackage.build.file="+build_file_path+" -Dproject.root=/proj -Dexclude_files='dep_arch/**,build/**,src/**,doc/**,test/**,jar/**,template/**,.classpath,.project' -Dlogname=zmudshu")

cleanup()

