'''
@author : zhshees
Created on Dec,21
'''
import datetime
from jira import JIRA
from datetime import date

def str_issues(num):
    if num == 1:
        return "issue"
    else:
        return "issues"

#jiraOptions = {'server': "https://jira-oss.seli.wh.rnd.internal.ericsson.com"}
jiraOptions = {'server': "https://eteamproject.internal.ericsson.com/"}

jira = JIRA(options=jiraOptions, basic_auth=("esjkadm100", "Naples!0512"))

############### jira filters (last week)  ####################

TP_open_jiras = len(jira.search_issues("filter=261571"))
TP_closed_jiras = len(jira.search_issues("filter=261572"))
kpi_open_jiras = len(jira.search_issues("filter=261870"))
kpi_closed_jiras = len(jira.search_issues("filter=261871"))
nmi_open_jiras = len(jira.search_issues("filter=261872"))
nmi_closed_jiras = len(jira.search_issues("filter=261873"))
nmisap_open_jiras = len(jira.search_issues("filter=261874"))
nmisap_closed_jiras = len(jira.search_issues("filter=261875"))
netan_open_jiras = len(jira.search_issues("filter=261970"))
netan_closed_jiras = len(jira.search_issues("filter=261971"))
bo_ocs_open_jiras = len(jira.search_issues("filter=261972"))
bo_ocs_closed_jiras = len(jira.search_issues("filter=261973"))
infra_open_jiras = len(jira.search_issues("filter=261974"))
infra_closed_jiras = len(jira.search_issues("filter=261975"))
pf_open_jiras = len(jira.search_issues("filter=261976"))
pf_closed_jiras = len(jira.search_issues("filter=261977"))
#epfg_open_jiras = len(jira.search_issues("filter=102242"))
#epfg_closed_jiras = len(jira.search_issues("filter=102243"))
ddc_ddp_open_jiras = len(jira.search_issues("filter=261978"))
ddc_ddp_closed_jiras = len(jira.search_issues("filter=261979"))
sec_open_jiras = len(jira.search_issues("filter=261980"))
sec_closed_jiras = len(jira.search_issues("filter=261981"))

############### jira filters (last 2nd week)  ####################

TP_open_jiras2 = len(jira.search_issues("filter=262070"))
TP_closed_jiras2 = len(jira.search_issues("filter=262072"))
kpi_open_jiras2 = len(jira.search_issues("filter=262073"))
kpi_closed_jiras2 = len(jira.search_issues("filter=262074"))
nmi_open_jiras2 = len(jira.search_issues("filter=262075"))
nmi_closed_jiras2 = len(jira.search_issues("filter=262076"))
nmisap_open_jiras2 = len(jira.search_issues("filter=262077"))
nmisap_closed_jiras2 = len(jira.search_issues("filter=262078"))
netan_open_jiras2 = len(jira.search_issues("filter=262079"))
netan_closed_jiras2 = len(jira.search_issues("filter=262080"))
bo_ocs_open_jiras2 = len(jira.search_issues("filter=262081"))
bo_ocs_closed_jiras2 = len(jira.search_issues("filter=262082"))
infra_open_jiras2 = len(jira.search_issues("filter=262083"))
infra_closed_jiras2 = len(jira.search_issues("filter=262086"))
pf_open_jiras2 = len(jira.search_issues("filter=262087"))
pf_closed_jiras2 = len(jira.search_issues("filter=262088"))
#epfg_open_jiras2 = len(jira.search_issues("filter=102760"))
#epfg_closed_jiras2 = len(jira.search_issues("filter=102761"))
ddc_ddp_open_jiras2 = len(jira.search_issues("filter=262089"))
ddc_ddp_closed_jiras2 = len(jira.search_issues("filter=262090"))
sec_open_jiras2 = len(jira.search_issues("filter=262091"))
sec_closed_jiras2 = len(jira.search_issues("filter=262092"))

########################### jira filters (last 3rd week) #####################

TP_open_jiras3 = len(jira.search_issues("filter=261982"))
TP_closed_jiras3 = len(jira.search_issues("filter=261983"))
kpi_open_jiras3 = len(jira.search_issues("filter=261984"))
kpi_closed_jiras3 = len(jira.search_issues("filter=263676"))
nmi_open_jiras3 = len(jira.search_issues("filter=261987"))
nmi_closed_jiras3 = len(jira.search_issues("filter=261989"))
nmisap_open_jiras3 = len(jira.search_issues("filter=263676"))
nmisap_closed_jiras3 = len(jira.search_issues("filter=261991"))
netan_open_jiras3 = len(jira.search_issues("filter=261992"))
netan_closed_jiras3 = len(jira.search_issues("filter=261993"))
bo_ocs_open_jiras3 = len(jira.search_issues("filter=261994"))
bo_ocs_closed_jiras3 = len(jira.search_issues("filter=261996"))
infra_open_jiras3 = len(jira.search_issues("filter=261997"))
infra_closed_jiras3 = len(jira.search_issues("filter=261998"))
pf_open_jiras3 = len(jira.search_issues("filter=261999"))
pf_closed_jiras3 = len(jira.search_issues("filter=262000"))
#epfg_open_jiras3 = len(jira.search_issues("filter=102837"))
#epfg_closed_jiras3 = len(jira.search_issues("filter=102838"))
ddc_ddp_open_jiras3 = len(jira.search_issues("filter=262001"))
ddc_ddp_closed_jiras3 = len(jira.search_issues("filter=262002"))
sec_open_jiras3 = len(jira.search_issues("filter=262006"))
sec_closed_jiras3 = len(jira.search_issues("filter=262008"))

################ Open total team basis #####################
#tp_total_team = TP_open_jiras + TP_open_jiras2 + TP_open_jiras3
tp_total_team = len(jira.search_issues("filter=262095"))
kpi_total_team = len(jira.search_issues("filter=262096"))
nmi_total_team = len(jira.search_issues("filter=262097"))
nmisap_total_team = len(jira.search_issues("filter=262100"))
netan_total_team = len(jira.search_issues("filter=262101"))
bo_ocs_total_team = len(jira.search_issues("filter=262102"))
infra_total_team = len(jira.search_issues("filter=262103"))
pf_total_team = len(jira.search_issues("filter=262104"))
#epfg_total_team = len(jira.search_issues("filter=105067"))
ddc_ddp_total_team  = len(jira.search_issues("filter=262105"))
sec_total_team = len(jira.search_issues("filter=262106"))

############## Total unique issues/jiras #################
#uni_open_last = len(jira.search_issues("filter=102743"))
#uni_closed_last = len(jira.search_issues("filter=102744"))
#uni_open_last2 = len(jira.search_issues("filter=102740"))
#uni_closed_last2 = len(jira.search_issues("filter=102741"))
#uni_open_last3 = len(jira.search_issues("filter=102843"))
#uni_closed_last3 = len(jira.search_issues("filter=102844"))
unique_total = len(jira.search_issues("filter=262108"))

uni_open_last = sec_open_jiras + infra_open_jiras + bo_ocs_open_jiras + netan_open_jiras + kpi_open_jiras + TP_open_jiras + pf_open_jiras + ddc_ddp_open_jiras + nmisap_open_jiras + nmi_open_jiras
uni_closed_last = nmi_closed_jiras + nmisap_closed_jiras + ddc_ddp_closed_jiras + pf_closed_jiras + TP_closed_jiras + kpi_closed_jiras + netan_closed_jiras + bo_ocs_closed_jiras + infra_closed_jiras + sec_closed_jiras
uni_open_last2 = nmi_open_jiras2 + nmisap_open_jiras2 + ddc_ddp_open_jiras2 + pf_open_jiras2 + TP_open_jiras2 + kpi_open_jiras2 + netan_open_jiras2 + bo_ocs_open_jiras2 + infra_open_jiras2 + sec_open_jiras2
uni_closed_last2 = sec_closed_jiras2 + infra_closed_jiras2 + bo_ocs_closed_jiras2 + netan_closed_jiras2 + kpi_closed_jiras2 + TP_closed_jiras2 + pf_closed_jiras2 + ddc_ddp_closed_jiras2 + nmisap_closed_jiras2 + nmi_closed_jiras2
uni_open_last3 = sec_open_jiras3 + infra_open_jiras3 + bo_ocs_open_jiras3 + netan_open_jiras3 + kpi_open_jiras3 + TP_open_jiras3 + pf_open_jiras3 + ddc_ddp_open_jiras3 + nmisap_open_jiras3 + nmi_open_jiras3
uni_closed_last3 = nmi_closed_jiras3 + nmisap_closed_jiras3 + ddc_ddp_closed_jiras3 + pf_closed_jiras3 + TP_closed_jiras3 + kpi_closed_jiras3 + netan_closed_jiras3 + bo_ocs_closed_jiras3 + infra_closed_jiras3 + sec_closed_jiras3

