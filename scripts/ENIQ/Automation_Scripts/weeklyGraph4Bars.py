from jira import JIRA
import os
import paramiko
import matplotlib.pyplot as plt
import numpy as np

jiraOptions = {'server': "https://jira-oss.seli.wh.rnd.internal.ericsson.com"}

jira = JIRA(options=jiraOptions, basic_auth=("zhshees", "CaspoO2525@1"))

########################### 22.4  total MRs #################
new = len(jira.search_issues("filter=109082"))
F0 = len(jira.search_issues("filter=109076"))
Ready = len(jira.search_issues("filter=109083"))
F1 = len(jira.search_issues("filter=109077"))
F2 = len(jira.search_issues("filter=109078"))
F3 = len(jira.search_issues("filter=109079"))
F4 = len(jira.search_issues("filter=109080"))
FG = len(jira.search_issues("filter=109055"))
total = len(jira.search_issues("filter=109054",maxResults=1000))

####################### NetAn MRs ####################
new_net = len(jira.search_issues("filter=109064"))
F0_net = len(jira.search_issues("filter=109057"))
Ready_net = len(jira.search_issues("filter=109065"))
F1_net = len(jira.search_issues("filter=109058"))
F2_net = len(jira.search_issues("filter=109060"))
F3_net = len(jira.search_issues("filter=109061"))
F4_net = len(jira.search_issues("filter=109062"))
FG_net = len(jira.search_issues("filter=109063"))
total_net = len(jira.search_issues("filter=109066"))

############################### Platform MRs #####################
new_pf = len(jira.search_issues("filter=109073"))
F0_pf = len(jira.search_issues("filter=109067"))
Ready_pf = len(jira.search_issues("filter=109074"))
F1_pf = len(jira.search_issues("filter=109068"))
F2_pf = len(jira.search_issues("filter=109069"))
F3_pf = len(jira.search_issues("filter=109070"))
F4_pf = len(jira.search_issues("filter=109071"))
FG_pf = len(jira.search_issues("filter=109072"))
total_pf = len(jira.search_issues("filter=109075"))

############################ TP MRs #############################
new_tp = len(jira.search_issues("filter=109089"))
F0_tp = len(jira.search_issues("filter=109081"))
Ready_tp = len(jira.search_issues("filter=109090"))
F1_tp = len(jira.search_issues("filter=109084"))
F2_tp = len(jira.search_issues("filter=109085"))
F3_tp = len(jira.search_issues("filter=109086"))
F4_tp = len(jira.search_issues("filter=109087"))
FG_tp = len(jira.search_issues("filter=109088"))
total_tp = len(jira.search_issues("filter=109091"))

#data
#x-axis
years = ['New', 'F0', 'Ready for F1', 'F1', 'F2', 'F3', 'F4', 'FG', 'Grand Total']
#y_axis = [10,20,30,40,50,60]

###y-axis
TP = [new_tp,F0_tp,Ready_tp,F1_tp,F2_tp,F3_tp,F4_tp,FG_tp,total_tp]
Platform = [new_pf,F0_pf,Ready_pf,F1_pf,F2_pf,F3_pf,F4_pf,FG_pf,total_pf]
NetAn = [new_net,F0_net,Ready_net,F1_net,F2_net,F3_net,F4_net,FG_net,total_net]
Total = [new,F0,Ready,F1,F2,F3,F4,FG,total]

#bar chart properties
x = np.arange(len(years))
#y = np.arange(len(y_axis))
width = 0.2

#draw grouped bar chart
fig, ax = plt.subplots(figsize =(12, 8))
bar1 = ax.bar(x - width, Platform, width, label='Platform', align='center')
bar2 = ax.bar(x, TP, width, label='TP',align='center')
bar3 = ax.bar(x + width, NetAn, width, label='NetAn', align='center')
bar4 = ax.bar(x + width + width, Total, width, label='Total', align='center', color='c')

#ax.set_ylabel('Expenses($)')
ax.set_title('22.4 MRs Detailed F Status')
ax.set_xticks(x,years)
#ax.set_yticks(y,y_axis)
ax.legend()

#setting bar labels
ax.bar_label(bar1)
ax.bar_label(bar2)
ax.bar_label(bar3)
ax.bar_label(bar4)
 
fig.tight_layout()
plt.savefig('MR2.png')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='10.120.176.102', username='esjkadm100', password='Naples!0512',port=22)
sftp_client = ssh.open_sftp()
sftp_client.put("MR2.png", "/proj/eiffel013_config_fem7s11/eiffel_home/slaves/ComputeFarm1/workspace/Weekly_BUG_Report/MR2.png")
sftp_client.close()
ssh.close()

plt.show()
plt.close
