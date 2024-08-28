import os
import subprocess
import sys


def checkout_branch(branch,j):
	print("Trying to checkout " + branch + " branch")
	os.chdir(sys.argv[1])
	d = os.system("git checkout " + branch)
	if(d == 256):
		print(branch + " doesn't exist")
		print("Trying to checkout the previous branch")	
		j = j+1
		checkout_branch(l[j].strip(),j)

os.chdir("/proj/eiffel013_config_fem6s11/tools/")
fp1 = open("branch.txt",'r')
l = fp1.readlines()
fp1.close()

length = len(l)
for i in range(length):
	if(l[i].strip() == sys.argv[2]):
		break

checkout_branch(l[i].strip(),i)