############### GA Blocker jiras ############
nmi_ga = len(jira.search_issues("filter=262110"))
nmisap_ga = len(jira.search_issues("filter=262111"))
ddc_ga  = len(jira.search_issues("filter=262112"))
pf_ga = len(jira.search_issues("filter=262113"))
tp_ga = len(jira.search_issues("filter=262114"))
kpi_ga = len(jira.search_issues("filter=262115"))
netan_ga = len(jira.search_issues("filter=262116"))
bo_ga = len(jira.search_issues("filter=262117"))
infra_ga = len(jira.search_issues("filter=262118"))
sec_ga = len(jira.search_issues("filter=262119"))
#epfg_ga = len(jira.search_issues("filter=106188"))
total_ga = len(jira.search_issues("filter=262120"))

################### team ga status count jiras ################
nmi_inprog_ga = len(jira.search_issues("filter=262010"))
nmi_hold_ga = len(jira.search_issues("filter=262011"))
nmi_open_ga = len(jira.search_issues("filter=262012"))
nmi_resolve_ga = len(jira.search_issues("filter=264783"))
nmi_review_ga = len(jira.search_issues("filter=262013"))
nmi_sap_inprog_ga = len(jira.search_issues("filter=262014"))
nmi_sap_hold_ga = len(jira.search_issues("filter=262015"))
nmi_sap_open_ga = len(jira.search_issues("filter=262019"))
nmi_sap_resolved_ga = len(jira.search_issues("filter=262472"))
nmi_sap_review_ga = len(jira.search_issues("filter=262021"))
ddc_inprog_ga = len(jira.search_issues("filter=262024"))
ddc_hold_ga = len(jira.search_issues("filter=262025"))
ddc_resolve_ga = len(jira.search_issues("filter=262474"))
ddc_open_ga = len(jira.search_issues("filter=262028"))
ddc_review_ga = len(jira.search_issues("filter=264784"))
pf_inprog_ga = len(jira.search_issues("filter=262036"))
pf_hold_ga = len(jira.search_issues("filter=262037"))
pf_resolve_ga = len(jira.search_issues("filter=262475"))
pf_open_ga = len(jira.search_issues("filter=262038"))
pf_review_ga = len(jira.search_issues("filter=262039"))
tp_inprog_ga = len(jira.search_issues("filter=262040"))
tp_hold_ga = len(jira.search_issues("filter=262042"))
tp_resolve_ga = len(jira.search_issues("filter=262476"))
tp_open_ga = len(jira.search_issues("filter=262043"))
tp_review_ga = len(jira.search_issues("filter=262044"))
kpi_inprog_ga = len(jira.search_issues("filter=262045"))
kpi_hold_ga = len(jira.search_issues("filter=262046"))
kpi_resolve_ga = len(jira.search_issues("filter=262477"))
kpi_open_ga = len(jira.search_issues("filter=262047"))
kpi_review_ga = len(jira.search_issues("filter=262048"))
netan_inprog_ga = len(jira.search_issues("filter=262049"))
netan_hold_ga = len(jira.search_issues("filter=262050"))
netan_resolve_ga = len(jira.search_issues("filter=262481"))
netan_open_ga = len(jira.search_issues("filter=262051"))
netan_review_ga = len(jira.search_issues("filter=262052"))
bo_inprog_ga = len(jira.search_issues("filter=262053"))
bo_hold_ga = len(jira.search_issues("filter=262054"))
bo_resolve_ga = len(jira.search_issues("filter=262480"))
bo_open_ga = len(jira.search_issues("filter=262055"))
bo_review_ga = len(jira.search_issues("filter=262056"))
infra_inprog_ga = len(jira.search_issues("filter=262057"))
infra_hold_ga = len(jira.search_issues("filter=262058"))
infra_resolve_ga = len(jira.search_issues("filter=262479"))
infra_open_ga = len(jira.search_issues("filter=262059"))
infra_review_ga = len(jira.search_issues("filter=262060"))
sec_inprog_ga = len(jira.search_issues("filter=262061"))
sec_hold_ga = len(jira.search_issues("filter=262062"))
sec_resolve_ga = len(jira.search_issues("filter=264785"))
sec_open_ga = len(jira.search_issues("filter=262063"))
sec_review_ga = len(jira.search_issues("filter=262064"))
#epfg_inprog_ga = len(jira.search_issues("filter=107859"))
#epfg_hold_ga = len(jira.search_issues("filter=107860"))
#epfg_resolve_ga = len(jira.search_issues("filter=107861"))
#epfg_open_ga = len(jira.search_issues("filter=107862"))

###################### team open jiras status #################
nmi_inprog = len(jira.search_issues("filter=262130"))
nmi_hold = len(jira.search_issues("filter=264786"))
nmi_resolve = len(jira.search_issues("filter=262384"))
nmi_open = len(jira.search_issues("filter=264787"))
nmi_re = len(jira.search_issues("filter=264878"))
nmi_sap_inprog = len(jira.search_issues("filter=262133"))
nmi_sap_hold = len(jira.search_issues("filter=262134"))
nmi_sap_resolve = len(jira.search_issues("filter=262383"))
nmi_sap_open = len(jira.search_issues("filter=262135"))
nmi_sap_re = len(jira.search_issues("filter=262136"))
ddc_inprog = len(jira.search_issues("filter=262137"))
ddc_hold = len(jira.search_issues("filter=262138"))
ddc_resolve = len(jira.search_issues("filter=262386"))
ddc_open = len(jira.search_issues("filter=262139"))
ddc_re = len(jira.search_issues("filter=262140"))
pf_open = len(jira.search_issues("filter=262141"))
pf_resolve = len(jira.search_issues("filter=262387"))
pf_hold = len(jira.search_issues("filter=262142"))
pf_inprog = len(jira.search_issues("filter=262144"))
pf_re = len(jira.search_issues("filter=262145"))
tp_inprog = len(jira.search_issues("filter=262146"))
tp_open = len(jira.search_issues("filter=262147"))
tp_hold = len(jira.search_issues("filter=262148"))
tp_resolve = len(jira.search_issues("filter=262388"))
tp_re = len(jira.search_issues("filter=262149"))
kpi_inprog = len(jira.search_issues("filter=262150"))
kpi_hold = len(jira.search_issues("filter=262151"))
kpi_resolve = len(jira.search_issues("filter=262391"))
kpi_open = len(jira.search_issues("filter=262152"))
kpi_re = len(jira.search_issues("filter=262153"))
netan_inprog = len(jira.search_issues("filter=262155"))
netan_hold = len(jira.search_issues("filter=262156"))
netan_resolve = len(jira.search_issues("filter=264788"))
netan_open = len(jira.search_issues("filter=262157"))
netan_re = len(jira.search_issues("filter=262158"))
bo_inprog = len(jira.search_issues("filter=262159"))
bo_hold = len(jira.search_issues("filter=262160"))
bo_resolve = len(jira.search_issues("filter=262392"))
bo_open = len(jira.search_issues("filter=262162"))
bo_re = len(jira.search_issues("filter=262164"))
infra_inprog = len(jira.search_issues("filter=262165"))
infra_hold = len(jira.search_issues("filter=262166"))
infra_resolve = len(jira.search_issues("filter=262393"))
infra_open = len(jira.search_issues("filter=262167"))
infra_re = len(jira.search_issues("filter=262168"))
sec_inprog = len(jira.search_issues("filter=262169"))
sec_hold = len(jira.search_issues("filter=262370"))
sec_resolve = len(jira.search_issues("filter=262395"))
sec_open = len(jira.search_issues("filter=262371"))
sec_re = len(jira.search_issues("filter=262372"))

############### total status GA ##############
total_inprog_ga = len(jira.search_issues("filter=264789"))
total_hold_ga = len(jira.search_issues("filter=264790"))
total_resolve_ga = len(jira.search_issues("filter=264791"))
total_open_ga = len(jira.search_issues("filter=264792"))
total_review_ga = len(jira.search_issues("filter=264793"))

