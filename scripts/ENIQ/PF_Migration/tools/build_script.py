import os
import sys

##########storing command line arguments in variable###########
repoName = sys.argv[1]
branch = sys.argv[2]
pkg = sys.argv[3]
jbName = sys.argv[4]
productNo = sys.argv[5]
Rstate = sys.argv[6]
xid = sys.argv[7]
jdk =""
if len(sys.argv) >= 9:
        jdk = sys.argv[8]
else:
        print("\njdk version is not selected\n")
        sys.stdout.flush()
flag =""


#########################Files used for building package############################
antfile = "/proj/eiffel013_config_fem6s11/tools/ant/bin/ant"
buildFile = "/proj/eiffel013_config_fem6s11/tools/ant_unsigned.xml"
if ("CONSOLIDATION" not in branch) and ("Parser_Build" not in branch):
        buildFile = "/proj/eiffel013_config_fem6s11/tools/ant_sonar_build_unsigned.xml"
pkgBuildFile = "/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+jbName+"/"+repoName+"/dev/build/build.xml"
excludeFiles = "dep_arch/**,build/**,src/**,doc/**,test/**,jar/**,template/**,.classpath,.project,**/.gitkeep,**/.scannerwork/**"
pkgDir = "/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+jbName+"/"+repoName+"/dev"
jarDir = "/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+jbName+"/"+repoName+"/build/"+repoName
os.system("rm -rf /proj/eiffel013_config_fem6s11/buildPackage/"+repoName)
os.system("mkdir /proj/eiffel013_config_fem6s11/buildPackage/"+repoName)
deliveryDir = "/proj/eiffel013_config_fem6s11/buildPackage/"+repoName
if (pkg == "runtime") and ("18." not in branch):
                pkgBuildFile = "/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+jbName+"/"+repoName+"/dev/build/build_linux.xml"

                
#####################Printing files which will use for building Package############################
print("\n\nPackage : "+pkg)
print("Product Number : "+productNo)
print("RState : "+Rstate)
print("Label : "+productNo+"-"+Rstate)
print("Branch : "+branch)
print("User : esjkadm100")
print("Build XML File : "+buildFile)
print("Jar Directory : "+jarDir)
print("Package Directory : "+pkgDir)
print("Delivery Directory : "+deliveryDir)
print("Excluded Files : "+excludeFiles)
sys.stdout.flush()


