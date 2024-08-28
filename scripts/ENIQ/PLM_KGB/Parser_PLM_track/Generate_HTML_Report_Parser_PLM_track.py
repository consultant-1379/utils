import sys
import os

print "*"*50
print "Generating the HTML Report!!".center(50)
print "*"*50
#BUILD_NO = sys.argv[1]

try:
    file_path = "/var/tmp/PF_installation_result.html"
    log = "/tmp/log"
    log_file = open(log, 'r')
    lines = log_file.readlines()
    log_file.close()
    #pkg_list = ("runtime","libs","eniq_config","installer")
    header = "<html><head><title>Platform Details Table</title></head>\n<body><table border=\"2\"><tr><th><b> NO </th><th><b>Platform Packages</th><th><b>Installation</th></tr>\n"
    footer = "</table></body></html>\n"
    
    PF_install_Flag = False
    Pf_install = {}
    for line in lines:
        if "Installation***" in line:
            print line
            PF_install_Flag = True
            Pf_pkg_fullName = line.split(" ")[0].split("***")[1]
            Pf_pkg = line.split("_")[0].split("***")[1]
            Pf_install[Pf_pkg_fullName] = ""
            #print (Pf_pkg + " <== Pkg Name")
            continue
        
        if PF_install_Flag:
            if "BUILD SUCCESSFUL" in line:
                print line
                Pf_install[Pf_pkg_fullName] = "Pass"
                PF_install_Flag = False
            elif "BUILD FAILED" in line:
                print line
                Pf_install[Pf_pkg_fullName] = "Fail"
                PF_install_Flag = False
            elif "Skipped " + str(Pf_pkg) + " installation" in line:
                print line
                Pf_install[Pf_pkg_fullName] = "Skipped"
                PF_install_Flag = False
            elif (("successfully") in line.lower() or Pf_pkg in line.lower()) and ("installed") in line.lower():
                print line
                Pf_install[Pf_pkg_fullName] = "Pass"
                PF_install_Flag = False
    
    print (Pf_install)
    row=''
    for no, pkg in enumerate(Pf_install.keys()):
            if Pf_install[pkg] == "Pass":
                    row+="<tr><td>"+ str(no+1) +"</td><td>" + str(pkg) + "</td><td align=\"center\"><font color=\"green\"><b>" + str(Pf_install[pkg]) + "</font></td></tr>\n";
            elif Pf_install[pkg] == "Fail":
                    row+="<tr><td>"+ str(no+1) +"</td><td>" + str(pkg) + "</td><td align=\"center\"><font color=\"red\"><b>" + str(Pf_install[pkg]) + "</font></td></tr>\n";
            elif Pf_install[pkg] == "Skipped":
                    row+="<tr><td>"+ str(no+1) +"</td><td>" + str(pkg) + "</td><td align=\"center\"><font color=\"maroon\"><b>" + str(Pf_install[pkg]) + "</font></td></tr>\n";
            else:
                    row+="<tr><td>"+ str(no+1) +"</td><td>" + str(pkg) + "</td><td align=\"center\"><font color=\"blue\"><b>No Log</font></td></tr>\n";
    html = header + row + footer
    html_file = open(file_path, "w")
    html_file.write(html)
    html_file.close()
    os.chmod(file_path, 509) #has to pass equivalent value of 775 in octal
    #print (html)
except Exception as error:
    print "ERROR : " + str(error) + "\nPlease refer the error for EXCEPTION..!!\n"