################## total status main table ##################
total_open = nmi_open + nmi_sap_open + sec_open + infra_open + bo_open + netan_open + kpi_open + tp_open + pf_open + ddc_open
total_inprog = sec_inprog + infra_inprog + bo_inprog + netan_inprog + kpi_inprog + tp_inprog + pf_inprog + ddc_inprog + nmi_inprog + nmi_sap_inprog
total_hold = sec_hold + bo_hold + netan_hold + kpi_hold + tp_hold + pf_hold + ddc_hold + nmi_hold + nmi_sap_hold + infra_hold
total_resolve = sec_resolve + infra_resolve + bo_resolve + netan_resolve + kpi_resolve + tp_resolve + pf_resolve + ddc_resolve + nmi_resolve + nmi_sap_resolve
total_review = sec_re + infra_re + bo_re + netan_re + kpi_re + tp_re + pf_re + ddc_re + nmi_re + nmi_sap_re
total_others = len(jira.search_issues("filter=264794"))

#################### total unique without filter ####################
uniq_total = tp_total_team + kpi_total_team + nmi_total_team + nmisap_total_team + netan_total_team + bo_ocs_total_team + infra_total_team + pf_total_team + ddc_ddp_total_team + sec_total_team

################# Overall status count jiras (small table) #################
#in_prog = len(jira.search_issues("filter=107950"))
#on_hold = len(jira.search_issues("filter=107951"))
#resolved = len(jira.search_issues("filter=107952"))
#Opened = len(jira.search_issues("filter=107949"))

ClassC_total_op = len(jira.search_issues("filter=264795"))
ClassC_total_Inpro = len(jira.search_issues("filter=264796"))
ClassC_total_OnHo = len(jira.search_issues("filter=264797"))
ClassC_total_Reso = len(jira.search_issues("filter=264798"))
ClassC_total_Oth = len(jira.search_issues("filter=264799"))

ClassB_total_op = len(jira.search_issues("filter=264800"))
ClassB_total_Inpro = len(jira.search_issues("filter=264801"))
ClassB_total_OnHo = len(jira.search_issues("filter=264802"))
ClassB_total_Reso = len(jira.search_issues("filter=264803"))
ClassB_total_Oth = len(jira.search_issues("filter=264804"))

ClassA_total_op = len(jira.search_issues("filter=264814"))
ClassA_total_Inpro = len(jira.search_issues("filter=264813"))
ClassA_total_OnHo = len(jira.search_issues("filter=264812"))
ClassA_total_Reso = len(jira.search_issues("filter=264811"))
ClassA_total_Oth = len(jira.search_issues("filter=264805"))

ClassUn_total_op = len(jira.search_issues("filter=264810"))
ClassUn_total_Inpro = len(jira.search_issues("filter=264809"))
ClassUn_total_OnHo = len(jira.search_issues("filter=264808"))
ClassUn_total_Reso = len(jira.search_issues("filter=264807"))
ClassUn_total_Oth = len(jira.search_issues("filter=264806"))

year, week_num, day_of_week = datetime.date.today().isocalendar()

f = open('/home/esjkadm100/zhshees/report.html','w')

f.write("<b>Hi All,</b>")
f.write("<br><br><b>Please find the BUGs status as of "+str(date.today().strftime('%B %d, %Y'))+"</b>")

f.write('<br><br><b>Current BUG count : </b>')
#if uni_open_last <=10:
if unique_total <= 10:
	f.write("<font color=\'black\' <td><a>"+str(unique_total)+"</a></td></font>")
else:
	f.write("<font color=\'red\' <td><a>"+str(unique_total)+"</a></td></font>")

f.write('<br><br><a href=\"https://eteamproject.internal.ericsson.com/secure/Dashboard.jspa?selectPageId=84017\">Dashboard link for open BUGs</a><br>')

f.write("<table><br>\n")
f.write("<table border=\"2\"><tr style='background-color:#e0ff44;'><b><font style='font-family:arial;'><th rowspan='1'>Overall Status</th><th>Class A</th><th>Class B</th><th>Class C</th><th>Unaccessed</th></font></b></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td align=\"left\"><a><b>Open/Reopened: </b>"+str(total_open)+" "+str_issues(total_open)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122956\">"+str(ClassA_total_op)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122955\">"+str(ClassB_total_op)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122947\">"+str(ClassC_total_op)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122957\">"+str(ClassUn_total_op)+"</a></td></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td align=\"left\"><a><b>In-Progress: </b>"+str(total_inprog)+" "+str_issues(total_inprog)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122959\">"+str(ClassA_total_Inpro)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122958\">"+str(ClassB_total_Inpro)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122948\">"+str(ClassC_total_Inpro)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122960\">"+str(ClassUn_total_Inpro)+"</a></td></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td align=\"left\"><a><b>On-Hold: </b>"+str(total_hold)+" "+str_issues(total_hold)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=123253\">"+str(ClassA_total_OnHo)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=123252\">"+str(ClassB_total_OnHo)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122949\">"+str(ClassC_total_OnHo)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=123254\">"+str(ClassUn_total_OnHo)+"</a></td></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td align=\"left\"><a><b>Resolved: </b>"+str(total_resolve)+" "+str_issues(total_resolve)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122962\">"+str(ClassA_total_Reso)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122961\">"+str(ClassB_total_Reso)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122950\">"+str(ClassC_total_Reso)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122964\">"+str(ClassUn_total_Reso)+"</a></td></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td align=\"left\"><a><b>Others: </b>"+str(total_others)+" "+str_issues(total_others)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122953\">"+str(ClassA_total_Oth)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122952\">"+str(ClassB_total_Oth)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122951\">"+str(ClassC_total_Oth)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=122954\">"+str(ClassUn_total_Oth)+"</a></td></tr>\n")

#f.write("<tr align=\"center\"><font style='font-family:arial;'><td align=\"left\"><a><b>Resolved(In-Test): </b>"+str(resolved_test)+" "+str_issues(resolved_test)+"</a></td></tr>\n")

f.write("</table></br>\n")

f.write("<b><u><font size='2' style='font-family:arial;'><u><b>NOTE</b></u></font></u></b><br>")
f.write("<b><font size='1' style='font-family:arial;'>Open: </b><i>Analysis/work to be started</i><b>, In Progress: </b><i>Design work is in-progress</i><b>, On-Hold: </b><i>Under monitor/ paused due to some dependency</i><b>, Resolved: </b><i>Design activity completed and under test</i><b>, Others: </b><i>Any other JIRA status. e.g. Review etc.</i></font><br>")

f.write('<br><b><u>GA BLOCKER BUGs details</u></b>')

f.write("</table></br></br>\n")

f.write("<table border=\"2\"><tr style='background-color:#e0ff44;'><b><font style='font-family:arial;'><th rowspan='2'>Team</th><th rowspan='2'>GA Blocker</th><th rowspan='13'></th><th colspan='5'>Status</th></font></b></tr>\n")

f.write("<tr align=\"center\"><b><font style='font-family:arial;'><td style='background-color:#e0ff44;'>Open/Reopened</td><td style='background-color:#e0ff44;'>In-Progress</td><td style='background-color:#e0ff44;'>On-Hold</td><td style='background-color:#e0ff44;'>Resolved</td><td style='background-color:#e0ff44;'>Review</td></font></b></tr>\n")

################ status cells update with - if 0 ################

############# NMI status #################
if nmi_open_ga == 0:
	nmi_op="<td align=\"center\">-</td>"
else:
	nmi_op="<td align=\"center\">"+str(nmi_open_ga)+"</td>"

if nmi_inprog_ga == 0:
	nmi_inpr="<td align=\"center\">-</td>"
else:
	nmi_inpr="<td align=\"center\">"+str(nmi_inprog_ga)+"</td>"

if nmi_hold_ga == 0:
	nmi_ho="<td align=\"center\">-</td>"
else:
	nmi_ho="<td align=\"center\">"+str(nmi_hold_ga)+"</td>"

if nmi_resolve_ga == 0:
	nmi_reso="<td align=\"center\">-</td>"
else:
	nmi_reso="<td align=\"center\">"+str(nmi_resolve_ga)+"</td>"

if nmi_review_ga == 0:
        nmi_rev="<td align=\"center\">-</td>"
else:
        nmi_rev="<td align=\"center\">"+str(nmi_review_ga)+"</td>"

