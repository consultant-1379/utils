'''
Created on Jun 29, 2021
@author: zpunvai
'''

from jira import JIRA
import base64

def str_issues(num):
    if num == 1:
        return "issue"
    else:
        return "issues"

try:
    jira_user = 'esjkadm100'
    jira_pwd = base64.b64decode("TmFwbGVzITA1MTI=")
    jira = JIRA(basic_auth=(jira_user, jira_pwd), options={'server':'http://jira-oss.seli.wh.rnd.internal.ericsson.com'})
except Exception as e:
    print "Cannot connect to JIRA\n"
    print e

################JIRA filters for 1st Release####################
#pf_open_jiras = len(jira.search_issues("filter=101757"))
#pf_closed_jiras = len(jira.search_issues("filter=101758"))
#infra_open_jiras = len(jira.search_issues("filter=101739"))
#infra_closed_jiras = len(jira.search_issues("filter=101740"))
#ocs_open_jiras = len(jira.search_issues("filter=101731"))
#ocs_closed_jiras = len(jira.search_issues("filter=101734"))
#netan_open_jiras = len(jira.search_issues("filter=101745"))
#netan_closed_jiras = len(jira.search_issues("filter=101746"))
#nmi_open_jiras = len(jira.search_issues("filter=101751"))
#nmi_closed_jiras = len(jira.search_issues("filter=101752"))
#sec_open_jiras = len(jira.search_issues("filter=101764"))
#sec_closed_jiras = len(jira.search_issues("filter=101765"))
#tp_open_jiras = len(jira.search_issues("filter=101770"))
#tp_closed_jiras = len(jira.search_issues("filter=101771"))

#class_A = len(jira.search_issues("project in (EQEV, EN, \"IS\") AND issuetype in (Bug, \"Story Bug\", TR) AND component in (\"ENIQ Stats\", \"ENIQ Stats RV\", \"Code Chef\", \"Creative Crew\", \"Eniq Stats\", \"Ignited Minds\", \"Rising Stars\", \"Indian Ocean\", E_Fireballs, MegaMinds, Wizzards, ENIQ_Knights, STATS_Regression, Solitaire, Asterix, Elites, \"Team 8\", INFRA-SPARTAN, Security_ENIQ) AND component not in (\"Eniq Events\", FROP, EE_tools) AND status not in (Closed) AND fixVersion in (19.4, 19.4_PostGA) AND labels in (Class_A)"))
#class_B = len(jira.search_issues("project in (EQEV, EN, \"IS\") AND issuetype in (Bug, \"Story Bug\", TR) AND component in (\"ENIQ Stats\", \"ENIQ Stats RV\", \"Code Chef\", \"Creative Crew\", \"Eniq Stats\", \"Ignited Minds\", \"Rising Stars\", \"Indian Ocean\", E_Fireballs, MegaMinds, Wizzards, ENIQ_Knights, STATS_Regression, Solitaire, Asterix, Elites, \"Team 8\", INFRA-SPARTAN, Security_ENIQ) AND component not in (\"Eniq Events\", FROP, EE_tools) AND status not in (Closed) AND fixVersion in (19.4, 19.4_PostGA) AND labels in (Class_B)"))
#class_C = len(jira.search_issues("project in (EQEV, EN, \"IS\") AND issuetype in (Bug, \"Story Bug\", TR) AND component in (\"ENIQ Stats\", \"ENIQ Stats RV\", \"Code Chef\", \"Creative Crew\", \"Eniq Stats\", \"Ignited Minds\", \"Rising Stars\", \"Indian Ocean\", E_Fireballs, MegaMinds, Wizzards, ENIQ_Knights, STATS_Regression, Solitaire, Asterix, Elites, \"Team 8\", INFRA-SPARTAN, Security_ENIQ) AND component not in (\"Eniq Events\", FROP, EE_tools) AND status not in (Closed) AND fixVersion in (19.4, 19.4_PostGA) AND labels in (Class_C)"))
#not_assessed = len(jira.search_issues("project in (EQEV, EN, \"IS\") AND issuetype in (Bug, \"Story Bug\", TR) AND component in (\"ENIQ Stats\", \"ENIQ Stats RV\", \"Code Chef\", \"Creative Crew\", \"Eniq Stats\", \"Ignited Minds\", \"Rising Stars\", \"Indian Ocean\", E_Fireballs, MegaMinds, Wizzards, ENIQ_Knights, STATS_Regression, Solitaire, Asterix, Elites, \"Team 8\", INFRA-SPARTAN, Security_ENIQ) AND component not in (\"Eniq Events\", FROP, EE_tools, Eagles) AND status not in (Closed) AND fixVersion in (19.4, 19.4_PostGA) AND (labels != Class_B AND labels != Class_C AND labels != Class_A OR labels is EMPTY)"))

