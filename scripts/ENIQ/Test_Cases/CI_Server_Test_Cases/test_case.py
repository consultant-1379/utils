import os
import sys

os.chdir("/var/tmp/")

log_file = sys.argv[1]
test_case_file = sys.argv[2]

fp = open(test_case_file,'r')
l = fp.readlines()
fp.close()


fail = 0
total = 0
pas = 0

fp = open("TC_Result.html",'w')
fp.writelines("<html><head><title>FFU TestCase Results</title></head><body><table border=\"2\"><tr><th><b> TestCase Name </th><th><b> TestCase </th><th><b>PASS/FAIL</th></tr>")
fp.close()

for i in range(len(l)):
	tc = l[i]
	tc = tc.strip("\n")

	if(tc == "Log Sanity" or tc == "---------------" or tc == "" or tc == "Server Sanity"):
		print("Ignoring "+tc+" from the input files")

	elif(("ERROR" in tc) or ("failed" in tc) or ("warning" in tc) or ("error" in tc) or ("permission denied" in tc) or ("cannot" in tc) or ("can.t open" in tc) or ("Can.t open" in tc) or ("could not" in tc) or ("couldn" in tc) or ("no such" in tc)):
		d = os.system("cat "+log_file+" | grep -i '"+tc+"'")
                if (d == 0):
                        fp = open("TC_Result.html",'a')
                        status="<td style=\"color:red;\"> FAIL"
                        fp.writelines("<tr> <td>"+tc+" Check</td> <td> cat "+log_file+" | grep -i"+tc+"</td>"+ status+" </td> </tr>")
                        fp.close()
			fail = fail+1
                        total = total+1
                else:
                        fp = open("TC_Result.html",'a')
                        status="<td style=\"color:green;\"> PASS"
                        fp.writelines("<tr> <td>"+tc+" Check</td> <td> cat "+log_file+" | grep -i"+tc+"</td>"+ status+" </td> </tr>")
                        fp.close()

			pas = pas+1
                        total = total+1

	else:
		d = os.system("cat "+log_file+" | grep -i '"+tc+"'")
		if (d == 0):
			fp = open("TC_Result.html",'a')
			status="<td style=\"color:green;\"> PASS"
			fp.writelines("<tr> <td>"+tc+" Check</td> <td> cat "+log_file+" | grep -i"+tc+"</td>"+ status+" </td> </tr>")
			fp.close()
			pas = pas+1
			total = total+1
		else:
			fp = open("TC_Result.html",'a')
                        status="<td style=\"color:red;\"> FAIL"
                        fp.writelines("<tr> <td>"+tc+" Check</td> <td> cat "+log_file+" | grep -i"+tc+"</td>"+ status+" </td> </tr>")
                        fp.close()

			fail = fail+1
			total = total+1
	j=0
	if(tc == "Server Sanity"):
		for j in range(i,len(l)):
			tc = l[j]
		        tc = tc.strip("\n")

        		if(tc == "Server Sanity" or tc == "---------------" or tc == ""):
                		print("Ignoring "+tc+" from the input files")

			elif(("ERROR" in tc) or ("failed" in tc) or ("warning" in tc) or ("error" in tc) or ("permission denied" in tc) or ("cannot" in tc) or ("can.t open" in tc) or ("Can.t open" in tc) or ("could not" in tc) or ("couldn" in tc) or ("no such" in tc)):
				#print("os.system("+tc+")")
                		d = os.system(tc)
                		if (d == 0):
                        		fp = open("TC_Result.html",'a')
                        		status="<td style=\"color:red;\"> FAIL"
                        		fp.writelines("<tr> <td>"+tc+" Check</td> <td> cat "+log_file+" | grep -i"+tc+"</td>"+ status+" </td> </tr>")
                        		fp.close()
                        		fail = fail+1
                        		total = total+1
                		else:
                        		fp = open("TC_Result.html",'a')
                        		status="<td style=\"color:green;\"> PASS"
                        		fp.writelines("<tr> <td>"+tc+" Check</td> <td> cat "+log_file+" | grep -i"+tc+"</td>"+ status+" </td> </tr>")
                        		fp.close()

                        		pas = pas+1
                        		total = total+1

        		else:
				#print("os.system("+tc+")")
                		d = os.system(tc)
                		if (d == 0):
                        		fp = open("TC_Result.html",'a')
                        		status="<td style=\"color:green;\"> PASS"
                        		fp.writelines("<tr> <td>"+tc+" Check</td> <td> cat "+log_file+" | grep -i"+tc+"</td>"+ status+" </td> </tr>")
                        		fp.close()
                        		pas = pas+1
                        		total = total+1
                		else:
                        		fp = open("TC_Result.html",'a')
                        		status="<td style=\"color:red;\"> FAIL"
                        		fp.writelines("<tr> <td>"+tc+" Check</td> <td> cat "+log_file+" | grep -i"+tc+"</td>"+ status+" </td> </tr>")
                        		fp.close()

                        		fail = fail+1
                        		total = total+1
	#print("j = ",j)
	#print(len(l))
	if(j == len(l)-1):
		#print("Breaking")
		break

print("Total: "+str(total))
print("Pass: "+str(pas))
print("Fail: "+str(fail))