################### NMI-SAP status ####################
if nmi_sap_open_ga == 0:
        nmi_sap_op="<td align=\"center\">-</td>"
else:
        nmi_sap_op="<td align=\"center\">"+str(nmi_sap_open_ga)+"</td>"

if nmi_sap_inprog_ga == 0:
        nmi_sap_inpr="<td align=\"center\">-</td>"
else:
        nmi_sap_inpr="<td align=\"center\">"+str(nmi_sap_inprog_ga)+"</td>"

if nmi_sap_hold_ga == 0:
        nmi_sap_ho="<td align=\"center\">-</td>"
else:
        nmi_sap_ho="<td align=\"center\">"+str(nmi_sap_hold_ga)+"</td>"

if nmi_sap_resolved_ga == 0:
        nmi_sap_reso="<td align=\"center\">-</td>"
else:
        nmi_sap_reso="<td align=\"center\">"+str(nmi_sap_resolved_ga)+"</td>"

if nmi_sap_review_ga == 0:
        nmi_sap_rev="<td align=\"center\">-</td>"
else:
        nmi_sap_rev="<td align=\"center\">"+str(nmi_sap_review_ga)+"</td>"

################### DDC/DDP status #####################
if ddc_open_ga == 0:
        ddc_op="<td align=\"center\">-</td>"
else:
        ddc_op="<td align=\"center\">"+str(ddc_open_ga)+"</td>"

if ddc_inprog_ga == 0:
        ddc_inpr="<td align=\"center\">-</td>"
else:
        ddc_inpr="<td align=\"center\">"+str(ddc_inprog_ga)+"</td>"

if ddc_hold_ga == 0:
        ddc_ho="<td align=\"center\">-</td>"
else:
        ddc_ho="<td align=\"center\">"+str(ddc_hold_ga)+"</td>"

if ddc_resolve_ga == 0:
        ddc_reso="<td align=\"center\">-</td>"
else:
        ddc_reso="<td align=\"center\">"+str(ddc_resolve_ga)+"</td>"

if ddc_review_ga == 0:
        ddc_rev="<td align=\"center\">-</td>"
else:
        ddc_rev="<td align=\"center\">"+str(ddc_review_ga)+"</td>"

####################### PF status ########################
if pf_open_ga == 0:
        pf_op="<td align=\"center\">-</td>"
else:
        pf_op="<td align=\"center\">"+str(pf_open_ga)+"</td>"

if pf_inprog_ga == 0:
        pf_inpr="<td align=\"center\">-</td>"
else:
        pf_inpr="<td align=\"center\">"+str(pf_inprog_ga)+"</td>"

if pf_hold_ga == 0:
        pf_ho="<td align=\"center\">-</td>"
else:
        pf_ho="<td align=\"center\">"+str(pf_hold_ga)+"</td>"

if pf_resolve_ga == 0:
        pf_reso="<td align=\"center\">-</td>"
else:
        pf_reso="<td align=\"center\">"+str(pf_resolve_ga)+"</td>"

if pf_review_ga == 0:
        pf_rev="<td align=\"center\">-</td>"
else:
        pf_rev="<td align=\"center\">"+str(pf_review_ga)+"</td>"

########################## TP status #######################
if tp_open_ga == 0:
        tp_op="<td align=\"center\">-</td>"
else:
        tp_op="<td align=\"center\">"+str(tp_open_ga)+"</td>"

if tp_inprog_ga == 0:
        tp_inpr="<td align=\"center\">-</td>"
else:
        tp_inpr="<td align=\"center\">"+str(tp_inprog_ga)+"</td>"

if tp_hold_ga == 0:
        tp_ho="<td align=\"center\">-</td>"
else:
        tp_ho="<td align=\"center\">"+str(tp_hold_ga)+"</td>"

if tp_resolve_ga == 0:
        tp_reso="<td align=\"center\">-</td>"
else:
        tp_reso="<td align=\"center\">"+str(tp_resolve_ga)+"</td>"

if tp_review_ga == 0:
        tp_rev="<td align=\"center\">-</td>"
else:
        tp_rev="<td align=\"center\">"+str(tp_review_ga)+"</td>"

####################### KPI status ####################
if kpi_open_ga == 0:
        kpi_op="<td align=\"center\">-</td>"
else:
        kpi_op="<td align=\"center\">"+str(kpi_open_ga)+"</td>"

if kpi_inprog_ga == 0:
        kpi_inpr="<td align=\"center\">-</td>"
else:
        kpi_inpr="<td align=\"center\">"+str(kpi_inprog_ga)+"</td>"

if kpi_hold_ga == 0:
        kpi_ho="<td align=\"center\">-</td>"
else:
        kpi_ho="<td align=\"center\">"+str(kpi_hold_ga)+"</td>"

if kpi_resolve_ga == 0:
        kpi_reso="<td align=\"center\">-</td>"
else:
        kpi_reso="<td align=\"center\">"+str(kpi_resolve_ga)+"</td>"

if kpi_review_ga == 0:
        kpi_rev="<td align=\"center\">-</td>"
else:
        kpi_rev="<td align=\"center\">"+str(kpi_review_ga)+"</td>"

#################### Netan status ##################
if netan_open_ga == 0:
        netan_op="<td align=\"center\">-</td>"
else:
        netan_op="<td align=\"center\">"+str(netan_open_ga)+"</td>"

if netan_inprog_ga == 0:
        netan_inpr="<td align=\"center\">-</td>"
else:
        netan_inpr="<td align=\"center\">"+str(netan_inprog_ga)+"</td>"

if netan_hold_ga == 0:
        netan_ho="<td align=\"center\">-</td>"
else:
        netan_ho="<td align=\"center\">"+str(netan_hold_ga)+"</td>"

if netan_resolve_ga == 0:
        netan_reso="<td align=\"center\">-</td>"
else:
        netan_reso="<td align=\"center\">"+str(netan_resolve_ga)+"</td>"

if netan_review_ga == 0:
        netan_rev="<td align=\"center\">-</td>"
else:
        netan_rev="<td align=\"center\">"+str(netan_review_ga)+"</td>"

##################### BO/OCS status ######################
if bo_open_ga == 0:
        bo_op="<td align=\"center\">-</td>"
else:
        bo_op="<td align=\"center\">"+str(bo_open_ga)+"</td>"

if bo_inprog_ga == 0:
        bo_inpr="<td align=\"center\">-</td>"
else:
        bo_inpr="<td align=\"center\">"+str(bo_inprog_ga)+"</td>"

if bo_hold_ga == 0:
        bo_ho="<td align=\"center\">-</td>"
else:
        bo_ho="<td align=\"center\">"+str(bo_hold_ga)+"</td>"

if bo_resolve_ga == 0:
        bo_reso="<td align=\"center\">-</td>"
else:
        bo_reso="<td align=\"center\">"+str(bo_resolve_ga)+"</td>"

if bo_review_ga == 0:
        bo_rev="<td align=\"center\">-</td>"
else:
        bo_rev="<td align=\"center\">"+str(bo_review_ga)+"</td>"

########################### Infra status #########################
if infra_open_ga == 0:
        infra_op="<td align=\"center\">-</td>"
else:
        infra_op="<td align=\"center\">"+str(infra_open_ga)+"</td>"

if infra_inprog_ga == 0:
        infra_inpr="<td align=\"center\">-</td>"
else:
        infra_inpr="<td align=\"center\">"+str(infra_inprog_ga)+"</td>"

if infra_hold_ga == 0:
        infra_ho="<td align=\"center\">-</td>"
else:
        infra_ho="<td align=\"center\">"+str(infra_hold_ga)+"</td>"

if infra_resolve_ga == 0:
        infra_reso="<td align=\"center\">-</td>"
else:
        infra_reso="<td align=\"center\">"+str(infra_resolve_ga)+"</td>"

if infra_review_ga == 0:
        infra_rev="<td align=\"center\">-</td>"
else:
        infra_rev="<td align=\"center\">"+str(infra_review_ga)+"</td>"

######################## Security status ############################
if sec_open_ga == 0:
        sec_op="<td align=\"center\">-</td>"
else:
        sec_op="<td align=\"center\">"+str(sec_open_ga)+"</td>"

if sec_inprog_ga == 0:
        sec_inpr="<td align=\"center\">-</td>"
else:
        sec_inpr="<td align=\"center\">"+str(sec_inprog_ga)+"</td>"

if sec_hold_ga == 0:
        sec_ho="<td align=\"center\">-</td>"
