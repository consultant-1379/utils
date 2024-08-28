import os
import sys
import subprocess

flag = "1"
mountDir = ""
isoPath = "/JUMP/export/kickstart/"+sys.argv[1]+"/"+sys.argv[2]+"/iso"
mediaPath = "/JUMP/OM_LINUX_MEDIA/"

####creating temporary directory to mount the iso#####
if (sys.argv[1] == "ENIQ_I19.4"):
	os.system("mkdir -p /oam_19.4")
	mountDir = "/oam_19.4"
elif (sys.argv[1] == "ENIQ_I20.2"):
	os.system("mkdir -p /oam_20.2")
        mountDir = "/oam_20.2"
elif (sys.argv[1] == "ENIQ_I20.4"):
        os.system("mkdir -p /oam_20.4")
        mountDir = "/oam_20.4"
elif (sys.argv[1] == "ENIQ_I21.2"):
        os.system("mkdir -p /oam_21.2")
        mountDir = "/oam_21.2"
elif (sys.argv[1] == "ENIQ_I21.4"):
        os.system("mkdir -p /oam_21.4")
        mountDir = "/oam_21.4"
else:
	os.system("mkdir -p /oam_zpunvai")
	mountDir = "/oam_zpunvai"

####taking name of iso file#####
os.chdir(isoPath)
ISO =  os.listdir(isoPath)
ISO = ISO[0].strip()

#####mounting latest ISO######
os.system("mount -o ro,loop "+isoPath+"/"+ISO+" "+mountDir)
os.system("ls "+mountDir)

#####Checking if older media exist#######
ship = (sys.argv[2]).split(".")
mediaPath = mediaPath+"OM_LINUX_0"+ship[0]+"_"+ship[1]+"/"+sys.argv[2]
print(mediaPath)
flag = os.system("ls "+mediaPath)

os.chdir("/ericsson/kickstart/bin/")
os.system("pwd")

######removing older media######
if (flag == 0):
	print("********Removing Older Media, if exist********")
	sys.stdout.flush()
	removeIso ='/ericsson/kickstart/bin/manage_nfs_media.bsh -a remove -m om_linux -p '+mediaPath+' -N'
	os.system(removeIso)

######caching latest media#####
commandToAdd ='/ericsson/kickstart/bin/manage_nfs_media.bsh -a add -m om_linux -p '+mountDir+' -N'
print("*******Caching Latest Media in ieatrcx6786 Server********")
sys.stdout.flush()
os.system(commandToAdd)

######unmounting and removing temporary files/folders#######
os.system("umount "+mountDir)
os.system("rm -rf "+mountDir)
#os.system("rm -rf "+isoPath+"/"+ISO)
