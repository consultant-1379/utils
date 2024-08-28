import subprocess
import sys
import os
import itertools

module = sys.argv[1]
path = sys.argv[2]
b_no = path.split('/')[6]
features = ["network-analytics-pm-explorer","network-analytics-pm-alarming-2"]
test = []
passed = []
failed = []
skipped = []
pending = []
os.chdir('/proj/eiffel013_config_fem5s11/eiffel_home/jobs/NetAn_TestCase/builds/'+b_no)
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

f = open('/proj/eiffel013_config_fem5s11/slaves/RHEL_ENIQ_STATS/netan/report.html','w')
f.write('<html><body><table border=\'2\'>\n')
f.write('<tr><th>Feature</th><th>No of Tests</th><th>Passed</th><th>Failed</th><th>Skipped</th></tr>\n')

for (feature, all, pas, fail,skip, pend) in zip(features, test, passed, failed, skipped, pending):
        #print feature+" "+all+" "+pas+" "+fail+" "+skip
        skip = int(skip) + int(pend)
        skip = str(skip)
        f.write('<tr><td>'+feature+'</td><td>'+all+'</td><td>'+pas+'</td><td>'+fail+'</td><td>'+skip+'</td></tr>\n')
f.write('</table></body></html>')
f.close()