else:
        sec_ho="<td align=\"center\">"+str(sec_hold_ga)+"</td>"

if sec_resolve_ga == 0:
        sec_reso="<td align=\"center\">-</td>"
else:
        sec_reso="<td align=\"center\">"+str(sec_resolve_ga)+"</td>"

if sec_review_ga == 0:
        sec_rev="<td align=\"center\">-</td>"
else:
        sec_rev="<td align=\"center\">"+str(sec_review_ga)+"</td>"

#################### total status GA ###################
if total_inprog_ga == 0:
        total_inpr="<td align=\"center\">-</td>"
else:
        total_inpr="<td align=\"center\">"+str(total_inprog_ga)+"</td>"

if total_open_ga == 0:
        total_op="<td align=\"center\">-</td>"
else:
        total_op="<td align=\"center\">"+str(total_open_ga)+"</td>"

if total_hold_ga == 0:
        total_ho="<td align=\"center\">-</td>"
else:
        total_ho="<td align=\"center\">"+str(total_hold_ga)+"</td>"

if total_resolve_ga == 0:
        total_reso="<td align=\"center\">-</td>"
else:
        total_reso="<td align=\"center\">"+str(total_resolve_ga)+"</td>"

if total_review_ga == 0:
        total_rev="<td align=\"center\">-</td>"
else:
        total_rev="<td align=\"center\">"+str(total_review_ga)+"</td>"

###########################################################################
if nmi_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106181\"><font color=\"red\">"+str(nmi_ga)+"</font></a></td>"+nmi_op+" "+nmi_inpr+" "+nmi_ho+" "+nmi_reso+" "+nmi_rev+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106181\"><font color=\"blue\">"+str(nmi_ga)+"</font></a></td>"+nmi_op+" "+nmi_inpr+" "+nmi_ho+" "+nmi_reso+" "+nmi_rev+"</font></tr>\n")

if nmisap_ga >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI-SAP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106415\"><font color=\"red\">"+str(nmisap_ga)+"</font></a></td>"+nmi_sap_op+" "+nmi_sap_inpr+" "+nmi_sap_ho+" "+nmi_sap_reso+" "+nmi_sap_rev+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI-SAP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106415\"><font color=\"blue\">"+str(nmisap_ga)+"</font></a></td>"+nmi_sap_op+" "+nmi_sap_inpr+" "+nmi_sap_ho+" "+nmi_sap_reso+" "+nmi_sap_rev+"</font></tr>\n")

if ddc_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>DDC/DDP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106182\"><font color=\"red\">"+str(ddc_ga)+"</font></a></td>"+ddc_op+" "+ddc_inpr+" "+ddc_ho+" "+ddc_reso+" "+ddc_rev+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>DDC/DDP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106182\"><font color=\"blue\">"+str(ddc_ga)+"</font></a></td>"+ddc_op+" "+ddc_inpr+" "+ddc_ho+" "+ddc_reso+" "+ddc_rev+"</font></tr>\n")

if pf_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>PF</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106180\"><font color=\"red\">"+str(pf_ga)+"</font></a></td>"+pf_op+" "+pf_inpr+" "+pf_ho+" "+pf_reso+" "+pf_rev+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>PF</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106180\"><font color=\"blue\">"+str(pf_ga)+"</font></a></td>"+pf_op+" "+pf_inpr+" "+pf_ho+" "+pf_reso+" "+pf_rev+"</font></tr>\n")

if tp_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>TP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106183\"><font color=\"red\">"+str(tp_ga)+"</font></a></td>"+tp_op+" "+tp_inpr+" "+tp_ho+" "+tp_reso+" "+tp_rev+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>TP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106183\"><font color=\"blue\">"+str(tp_ga)+"</font></a></td>"+tp_op+" "+tp_inpr+" "+tp_ho+" "+tp_reso+" "+tp_rev+"</font></tr>\n")

if kpi_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>KPI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107191\"><font color=\"red\">"+str(kpi_ga)+"</font></a></td>"+kpi_op+" "+kpi_inpr+" "+kpi_ho+" "+kpi_reso+" "+kpi_rev+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>KPI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107191\"><font color=\"blue\">"+str(kpi_ga)+"</font></a></td>"+kpi_op+" "+kpi_inpr+" "+kpi_ho+" "+kpi_reso+" "+kpi_rev+"</font></tr>\n")

if netan_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NetAn</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106184\"><font color=\"red\">"+str(netan_ga)+"</font></a></td>"+netan_op+" "+netan_inpr+" "+netan_ho+" "+netan_reso+" "+netan_rev+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NetAn</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106184\"><font color=\"blue\">"+str(netan_ga)+"</font></a></td>"+netan_op+" "+netan_inpr+" "+netan_ho+" "+netan_reso+" "+netan_rev+"</font></tr>\n")

if bo_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>BO/OCS</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106185\"><font color=\"red\">"+str(bo_ga)+"</font></a></td>"+bo_op+" "+bo_inpr+" "+bo_ho+" "+bo_reso+" "+bo_rev+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>BO/OCS</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106185\"><font color=\"blue\">"+str(bo_ga)+"</font></a></td>"+bo_op+" "+bo_inpr+" "+bo_ho+" "+bo_reso+" "+bo_rev+"</font></tr>\n")

if infra_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Infra</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106186\"><font color=\"red\">"+str(infra_ga)+"</font></a></td>"+infra_op+" "+infra_inpr+" "+infra_ho+" "+infra_reso+" "+infra_rev+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Infra</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106186\"><font color=\"blue\">"+str(infra_ga)+"</font></a></td>"+infra_op+" "+infra_inpr+" "+infra_ho+" "+infra_reso+" "+infra_rev+"</font></tr>\n")

if sec_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Security</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106187\"><font color=\"red\">"+str(sec_ga)+"</font></a></td>"+sec_op+" "+sec_inpr+" "+sec_ho+" "+sec_reso+" "+sec_rev+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Security</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106187\"><font color=\"blue\">"+str(sec_ga)+"</font></a></td>"+sec_op+" "+sec_inpr+" "+sec_ho+" "+sec_reso+" "+sec_rev+"</font></tr>\n")

#if epfg_ga >= 1:
#	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>EPFG</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106188\"><font color=\"red\">"+str(epfg_ga)+"</font></a></td><td><a>"+str(epfg_open_ga)+"</a></td><td><a>"+str(epfg_inprog_ga)+"</a></td><td><a>"+str(epfg_hold_ga)+"</a></td><td><a>"+str(epfg_resolve_ga)+"</a></td></font></tr>\n")
#else:
#	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>EPFG</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106188\"><font color=\"blue\">"+str(epfg_ga)+"</font></a></td><td><a>"+str(epfg_open_ga)+"</a></td><td><a>"+str(epfg_inprog_ga)+"</a></td><td><a>"+str(epfg_hold_ga)+"</a></td><td><a>"+str(epfg_resolve_ga)+"</a></td></font></tr>\n")

if total_ga > 0:
	f.write("<tr align=\"center\" style='background-color:#fcdfff;'><font style='font-family:arial;'><b><td>Total</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106189\"><font color=\"red\">"+str(total_ga)+"</font></a></td>"+total_op+" "+total_inpr+" "+total_ho+" "+total_reso+" "+total_rev+"</b></font></tr>\n")
else:
	f.write("<tr align=\"center\" style='background-color:#fcdfff;'><font style='font-family:arial;'><b><td>Total</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106189\"><font color=\"blue\">"+str(total_ga)+"</font></a></td>"+total_op+" "+total_inpr+" "+total_ho+" "+total_reso+" "+total_rev+"</b></font></tr>\n")

#f.write("<tr align=\"center\" style='background-color:#fcdfff;'><font color=\"black\" style='font-family:arial;'><b><td>Total</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106189\">"+str(total_ga)+"</a></td></b></font></tr>\n")

f.write("</table></br>\n")

#f.write("<table><br>\n")
#f.write("<table border=\"2\"><tr style='background-color:#e0ff44;'><b><font style='font-family:arial;'><th rowspan='1'>Overall Status</th></font></b></tr>\n")

#f.write("<tr align=\"center\"><font style='font-family:arial;'><td align=\"left\"><a><b>Open: </b>"+str(Opened)+" "+str_issues(Opened)+"</a></td></tr>\n")

#f.write("<tr align=\"center\"><font style='font-family:arial;'><td align=\"left\"><a><b>In-Progress: </b>"+str(in_prog)+" "+str_issues(in_prog)+"</a></td></tr>\n")

