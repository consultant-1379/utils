import subprocess
import sys
import os

module = sys.argv[1]
path = sys.argv[2]
b_no = path.split('/')[6]

def change_hypen_to_0(name):
    if '-' in name:
        name = "0"
    return name

os.chdir('/proj/eiffel013_config_fem5s11/eiffel_home/jobs/NetAn_pm_explorer_tcs/builds/'+b_no)
if 'All specs passed' in open('log').read():
        mod = 'All specs passed!'
else:
        mod = 'failed ('
#x=subprocess.Popen("cat log | grep -w 'pm_explorer_collection_manager.feat'", stdout=subprocess.PIPE, shell=True)
x=subprocess.Popen("cat log | grep '"+mod+"'", stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split(' ')
list = [i for i in list if i]
Tests = list[-5].strip()
Tests = change_hypen_to_0(Tests)
Passed = list[-4].strip()
Passed = change_hypen_to_0(Passed)
Failed = list[-3].strip()
Failed = change_hypen_to_0(Failed)
Pending = list[-2].strip()
Pending = change_hypen_to_0(Pending)
Skipped = list[-1].strip()
Skipped = change_hypen_to_0(Skipped)
Skipped = int(Skipped) + int(Pending)
Skipped = str(Skipped)
print Tests+"  "+Passed+"  "+Failed+"  "+Skipped+" "+Pending
f = open('/proj/eiffel013_config_fem5s11/slaves/RHEL_ENIQ_STATS/netan/pmx_report.html','w')
f.write('<html><body><table border=\'2\'>')
f.write('<tr><th>Feature</th><th>No of Tests</th><th>Passed</th><th>Failed</th><th>Skipped</th></tr>')
f.write('<tr><td>'+module+'</td><td>'+Tests+'</td><td>'+Passed+'</td><td>'+Failed+'</td><td>'+Skipped+'</td></tr>')
f.write('</table></body></html>')
f.close()

