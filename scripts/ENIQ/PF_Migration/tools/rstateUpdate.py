import os
import sys
from itertools import groupby

####storing command line arguments in variable####
module = sys.argv[1]
branch = sys.argv[2]
flag =""
availRstate =""
newRstate =""

####Function to set JAVA_HOME path for the given branch####
def setJavaPath(branch):
        if (branch ==  "20.4.7"):
            os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_172_bkp"
        if (branch == "18.2.8"):
            os.environ["JAVA_HOME"] = "/proj/jkadm100/tools/jdk1.8.0_172_bkp"

####function to split Alphanumeric R-state####
def split_text(oldRstate):
    for k, g in groupby(oldRstate, str.isalpha):
        yield ''.join(g)

####function to increament r-state by 1####
def increase_rstate(oldRstate):
        rstateData=(list(split_text(oldRstate)))
        len1 = len(rstateData)
        num = rstateData[len1-1].strip()
        num = int(num)+1
        if((num%10) == num):
                rstateData[len1-1] = "0"+str(num)
        else:
                rstateData[len1-1] = str(num)
        newRstate = ''.join(rstateData)
        return(newRstate)

#Taking backup of rstate file
os.chdir("/proj/eiffel013_config_fem6s11/tools/")
os.system("cp /proj/eiffel013_config_fem6s11/tools/rstate.txt /proj/eiffel013_config_fem6s11/tools/rstate_bkp.txt")

#####stroing content of existing r-state file in list#####
rsFile = open("rstate.txt" , 'r')
lines = rsFile.readlines()
lines = [item.strip() for item in lines]
rsFile.close()

#####checking for available r-state for the give module/branch#####
for index,item in enumerate(lines):
        data = item.split(":")
        if (len(data) == 1) or (len(data) == 0):
                continue
        moduleInFile = data[0].strip()
        branchInFile = data[1].strip()
        rstateInFile = data[2].strip()
        if ( moduleInFile == module ):
                if(branch in branchInFile):
                        flag = 1
                        availRstate = rstateInFile
                        print (availRstate)
                        newRstate = increase_rstate(availRstate)
                        data[2] = newRstate
                        data = ':'.join(data)
                        lines[index] = data
                        break
                                   
#####Updating next available r-state inr-state file#####
if (flag != 1):
        sys.exit("Branch not found. Please update the Rstate File\n")
else:
        newFile = open("newRstate.txt" , 'w')
        for item in lines:
                newFile.writelines(item)
                newFile.writelines("\n")
        newFile.close()
        os.system("mv newRstate.txt rstate.txt")