#f.write("<tr align=\"center\"><font style='font-family:arial;'><td align=\"left\"><a><b>On-Hold: </b>"+str(on_hold)+" "+str_issues(on_hold)+"</a></td></tr>\n")

#f.write("<tr align=\"center\"><font style='font-family:arial;'><td align=\"left\"><a><b>Resolved: </b>"+str(resolved)+" "+str_issues(resolved)+"</a></td></tr>\n")

#f.write("<tr align=\"center\"><font style='font-family:arial;'><td align=\"left\"><a><b>Resolved(In-Test): </b>"+str(resolved_test)+" "+str_issues(resolved_test)+"</a></td></tr>\n")

#f.write("</table></br>\n")

#f.write("<b><u><font size='2' style='font-family:arial;'><u><b>NOTE</b></u></font></u></b><br>")
#f.write("<b><font size='1' style='font-family:arial;'>Open: </b><i>Analysis/work to be started</i><b>, In Progress: </b><i>Design work is in-progress</i><b>, On-Hold: </b><i>Under monitor/ paused due to some dependency</i><b>, Resolved: </b><i>Design activity completed and under test</i></font><br>")

###Threshold check############

#for epfg 
#if epfg_total_team <= 1:
#		epfg_threshold="<td style='background-color:#98FF98;'>No</td>"
#else:
#		epfg_threshold="<td style='background-color:red'>Yes</td>"

#for security 
if sec_total_team <= 1:
		sec_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
		sec_threshold="<td style='background-color:red'>Yes</td>"
		
#for ddc_ddp  
if ddc_ddp_total_team <= 1:
		ddc_ddp_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
		ddc_ddp_threshold="<td style='background-color:red'>Yes</td>"

#for infra 
if infra_total_team <= 2:
		infra_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
		infra_threshold="<td style='background-color:red'>Yes</td>"

#for tp 
tp_kpi_total = tp_total_team + kpi_total_team
if tp_kpi_total <= 2:
		tp_threshold="<td style='background-color:#98FF98;' rowspan='2'>No</td>"
else:
		tp_threshold="<td style='background-color:red' rowspan='2'>Yes</td>"

#for nmi
nmi_nmisap_total = nmi_total_team + nmisap_total_team
if nmi_nmisap_total <= 3:
		nmi_threshold="<td style='background-color:#98FF98;' rowspan='2'>No</td>"
else:
		nmi_threshold="<td style='background-color:red' rowspan='2'>Yes</td>"

#for netan 
if netan_total_team <= 3:
		netan_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
		netan_threshold="<td style='background-color:red'>Yes</td>"

#for bo_ocs
if bo_ocs_total_team <= 1:
		bo_ocs_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
		bo_ocs_threshold="<td style='background-color:red'>Yes</td>"

#for pf 
if pf_total_team <= 3:
		pf_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
		pf_threshold="<td style='background-color:red'>Yes</td>"

#for total teams 
if unique_total <= 16:
		total_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
		total_threshold="<td style='background-color:red'>Yes</td>"		

########################## NMI status main table #############
if nmi_open == 0:
        nmi_op1="<td align=\"center\">-</td>"
else:
        nmi_op1="<td align=\"center\">"+str(nmi_open)+"</td>"

if nmi_inprog == 0:
        nmi_inpr1="<td align=\"center\">-</td>"
else:
        nmi_inpr1="<td align=\"center\">"+str(nmi_inprog)+"</td>"

if nmi_hold == 0:
        nmi_ho1="<td align=\"center\">-</td>"
else:
        nmi_ho1="<td align=\"center\">"+str(nmi_hold)+"</td>"

if nmi_resolve == 0:
        nmi_reso1="<td align=\"center\">-</td>"
else:
        nmi_reso1="<td align=\"center\">"+str(nmi_resolve)+"</td>"

if nmi_re == 0:
	nmi_re1="<td align=\"center\">-</td>"
else:
        nmi_re1="<td align=\"center\">"+str(nmi_re)+"</td>"

############################ NMI-SAP status main table ###################
if nmi_sap_open == 0:
        nmi_sap_op1="<td align=\"center\">-</td>"
else:
        nmi_sap_op1="<td align=\"center\">"+str(nmi_sap_open)+"</td>"

if nmi_sap_inprog == 0:
        nmi_sap_inpr1="<td align=\"center\">-</td>"
else:
        nmi_sap_inpr1="<td align=\"center\">"+str(nmi_sap_inprog)+"</td>"

if nmi_sap_hold == 0:
        nmi_sap_ho1="<td align=\"center\">-</td>"
else:
        nmi_sap_ho1="<td align=\"center\">"+str(nmi_sap_hold)+"</td>"

if nmi_sap_resolve == 0:
        nmi_sap_reso1="<td align=\"center\">-</td>"
else:
        nmi_sap_reso1="<td align=\"center\">"+str(nmi_sap_resolve)+"</td>"

if nmi_sap_re == 0:
        nmi_sap_re1="<td align=\"center\">-</td>"
else:
        nmi_sap_re1="<td align=\"center\">"+str(nmi_sap_re)+"</td>"

######################### DDC/DDP status main table #######################
if ddc_open == 0:
        ddc_op1="<td align=\"center\">-</td>"
else:
        ddc_op1="<td align=\"center\">"+str(ddc_open)+"</td>"

if ddc_inprog == 0:
        ddc_inpr1="<td align=\"center\">-</td>"
else:
        ddc_inpr1="<td align=\"center\">"+str(ddc_inprog)+"</td>"

if ddc_hold == 0:
        ddc_ho1="<td align=\"center\">-</td>"
else:
        ddc_ho1="<td align=\"center\">"+str(ddc_hold)+"</td>"

if ddc_resolve == 0:
        ddc_reso1="<td align=\"center\">-</td>"
else:
        ddc_reso1="<td align=\"center\">"+str(ddc_resolve)+"</td>"

if ddc_re == 0:
        ddc_re1="<td align=\"center\">-</td>"
else:
        ddc_re1="<td align=\"center\">"+str(ddc_re)+"</td>"

################################### PF status main table #############################
if pf_open == 0:
        pf_op1="<td align=\"center\">-</td>"
else:
        pf_op1="<td align=\"center\">"+str(pf_open)+"</td>"

if pf_inprog == 0:
        pf_inpr1="<td align=\"center\">-</td>"
else:
        pf_inpr1="<td align=\"center\">"+str(pf_inprog)+"</td>"

if pf_hold == 0:
        pf_ho1="<td align=\"center\">-</td>"
else:
        pf_ho1="<td align=\"center\">"+str(pf_hold)+"</td>"

if pf_resolve == 0:
        pf_reso1="<td align=\"center\">-</td>"
else:
        pf_reso1="<td align=\"center\">"+str(pf_resolve)+"</td>"

if pf_re == 0:
        pf_re1="<td align=\"center\">-</td>"
else:
        pf_re1="<td align=\"center\">"+str(pf_re)+"</td>"

########################################## TP status main table ##########################
if tp_open == 0:
        tp_op1="<td align=\"center\">-</td>"
else:
        tp_op1="<td align=\"center\">"+str(tp_open)+"</td>"

if tp_inprog == 0:
        tp_inpr1="<td align=\"center\">-</td>"
else:
        tp_inpr1="<td align=\"center\">"+str(tp_inprog)+"</td>"

if tp_hold == 0:
        tp_ho1="<td align=\"center\">-</td>"
else:
        tp_ho1="<td align=\"center\">"+str(tp_hold)+"</td>"

if tp_resolve == 0:
        tp_reso1="<td align=\"center\">-</td>"
else:
        tp_reso1="<td align=\"center\">"+str(tp_resolve)+"</td>"

if tp_re == 0:
        tp_re1="<td align=\"center\">-</td>"
else:
        tp_re1="<td align=\"center\">"+str(tp_re)+"</td>"

################################## KPI status main table #########################
if kpi_open == 0:
        kpi_op1="<td align=\"center\">-</td>"
else:
        kpi_op1="<td align=\"center\">"+str(kpi_open)+"</td>"

if kpi_inprog == 0:
        kpi_inpr1="<td align=\"center\">-</td>"
else:
        kpi_inpr1="<td align=\"center\">"+str(kpi_inprog)+"</td>"

if kpi_hold == 0:
        kpi_ho1="<td align=\"center\">-</td>"
