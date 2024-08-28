import os
import sys

shipment = sys.argv[1]

path = "/net/10.45.192.153/JUMP/ENIQ_STATS/ENIQ_STATS/" + shipment + "/eniq_base_sw/eniq_sw/"
kgbPath = "/tmp/PLM_PF_KGB/"
tafParserFile = "/eniq/home/dcuser/latest_packages.txt"

if not os.path.exists(kgbPath):
	os.makedirs("/tmp/PLM_PF_KGB/")
	
if os.path.exists(tafParserFile):
	with open (tafParserFile) as tafFile:
		current_pkgs = [i.strip() for i in tafFile.readlines() if "zip" in i]
else:
	current_pkgs = [i for i in os.listdir(path) if i.endswith('.zip')]
	
kgb_pkgs = [i for i in os.listdir(kgbPath) if i.endswith('.zip')]

print "="*30
print "Current Packages available list in vApp..!!"
print ", ".join(current_pkgs)
print "="*30
print "\n\n"
print "="*30
print "PF KGB Packages available in /tmp/PLM_PF_KGB/ folder"
print ", ".join(kgb_pkgs)
print "="*30
print "\n\n"

with open(tafParserFile, 'w') as pkgFile:
	for pkg in kgb_pkgs:
		for index, oldPkg in enumerate(current_pkgs):
			module = pkg.split("_R")[0]
			if oldPkg.startswith(module):
				if pkg > oldPkg:
					current_pkgs[index] = pkg
	
	pkgFile.write("\n".join(current_pkgs))

print "="*30
print "Packages list after Automation..!!"
print ", ".join(current_pkgs)
print "="*30