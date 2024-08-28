import os
import sys
import subprocess

flag = "1"
mountDir = ""
isoPath = "/JUMP/export/jumpstart/"+sys.argv[1]+"/"+sys.argv[2]+"/iso"
mediaPath = "/JUMP/ENIQ_STATS/ENIQ_STATS/"+sys.argv[2]

####creating temporary directory to mount the iso#####
if (sys.argv[1] == "ENIQ_S19.4"):
	os.system("mkdir -p /iso_19.4")
	mountDir = "/iso_19.4"
elif (sys.argv[1] == "ENIQ_S20.2"):
	os.system("mkdir -p /iso_20.2")
        mountDir = "/iso_20.2"
elif (sys.argv[1] == "ENIQ_S20.4"):
        os.system("mkdir -p /iso_20.4")
        mountDir = "/iso_20.4"
elif (sys.argv[1] == "ENIQ_S21.2"):
        os.system("mkdir -p /iso_21.2")
        mountDir = "/iso_21.2"
elif (sys.argv[1] == "ENIQ_S21.4"):
        os.system("mkdir -p /iso_21.4")
        mountDir = "/iso_21.4"
else:
	os.system("mkdir -p /zpunvai")
	mountDir = "/zpunvai"

####taking name of iso file#####
os.chdir(isoPath)
ISO =  os.listdir(isoPath)
ISO = ISO[0].strip()

#####mounting latest ISO######
os.system("mount -o ro,loop "+isoPath+"/"+ISO+" "+mountDir)
os.system("ls "+mountDir)
flag = os.system("ls "+mediaPath)

os.chdir("/ericsson/kickstart/bin/")
os.system("pwd")

######removing older media######
if (flag == 0):
	print("********Removing Older Media, if exist********")
	sys.stdout.flush()
	removeIso ='/ericsson/kickstart/bin/manage_nfs_media.bsh -a remove -m eniq_stats -p '+mediaPath+' -N'
	os.system(removeIso)

######caching latest media#####
commandToAdd ='/ericsson/kickstart/bin/manage_nfs_media.bsh -a add -m eniq_stats -p '+mountDir+' -N'
print("*******Caching Latest Media in ieatrcx6786 Server********")
sys.stdout.flush()
os.system(commandToAdd)

######unmounting and removing temporary files/folders#######
os.system("umount "+mountDir)
os.system("rm -rf "+mountDir)
os.system("rm -rf "+isoPath+"/"+ISO)