else:
        kpi_ho1="<td align=\"center\">"+str(kpi_hold)+"</td>"

if kpi_resolve == 0:
        kpi_reso1="<td align=\"center\">-</td>"
else:
        kpi_reso1="<td align=\"center\">"+str(kpi_resolve)+"</td>"

if kpi_re == 0:
        kpi_re1="<td align=\"center\">-</td>"
else:
        kpi_re1="<td align=\"center\">"+str(kpi_re)+"</td>"

############################ Netam status main table ######################
if netan_open == 0:
        netan_op1="<td align=\"center\">-</td>"
else:
        netan_op1="<td align=\"center\">"+str(netan_open)+"</td>"

if netan_inprog == 0:
        netan_inpr1="<td align=\"center\">-</td>"
else:
        netan_inpr1="<td align=\"center\">"+str(netan_inprog)+"</td>"

if netan_hold == 0:
        netan_ho1="<td align=\"center\">-</td>"
else:
        netan_ho1="<td align=\"center\">"+str(netan_hold)+"</td>"

if netan_resolve == 0:
        netan_reso1="<td align=\"center\">-</td>"
else:
        netan_reso1="<td align=\"center\">"+str(netan_resolve)+"</td>"

if netan_re == 0:
        netan_re1="<td align=\"center\">-</td>"
else:
        netan_re1="<td align=\"center\">"+str(netan_re)+"</td>"

###################################### BO/OCS status main table ###########################
if bo_open == 0:
        bo_op1="<td align=\"center\">-</td>"
else:
        bo_op1="<td align=\"center\">"+str(bo_open)+"</td>"

if bo_inprog == 0:
        bo_inpr1="<td align=\"center\">-</td>"
else:
        bo_inpr1="<td align=\"center\">"+str(bo_inprog)+"</td>"

if bo_hold == 0:
        bo_ho1="<td align=\"center\">-</td>"
else:
        bo_ho1="<td align=\"center\">"+str(bo_hold)+"</td>"

if bo_resolve == 0:
        bo_reso1="<td align=\"center\">-</td>"
else:
        bo_reso1="<td align=\"center\">"+str(bo_resolve)+"</td>"

if bo_re == 0:
        bo_re1="<td align=\"center\">-</td>"
else:
        bo_re1="<td align=\"center\">"+str(bo_re)+"</td>"

############################### Infra status main table ###################
if infra_open == 0:
        infra_op1="<td align=\"center\">-</td>"
else:
        infra_op1="<td align=\"center\">"+str(infra_open)+"</td>"

if infra_inprog == 0:
        infra_inpr1="<td align=\"center\">-</td>"
else:
        infra_inpr1="<td align=\"center\">"+str(infra_inprog)+"</td>"

if infra_hold == 0:
        infra_ho1="<td align=\"center\">-</td>"
else:
        infra_ho1="<td align=\"center\">"+str(infra_hold)+"</td>"

if infra_resolve == 0:
        infra_reso1="<td align=\"center\">-</td>"
else:
        infra_reso1="<td align=\"center\">"+str(infra_resolve)+"</td>"

if infra_re == 0:
        infra_re1="<td align=\"center\">-</td>"
else:
        infra_re1="<td align=\"center\">"+str(infra_re)+"</td>"

############################# security status main table ##################
if sec_open == 0:
        sec_op1="<td align=\"center\">-</td>"
else:
        sec_op1="<td align=\"center\">"+str(sec_open)+"</td>"

if sec_inprog == 0:
        sec_inpr1="<td align=\"center\">-</td>"
else:
        sec_inpr1="<td align=\"center\">"+str(sec_inprog)+"</td>"

if sec_hold == 0:
        sec_ho1="<td align=\"center\">-</td>"
else:
        sec_ho1="<td align=\"center\">"+str(sec_hold)+"</td>"

if sec_resolve == 0:
        sec_reso1="<td align=\"center\">-</td>"
else:
        sec_reso1="<td align=\"center\">"+str(sec_resolve)+"</td>"

if sec_re == 0:
        sec_re1="<td align=\"center\">-</td>"
else:
        sec_re1="<td align=\"center\">"+str(sec_re)+"</td>"

f.write("<br><table border=\"2\"><tr style='background-color:#e0ff44;'><b><font style='font-family:arial;'><th rowspan='2'>Team</th><th colspan='3'>BUGs Opened in</th><th rowspan='13'></th><th colspan='3'>BUGs Closed in</th><th rowspan='13'></th><th rowspan='2'>Threshold</th><th rowspan='2'>Open BUGs</th><th colspan='5'>Status</th><th rowspan='13'></th><th rowspan='2'>Above Threshold</th></font></b></tr>\n")

