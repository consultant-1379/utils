'''
Created on Jul 15, 2021
@author: zpunvai
'''

import os
import sys
import base64


######################################
##########GLOBAL VARIABLES############
######################################
ant_file = "/proj/eiffel013_config_fem6s11/tools/ant/bin/ant"
fid = "esjakdm100"
fid_pswrd = base64.b64decode("TmFwbGVzITA1MTI=")

Procus_list = ["3GPP32435DYN_CBA", "3GPP32435DYN_CEE", "3GPP32435DYN_CEE", "3GPP32435DYN_OCC", "3GPP32435ECEParser", "3GPP32435ProCus1", "3GPP32435_CBA", "Bulk_CM_Custom_Parser", "NpPmCustomParser", "SnaPmCustomParser", "CUDBLdif", "GeoRed_FLS", "HXML", "IMXmlParser", "LDAP", "ebinary", "epochascii", "htmltable", "mlxml", "nascii", "omes", "omes2", "parser_test_fwk", "prefix_ascii", "raml", "seqs", "simcfg_procus", "simulator", "split_ascii"]

Parser_list = ["information_store_parser", "kpiparser", "volte", "3GPP32435", "sim", "3GPP32435BCS", "3GPP32435DYN", "ascii", "asn1", "bcd", "csexport", "ct", "ebs", "eascii", "HXMLCsIptnms", "HXMLPsIptnms", "MDC_CCN", "MDC_DYN", "MDC_PC", "MDC", "minilink", "mlxml", "nossdb", "redback", "sasn", "stfiop", "twampm", "twamppt", "twampst", "wifi", "wifiinventory", "xml", "mrr", "parser", "json"]

PF_list = ["AdminUI", "BusyHour", "afj_manager", "alarm", "alarmcfg", "common", "diskmanager", "dwhmanager", "ebsmanager", "engine", "eniq_config", "export", "helpset_stats", "installer", "libs", "licensing", "mediation", "monitoring", "repository", "runtime", "scheduler", "statlibs", "uncompress", "symboliclinkcreator", "techpackide", "dbbaseline"]



######################################################
#######Function To Take Command Line Parameters#######
######################################################
def get_parameters():
	global repo_name
	global branch
	global pkg_name
	global job_name
	global product_num
	global r_state
	global user_id
	global jdk

        repo_name = sys.argv[1]
        branch = sys.argv[2]
        pkg_name = sys.argv[3]
        job_name = sys.argv[4]
        product_num = sys.argv[5]
        r_state = sys.argv[6]
        user_id = sys.argv[7]
        if len(sys.argv) >= 9:
        	jdk = sys.argv[8]
        else:
		jdk = ""
        	print("\njdk version is not selected\n")
	        sys.stdout.flush()