################JIRA filters for 2nd Release###################
pf_open_jiras_2 = len(jira.search_issues("filter=104768"))
pf_closed_jiras_2 = len(jira.search_issues("filter=104769"))
infra_open_jiras_2 = len(jira.search_issues("filter=101741"))
infra_closed_jiras_2 = len(jira.search_issues("filter=101742"))


ocs_open_jiras_2 = len(jira.search_issues("filter=104891"))
ocs_closed_jiras_2 = len(jira.search_issues("filter=104892"))

bis_open_jiras_2 = len(jira.search_issues("filter=104889"))
bis_closed_jiras_2 = len(jira.search_issues("filter=104890"))

netan_open_jiras_2 = len(jira.search_issues("filter=101747"))
netan_closed_jiras_2 = len(jira.search_issues("filter=101748"))
nmi_open_jiras_2 = len(jira.search_issues("filter=101753"))
nmi_closed_jiras_2 = len(jira.search_issues("filter=101754"))
sec_open_jiras_2 = len(jira.search_issues("filter=101766"))
sec_closed_jiras_2 = len(jira.search_issues("filter=101767"))
tp_open_jiras_2 = len(jira.search_issues("filter=101772"))
tp_closed_jiras_2 = len(jira.search_issues("filter=101773"))

################GRAND TOTAL of All JIRAS##########################
pf_total_open = len(jira.search_issues("filter=104768"))
pf_total_closed = len(jira.search_issues("filter=104769"))
infra_total_open = len(jira.search_issues("filter=104770"))
infra_total_closed = len(jira.search_issues("filter=104771"))
ocs_total_open = len(jira.search_issues("filter=104772"))
ocs_total_closed = len(jira.search_issues("filter=104773"))
netan_total_open = len(jira.search_issues("filter=104774"))
netan_total_closed =len(jira.search_issues("filter=104775"))
nmi_total_open = len(jira.search_issues("filter=104776"))
nmi_total_closed = len(jira.search_issues("filter=104777"))
sec_total_open = len(jira.search_issues("filter=104778"))
sec_total_closed = len(jira.search_issues("filter=104779")) 
tp_total_open = len(jira.search_issues("filter=104780"))
tp_total_closed = len(jira.search_issues("filter=104781"))

pf_total_jiras = pf_total_open + pf_total_closed
infra_total_jiras = infra_total_open + infra_total_closed
ocs_total_jiras = ocs_total_open + ocs_total_closed
bis_total_jiras = bis_open_jiras_2 + bis_closed_jiras_2
netan_total_jiras = netan_total_open + netan_total_closed
nmi_total_jiras = nmi_total_open + nmi_total_closed
sec_total_jiras = sec_total_open + sec_total_closed
tp_total_jiras = tp_total_open + tp_total_closed

######################OVERALL COUNT###############################
overall_count = len(jira.search_issues("filter=104782"))
f = open('/proj/eiffel013_config_fem7s11/eiffel_home/slaves/ComputeFarm1/workspace/Jira_Report/jira_report.html','w')  #'/proj/eiffel013_config_fem7s11/eiffel_home/slaves/ComputeFarm1/workspace/Jira_Report/jira_report.html'
f.write("<html>\n<body><h3> 22.2 Bug Report </h3>\n")
f.write("<table border=\"3\"><b><th>Team</th><th>22.2 Jiras Open</th><th>22.2 Jiras Resolved</th><th>Unique Grand Total</th></b>\n")

#f.write("<table border=\"3\"><b><th>Team</th><th>22.1 Jiras Open</th><th>22.1 Jiras Resolved</th><th>22.2 Jiras Open</th><th>22.2 Jiras Resolved</th><th>Unique Grand Total</th></b>\n")

