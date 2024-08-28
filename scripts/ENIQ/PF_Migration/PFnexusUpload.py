import os
import sys

packagePath = "/proj/eiffel013_config_fem6s11/buildPackage"
os.chdir("/proj/eiffel013_config_fem6s11/buildPackage")
Package =  os.listdir(packagePath)
Package = Package[0].strip()
shipment = sys.argv[1]
xid = sys.argv[3]

####Uploading package to Nexus####
os.system("curl -v -u esjkadm100:Naples\!0512 --upload-file "+Package+" https://arm1s11-eiffel013.eiffel.gic.ericsson.se:8443/nexus/content/repositories/eniq_platform/"+ sys.argv[2] + "/" + sys.argv[1] + "/" +Package)

######checking if package uploaded successfully or not########
nexusPath = "/proj/eiffel013_config_arm1s11/eiffel_home/storage/eniq_platform/"+sys.argv[2]+"/"+sys.argv[1]
os.chdir("/proj/eiffel013_config_arm1s11/eiffel_home/storage/eniq_platform/"+sys.argv[2]+"/"+sys.argv[1])
nexusPackage = os.listdir(nexusPath)
for item in nexusPackage:
      availPackage = item.strip()
      if ( availPackage == Package):
                print "\n\n *********"+Package+" uploaded to nexus successfully*********\n\n"
                break

if ( "21.2" in shipment ):
    os.chdir("/proj/eiffel013_config_fem6s11/buildPackage")
    os.system("cp "+Package+" /proj/eiffel013_config_fem5s11/eiffel_home/FULL_PF_KGB_DATA/Pkg_List")
    
    file = Package[0:Package.index('.')]
    os.chdir("/proj/eiffel013_config_fem5s11/eiffel_home/FULL_PF_KGB_DATA/Pkg_List")
    f= open(file+".txt","w+")
    f.writelines("SHIPMENT="+shipment+"\n")
    f.writelines("XID="+xid)
    f.close()
     