##########################################################
##############Function To Set Build Files#################
##########################################################
def set_build_files(jdk):
	global build_file
	global pkg_build_file
	global exclude_files
	global pkg_dir
	global jar_dir
	global delivery_dir

        build_unsigned = "/proj/eiffel013_config_fem6s11/tools/ant_unsigned.xml"
	build_jar = "/proj/eiffel013_config_fem6s11/tools/ant_build_jar.xml"
        build_sonar = "/proj/eiffel013_config_fem6s11/tools/ant_sonar_build_unsigned.xml"
        if ("21.4" in branch) and ("CONSOLIDATION" not in branch):
                if pkg_name in PF_list:
                        if jdk == "jdk11":
                                build_file = build_sonar
                        if jdk == "jdk1.8":
                                build_file = build_jar
                elif pkg_name == "parser":
                        if jdk == "jdk11":
                                build_file = build_jar
                        if jdk == "jdk1.8":
                                build_file = build_sonar
                else:
                        build_file = build_sonar
        elif ("21.4" in branch) and ("CONSOLIDATION" in branch):
		if pkg_name in PF_list:
                        if jdk == "jdk11":
                                build_file = build_unsigned
                        if jdk == "jdk1.8":
                                build_file = build_jar
                elif pkg_name == "parser":
                        if jdk == "jdk11":
                                build_file = build_jar
                        if jdk == "jdk1.8":
                                build_file = build_unsigned
                else:
                        build_file = build_unsigned
	else:
		if "CONSOLIDATION" not in branch:
                        build_file = build_sonar
                else:
                        build_file = build_unsigned

        if ("21.4" in branch) and (pkg_name in PF_list or pkg_name == "parser"):
                jar_dir = "/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+job_name+"/"+repo_name+"/build/"+repo_name+"/"+jdk
        else:
                jar_dir = "/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+job_name+"/"+repo_name+"/build/"+repo_name

        ant_file = "/proj/eiffel013_config_fem6s11/tools/ant/bin/ant"
        pkg_build_file = "/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+job_name+"/"+repo_name+"/dev/build/build.xml"
	cmd_to_change_jdk_folder = "sed -i 's/<property name=\"jar.folder\".*/<property name=\"jar.folder\" value=\""+jdk+"\"\/>/g\' "+pkg_build_file
	os.system(cmd_to_change_jdk_folder)
		
        exclude_files = "dep_arch/**,build/**,src/**,doc/**,test/**,jar/**,template/**,.classpath,.project,**/.gitkeep,**/.scannerwork/**"
        pkg_dir = "/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+job_name+"/"+repo_name+"/dev"

        os.system("rm -rf /proj/eiffel013_config_fem6s11/buildPackage/"+repo_name)
        os.system("mkdir /proj/eiffel013_config_fem6s11/buildPackage/"+repo_name)
        delivery_dir = "/proj/eiffel013_config_fem6s11/buildPackage/"+repo_name
        if (pkg_name == "runtime") and ("18." not in branch):
		pkg_build_file = "/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+job_name+"/"+repo_name+"/dev/build/build_linux.xml"


        #############Printing files which will use for building Package################
        print("\n\nPackage : "+pkg_name)
        print("Product Number : "+product_num)
        print("r_state : "+r_state)
        print("Label : "+product_num+"-"+r_state)
        print("Branch : "+branch)
        print("User : esjkadm100")
        print("Build XML File : "+build_file)
        print("Jar Directory : "+jar_dir)
        print("Package Directory : "+pkg_dir)
        print("Delivery Directory : "+delivery_dir)
        print("Excluded Files : "+exclude_files)
	print("JAR Folder: "+jdk)
        sys.stdout.flush()