#f.write("<tr align=\"center\"><td>Platform</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?jql=filter%3D101757%20\">"+str(pf_open_jiras)+" "+str_issues(pf_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?jql=filter%3D101758%20\">"+str(pf_closed_jiras)+" "+str_issues(pf_closed_jiras)+"</a></td> \
  #<td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101759\">"+str(pf_open_jiras_2)+" "+str_issues(pf_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101760\">"+str(pf_closed_jiras_2)+" "+str_issues(pf_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(pf_total_jiras)+" "+str_issues(pf_total_jiras)+"</td></tr>\n")

f.write("<tr align=\"center\"><td>Platform</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=104768\">"+str(pf_open_jiras_2)+" "+str_issues(pf_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=104769\">"+str(pf_closed_jiras_2)+" "+str_issues(pf_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(pf_total_jiras)+" "+str_issues(pf_total_jiras)+"</td></tr>\n")

#f.write("<tr align=\"center\"><td>Infra</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?jql=filter%3D101739%20\">"+str(infra_open_jiras)+" "+str_issues(infra_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?jql=filter%3D101740%20\">"+str(infra_closed_jiras)+" "+str_issues(infra_closed_jiras)+"</a></td> \
  #<td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101741\">"+str(infra_open_jiras_2)+" "+str_issues(infra_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101742\">"+str(infra_closed_jiras_2)+" "+str_issues(infra_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(infra_total_jiras)+" "+str_issues(infra_total_jiras)+"</td></tr>\n")

f.write("<tr align=\"center\"><td>Infra</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101741\">"+str(infra_open_jiras_2)+" "+str_issues(infra_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101742\">"+str(infra_closed_jiras_2)+" "+str_issues(infra_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(infra_total_jiras)+" "+str_issues(infra_total_jiras)+"</td></tr>\n")

#f.write("<tr align=\"center\"><td>BIS-OCS</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?jql=filter%3D101731%20\">"+str(ocs_open_jiras)+" "+str_issues(ocs_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?jql=filter%3D101734%20\">"+str(ocs_closed_jiras)+" "+str_issues(ocs_closed_jiras)+"</a></td> \
  #<td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=99714\">"+str(ocs_open_jiras_2)+" "+str_issues(ocs_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101735\">"+str(ocs_closed_jiras_2)+" "+str_issues(ocs_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(ocs_total_jiras)+" "+str_issues(ocs_total_jiras)+"</td></tr>\n")

#f.write("<tr align=\"center\"><td>BIS-OCS</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=99714\">"+str(ocs_open_jiras_2)+" "+str_issues(ocs_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101735\">"+str(ocs_closed_jiras_2)+" "+str_issues(ocs_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(ocs_total_jiras)+" "+str_issues(ocs_total_jiras)+"</td></tr>\n")


f.write("<tr align=\"center\"><td>OCS</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=104891\">"+str(ocs_open_jiras_2)+" "+str_issues(ocs_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=104892\">"+str(ocs_closed_jiras_2)+" "+str_issues(ocs_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(ocs_total_jiras)+" "+str_issues(ocs_total_jiras)+"</td></tr>\n")


f.write("<tr align=\"center\"><td>BIS</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=104889\">"+str(bis_open_jiras_2)+" "+str_issues(bis_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=104890\">"+str(bis_closed_jiras_2)+" "+str_issues(bis_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(bis_total_jiras)+" "+str_issues(bis_total_jiras)+"</td></tr>\n")



#f.write("<tr align=\"center\"><td>NetAn</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?jql=filter%3D101745%20\">"+str(netan_open_jiras)+" "+str_issues(netan_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?jql=filter%3D101746%20\">"+str(netan_closed_jiras)+" "+str_issues(netan_closed_jiras)+"</a></td> \
  #<td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101747\">"+str(netan_open_jiras_2)+" "+str_issues(netan_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101748\">"+str(netan_closed_jiras_2)+" "+str_issues(netan_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(netan_total_jiras)+" "+str_issues(netan_total_jiras)+"</td></tr>\n")

f.write("<tr align=\"center\"><td>NetAn</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101747\">"+str(netan_open_jiras_2)+" "+str_issues(netan_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101748\">"+str(netan_closed_jiras_2)+" "+str_issues(netan_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(netan_total_jiras)+" "+str_issues(netan_total_jiras)+"</td></tr>\n")

#f.write("<tr align=\"center\"><td>NMI</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?jql=filter%3D101751%20\">"+str(nmi_open_jiras)+" "+str_issues(nmi_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?jql=filter%3D101752%20\">"+str(nmi_closed_jiras)+" "+str_issues(nmi_closed_jiras)+"</a></td> \
  #<td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101753\">"+str(nmi_open_jiras_2)+" "+str_issues(nmi_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101754\">"+str(nmi_closed_jiras_2)+" "+str_issues(nmi_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(nmi_total_jiras)+" "+str_issues(nmi_total_jiras)+"</td></tr>\n")

f.write("<tr align=\"center\"><td>NMI</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101753\">"+str(nmi_open_jiras_2)+" "+str_issues(nmi_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101754\">"+str(nmi_closed_jiras_2)+" "+str_issues(nmi_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(nmi_total_jiras)+" "+str_issues(nmi_total_jiras)+"</td></tr>\n")

#f.write("<tr align=\"center\"><td>Security</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?jql=filter%3D101764%20\">"+str(sec_open_jiras)+" "+str_issues(sec_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?jql=filter%3D101765%20\">"+str(sec_closed_jiras)+" "+str_issues(sec_closed_jiras)+"</a></td> \
 # <td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101766\">"+str(sec_open_jiras_2)+" "+str_issues(sec_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101767\">"+str(sec_closed_jiras_2)+" "+str_issues(sec_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(sec_total_jiras)+" "+str_issues(sec_total_jiras)+"</td></tr>\n")

f.write("<tr align=\"center\"><td>Security</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101766\">"+str(sec_open_jiras_2)+" "+str_issues(sec_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101767\">"+str(sec_closed_jiras_2)+" "+str_issues(sec_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(sec_total_jiras)+" "+str_issues(sec_total_jiras)+"</td></tr>\n")

#f.write("<tr align=\"center\"><td>TP-KPI</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?jql=filter%3D101770%20\">"+str(tp_open_jiras)+" "+str_issues(tp_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?jql=filter%3D101771%20\">"+str(tp_closed_jiras)+" "+str_issues(tp_closed_jiras)+"</a></td> \
#  <td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101772\">"+str(tp_open_jiras_2)+" "+str_issues(tp_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101773\">"+str(tp_closed_jiras_2)+" "+str_issues(tp_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(tp_total_jiras)+" "+str_issues(tp_total_jiras)+"</td></tr>\n")

f.write("<tr align=\"center\"><td>TP-KPI</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101772\">"+str(tp_open_jiras_2)+" "+str_issues(tp_open_jiras_2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=101773\">"+str(tp_closed_jiras_2)+" "+str_issues(tp_closed_jiras_2)+"</a></td><td><font color=\"blue\">"+str(tp_total_jiras)+" "+str_issues(tp_total_jiras)+"</td></tr>\n")

f.write("<tr align=\"center\"><b><td colspan='4'> Total Number Of Unique Issues: "+str(overall_count)+" " +str_issues(overall_count)+"</td></b></tr>\n")

f.write("</table></br></br>\n")

#f.write("<table border=\"3\"><b><th>Class</th><th>Count</th></b>\n")
#f.write("<tr align=\"center\"><td>Class_A</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=83168\">"+str(class_A)+" "+str_issues(class_A)+"</a></td></tr>\n")
#f.write("<tr align=\"center\"><td>Class_B</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=83169\">"+str(class_B)+" "+str_issues(class_B)+"</a></td></tr>\n")
#f.write("<tr align=\"center\"><td>Class_C</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=83170\">"+str(class_C)+" "+str_issues(class_C)+"</a></td></tr>\n")
#f.write("<tr align=\"center\"><td>Not assessed</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=83171\">"+str(not_assessed)+" "+str_issues(not_assessed)+"</a></td></tr>\n")
#f.write("</table></br></br></br>")

f.write("</body></html>")
f.close()
