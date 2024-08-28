import os
import sys
import subprocess

 

args = sys.argv
vob = args[1] 
git = args[2]

 
os.chdir(vob)
x=subprocess.Popen('find -type f', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list_vob = out.split("\n")
#print("Vobs contents")
#print(list_vob)
 

os.chdir(git)
x=subprocess.Popen('find -type f | grep -v .gitkeep ', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list_git = out.split("\n")
#print("Git Content")
#print(list_git)
 
print("Total Vobs Element :",len(list_vob))
print("Total Git Element :",len(list_git))

for i in range(len(list_git)):
	f=0
	element = list_git[i]
	for j in range(len(list_vob)):
		if(element == list_vob[j]):
			f=1;
			break;
	if(f==0):
		print(element," is not present in the vobs")