##########seting JAVA_HOME path for the given branch###########
def setJavaPath(branch):
        if (jdk == "jdk11"):
		os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk-11.0.11"

	elif (jdk == "jdk1.8"):
		os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_172_bkp"

	elif (branch ==  "Linux"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_172_bkp"

        elif (branch ==  "Standalone"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_172_bkp"

        elif (branch ==  "Solaris"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_152_bkp"

	elif branch == "21.4.2_Linux" or branch == "21.4.3_Linux" or branch == "21.4.4_Linux" or branch == "21.4.5_Linux" or branch == "21.4.6_Linux" or branch == "21.4.7_Linux" or branch == "21.4.8_Linux" :
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
                if (pkg == "information_store_parser") or (pkg == "kpiparser") or (pkg == "volte") or (pkg == "3GPP32435") or (pkg == "sim") or (pkg == "3GPP32435BCS") or (pkg == "3GPP32435DYN") or (pkg == "3GPP32435DYN_CBA") or (pkg == "3GPP32435_CBA") or (pkg == "3GPP32435ProCus1") or (pkg == "ascii") or (pkg == "asn1") or (pkg == "bcd") or (pkg == "csexport") or (pkg == "ct") or (pkg == "ebs") or (pkg == "eascii") or (pkg == "epochascii") or (pkg == "HTMLTABLE") or (pkg == "HXML") or (pkg == "HXMLCsIptnms") or (pkg == "HXMLPsIptnms") or (pkg == "LDAP") or (pkg == "MDC_CCN") or (pkg == "MDC_DYN") or (pkg == "MDC_PC") or (pkg == "MDC") or (pkg == "minilink") or (pkg == "mlxml") or (pkg == "nossdb") or (pkg == "prefix_ascii") or (pkg == "redback") or (pkg == "sasn") or (pkg == "stfiop") or (pkg == "twampm") or (pkg == "twamppt") or (pkg == "twampst") or (pkg == "wifi") or (pkg == "wifiinventory") or (pkg == "xml") or (pkg == "mrr") or (pkg == "parser") or (pkg == "IMXmlParser") or (pkg == "json"):
                        if ( jdk == "jdk1.7"):
                                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.7.0_141_bkp"
                        if ( jdk == "jdk1.8"):
                                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_152_bkp"
                else:
                        os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_152_bkp"

        elif (branch == "18.4.2") or (branch == "18.2.2") or (branch == "18.2.6") or (branch == "18.2.7") or (branch == "18.2.8") or (branch == "18.2.8.EU1") or (branch == "18.2_CONSOLIDATION") or (branch == "eniq_stats_18b_18.2.8.eu2_hot_ec") or (branch == "eniq_stats_rhel") or (branch == "18.2.6") or (branch == "18.2.7") or (branch == "18.2.8") or (branch == "priv_eqev_49562") or (branch == "eqev_41277_enm"):
                if (pkg == "information_store_parser") or (pkg == "kpiparser") or (pkg == "volte") or (pkg == "3GPP32435") or (pkg == "sim") or (pkg == "3GPP32435BCS") or (pkg == "3GPP32435DYN") or (pkg == "3GPP32435DYN_CBA") or (pkg == "3GPP32435_CBA") or (pkg == "3GPP32435ProCus1") or (pkg == "ascii") or (pkg == "asn1") or (pkg == "bcd") or (pkg == "csexport") or (pkg == "ct") or (pkg == "ebs") or (pkg == "eascii") or (pkg == "epochascii") or (pkg == "HTMLTABLE") or (pkg == "HXML") or (pkg == "HXMLCsIptnms") or (pkg == "HXMLPsIptnms") or (pkg == "LDAP") or (pkg == "MDC_CCN") or (pkg == "MDC_DYN") or (pkg == "MDC_PC") or (pkg == "MDC") or (pkg == "minilink") or (pkg == "mlxml") or (pkg == "nossdb") or (pkg == "prefix_ascii") or (pkg == "redback") or (pkg == "sasn") or (pkg == "stfiop") or (pkg == "twampm") or (pkg == "twamppt") or (pkg == "twampst") or (pkg == "wifi") or (pkg == "wifiinventory") or (pkg == "xml") or (pkg == "mrr") or (pkg == "parser") or (pkg == "IMXmlParser") or (pkg == "json") or (pkg == "3GPP32435DYN_CEE") or (pkg == "3GPP32435DYN_OCC"):
                        os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.7.0_141_bkp"
                else:
                        os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_152_bkp"

        elif (branch == "18.2.5") or (branch == "18.2.4"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_172_bkp"

        elif (branch == "18.0.6") or (branch == "18.0.7"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.7.0_141_bkp"

        elif (branch == "16.2_CONSOLIDATION") or (branch == "16.0_CONSOLIDATION"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.7.0_80_Linux"

        if (branch == "18.2.2") and (pkg == "diskmanager"):
                os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_131_new/jdk1.8.0_131"

        print ('\n\nFinal JAVA_HOME path: '+os.environ["JAVA_HOME"])
        sys.stdout.flush()
 
  
####################Building Package##################################
def buildPackage():
        buildCommand = antfile+" -v -buildfile "+buildFile+" -Dpackage.build.file="+pkgBuildFile+" -Dbuild.label="+productNo+"-"+Rstate+" -Dbuild.revision="+Rstate+" -Dproject.root=/proj -Dexclude_files="+excludeFiles+" -Dproduct.number="+productNo+" -Dlogname=esjkadm100 -Dpackage_dir="+pkgDir+" -Dpackage="+pkg+" -Djar_dir="+jarDir+" -Ddelivery_dir="+deliveryDir+" -Djobname="+jbName+" -Dbranch="+branch
        print("\n\nRunning build command : "+buildCommand)
        sys.stdout.flush()
        os.system(buildCommand)


###################Function to delete files before pushing it to git which are created as part of package building###################### 
def deletingExtraFiles():
        os.system("mkdir /proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+jbName+"/test/")
        os.chdir("/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+jbName+"/test/")
        if (repoName == "3GPP32435DYN_CBA")  or (repoName == "Bulk_CM_Custom_Parser") or (repoName == "NpPmCustomParser") or (repoName == "SnaPmCustomParser") or (repoName == "CUDBLdif") or (repoName == "3GPP32435DYN_EDA") or (repoName == "3GPP32435DYN_CEE") or (repoName == "3GPP32435DYN_OCC") or (repoName == "3GPP32435ProCus1") or (repoName == "3GPP32435_CBA") or (repoName == "HXML") or (repoName == "IMXmlParser") or (repoName == "LDAP") or (repoName == "ebinary") or (repoName == "epochascii") or (repoName == "htmltable") or (repoName == "mlxml") or (repoName == "nascii") or (repoName == "omes") or (repoName == "omes2") or (repoName == "parser_test_fwk") or (repoName == "prefix_ascii") or (repoName == "raml") or (repoName == "seqs") or (repoName == "simcfg_procus") or (repoName == "simulator") or (repoName == "split_ascii"):
                os.system("git clone ssh://esjkadm100@gerrit.ericsson.se:29418/OSS/ENIQ-CR-Parent/com.ericsson.eniq.stats.procus/"+repoName+" && scp -p -P 29418 esjkadm100@gerrit.ericsson.se:hooks/commit-msg "+repoName+"/.git/hooks/")
        else:
                os.system("git clone ssh://esjkadm100@gerrit.ericsson.se:29418/OSS/ENIQ-CR-Parent/com.ericsson.eniq.stats.plat/"+repoName+" && scp -p -P 29418 esjkadm100@gerrit.ericsson.se:hooks/commit-msg "+repoName+"/.git/hooks/")
        os.chdir(repoName)
        os.system("git checkout "+branch)
        os.system("python /proj/eiffel013_config_fem6s11/difference/file_difference_build.py /proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+jbName+"/test/"+repoName+"/dev /proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+jbName+"/"+repoName+"/dev")
        os.chdir("/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+jbName+"/"+repoName)


###################Function to push the code to git with latest tag##################################
def gitPush():
		os.system("git add -A .")
		os.system("git commit -m \"update buildnumber and Jar File\"")
		os.system("git push origin "+branch)
		os.system("git tag -a "+productNo+"-"+Rstate+" -m \""+productNo+"-"+Rstate+" label is used\"")
		os.system("git push origin "+productNo+"-"+Rstate)
        

################Function to upload package to nexus#####################################
def nexusUpload():
        os.chdir(deliveryDir)
        Package =  os.listdir(deliveryDir)
        Package = Package[0].strip()
        if (repoName == "3GPP32435DYN_CBA") or (repoName == "Bulk_CM_Custom_Parser") or (repoName == "NpPmCustomParser") or (repoName == "SnaPmCustomParser") or (repoName == "CUDBLdif") or (repoName == "3GPP32435DYN_EDA") or (repoName == "3GPP32435DYN_CEE") or (repoName == "3GPP32435DYN_OCC") or (repoName == "3GPP32435ProCus1") or (repoName == "3GPP32435_CBA") or (repoName == "HXML") or (repoName == "IMXmlParser") or (repoName == "LDAP") or (repoName == "ebinary") or (repoName == "epochascii") or (repoName == "htmltable") or (repoName == "mlxml") or (repoName == "nascii") or (repoName == "omes") or (repoName == "omes2") or (repoName == "parser_test_fwk") or (repoName == "prefix_ascii") or (repoName == "raml") or (repoName == "seqs") or (repoName == "simcfg_procus") or (repoName == "simulator") or (repoName == "split_ascii"):
            os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+Package+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/eniq_platform/Procus/"+branch+ "/" +Package)
        else:
            os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+Package+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/eniq_platform/Packages/"+branch+ "/" +Package)
        print "\n\n *********"+Package+" uploaded to nexus*********\n\n"
        if ( "21.4" in branch ):
            os.chdir(deliveryDir)
            os.system("cp "+Package+" /proj/eiffel013_config_fem5s11/eiffel_home/FULL_PF_KGB_DATA/Pkg_List")
	    os.system("cp "+Package+" /proj/eiffel013_config_fem5s11/eiffel_home/ALL_PF_KGB_DATA/Pkg_List")

            file = Package[0:Package.index('.')]
            os.chdir("/proj/eiffel013_config_fem5s11/eiffel_home/FULL_PF_KGB_DATA/Pkg_List")
            f= open(file+".txt","w+")
            f.writelines("SHIPMENT="+branch+"\n")
            f.writelines("XID="+xid)
            f.close()
	    os.system("cp "+file+".txt /proj/eiffel013_config_fem5s11/eiffel_home/ALL_PF_KGB_DATA/Pkg_List")


####################cleanup clonned repos################
def cleanup():
        os.chdir("/proj/eiffel013_config_fem6s11/eiffel_home/jobs/"+jbName)
        file = open("dependentModule.txt",'r')
        list = file.readlines()
        file.close()
        for i in list:
                os.system("rm -rf "+i)
        os.system("rm -rf dependentModule.txt test "+repoName)
        os.system("rm -rf /proj/eiffel013_config_fem6s11/eiffel_home/slaves/ComputeFarm1/workspace/"+jbName+"/scripts")


####################calling functions###############################
setJavaPath(branch)
buildPackage()
deletingExtraFiles()
gitPush()
nexusUpload()
cleanup()
