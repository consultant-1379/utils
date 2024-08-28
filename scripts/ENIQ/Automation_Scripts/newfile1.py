import os
import subprocess
import sys

os.chdir("/home/eniqdmt/gagan/")
os.system("rm -rf ENIQ_Feature_Files_Linux/ENIQ_Feature_File/property_files/")
os.system("rm -rf ENIQ_Feature_Files_Linux/eniq_executable/property_files/")
os.system("rm -rf ENIQ_Feature_Files_Linux/property_files/")
os.system("rm -rf ENIQ_Feature_Files_Linux/Common_file.txt")
os.chdir("/home/eniqdmt/gagan/ENIQ_Feature_Files_Linux/ENIQ_Feature_File/")
y=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
out,err = y.communicate()
out = out.strip()
list = out.split('\n')
print(list)
list.sort()
print(list)
length = len(list)
print(list[length-1])
os.system("rm -rf ENIQ_Feature_Files_Linux/ENIQ_Feature_File/")
os.chdir("/home/eniqdmt/gagan/")
os.system("rm -rf ENIQ_Feature_Files_Linux/ENIQ_Feature_File/")
#subprocess.call(['chmod', '-R', '777', '/home/eniqdmt/gagan/ENIQ_Feature_Files_Linux/'])
os.system('chmod -R 777 ENIQ_Feature_Files_Linux/')
os.chdir("/home/eniqdmt/gagan/ENIQ_Feature_Files_Linux/")
z=subprocess.Popen('ls', stdout=subprocess.PIPE, shell=True)
out1,err1 = z.communicate()
out1 = out1.strip()
list1 = out1.split('\n')
print(list1)
#for m in range(len(list1)):
#    os.system("chmod -R 777 " + list1[m])
   # os.chmod(list1[m],0777)
os.chdir("/home/eniqdmt/gagan/")
x = subprocess.Popen("find ENIQ_Feature_Files_Linux -type f", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output,error = x.communicate()
output = output.strip()
allfiles=output.split('\n')
for file in allfiles:
    os.system("dos2unix -437 "+file+" "+file)
    print(file)
os.system('chmod -R 777 ENIQ_Feature_Files_Linux/')
#os.chdir("/home/eniqdmt/gagan/ENIQ_Feature_Files_Linux/ENIQ_Feature_File/")
#os.system("zip -r ENIQ_Feature_Files_R21C43.zip . *")
s = list[length-1]
#print(s)
l = s.split("_")
#print(l)
#print(l[3])
s = l[3]
l1 =len(s)
for i in range(1,l1):
    if(s[i] >= 'A' and s[i] <= 'Z'):
        #print("i:",i)
        #print(s[i])
        break;
#print(i)
r =0
for j in range(1,i):
    r =  (r*10) + int(s[j])
#print(r)
for j in range(i,l1):
    #print(s[i])
    if(s[j] == '.'):
        #print(s[i])
        break;
#print(j)
r1 =0
for k  in range(i+1,j):
    r1 = (r1*10) + int(s[k])
#print(r1)

if(sys.argv[1] == "Same_Sprint"):
    r1 = r1 +1
    result = "R" + str(r) + s[i] + str(r1)
elif(sys.argv[1] == "Different_Sprint"):
    r1 = r1 +1
    p = ord(s[i])
    q = chr(p + 1)
    if(q == 'W' or q == 'I' or q == 'P' or q == 'R' or q == 'O' or q == 'Q'):
        q = chr(p + 2)

    #print(chr(p+1))
    result = "R" + str(r) + q + str(r1)
elif(sys.argv[1] == "Different_Release"):
    r1 = r1 + 1
    q = 'A'
    r = r + 1
    result = "R" + str(r) + q + str(r1)


print(result)
os.chdir("/home/eniqdmt/gagan/ENIQ_Feature_Files_Linux/")
os.system("zip -r ENIQ_Feature_Files_" + result +".zip . *")

w=subprocess.Popen('ls | grep ENIQ_Feature_Files_R', stdout=subprocess.PIPE, shell=True)
out2,err2 = w.communicate()
out2 = out2.strip()
list2 = out2.split('\n')
print(list2[0])
os.system("scp /home/eniqdmt/gagan/ENIQ_Feature_Files_Linux/" + list2[0] + " eniqdmt@fem6s11-eiffel013.eiffel.gic.ericsson.se:/home/eniqdmt/zpunvai")
#os.system("scp /home/eniqdmt/gagan/ENIQ_Feature_Files_Linux/" + list2[0] + " esjkadm100@fem6s11-eiffel013.eiffel.gic.ericsson.se:/proj/eiffel013_config_fem6s11/eiffel_home/slaves/ComputeFarm1/workspace/")
#os.system("cp -r /home/eniqdmt/gagan/" + list2[0] + " /vobs/eniq/delivery/tp/ENIQ_Feature_Files_Linux/ENIQ_Feature_File/")
#os.system("cp -r /home/eniqdmt/gagan/" + list2[0] + " /home/eniqdmt/gagan1/")
#os.system('sshpass -p shroot12 scp -P 2251 -o StrictHostKeyChecking=no '+list2[0]+' root@'+sys.argv[2]+'.athtem.eei.ericsson.se:/eniq/home/dcuser')
#os.system('sshpass -p shroot12 scp -P 2251 -o StrictHostKeyChecking=no /home/eniqdmt/gagan/'+list2[0]+' root@'+sys.argv[1]+'.athtem.eei.ericsson.se:/eniq/home/dcuser')
#os.system("rm -rf " + list2[0])
os.system("rm -rf /home/eniqdmt/gagan/ENIQ_Feature_Files_Linux")