###############################################################
###############Functin to set JAVA_HOME path ##################
###############################################################
def setJavaPath():
        if (jdk == "jdk11"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk-11.0.11"

        elif (pkg_name in Parser_list) or (jdk == "jdk1.8") or (branch ==  "Linux") or (branch ==  "Standalone"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_172_bkp"

        elif (branch ==  "Solaris"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_152_bkp"

        elif branch == "21.4.5_Linux" or branch == "21.4.6_Linux" or branch == "21.4.7_Linux" or branch == "21.4.8_Linux" :
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk-11.0.11"

        elif (branch == "21.4.4_Linux") or (branch == "21.4.3_Linux") or (branch == "21.4.2_Linux"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_172_bkp"

        elif (branch == "21.2_CONSOLIDATION") or (branch == "21.2.8_Linux")or (branch == "21.2.7_Linux")or(branch == "21.2.6_Linux")or(branch == "21.2.5_Linux")or(branch == "21.2.4_Linux") or (branch == "21.2.3_Linux") or (branch == "21.2.2_Linux") or (branch == "21.2.1_Linux"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_172_bkp"

        elif (branch == "20.4_CONSOLIDATION") or (branch == "20.4.9_Linux") or (branch == "20.4.8_Linux")or (branch == "20.4.7_Linux")or(branch == "20.4.6_Linux")or(branch == "20.4.5_Linux")or(branch == "20.4.4_Linux") or (branch == "20.4.3_Linux") or (branch == "20.4.2_Linux") or (branch == "20.4.1_Linux"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_172_bkp"

        elif (branch == "20.2_CONSOLIDATION") or (branch == "20.2.8_Linux")or (branch == "20.2.7_Linux")or(branch == "20.2.6_Linux")or(branch == "20.2.5_Linux")or(branch == "20.2.4_Linux") or (branch == "20.2.3_Linux") or (branch == "20.2.2_Linux") or (branch == "20.2.1_Linux"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_172_bkp"

        elif (branch == "19.4_CONSOLIDATION") or (branch == "19.4.9_Linux") or (branch == "19.4.8_Linux")or (branch == "19.4.7_Linux")or(branch == "19.4.6_Linux")or(branch == "19.4.5_Linux")or(branch == "19.4.4_Linux") or (branch == "19.4.3_Linux") or (branch == "19.4.2") or (branch == "19.4.1"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_172_bkp"
                print("java_home path: "+os.environ["JAVA_HOME"])

        elif (branch == "19.2_CONSOLIDATION") or (branch == "19.2.13_Linux") or (branch == "19.2.12")or (branch == "19.2.11")or(branch == "19.2.10")or(branch == "19.2.9")or(branch == "19.2.8") or (branch == "19.2.7") or (branch == "19.2.6") or (branch == "19.2.5") or (branch == "19.2.4") or (branch=="19.2.3") or (branch=="19.2.2"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_172_bkp"

        elif (branch == "18.4.2") or (branch == "18.2.8.EU1") or (branch == "18.2_CONSOLIDATION") or (branch == "eniq_stats_18b_18.2.8.eu2_hot_ec") or (branch == "eniq_stats_rhel") or (branch == "18.2.6") or (branch == "18.2.7") or (branch == "18.2.8") or (branch == "priv_eqev_49562") or (branch == "eqev_41277_enm"):
                if pkg_name in Parser_list:
                        if ( jdk == "jdk1.7"):
                                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.7.0_141_bkp"
                        if ( jdk == "jdk1.8"):
                                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_152_bkp"
                else:
                        os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_152_bkp"

        elif (branch == "18.4.2") or (branch == "18.2.2") or (branch == "18.2.6") or (branch == "18.2.7") or (branch == "18.2.8") or (branch == "18.2.8.EU1") or (branch == "18.2_CONSOLIDATION") or (branch == "eniq_stats_18b_18.2.8.eu2_hot_ec") or (branch == "eniq_stats_rhel") or (branch == "18.2.6") or (branch == "18.2.7") or (branch == "18.2.8") or (branch == "priv_eqev_49562") or (branch == "eqev_41277_enm"):
                if pkg_name in Parser_list:
                        os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.7.0_141_bkp"
                else:
                        os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_152_bkp"

        elif (branch == "18.2.5") or (branch == "18.2.4"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_172_bkp"

        elif (branch == "18.0.6") or (branch == "18.0.7"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.7.0_141_bkp"

        elif (branch == "16.2_CONSOLIDATION") or (branch == "16.0_CONSOLIDATION"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.7.0_80_Linux"

        if (branch == "18.2.2") and (pkg_name == "diskmanager"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_131_new/jdk1.8.0_131"

        print ('Final JAVA_HOME path: '+os.environ["JAVA_HOME"])
        sys.stdout.flush()



######################################################
############Function to Build the Package#############
######################################################
def buildPackage():
        buildCommand = ant_file+" -v -buildfile "+build_file+" -Dpackage.build.file="+pkg_build_file+" -Dbuild.label="+product_num+"-"+r_state+" -Dbuild.revision="+r_state+" -Dproject.root=/proj -Dexclude_files="+exclude_files+" -Dproduct.number="+product_num+" -Dlogname=esjkadm100 -Dpackage_dir="+pkg_dir+" -Dpackage="+pkg_name+" -Djar_dir="+jar_dir+" -Ddelivery_dir="+delivery_dir+" -Djobname="+job_name+" -Dbranch="+branch
        print("\n\nRunning build command : "+buildCommand)
        sys.stdout.flush()
        os.system(buildCommand)



############################################################################################################
##################Function to delete files created during build before pushing to git ######################
############################################################################################################
def deletingExtraFiles():
        os.system("mkdir /proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+job_name+"/test/")
        os.chdir("/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+job_name+"/test/")
        if repo_name in Procus_list:
                os.system("git clone ssh://esjkadm100@gerrit.ericsson.se:29418/OSS/ENIQ-CR-Parent/com.ericsson.eniq.stats.procus/"+repo_name+" && scp -p -P 29418 esjkadm100@gerrit.ericsson.se:hooks/commit-msg "+repo_name+"/.git/hooks/")
        else:
                os.system("git clone ssh://esjkadm100@gerrit.ericsson.se:29418/OSS/ENIQ-CR-Parent/com.ericsson.eniq.stats.plat/"+repo_name+" && scp -p -P 29418 esjkadm100@gerrit.ericsson.se:hooks/commit-msg "+repo_name+"/.git/hooks/")
        os.chdir(repo_name)
        os.system("git checkout "+branch)
        os.system("python /proj/eiffel013_config_fem6s11/tools/file_difference_build.py /proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+job_name+"/test/"+repo_name+"/dev /proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+job_name+"/"+repo_name+"/dev")
	os.system("rm -rf /proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+job_name+"/test/")



#################################################################################################
######################Function to push the code to git with latest tag###########################
#################################################################################################
def gitPush():
		os.chdir("/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+job_name+"/"+repo_name)
                cmd = "git add build/"+repo_name+"/ dev/build/"
		os.system(cmd)
                os.system("git commit -m \"update buildnumber and Jar File\"")
                os.system("git push origin "+branch)
                os.system("git tag -a "+product_num+"-"+r_state+" -m \""+product_num+"-"+r_state+" label is used\"")
                os.system("git push origin "+product_num+"-"+r_state)



#########################################################################
################Function To Upload Package To Nexus######################
#########################################################################
def nexusUpload():
        os.chdir(delivery_dir)
        Package =  os.listdir(delivery_dir)
        Package = Package[0].strip()

        if repo_name in Procus_list:
            os.system("curl -v -u esjkadm100:"+fid_pswrd+" --upload-file "+Package+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/eniq_platform/Procus/"+branch+ "/" +Package)
        else:
            os.system("curl -v -u esjkadm100:"+fid_pswrd+" --upload-file "+Package+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/eniq_platform/Packages/"+branch+ "/" +Package)
        print "\n\n*****************************"+Package+" uploaded to nexus************************************\n"

        if ( "21.4" in branch ):
            os.chdir(delivery_dir)
            os.system("cp "+Package+" /proj/eiffel013_config_fem5s11/eiffel_home/FULL_PF_KGB_DATA/Pkg_List")
            os.system("cp "+Package+" /proj/eiffel013_config_fem5s11/eiffel_home/ALL_PF_KGB_DATA/Pkg_List")

            file = Package[0:Package.index('.')]
            os.chdir("/proj/eiffel013_config_fem5s11/eiffel_home/FULL_PF_KGB_DATA/Pkg_List")
            f= open(file+".txt","w+")
            f.writelines("SHIPMENT="+branch+"\n")
            f.writelines("user_id="+user_id)
            f.close()
            os.system("cp "+file+".txt /proj/eiffel013_config_fem5s11/eiffel_home/ALL_PF_KGB_DATA/Pkg_List")



###########################################################
#############Function to cleanup clonned repos#############
###########################################################
def cleanup():
        os.chdir("/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+job_name)
        file = open("dependentModule.txt",'r')
        list = file.readlines()
        file.close()
        for i in list:
                os.system("rm -rf "+i)
        os.system("rm -rf dependentModule.txt test "+repo_name)
        os.system("rm -rf /proj/eiffel013_config_fem6s11/eiffel_home/slaves/ComputeFarm1/workspace/"+job_name+"/scripts")



#############################################################
##############Main Script - Calling Functions################
#############################################################
get_parameters()
if "21.4" in branch:
        if pkg_name in PF_list:
                jdk = "jdk11"
        else:
                jdk = "jdk1.8"
set_build_files(jdk)
setJavaPath()
buildPackage()
deletingExtraFiles()
nexusUpload()

#######building only for dependent jar########
if ("21.4" in branch) and (pkg_name in PF_list or pkg_name == "parser"):
	print("#" * 60)
	print("Building Dependent JAR")
	print("#" * 60)
        if pkg_name in PF_list:
                jdk = "jdk1.8"
        else:
                jdk = "jdk11"
        set_build_files(jdk)
        setJavaPath()
        buildPackage()
        deletingExtraFiles()

######git push and cleanup temporary directories###########
gitPush()
cleanup()
