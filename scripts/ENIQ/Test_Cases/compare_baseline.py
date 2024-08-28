import os
import sys
import subprocess
#Reading inputs
args = sys.argv
os.chdir("/eniq/home/dcuser")
host_name=args[1]
x=subprocess.Popen('cat mws.properties', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
ship = list[0].split('=')[1]
fea = list[1].split('=')[1]
fp=open("Compare_Baseline_Report.html",'w')
fp.writelines("<html><head><title>Compare Baseline Report</title><body><h4>Shipment="+ship+"</h4><h4>Host Name="+host_name+"</h4></body>")
fp.close()
fp=open("Compare_Baseline_Report.html",'a')
fp.writelines("<table border=\"1\">")
fp.close()
#Getting packages list and compare
def pkgverify(modu,path):
        x=subprocess.Popen('ls '+path, stdout=subprocess.PIPE, shell=True)
        out,err = x.communicate()
        out = out.strip()
        list = out.split('\n')
        fp=open("Compare_Baseline_Report.html",'a')
        fp.writelines("<tr><th colspan=3><br>"+modu.upper()+"</th></tr><tr><th><b>Baseline</th><th><b>Servers</th><th><b>Status</th></tr>")
        fp.close()
        for pkg in list:

                c=0
        #platform and parser pkg check
                if modu=="platform" or modu=="parser":
                    if '.' in pkg:
                                check=pkg.split(".")[1]
                                if check=="zip":
                                        md=pkg.split("_R")[0]
                                        rstate="R"+(pkg.split("_R")[1]).split(".")[0]
                                        c=os.system("cat /eniq/sw/installer/versiondb.properties | grep "+md+" | grep "+rstate)
                                        if c==0:
                                                status="<td style=\"color:green;\"> PASS"
                                                servers=pkg
                                                
                                                
                                        else:
                                                status="<td style=\"color:red;\"> FAIL"
                                                y=subprocess.Popen('cat /eniq/sw/installer/versiondb.properties | grep '+md, stdout=subprocess.PIPE, shell=True)
                                                out,err = y.communicate()
                                                out = out.strip()
                                                servers = out.split(".")[1].split("=")[0]+"_"+out.split(".")[1].split("=")[1]+".zip"
                                               
                                                
                                        fp=open("Compare_Baseline_Report.html",'a')
                                        fp.writelines("<tr><td>"+pkg+"</td><td>"+servers+"</td>"+status+"</td></tr>")
                                        fp.close()
        #tp check
        
                if modu=="techpack":
                    if '.' in pkg:
                                check=pkg.split(".")[1]
                                if check=="tpi":
                                        groups=pkg.split("_R")
                                        n=len(groups)
                                        name=pkg.split(".")[0]
                                        md = '_R'.join(groups[:n-1])
                                        rstate="R"+(pkg.split("_R")[len(pkg.split("_R"))-1]).split(".")[0]
                                        c=os.system("ls /eniq/log/sw_log/tp_installer/ | grep "+md+" | grep "+rstate)
                                        if c==0:
                                                status="<td style=\"color:green;\"> PASS"
                                                servers=pkg
                                                
                                        else:
                                                status="<td style=\"color:red;\"> FAIL"
                                                y=subprocess.Popen("ls /eniq/log/sw_log/tp_installer/ | grep [0-9.:]_ "+md+ "| grep "+rstate, stdout=subprocess.PIPE, shell=True)
                                                out,err = y.communicate()
                                                out = out.strip()
                                                servers=out
                                               
                                        fp=open("Compare_Baseline_Report.html",'a')
                                        fp.writelines("<tr><td>"+pkg+"</td><td>"+servers+"</td>"+status+"</td></tr>")
                                        fp.close()            
                
pkgverify("platform","/net/10.45.192.134/JUMP/ENIQ_STATS/ENIQ_STATS/"+ship+"/eniq_base_sw/eniq_sw/")
pkgverify("parser","/net/10.45.192.134/JUMP/ENIQ_STATS/ENIQ_STATS/"+fea+"/eniq_parsers")
pkgverify("techpack","/net/10.45.192.134/JUMP/ENIQ_STATS/ENIQ_STATS/"+fea+"/eniq_techpacks")

