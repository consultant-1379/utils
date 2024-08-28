import subprocess
import sys
import os
import itertools

#features = ["network-analytics-app-coverage","network-analytics-nr-kpi-dashboard","network-analytics-pm-explorer","network-analytics-energy-report","network-analytics-pm-alarming-2","network-analytics-RNO-MRR","network-analytics-ran-performance-overview","network-analytics-volte","network-analytics-IMS-capacity-Analysis","NetAn_AdminUi_Tests","network-analytics-uplink-interference"]
features = ["network-analytics-uplink-interference","network-analytics-app-coverage","network-analytics-RNO-MRR","network-analytics-pm-explorer","network-analytics-IMS-capacity-Analysis","NetAn_AdminUi_Tests","network-analytics-nr-kpi-dashboard","network-analytics-pm-alarming-2","network-analytics-ran-performance-overview","network-analytics-energy-report","network-analytics-volte"]
test = []
passed = []
failed = []
skipped = []
pending = []
os.chdir('/proj/eiffel013_config_fem5s11/eiffel_home/jobs/NetAn10_Cypress_Test/builds')
x=subprocess.Popen('ls -t', stdout=subprocess.PIPE, shell=True)
out,err = x.communicate()
out = out.strip()
list = out.split('\n')
list = [i for i in list if not i.startswith('last') and not i.startswith('legacy')]
os.chdir(list[0])
f = open('log','r')
res = []
for line in f.readlines():
        if 'failed (' in line or 'passed!' in line:
                res.append(line)

f.close()
for elem in res:
        result = elem.split("  ")
        result = [i for i in result if i]
        print "Result  : "
        print result
        for index,item in enumerate(result):
                if item == '-':
                        result[index] = '0'
        test.append(result[-6])
        passed.append(result[-5])
        failed.append(result[-4])
	pending.append(result[-3])
        skipped.append(result[-2])

while len(test) != len(features):
        test.append('0')
        passed.append('0')
        failed.append('0')
        skipped.append('0')
	pending.append('0')

# print features
# print test
# print passed
# print failed
# print skipped

f = open('/proj/eiffel013_config_fem5s11/slaves/RHEL_ENIQ_STATS/netan/test_report10.html','w')
f.write('<html><body><table border=\'2\'>\n')
f.write('<tr><th>Feature</th><th>No of Tests</th><th>Passed</th><th>Failed</th><th>Skipped</th></tr>\n')

for (feature, all, pas, fail,skip, pend) in zip(features, test, passed, failed, skipped, pending):
        #print feature+" "+all+" "+pas+" "+fail+" "+skip
	skip = int(skip) + int(pend)
	skip = str(skip)
        f.write('<tr><td>'+feature+'</td><td>'+all+'</td><td>'+pas+'</td><td>'+fail+'</td><td>'+skip+'</td></tr>\n')
f.write('</table></body></html>')
f.close()