f.write("<tr align=\"center\"><b><font style='font-family:arial;'><td style='background-color:#e0ff44;'>Wk"+str(week_num-2)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num-1)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num-2)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num-1)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num)+"</td><td style='background-color:#e0ff44;'>Open/Reopened</td><td style='background-color:#e0ff44;'>In-Progress</td><td style='background-color:#e0ff44;'>On-Hold</td><td style='background-color:#e0ff44;'>Resolved</td><td style='background-color:#e0ff44;'>Review</td></font></b></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">NMI</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102827\">"+str(nmi_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102747\">"+str(nmi_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102227\">"+str(nmi_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102828\">"+str(nmi_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102748\">"+str(nmi_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102228\">"+str(nmi_closed_jiras)+"</a></td><td rowspan='2'>3</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105059\">"+str(nmi_total_team)+"</a></td>"+nmi_op1+" "+nmi_inpr1+" "+nmi_ho1+" "+nmi_reso1+" "+nmi_re1+" "+nmi_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">NMI-SAP</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106411\">"+str(nmisap_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106410\">"+str(nmisap_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106409\">"+str(nmisap_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106414\">"+str(nmisap_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106413\">"+str(nmisap_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106412\">"+str(nmisap_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106416\">"+str(nmisap_total_team)+"</a></td>"+nmi_sap_op1+" "+nmi_sap_inpr1+" "+nmi_sap_ho1+" "+nmi_sap_reso1+" "+nmi_sap_re1+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">DDC/DDP</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102839\">"+str(ddc_ddp_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102762\">"+str(ddc_ddp_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102244\">"+str(ddc_ddp_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102840\">"+str(ddc_ddp_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102763\">"+str(ddc_ddp_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102245\">"+str(ddc_ddp_closed_jiras)+"</a></td><td>1</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105060\">"+str(ddc_ddp_total_team)+"</a></td>"+ddc_op1+" "+ddc_inpr1+" "+ddc_ho1+" "+ddc_reso1+" "+ddc_re1+" "+ddc_ddp_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">PF</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102835\">"+str(pf_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102758\">"+str(pf_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102235\">"+str(pf_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102836\">"+str(pf_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102759\">"+str(pf_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102236\">"+str(pf_closed_jiras)+"</a></td><td>3</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105061\">"+str(pf_total_team)+"</a></td>"+pf_op1+" "+pf_inpr1+" "+pf_ho1+" "+pf_reso1+" "+pf_re1+" "+pf_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">TP</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102825\">"+str(TP_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102745\">"+str(TP_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102225\">"+str(TP_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102826\">"+str(TP_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102746\">"+str(TP_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102226\">"+str(TP_closed_jiras)+"</a></td><td rowspan='2'>2</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105062\">"+str(tp_total_team)+"</a></td>"+tp_op1+" "+tp_inpr1+" "+tp_ho1+" "+tp_reso1+" "+tp_re1+" "+tp_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">KPI</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107188\">"+str(kpi_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107187\">"+str(kpi_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107186\">"+str(kpi_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107185\">"+str(kpi_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107184\">"+str(kpi_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107183\">"+str(kpi_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107189\">"+str(kpi_total_team)+"</a></td>"+kpi_op1+" "+kpi_inpr1+" "+kpi_ho1+" "+kpi_reso1+" "+kpi_re1+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">NetAn</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102829\">"+str(netan_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102749\">"+str(netan_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102229\">"+str(netan_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102830\">"+str(netan_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102750\">"+str(netan_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102230\">"+str(netan_closed_jiras)+"</a></td><td>3</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105063\">"+str(netan_total_team)+"</a></td>"+netan_op1+" "+netan_inpr1+" "+netan_ho1+" "+netan_reso1+" "+netan_re1+" "+netan_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">BO/OCS</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102831\">"+str(bo_ocs_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102753\">"+str(bo_ocs_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102231\">"+str(bo_ocs_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102832\">"+str(bo_ocs_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102754\">"+str(bo_ocs_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102232\">"+str(bo_ocs_closed_jiras)+"</a></td><td>1</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105064\">"+str(bo_ocs_total_team)+"</a></td>"+bo_op1+" "+bo_inpr1+" "+bo_ho1+" "+bo_reso1+" "+bo_re1+" "+bo_ocs_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">Infra</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102833\">"+str(infra_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102755\">"+str(infra_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102233\">"+str(infra_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102834\">"+str(infra_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102756\">"+str(infra_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102234\">"+str(infra_closed_jiras)+"</a></td><td>2</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105065\">"+str(infra_total_team)+"</a></td>"+infra_op1+" "+infra_inpr1+" "+infra_ho1+" "+infra_reso1+" "+infra_re1+" "+infra_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">Security</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102841\">"+str(sec_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102764\">"+str(sec_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102246\">"+str(sec_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102842\">"+str(sec_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102765\">"+str(sec_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102247\">"+str(sec_closed_jiras)+"</a></td><td>1</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105066\">"+str(sec_total_team)+"</a></td>"+sec_op1+" "+sec_inpr1+" "+sec_ho1+" "+sec_reso1+" "+sec_re1+" "+sec_threshold+"</font></tr>\n")

#f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">EPFG</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102837\">"+str(epfg_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102760\">"+str(epfg_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102242\">"+str(epfg_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102838\">"+str(epfg_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102761\">"+str(epfg_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102243\">"+str(epfg_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105067\">"+str(epfg_total_team)+"</a></td><td><td>4</td>"+str(nmi_open)+"</td><td>"+str(nmi_inprog)+"</td><td>"+str(nmi_hold)+"</td><td>"+str(nmi_resolve)+"</td>"+epfg_threshold+"</font></tr>\n")

f.write("<tr align=\"center\" style='background-color:#fcdfff;'><font color=\"black\" style='font-family:arial;'><td><b>Total unique Count<b></font></td><td><a><b>"+str(uni_open_last3)+"</b></a></td><td><a><b>"+str(uni_open_last2)+"</b></a></td><td><a><b>"+str(uni_open_last)+"</b></a></td><td><a><b>"+str(uni_closed_last3)+"</b></a></td><td><a><b>"+str(uni_closed_last2)+"</b></a></td><td><a><b>"+str(uni_closed_last)+"</b></a></td><td>16</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105058\"><b>"+str(unique_total)+"</b></a></td><td>"+str(total_open)+"</td><td>"+str(total_inprog)+"</td><td>"+str(total_hold)+"</td><td>"+str(total_resolve)+"</td><td>"+str(total_review)+"</td>"+total_threshold+"</font></tr>\n")

f.write("</table></br>\n")

#f.write("<b><u>Opened JIRAS on week"+str(datetime.datetime.strftime(num, '%W'))+"</u></b>")
f.write("<b><u><font style='font-family:arial;'>Current open BUG details</font></u></b><br>")

#f.write('<br><b>NMI :   </b>')
jira_raised = jira.search_issues("filter=262097")
if not jira_raised:
    f.write(" ")
else:
    f.write('<br><b>NMI :   </b>')
    for issue in jira_raised:
	url = "https://jira-oss.seli.wh.rnd.internal.ericsson.com/browse/"+issue.key
	f.write("<a href="+ url +">"+issue.key+"    "+"</a>&nbsp;")
        #f.write(issue.key+"    ")

#f.write('<br><b>NMI-SAP :   </b>')
jira_raised = jira.search_issues("filter=262100")
if not jira_raised:
    f.write(" ")
else:
    f.write('<br><b>NMI-SAP :   </b>')
    for issue in jira_raised:
        url = "https://jira-oss.seli.wh.rnd.internal.ericsson.com/browse/"+issue.key
        f.write("<a href="+ url +">"+issue.key+"    "+"</a>&nbsp;")
        #f.write(issue.key+"    ")

#f.write('<br><b>DDC/DDP :   </b>')
jira_raised = jira.search_issues("filter=262105")
if not jira_raised:
    f.write(" ")
else:
    f.write('<br><b>DDC/DDP :   </b>')
    for issue in jira_raised:
	url = "https://jira-oss.seli.wh.rnd.internal.ericsson.com/browse/"+issue.key
	f.write("<a href="+ url +">"+issue.key+"    "+"</a>&nbsp;")
        #f.write(issue.key+"    ")

#f.write('<br><b>PF :   </b>')
jira_raised = jira.search_issues("filter=262104")
if not jira_raised:
    f.write(" ")
else:
    f.write('<br><b>PF :   </b>')
    for issue in jira_raised:
	url = "https://jira-oss.seli.wh.rnd.internal.ericsson.com/browse/"+issue.key
	f.write("<a href="+ url +">"+issue.key+"    "+"</a>&nbsp;")
        #f.write(issue.key+"    ")

#f.write('<br><b>TP :   </b>')
jira_raised = jira.search_issues("filter=262095")
if not jira_raised:
    f.write(" ")
else:
    f.write('<br><b>TP :   </b>')
    for issue in jira_raised:
	url = "https://jira-oss.seli.wh.rnd.internal.ericsson.com/browse/"+issue.key
	f.write("<a href="+ url +">"+issue.key+"    "+"</a>&nbsp;")
        #f.write(issue.key+"    ")

#f.write('<br><b>KPI :   </b>')
jira_raised = jira.search_issues("filter=262096")
if not jira_raised:
    f.write(" ")
else:
    f.write('<br><b>KPI :   </b>')
    for issue in jira_raised:
        url = "https://jira-oss.seli.wh.rnd.internal.ericsson.com/browse/"+issue.key
        f.write("<a href="+ url +">"+issue.key+"    "+"</a>&nbsp;")
        #f.write(issue.key+"    ")

#f.write('<br><b>NetAn :   </b>')
jira_raised = jira.search_issues("filter=262101")
if not jira_raised:
    f.write(" ")
else:
    f.write('<br><b>NetAn :   </b>')
    for issue in jira_raised:
	url = "https://jira-oss.seli.wh.rnd.internal.ericsson.com/browse/"+issue.key
	f.write("<a href="+ url +">"+issue.key+"    "+"</a>&nbsp;")
        #f.write(issue.key+"    ")

#f.write('<br><b>BO/OCS :   </b>')
jira_raised = jira.search_issues("filter=262102")
if not jira_raised:
    f.write(" ")
else:
    f.write('<br><b>BO/OCS :   </b>')
    for issue in jira_raised:
	url = "https://jira-oss.seli.wh.rnd.internal.ericsson.com/browse/"+issue.key
	f.write("<a href="+ url +">"+issue.key+"    "+"</a>&nbsp;")
        #f.write(issue.key+"    ")

#f.write('<br><b>Infra :   </b>')
jira_raised = jira.search_issues("filter=262103")
if not jira_raised:
    f.write(" ")
else:
    f.write('<br><b>Infra :   </b>')
    for issue in jira_raised:
	url = "https://jira-oss.seli.wh.rnd.internal.ericsson.com/browse/"+issue.key
	f.write("<a href="+ url +">"+issue.key+"    "+"</a>&nbsp;")
        #f.write(issue.key+"    ")

#f.write('<br><b>Security :   </b>')
jira_raised = jira.search_issues("filter=262106")
if not jira_raised:
    f.write(" ")
else:
    f.write('<br><b>Security :   </b>')
    for issue in jira_raised:
	url = "https://jira-oss.seli.wh.rnd.internal.ericsson.com/browse/"+issue.key
	f.write("<a href="+ url +">"+issue.key+"    "+"</a>&nbsp;")
	#f.write(issue.key+"    ")

#f.write('<br><b>EPFG :   </b>')
#jira_raised = jira.search_issues("filter=105067")
#if not jira_raised:
#    f.write(" ")
#else:
#    f.write('<br><b>EPFG :   </b>')
#    for issue in jira_raised:
#	url = "https://jira-oss.seli.wh.rnd.internal.ericsson.com/browse/"+issue.key
#	f.write("<a href="+ url +">"+issue.key+"    "+"</a>&nbsp;")
#        #f.write(issue.key+"    ")

f.write("<br><br><br><b>Thanks & Regards,</b>")
f.write("<br><b>Eniq Stats DM CI Team</b>")

f.write("</body></html>")
f.close()


