'''
@author : zhshees
Created on July 2022,25
'''
import base64
import datetime
from jira import JIRA
from datetime import date

def str_issues(num):
    if num == 1:
        return "issue"
    else:
        return "issues"

jiraOptions = {'server': "https://jira-oss.seli.wh.rnd.internal.ericsson.com"}

jira = JIRA(options=jiraOptions, basic_auth=("esjkadm100", "Naples!0512"))

############### =============== JIRA filters (current week)(Overall Count) =============  ####################
TP_open_jiras = len(jira.search_issues("filter=102225"))
TP_closed_jiras = len(jira.search_issues("filter=102226"))
kpi_open_jiras = len(jira.search_issues("filter=107186"))
kpi_closed_jiras = len(jira.search_issues("filter=107183"))
nmi_open_jiras = len(jira.search_issues("filter=102227"))
nmi_closed_jiras = len(jira.search_issues("filter=102228"))
nmisap_open_jiras = len(jira.search_issues("filter=106409"))
nmisap_closed_jiras = len(jira.search_issues("filter=106412"))
netan_open_jiras = len(jira.search_issues("filter=102229"))
netan_closed_jiras = len(jira.search_issues("filter=102230"))
bo_ocs_open_jiras = len(jira.search_issues("filter=102231"))
bo_ocs_closed_jiras = len(jira.search_issues("filter=102232"))
infra_open_jiras = len(jira.search_issues("filter=102233"))
infra_closed_jiras = len(jira.search_issues("filter=102234"))
pf_open_jiras = len(jira.search_issues("filter=102235"))
pf_closed_jiras = len(jira.search_issues("filter=102236"))
ddc_ddp_open_jiras = len(jira.search_issues("filter=102244"))
ddc_ddp_closed_jiras = len(jira.search_issues("filter=102245"))
sec_open_jiras = len(jira.search_issues("filter=102246"))
sec_closed_jiras = len(jira.search_issues("filter=102247"))

############### jira filters (last 2nd week)  ####################

TP_open_jiras2 = len(jira.search_issues("filter=102745"))
TP_closed_jiras2 = len(jira.search_issues("filter=102746"))
kpi_open_jiras2 = len(jira.search_issues("filter=107187"))
kpi_closed_jiras2 = len(jira.search_issues("filter=107184"))
nmi_open_jiras2 = len(jira.search_issues("filter=102747"))
nmi_closed_jiras2 = len(jira.search_issues("filter=102748"))
nmisap_open_jiras2 = len(jira.search_issues("filter=106410"))
nmisap_closed_jiras2 = len(jira.search_issues("filter=106413"))
netan_open_jiras2 = len(jira.search_issues("filter=102749"))
netan_closed_jiras2 = len(jira.search_issues("filter=102750"))
bo_ocs_open_jiras2 = len(jira.search_issues("filter=102753"))
bo_ocs_closed_jiras2 = len(jira.search_issues("filter=102754"))
infra_open_jiras2 = len(jira.search_issues("filter=102755"))
infra_closed_jiras2 = len(jira.search_issues("filter=102756"))
pf_open_jiras2 = len(jira.search_issues("filter=102758"))
pf_closed_jiras2 = len(jira.search_issues("filter=102759"))
ddc_ddp_open_jiras2 = len(jira.search_issues("filter=102762"))
ddc_ddp_closed_jiras2 = len(jira.search_issues("filter=102763"))
sec_open_jiras2 = len(jira.search_issues("filter=102764"))
sec_closed_jiras2 = len(jira.search_issues("filter=102765"))

########################### jira filters (last 3rd week) #####################

TP_open_jiras3 = len(jira.search_issues("filter=102825"))
TP_closed_jiras3 = len(jira.search_issues("filter=102826"))
kpi_open_jiras3 = len(jira.search_issues("filter=107188"))
kpi_closed_jiras3 = len(jira.search_issues("filter=107185"))
nmi_open_jiras3 = len(jira.search_issues("filter=102827"))
nmi_closed_jiras3 = len(jira.search_issues("filter=102828"))
nmisap_open_jiras3 = len(jira.search_issues("filter=106411"))
nmisap_closed_jiras3 = len(jira.search_issues("filter=106414"))
netan_open_jiras3 = len(jira.search_issues("filter=102829"))
netan_closed_jiras3 = len(jira.search_issues("filter=102830"))
bo_ocs_open_jiras3 = len(jira.search_issues("filter=102831"))
bo_ocs_closed_jiras3 = len(jira.search_issues("filter=102832"))
infra_open_jiras3 = len(jira.search_issues("filter=102833"))
infra_closed_jiras3 = len(jira.search_issues("filter=102834"))
pf_open_jiras3 = len(jira.search_issues("filter=102835"))
pf_closed_jiras3 = len(jira.search_issues("filter=102836"))
ddc_ddp_open_jiras3 = len(jira.search_issues("filter=102839"))
ddc_ddp_closed_jiras3 = len(jira.search_issues("filter=102840"))
sec_open_jiras3 = len(jira.search_issues("filter=102841"))
sec_closed_jiras3 = len(jira.search_issues("filter=102842"))

################ Open total team basis (overall main table) #####################
tp_total_team = len(jira.search_issues("filter=105062"))
kpi_total_team = len(jira.search_issues("filter=107189"))
nmi_total_team = len(jira.search_issues("filter=105059"))
nmisap_total_team = len(jira.search_issues("filter=106416"))
netan_total_team = len(jira.search_issues("filter=105063"))
bo_ocs_total_team = len(jira.search_issues("filter=105064"))
infra_total_team = len(jira.search_issues("filter=105065"))
pf_total_team = len(jira.search_issues("filter=105061"))
ddc_ddp_total_team  = len(jira.search_issues("filter=105060"))
sec_total_team = len(jira.search_issues("filter=105066"))

############## Total unique issues/jiras (main overall table) #################
uni_open_last = len(jira.search_issues("filter=102743"))
uni_closed_last = len(jira.search_issues("filter=102744"))
uni_open_last2 = len(jira.search_issues("filter=102740"))
uni_closed_last2 = len(jira.search_issues("filter=102741"))
uni_open_last3 = len(jira.search_issues("filter=102843"))
uni_closed_last3 = len(jira.search_issues("filter=102844"))
unique_total = len(jira.search_issues("filter=105058"))

########################## ========= 22.3 filters current week (main table) =========== ############################
BTP_open_jiras = len(jira.search_issues("filter=108839"))
BTP_closed_jiras = len(jira.search_issues("filter=108833"))
Bkpi_open_jiras = len(jira.search_issues("filter=108849"))
Bkpi_closed_jiras = len(jira.search_issues("filter=108600"))
Bnmi_open_jiras = len(jira.search_issues("filter=108857"))
Bnmi_closed_jiras = len(jira.search_issues("filter=108812"))
Bnmisap_open_jiras = len(jira.search_issues("filter=108860"))
Bnmisap_closed_jiras = len(jira.search_issues("filter=108812"))
Bnetan_open_jiras = len(jira.search_issues("filter=108852"))
Bnetan_closed_jiras = len(jira.search_issues("filter=108809"))
Bbo_ocs_open_jiras = len(jira.search_issues("filter=108936"))
Bbo_ocs_closed_jiras = len(jira.search_issues("filter=108795"))
Binfra_open_jiras = len(jira.search_issues("filter=108846"))
Binfra_closed_jiras = len(jira.search_issues("filter=108802"))
Bpf_open_jiras = len(jira.search_issues("filter=108959"))
Bpf_closed_jiras = len(jira.search_issues("filter=108827"))
Bddc_ddp_open_jiras = len(jira.search_issues("filter=108843"))
Bddc_ddp_closed_jiras = len(jira.search_issues("filter=108799"))
Bsec_open_jiras = len(jira.search_issues("filter=108866"))
Bsec_closed_jiras = len(jira.search_issues("filter=108830"))

###############22.3 jira filters (last 2nd week)  ####################
BTP_open_jiras2 = len(jira.search_issues("filter=108840"))
BTP_closed_jiras2 = len(jira.search_issues("filter=108834"))
Bkpi_open_jiras2 = len(jira.search_issues("filter=108948"))
Bkpi_closed_jiras2 = len(jira.search_issues("filter=108807"))
Bnmi_open_jiras2 = len(jira.search_issues("filter=108858"))
Bnmi_closed_jiras2 = len(jira.search_issues("filter=108813"))
Bnmisap_open_jiras2 = len(jira.search_issues("filter=108861"))
Bnmisap_closed_jiras2 = len(jira.search_issues("filter=108816"))
Bnetan_open_jiras2 = len(jira.search_issues("filter=108853"))
Bnetan_closed_jiras2 = len(jira.search_issues("filter=108810"))
Bbo_ocs_open_jiras2 = len(jira.search_issues("filter=108939"))
Bbo_ocs_closed_jiras2 = len(jira.search_issues("filter=108796"))
Binfra_open_jiras2 = len(jira.search_issues("filter=108847"))
Binfra_closed_jiras2 = len(jira.search_issues("filter=108803"))
Bpf_open_jiras2 = len(jira.search_issues("filter=108960"))
Bpf_closed_jiras2 = len(jira.search_issues("filter=108828"))
Bddc_ddp_open_jiras2 = len(jira.search_issues("filter=108844"))
Bddc_ddp_closed_jiras2 = len(jira.search_issues("filter=108800"))
Bsec_open_jiras2 = len(jira.search_issues("filter=108864"))
Bsec_closed_jiras2 = len(jira.search_issues("filter=108831"))

###########################22.3 jira filters (last 3rd week) #####################
BTP_open_jiras3 = len(jira.search_issues("filter=108841"))
BTP_closed_jiras3 = len(jira.search_issues("filter=108835"))
Bkpi_open_jiras3 = len(jira.search_issues("filter=108949"))
Bkpi_closed_jiras3 = len(jira.search_issues("filter=108808"))
Bnmi_open_jiras3 = len(jira.search_issues("filter=108859"))
Bnmi_closed_jiras3 = len(jira.search_issues("filter=108814"))
Bnmisap_open_jiras3 = len(jira.search_issues("filter=108862"))
Bnmisap_closed_jiras3 = len(jira.search_issues("filter=108822"))
Bnetan_open_jiras3 = len(jira.search_issues("filter=108854"))
Bnetan_closed_jiras3 = len(jira.search_issues("filter=108811"))
Bbo_ocs_open_jiras3 = len(jira.search_issues("filter=108940"))
Bbo_ocs_closed_jiras3 = len(jira.search_issues("filter=108797"))
Binfra_open_jiras3 = len(jira.search_issues("filter=108848"))
Binfra_closed_jiras3 = len(jira.search_issues("filter=108804"))
Bpf_open_jiras3 = len(jira.search_issues("filter=108961"))
Bpf_closed_jiras3 = len(jira.search_issues("filter=108829"))
Bddc_ddp_open_jiras3 = len(jira.search_issues("filter=108845"))
Bddc_ddp_closed_jiras3 = len(jira.search_issues("filter=108801"))
Bsec_open_jiras3 = len(jira.search_issues("filter=108865"))
Bsec_closed_jiras3 = len(jira.search_issues("filter=108832"))

############## 22.3 Total unique issues/jiras overall table #################
Buni_open_last = len(jira.search_issues("filter=109308"))
Buni_closed_last = len(jira.search_issues("filter=109310"))
Buni_open_last2 = len(jira.search_issues("filter=109307"))
Buni_closed_last2 = len(jira.search_issues("filter=109312"))
Buni_open_last3 = len(jira.search_issues("filter=109314"))
Buni_closed_last3 = len(jira.search_issues("filter=109316"))
#Bunique_total = len(jira.search_issues("filter="))

################ 22.3 Open total team basis (overall main table) #####################
Btp_total_team = len(jira.search_issues("filter=109188"))
Bkpi_total_team = len(jira.search_issues("filter=108965"))
Bnmi_total_team = len(jira.search_issues("filter=109185"))
Bnmisap_total_team = len(jira.search_issues("filter=108966"))
Bnetan_total_team = len(jira.search_issues("filter=109189"))
Bbo_ocs_total_team = len(jira.search_issues("filter=108967"))
Binfra_total_team = len(jira.search_issues("filter=109190"))
Bpf_total_team = len(jira.search_issues("filter=109187"))
Bddc_ddp_total_team  = len(jira.search_issues("filter=109186"))
Bsec_total_team = len(jira.search_issues("filter=109191"))

########################## ========= 22.4 filters current week (main table) =========== ############################
CTP_open_jiras = len(jira.search_issues("filter=108839"))
CTP_closed_jiras = len(jira.search_issues("filter=108833"))
Ckpi_open_jiras = len(jira.search_issues("filter=108849"))
Ckpi_closed_jiras = len(jira.search_issues("filter=108600"))
Cnmi_open_jiras = len(jira.search_issues("filter=108857"))
Cnmi_closed_jiras = len(jira.search_issues("filter=108812"))
Cnmisap_open_jiras = len(jira.search_issues("filter=108860"))
Cnmisap_closed_jiras = len(jira.search_issues("filter=108812"))
Cnetan_open_jiras = len(jira.search_issues("filter=108852"))
Cnetan_closed_jiras = len(jira.search_issues("filter=108809"))
Cbo_ocs_open_jiras = len(jira.search_issues("filter=108936"))
Cbo_ocs_closed_jiras = len(jira.search_issues("filter=108795"))
Cinfra_open_jiras = len(jira.search_issues("filter=108846"))
Cinfra_closed_jiras = len(jira.search_issues("filter=108802"))
Cpf_open_jiras = len(jira.search_issues("filter=108959"))
Cpf_closed_jiras = len(jira.search_issues("filter=108827"))
Cddc_ddp_open_jiras = len(jira.search_issues("filter=108843"))
Cddc_ddp_closed_jiras = len(jira.search_issues("filter=108799"))
Csec_open_jiras = len(jira.search_issues("filter=108866"))
Csec_closed_jiras = len(jira.search_issues("filter=108830"))

###############22.4 jira filters (last 2nd week)  ####################
CTP_open_jiras2 = len(jira.search_issues("filter=108840"))
CTP_closed_jiras2 = len(jira.search_issues("filter=108834"))
Ckpi_open_jiras2 = len(jira.search_issues("filter=108948"))
Ckpi_closed_jiras2 = len(jira.search_issues("filter=108807"))
Cnmi_open_jiras2 = len(jira.search_issues("filter=108858"))
Cnmi_closed_jiras2 = len(jira.search_issues("filter=108813"))
Cnmisap_open_jiras2 = len(jira.search_issues("filter=108861"))
Cnmisap_closed_jiras2 = len(jira.search_issues("filter=108816"))
Cnetan_open_jiras2 = len(jira.search_issues("filter=108853"))
Cnetan_closed_jiras2 = len(jira.search_issues("filter=108810"))
Cbo_ocs_open_jiras2 = len(jira.search_issues("filter=108939"))
Cbo_ocs_closed_jiras2 = len(jira.search_issues("filter=108796"))
Cinfra_open_jiras2 = len(jira.search_issues("filter=108847"))
Cinfra_closed_jiras2 = len(jira.search_issues("filter=108803"))
Cpf_open_jiras2 = len(jira.search_issues("filter=108960"))
Cpf_closed_jiras2 = len(jira.search_issues("filter=108828"))
Cddc_ddp_open_jiras2 = len(jira.search_issues("filter=108844"))
Cddc_ddp_closed_jiras2 = len(jira.search_issues("filter=108800"))
Csec_open_jiras2 = len(jira.search_issues("filter=108864"))
Csec_closed_jiras2 = len(jira.search_issues("filter=108831"))

###########################22.4 jira filters (last 3rd week) #####################
CTP_open_jiras3 = len(jira.search_issues("filter=108841"))
CTP_closed_jiras3 = len(jira.search_issues("filter=108835"))
Ckpi_open_jiras3 = len(jira.search_issues("filter=108949"))
Ckpi_closed_jiras3 = len(jira.search_issues("filter=108808"))
Cnmi_open_jiras3 = len(jira.search_issues("filter=108859"))
Cnmi_closed_jiras3 = len(jira.search_issues("filter=108814"))
Cnmisap_open_jiras3 = len(jira.search_issues("filter=108862"))
Cnmisap_closed_jiras3 = len(jira.search_issues("filter=108822"))
Cnetan_open_jiras3 = len(jira.search_issues("filter=108854"))
Cnetan_closed_jiras3 = len(jira.search_issues("filter=108811"))
Cbo_ocs_open_jiras3 = len(jira.search_issues("filter=108940"))
Cbo_ocs_closed_jiras3 = len(jira.search_issues("filter=108797"))
Cinfra_open_jiras3 = len(jira.search_issues("filter=108848"))
Cinfra_closed_jiras3 = len(jira.search_issues("filter=108804"))
Cpf_open_jiras3 = len(jira.search_issues("filter=108961"))
Cpf_closed_jiras3 = len(jira.search_issues("filter=108829"))
Cddc_ddp_open_jiras3 = len(jira.search_issues("filter=108845"))
Cddc_ddp_closed_jiras3 = len(jira.search_issues("filter=108801"))
Csec_open_jiras3 = len(jira.search_issues("filter=108865"))
Csec_closed_jiras3 = len(jira.search_issues("filter=108832"))

############## 22.4 Total unique issues/jiras overall table #################
Cuni_open_last = len(jira.search_issues("filter=109309"))
Cuni_closed_last = len(jira.search_issues("filter=109311"))
Cuni_open_last2 = len(jira.search_issues("filter=109306"))
Cuni_closed_last2 = len(jira.search_issues("filter=109313"))
Cuni_open_last3 = len(jira.search_issues("filter=109315"))
Cuni_closed_last3 = len(jira.search_issues("filter=109317"))
#Cunique_total = len(jira.search_issues("filter="))

################ 22.4 Open total team basis (overall main table) #####################
Ctp_total_team = len(jira.search_issues("filter=109193"))
Ckpi_total_team = len(jira.search_issues("filter=109192"))
Cnmi_total_team = len(jira.search_issues("filter=109225"))
Cnmisap_total_team = len(jira.search_issues("filter=109226"))
Cnetan_total_team = len(jira.search_issues("filter=109229"))
Cbo_ocs_total_team = len(jira.search_issues("filter=109231"))
Cinfra_total_team = len(jira.search_issues("filter=109195"))
Cpf_total_team = len(jira.search_issues("filter=109228"))
Cddc_ddp_total_team  = len(jira.search_issues("filter=109227"))
Csec_total_team = len(jira.search_issues("filter=109194"))

############### ========================== Overall releases GA Blocker jiras ============================= ############
nmi_ga = len(jira.search_issues("filter=106181"))
nmisap_ga = len(jira.search_issues("filter=106415"))
ddc_ga  = len(jira.search_issues("filter=106182"))
pf_ga = len(jira.search_issues("filter=106180"))
tp_ga = len(jira.search_issues("filter=106183"))
kpi_ga = len(jira.search_issues("filter=107191"))
netan_ga = len(jira.search_issues("filter=106184"))
bo_ga = len(jira.search_issues("filter=106185"))
infra_ga = len(jira.search_issues("filter=106186"))
sec_ga = len(jira.search_issues("filter=106187"))
total_ga = len(jira.search_issues("filter=106189"))

########################## 22.3 GA Blocker jiras ################
nmi_ga2 = len(jira.search_issues("filter=108601"))
nmisap_ga2 = len(jira.search_issues("filter=108602"))
ddc_ga2 = len(jira.search_issues("filter=108603"))
pf_ga2 = len(jira.search_issues("filter=108604"))
tp_ga2 = len(jira.search_issues("filter=108605"))
kpi_ga2 = len(jira.search_issues("filter=108606"))
netan_ga2 = len(jira.search_issues("filter=108607"))
bo_ga2 = len(jira.search_issues("filter=108608"))
infra_ga2 = len(jira.search_issues("filter=108609"))
sec_ga2 = len(jira.search_issues("filter=108610"))
total_ga2 = len(jira.search_issues("filter=108611"))

########################## 22.4 GA Blocker jiras ################
nmi_ga3 = len(jira.search_issues("filter=108622"))
nmisap_ga3 = len(jira.search_issues("filter=108621"))
ddc_ga3 = len(jira.search_issues("filter=108620"))
pf_ga3 = len(jira.search_issues("filter=108619"))
tp_ga3 = len(jira.search_issues("filter=108618"))
kpi_ga3 = len(jira.search_issues("filter=108617"))
netan_ga3 = len(jira.search_issues("filter=108616"))
bo_ga3 = len(jira.search_issues("filter=108615"))
infra_ga3 = len(jira.search_issues("filter=108614"))
sec_ga3 = len(jira.search_issues("filter=108613"))
total_ga3 = len(jira.search_issues("filter=108612"))

################### team ga status count jiras(overall table) ################
nmi_inprog_ga = len(jira.search_issues("filter=107785"))
nmi_hold_ga = len(jira.search_issues("filter=107788"))
nmi_open_ga = len(jira.search_issues("filter=107818"))
nmi_resolve_ga = len(jira.search_issues("filter=107816"))
nmi_sap_inprog_ga = len(jira.search_issues("filter=107786"))
nmi_sap_hold_ga = len(jira.search_issues("filter=107821"))
nmi_sap_open_ga = len(jira.search_issues("filter=107820"))
nmi_sap_resolved_ga = len(jira.search_issues("filter=107819"))
ddc_inprog_ga = len(jira.search_issues("filter=107823"))
ddc_hold_ga = len(jira.search_issues("filter=107824"))
ddc_resolve_ga = len(jira.search_issues("filter=107825"))
ddc_open_ga = len(jira.search_issues("filter=107826"))
pf_inprog_ga = len(jira.search_issues("filter=107827"))
pf_hold_ga = len(jira.search_issues("filter=107829"))
pf_resolve_ga = len(jira.search_issues("filter=107830"))
pf_open_ga = len(jira.search_issues("filter=107831"))
tp_inprog_ga = len(jira.search_issues("filter=107833"))
tp_hold_ga = len(jira.search_issues("filter=107835"))
tp_resolve_ga = len(jira.search_issues("filter=107836"))
tp_open_ga = len(jira.search_issues("filter=107832"))
kpi_inprog_ga = len(jira.search_issues("filter=107837"))
kpi_hold_ga = len(jira.search_issues("filter=107838"))
kpi_resolve_ga = len(jira.search_issues("filter=107839"))
kpi_open_ga = len(jira.search_issues("filter=107840"))
netan_inprog_ga = len(jira.search_issues("filter=107841"))
netan_hold_ga = len(jira.search_issues("filter=107842"))
netan_resolve_ga = len(jira.search_issues("filter=107843"))
netan_open_ga = len(jira.search_issues("filter=107844"))
bo_inprog_ga = len(jira.search_issues("filter=107845"))
bo_hold_ga = len(jira.search_issues("filter=107846"))
bo_resolve_ga = len(jira.search_issues("filter=107847"))
bo_open_ga = len(jira.search_issues("filter=107848"))
infra_inprog_ga = len(jira.search_issues("filter=107849"))
infra_hold_ga = len(jira.search_issues("filter=107850"))
infra_resolve_ga = len(jira.search_issues("filter=107851"))
infra_open_ga = len(jira.search_issues("filter=107852"))
sec_inprog_ga = len(jira.search_issues("filter=107853"))
sec_hold_ga = len(jira.search_issues("filter=107855"))
sec_resolve_ga = len(jira.search_issues("filter=107857"))
sec_open_ga = len(jira.search_issues("filter=107858"))

################### team ga status count jiras(22.3 filter) ################
nmi_inprog_ga2 = len(jira.search_issues("filter=108771"))
nmi_hold_ga2 = len(jira.search_issues("filter=108772"))
nmi_open_ga2 = len(jira.search_issues("filter=108773"))
nmi_resolve_ga2 = len(jira.search_issues("filter=108774"))
nmi_sap_inprog_ga2 = len(jira.search_issues("filter=108770"))
nmi_sap_hold_ga2 = len(jira.search_issues("filter=108759"))
nmi_sap_open_ga2 = len(jira.search_issues("filter=108758"))
nmi_sap_resolved_ga2 = len(jira.search_issues("filter=108769"))
ddc_inprog_ga2 = len(jira.search_issues("filter=108731"))
ddc_hold_ga2 = len(jira.search_issues("filter=108732"))
ddc_resolve_ga2 = len(jira.search_issues("filter=108734"))
ddc_open_ga2 = len(jira.search_issues("filter=108733"))
pf_inprog_ga2 = len(jira.search_issues("filter=108747"))
pf_hold_ga2 = len(jira.search_issues("filter=108748"))
pf_resolve_ga2 = len(jira.search_issues("filter=108750"))
pf_open_ga2 = len(jira.search_issues("filter=108749"))
tp_inprog_ga2 = len(jira.search_issues("filter=108764"))
tp_hold_ga2 = len(jira.search_issues("filter=108765"))
tp_resolve_ga2 = len(jira.search_issues("filter=108768"))
tp_open_ga2 = len(jira.search_issues("filter=108767"))
kpi_inprog_ga2 = len(jira.search_issues("filter=108739"))
kpi_hold_ga2 = len(jira.search_issues("filter=108740"))
kpi_resolve_ga2 = len(jira.search_issues("filter=108742"))
kpi_open_ga2 = len(jira.search_issues("filter=108741"))
netan_inprog_ga2 = len(jira.search_issues("filter=108743"))
netan_hold_ga2 = len(jira.search_issues("filter=108744"))
netan_resolve_ga2 = len(jira.search_issues("filter=108746"))
netan_open_ga2 = len(jira.search_issues("filter=108745"))
bo_inprog_ga2 = len(jira.search_issues("filter=108727"))
bo_hold_ga2 = len(jira.search_issues("filter=108728"))
bo_resolve_ga2 = len(jira.search_issues("filter=108730"))
bo_open_ga2 = len(jira.search_issues("filter=108729"))
infra_inprog_ga2 = len(jira.search_issues("filter=108735"))
infra_hold_ga2 = len(jira.search_issues("filter=108736"))
infra_resolve_ga2 = len(jira.search_issues("filter=108738"))
infra_open_ga2 = len(jira.search_issues("filter=108737"))
sec_inprog_ga2 = len(jira.search_issues("filter=108751"))
sec_hold_ga2 = len(jira.search_issues("filter=108753"))
sec_resolve_ga2 = len(jira.search_issues("filter=108755"))
sec_open_ga2 = len(jira.search_issues("filter=108754"))

################### team ga status count jiras(22.4 filter) ################
nmi_inprog_ga3 = len(jira.search_issues("filter=108943"))
nmi_hold_ga3 = len(jira.search_issues("filter=108942"))
nmi_open_ga3 = len(jira.search_issues("filter=108941"))
nmi_resolve_ga3 = len(jira.search_issues("filter=108887"))
nmi_sap_inprog_ga3 = len(jira.search_issues("filter=108924"))
nmi_sap_hold_ga3 = len(jira.search_issues("filter=108851"))
nmi_sap_open_ga3 = len(jira.search_issues("filter=108901"))
nmi_sap_resolved_ga3 = len(jira.search_issues("filter=108850"))
ddc_inprog_ga3 = len(jira.search_issues("filter=108963"))
ddc_hold_ga3 = len(jira.search_issues("filter=108962"))
ddc_resolve_ga3 = len(jira.search_issues("filter=108952"))
ddc_open_ga3 = len(jira.search_issues("filter=108890"))
pf_inprog_ga3 = len(jira.search_issues("filter=108947"))
pf_hold_ga3 = len(jira.search_issues("filter=108805"))
pf_resolve_ga3 = len(jira.search_issues("filter=108951"))
pf_open_ga3 = len(jira.search_issues("filter=108875"))
tp_inprog_ga3 = len(jira.search_issues("filter=109199"))
tp_hold_ga3 = len(jira.search_issues("filter=109200"))
tp_resolve_ga3 = len(jira.search_issues("filter=109202"))
tp_open_ga3 = len(jira.search_issues("filter=109201"))
kpi_inprog_ga3 = len(jira.search_issues("filter=108956"))
kpi_hold_ga3 = len(jira.search_issues("filter=108815"))
kpi_resolve_ga3 = len(jira.search_issues("filter=108953"))
kpi_open_ga3 = len(jira.search_issues("filter=108955"))
netan_inprog_ga3 = len(jira.search_issues("filter=108857"))
netan_hold_ga3 = len(jira.search_issues("filter=108846"))
netan_resolve_ga3 = len(jira.search_issues("filter=108944"))
netan_open_ga3 = len(jira.search_issues("filter=108945"))
bo_inprog_ga3 = len(jira.search_issues("filter=108895"))
bo_hold_ga3 = len(jira.search_issues("filter=108904"))
bo_resolve_ga3 = len(jira.search_issues("filter=108964"))
bo_open_ga3 = len(jira.search_issues("filter=108927"))
infra_inprog_ga3 = len(jira.search_issues("filter=108900"))
infra_hold_ga3 = len(jira.search_issues("filter=108923"))
infra_resolve_ga3 = len(jira.search_issues("filter=108957"))
infra_open_ga3 = len(jira.search_issues("filter=108958"))
sec_inprog_ga3 = len(jira.search_issues("filter=108950"))
sec_hold_ga3 = len(jira.search_issues("filter=109205"))
sec_resolve_ga3 = len(jira.search_issues("filter=109203"))
sec_open_ga3 = len(jira.search_issues("filter=109204"))

###################### team open jiras status (overall main table)#################
nmi_inprog = len(jira.search_issues("filter=107863"))
nmi_hold = len(jira.search_issues("filter=107864"))
nmi_resolve = len(jira.search_issues("filter=107865"))
nmi_open = len(jira.search_issues("filter=107866"))
nmi_sap_inprog = len(jira.search_issues("filter=107867"))
nmi_sap_hold = len(jira.search_issues("filter=107869"))
nmi_sap_resolve = len(jira.search_issues("filter=107868"))
nmi_sap_open = len(jira.search_issues("filter=107870"))
ddc_inprog = len(jira.search_issues("filter=107872"))
ddc_hold = len(jira.search_issues("filter=107874"))
ddc_resolve = len(jira.search_issues("filter=107873"))
ddc_open = len(jira.search_issues("filter=107871"))
pf_open = len(jira.search_issues("filter=107875"))
pf_resolve = len(jira.search_issues("filter=107877"))
pf_hold = len(jira.search_issues("filter=107878"))
pf_inprog = len(jira.search_issues("filter=107876"))
tp_inprog = len(jira.search_issues("filter=107880"))
tp_open = len(jira.search_issues("filter=107879"))
tp_hold = len(jira.search_issues("filter=107881"))
tp_resolve = len(jira.search_issues("filter=107882"))
kpi_inprog = len(jira.search_issues("filter=107884"))
kpi_hold = len(jira.search_issues("filter=107885"))
kpi_resolve = len(jira.search_issues("filter=107886"))
kpi_open = len(jira.search_issues("filter=107883"))
netan_inprog = len(jira.search_issues("filter=107888"))
netan_hold = len(jira.search_issues("filter=107889"))
netan_resolve = len(jira.search_issues("filter=107890"))
netan_open = len(jira.search_issues("filter=107887"))
bo_inprog = len(jira.search_issues("filter=107892"))
bo_hold = len(jira.search_issues("filter=107893"))
bo_resolve = len(jira.search_issues("filter=107894"))
bo_open = len(jira.search_issues("filter=107891"))
infra_inprog = len(jira.search_issues("filter=107896"))
infra_hold = len(jira.search_issues("filter=107897"))
infra_resolve = len(jira.search_issues("filter=107898"))
infra_open = len(jira.search_issues("filter=107895"))
sec_inprog = len(jira.search_issues("filter=107900"))
sec_hold = len(jira.search_issues("filter=107901"))
sec_resolve = len(jira.search_issues("filter=107902"))
sec_open = len(jira.search_issues("filter=107899"))

###################### team open jiras status (22.3 main table)#################
nmi_inprog2 = len(jira.search_issues("filter=108922"))
nmi_hold2 = len(jira.search_issues("filter=108899"))
nmi_resolve2 = len(jira.search_issues("filter=108884"))
nmi_open2 = len(jira.search_issues("filter=109219"))
nmi_sap_inprog2 = len(jira.search_issues("filter=108923"))
nmi_sap_hold2 = len(jira.search_issues("filter=108900"))
nmi_sap_resolve2 = len(jira.search_issues("filter=108890"))
nmi_sap_open2 = len(jira.search_issues("filter=109218"))
ddc_inprog2 = len(jira.search_issues("filter=108920"))
ddc_hold2 = len(jira.search_issues("filter=108881"))
ddc_resolve2 = len(jira.search_issues("filter=108876"))
ddc_open2 = len(jira.search_issues("filter=109217"))
pf_open2 = len(jira.search_issues("filter=109216"))
pf_resolve2 = len(jira.search_issues("filter=108990"))
pf_hold2 = len(jira.search_issues("filter=108979"))
pf_inprog2 = len(jira.search_issues("filter=109244"))
tp_inprog2 = len(jira.search_issues("filter=108926"))
tp_open2 = len(jira.search_issues("filter=109215"))
tp_hold2 = len(jira.search_issues("filter=108903"))
tp_resolve2 = len(jira.search_issues("filter=108880"))
kpi_inprog2 = len(jira.search_issues("filter=109220"))
kpi_hold2 = len(jira.search_issues("filter=108883"))
kpi_resolve2 = len(jira.search_issues("filter=108878"))
kpi_open2 = len(jira.search_issues("filter=109214"))
netan_inprog2 = len(jira.search_issues("filter=108870"))
netan_hold2 = len(jira.search_issues("filter=108898"))
netan_resolve2 = len(jira.search_issues("filter=108879"))
netan_open2 = len(jira.search_issues("filter=109213"))
bo_inprog2 = len(jira.search_issues("filter=108919"))
bo_hold2 = len(jira.search_issues("filter=108897"))
bo_resolve2 = len(jira.search_issues("filter=108893"))
bo_open2 = len(jira.search_issues("filter=108969"))
infra_inprog2 = len(jira.search_issues("filter=108921"))
infra_hold2 = len(jira.search_issues("filter=108882"))
infra_resolve2 = len(jira.search_issues("filter=108877"))
infra_open2 = len(jira.search_issues("filter=109212"))
sec_inprog2 = len(jira.search_issues("filter=108925"))
sec_hold2 = len(jira.search_issues("filter=108902"))
sec_resolve2 = len(jira.search_issues("filter=108885"))
sec_open2 = len(jira.search_issues("filter=109211"))

###################### Team open jiras status (22.4 main table)#################
nmi_inprog3 = len(jira.search_issues("filter=108974"))
nmi_hold3 = len(jira.search_issues("filter=108985"))
nmi_resolve3 = len(jira.search_issues("filter=108996"))
nmi_open3 = len(jira.search_issues("filter=109232"))
nmi_sap_inprog3 = len(jira.search_issues("filter=108975"))
nmi_sap_hold3 = len(jira.search_issues("filter=108986"))
nmi_sap_resolve3 = len(jira.search_issues("filter=108997"))
nmi_sap_open3 = len(jira.search_issues("filter=109234"))
ddc_inprog3 = len(jira.search_issues("filter=108972"))
ddc_hold3 = len(jira.search_issues("filter=108981"))
ddc_resolve3 = len(jira.search_issues("filter=108992"))
ddc_open3 = len(jira.search_issues("filter=109235"))
pf_open3 = len(jira.search_issues("filter=109236"))
pf_resolve3 = len(jira.search_issues("filter=108998"))
pf_hold3 = len(jira.search_issues("filter=108987"))
pf_inprog3 = len(jira.search_issues("filter=108976"))
tp_inprog3 = len(jira.search_issues("filter=108978"))
tp_open3 = len(jira.search_issues("filter=109237"))
tp_hold3 = len(jira.search_issues("filter=108989"))
tp_resolve3 = len(jira.search_issues("filter=109000"))
kpi_inprog3 = len(jira.search_issues("filter=109223"))
kpi_hold3 = len(jira.search_issues("filter=108983"))
kpi_resolve3 = len(jira.search_issues("filter=108994"))
kpi_open3 = len(jira.search_issues("filter=109238"))
netan_inprog3 = len(jira.search_issues("filter=109224"))
netan_hold3 = len(jira.search_issues("filter=108984"))
netan_resolve3 = len(jira.search_issues("filter=108995"))
netan_open3 = len(jira.search_issues("filter=109239"))
bo_inprog3 = len(jira.search_issues("filter=108971"))
bo_hold3 = len(jira.search_issues("filter=108980"))
bo_resolve3 = len(jira.search_issues("filter=108991"))
bo_open3 = len(jira.search_issues("filter=109241"))
infra_inprog3 = len(jira.search_issues("filter=108973"))
infra_hold3 = len(jira.search_issues("filter=108982"))
infra_resolve3 = len(jira.search_issues("filter=108993"))
infra_open3 = len(jira.search_issues("filter=109242"))
sec_inprog3 = len(jira.search_issues("filter=108977"))
sec_hold3 = len(jira.search_issues("filter=108988"))
sec_resolve3 = len(jira.search_issues("filter=108999"))
sec_open3 = len(jira.search_issues("filter=109243"))

############### ============== Total status GA (ALL table) ================ ##############
total_inprog_ga = len(jira.search_issues("filter=107910"))
total_hold_ga = len(jira.search_issues("filter=107911"))
total_resolve_ga = len(jira.search_issues("filter=107912"))
total_open_ga = len(jira.search_issues("filter=107913"))
total_inprog_ga2 = len(jira.search_issues("filter=108760"))
total_hold_ga2 = len(jira.search_issues("filter=108761"))
total_resolve_ga2 = len(jira.search_issues("filter=108763"))
total_open_ga2 = len(jira.search_issues("filter=108762"))
total_inprog_ga3 = len(jira.search_issues("filter=109206"))
total_hold_ga3 = len(jira.search_issues("filter=109207"))
total_resolve_ga3 = len(jira.search_issues("filter=109210"))
total_open_ga3 = len(jira.search_issues("filter=109208"))

################## Total status main table (overall + 22.3 + 22.4) ##################
total_open = nmi_open + nmi_sap_open + sec_open + infra_open + bo_open + netan_open + kpi_open + tp_open + pf_open + ddc_open
total_inprog = sec_inprog + infra_inprog + bo_inprog + netan_inprog + kpi_inprog + tp_inprog + pf_inprog + ddc_inprog + nmi_inprog + nmi_sap_inprog
total_hold = sec_hold + bo_hold + netan_hold + kpi_hold + tp_hold + pf_hold + ddc_hold + nmi_hold + nmi_sap_hold
total_resolve = sec_resolve + infra_resolve + bo_resolve + netan_resolve + kpi_resolve + tp_resolve + pf_resolve + ddc_resolve + nmi_resolve + nmi_sap_resolve
Btotal_open = nmi_open2 + nmi_sap_open2 + sec_open2 + infra_open2 + bo_open2 + netan_open2 + kpi_open2 + tp_open2 + pf_open2 + ddc_open2
Btotal_inprog = sec_inprog2 + infra_inprog2 + bo_inprog2 + netan_inprog2 + kpi_inprog2 + tp_inprog2 + pf_inprog2 + ddc_inprog2 + nmi_inprog2 + nmi_sap_inprog2
Btotal_hold = sec_hold2 + bo_hold2 + netan_hold2 + kpi_hold2 + tp_hold2 + pf_hold2 + ddc_hold2 + nmi_hold2 + nmi_sap_hold2
Btotal_resolve = sec_resolve2 + infra_resolve2 + bo_resolve2 + netan_resolve2 + kpi_resolve2 + tp_resolve2 + pf_resolve2 + ddc_resolve2 + nmi_resolve2 + nmi_sap_resolve2
Ctotal_open = nmi_open3 + nmi_sap_open3 + sec_open3 + infra_open3 + bo_open3 + netan_open3 + kpi_open3 + tp_open3 + pf_open3 + ddc_open3
Ctotal_inprog = sec_inprog3 + infra_inprog3 + bo_inprog3 + netan_inprog3 + kpi_inprog3 + tp_inprog3 + pf_inprog3 + ddc_inprog3 + nmi_inprog3 + nmi_sap_inprog3
Ctotal_hold = sec_hold3 + bo_hold3 + netan_hold3 + kpi_hold3 + tp_hold3 + pf_hold3 + ddc_hold3 + nmi_hold3 + nmi_sap_hold3
Ctotal_resolve = sec_resolve3 + infra_resolve3 + bo_resolve3 + netan_resolve3 + kpi_resolve3 + tp_resolve3 + pf_resolve3 + ddc_resolve3 + nmi_resolve3 + nmi_sap_resolve3

################### total open jiras without filter (overall + 22.3 + 22.4) ##################
total_uniq = tp_total_team + kpi_total_team + nmi_total_team + nmisap_total_team + netan_total_team + bo_ocs_total_team + infra_total_team + pf_total_team + ddc_ddp_total_team + sec_total_team
Btotal_uniq = Btp_total_team + Bkpi_total_team + Bnmi_total_team + Bnmisap_total_team + Bnetan_total_team + Bbo_ocs_total_team + Binfra_total_team + Bpf_total_team + Bddc_ddp_total_team + Bsec_total_team
Ctotal_uniq = Ctp_total_team + Ckpi_total_team + Cnmi_total_team + Cnmisap_total_team + Cnetan_total_team + Cbo_ocs_total_team + Cinfra_total_team + Cpf_total_team + Cddc_ddp_total_team + Csec_total_team

year, week_num, day_of_week = datetime.date.today().isocalendar()

f = open('/home/esjkadm100/zhshees/Weeklyreport.html','w')

f.write("<tr align=\"center\"><td><b><font size=\"4\"><u>ENIQ-S Weekly Status Dashboard</u></b></font><br>\n")
f.write("<tr align=\"left\"><td><b><font size=\"4\"><u>BUGs Status</u></b></font><br>\n")

f.write("</table></br>\n")
f.write("<table cellspacing=\"26\"><tr align=\"center\"><td><b><font size=\"4\">All GA Blockers</b></font>\n")
f.write("<table border=\"2\" style=\'width:200\'><tr style='background-color:#e0ff44;'><b><font style='font-family:arial;'><th rowspan='2'>Team</th><th rowspan='2'>GA Blocker</th><th rowspan='13'></th><th colspan='4'>Status</th></font></b></tr>\n")

f.write("<tr align=\"center\"><b><font style='font-family:arial;'><td style='background-color:#e0ff44;'>Open</td><td style='background-color:#e0ff44;'>In-Progress</td><td style='background-color:#e0ff44;'>On-Hold</td><td style='background-color:#e0ff44;'>Resolved</td></font></b></tr>\n")

################ status cells update with - if 0 ################

############# NMI status (overall GA table) #################
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

############# NMI status (22.3 GA) #################
if nmi_open_ga2 == 0:
        nmi_op2="<td align=\"center\">-</td>"
else:
        nmi_op2="<td align=\"center\">"+str(nmi_open_ga2)+"</td>"

if nmi_inprog_ga2 == 0:
        nmi_inpr2="<td align=\"center\">-</td>"
else:
        nmi_inpr2="<td align=\"center\">"+str(nmi_inprog_ga2)+"</td>"

if nmi_hold_ga2 == 0:
        nmi_ho2="<td align=\"center\">-</td>"
else:
        nmi_ho2="<td align=\"center\">"+str(nmi_hold_ga2)+"</td>"

if nmi_resolve_ga2 == 0:
        nmi_reso2="<td align=\"center\">-</td>"
else:
        nmi_reso2="<td align=\"center\">"+str(nmi_resolve_ga2)+"</td>"

############# NMI status (22.4 GA) #################
if nmi_open_ga3 == 0:
        nmi_op3="<td align=\"center\">-</td>"
else:
        nmi_op3="<td align=\"center\">"+str(nmi_open_ga3)+"</td>"

if nmi_inprog_ga3 == 0:
        nmi_inpr3="<td align=\"center\">-</td>"
else:
        nmi_inpr3="<td align=\"center\">"+str(nmi_inprog_ga3)+"</td>"

if nmi_hold_ga3 == 0:
        nmi_ho3="<td align=\"center\">-</td>"
else:
        nmi_ho3="<td align=\"center\">"+str(nmi_hold_ga3)+"</td>"

if nmi_resolve_ga3 == 0:
        nmi_reso3="<td align=\"center\">-</td>"
else:
        nmi_reso3="<td align=\"center\">"+str(nmi_resolve_ga3)+"</td>"

################### NMI-SAP status (overall GA) ####################
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

################### NMI-SAP status (22.3 GA) ####################
if nmi_sap_open_ga2 == 0:
        nmi_sap_op2="<td align=\"center\">-</td>"
else:
        nmi_sap_op2="<td align=\"center\">"+str(nmi_sap_open_ga2)+"</td>"

if nmi_sap_inprog_ga2 == 0:
        nmi_sap_inpr2="<td align=\"center\">-</td>"
else:
        nmi_sap_inpr2="<td align=\"center\">"+str(nmi_sap_inprog_ga2)+"</td>"

if nmi_sap_hold_ga2 == 0:
        nmi_sap_ho2="<td align=\"center\">-</td>"
else:
        nmi_sap_ho2="<td align=\"center\">"+str(nmi_sap_hold_ga2)+"</td>"

if nmi_sap_resolved_ga2 == 0:
        nmi_sap_reso2="<td align=\"center\">-</td>"
else:
        nmi_sap_reso2="<td align=\"center\">"+str(nmi_sap_resolved_ga2)+"</td>"

################### NMI-SAP status (22.4 GA) ####################
if nmi_sap_open_ga3 == 0:
        nmi_sap_op3="<td align=\"center\">-</td>"
else:
        nmi_sap_op3="<td align=\"center\">"+str(nmi_sap_open_ga3)+"</td>"

if nmi_sap_inprog_ga3 == 0:
        nmi_sap_inpr3="<td align=\"center\">-</td>"
else:
        nmi_sap_inpr3="<td align=\"center\">"+str(nmi_sap_inprog_ga3)+"</td>"

if nmi_sap_hold_ga3 == 0:
        nmi_sap_ho3="<td align=\"center\">-</td>"
else:
        nmi_sap_ho3="<td align=\"center\">"+str(nmi_sap_hold_ga3)+"</td>"

if nmi_sap_resolved_ga3 == 0:
        nmi_sap_reso3="<td align=\"center\">-</td>"
else:
        nmi_sap_reso3="<td align=\"center\">"+str(nmi_sap_resolved_ga3)+"</td>"

################### DDC/DDP status (overall GA)#####################
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

if ddc_open_ga == 0:
        ddc_op="<td align=\"center\">-</td>"
else:
        ddc_op="<td align=\"center\">"+str(ddc_open_ga)+"</td>"

################################ 22.3 status GA ###############
if ddc_inprog_ga2 == 0:
        ddc_inpr2="<td align=\"center\">-</td>"
else:
        ddc_inpr2="<td align=\"center\">"+str(ddc_inprog_ga2)+"</td>"

if ddc_hold_ga2 == 0:
        ddc_ho2="<td align=\"center\">-</td>"
else:
        ddc_ho2="<td align=\"center\">"+str(ddc_hold_ga2)+"</td>"

if ddc_resolve_ga2 == 0:
        ddc_reso2="<td align=\"center\">-</td>"
else:
        ddc_reso2="<td align=\"center\">"+str(ddc_resolve_ga2)+"</td>"

if ddc_open_ga2 == 0:
        ddc_op2="<td align=\"center\">-</td>"
else:
        ddc_op2="<td align=\"center\">"+str(ddc_open_ga2)+"</td>"

################################ 22.4 status GA ###############
if ddc_inprog_ga3 == 0:
        ddc_inpr3="<td align=\"center\">-</td>"
else:
        ddc_inpr3="<td align=\"center\">"+str(ddc_inprog_ga3)+"</td>"

if ddc_hold_ga3 == 0:
        ddc_ho3="<td align=\"center\">-</td>"
else:
        ddc_ho3="<td align=\"center\">"+str(ddc_hold_ga3)+"</td>"

if ddc_resolve_ga3 == 0:
        ddc_reso3="<td align=\"center\">-</td>"
else:
        ddc_reso3="<td align=\"center\">"+str(ddc_resolve_ga3)+"</td>"

if ddc_open_ga3 == 0:
        ddc_op3="<td align=\"center\">-</td>"
else:
        ddc_op3="<td align=\"center\">"+str(ddc_open_ga3)+"</td>"

####################### PF status (overall GA) ########################
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

####################### PF status (22.3 GA) ########################
if pf_open_ga2 == 0:
        pf_op2="<td align=\"center\">-</td>"
else:
        pf_op2="<td align=\"center\">"+str(pf_open_ga2)+"</td>"

if pf_inprog_ga2 == 0:
        pf_inpr2="<td align=\"center\">-</td>"
else:
        pf_inpr2="<td align=\"center\">"+str(pf_inprog_ga2)+"</td>"

if pf_hold_ga2 == 0:
        pf_ho2="<td align=\"center\">-</td>"
else:
        pf_ho2="<td align=\"center\">"+str(pf_hold_ga2)+"</td>"

if pf_resolve_ga2 == 0:
        pf_reso2="<td align=\"center\">-</td>"
else:
        pf_reso2="<td align=\"center\">"+str(pf_resolve_ga2)+"</td>"

####################### PF status (22.4 GA) ########################
if pf_open_ga3 == 0:
        pf_op3="<td align=\"center\">-</td>"
else:
        pf_op3="<td align=\"center\">"+str(pf_open_ga3)+"</td>"

if pf_inprog_ga3 == 0:
        pf_inpr3="<td align=\"center\">-</td>"
else:
        pf_inpr3="<td align=\"center\">"+str(pf_inprog_ga3)+"</td>"

if pf_hold_ga3 == 0:
        pf_ho3="<td align=\"center\">-</td>"
else:
        pf_ho3="<td align=\"center\">"+str(pf_hold_ga3)+"</td>"

if pf_resolve_ga3 == 0:
        pf_reso3="<td align=\"center\">-</td>"
else:
        pf_reso3="<td align=\"center\">"+str(pf_resolve_ga3)+"</td>"

########################## TP status (overall GA) #######################
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

########################## TP status 22.3 GA #######################
if tp_open_ga2 == 0:
        tp_op2="<td align=\"center\">-</td>"
else:
        tp_op2="<td align=\"center\">"+str(tp_open_ga2)+"</td>"

if tp_inprog_ga2 == 0:
        tp_inpr2="<td align=\"center\">-</td>"
else:
        tp_inpr2="<td align=\"center\">"+str(tp_inprog_ga2)+"</td>"

if tp_hold_ga2 == 0:
        tp_ho2="<td align=\"center\">-</td>"
else:
        tp_ho2="<td align=\"center\">"+str(tp_hold_ga2)+"</td>"

if tp_resolve_ga2 == 0:
        tp_reso2="<td align=\"center\">-</td>"
else:
        tp_reso2="<td align=\"center\">"+str(tp_resolve_ga2)+"</td>"

########################## TP status 22.4 GA #######################
if tp_open_ga3 == 0:
        tp_op3="<td align=\"center\">-</td>"
else:
        tp_op3="<td align=\"center\">"+str(tp_open_ga3)+"</td>"

if tp_inprog_ga3 == 0:
        tp_inpr3="<td align=\"center\">-</td>"
else:
        tp_inpr3="<td align=\"center\">"+str(tp_inprog_ga3)+"</td>"

if tp_hold_ga3 == 0:
        tp_ho3="<td align=\"center\">-</td>"
else:
        tp_ho3="<td align=\"center\">"+str(tp_hold_ga3)+"</td>"

if tp_resolve_ga3 == 0:
        tp_reso3="<td align=\"center\">-</td>"
else:
        tp_reso3="<td align=\"center\">"+str(tp_resolve_ga3)+"</td>"

####################### KPI status (overall GA)####################
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

####################### KPI status (22.3 GA)####################
if kpi_open_ga2 == 0:
        kpi_op2="<td align=\"center\">-</td>"
else:
        kpi_op2="<td align=\"center\">"+str(kpi_open_ga2)+"</td>"

if kpi_inprog_ga2 == 0:
        kpi_inpr2="<td align=\"center\">-</td>"
else:
        kpi_inpr2="<td align=\"center\">"+str(kpi_inprog_ga2)+"</td>"

if kpi_hold_ga2 == 0:
        kpi_ho2="<td align=\"center\">-</td>"
else:
        kpi_ho2="<td align=\"center\">"+str(kpi_hold_ga2)+"</td>"

if kpi_resolve_ga2 == 0:
        kpi_reso2="<td align=\"center\">-</td>"
else:
        kpi_reso2="<td align=\"center\">"+str(kpi_resolve_ga2)+"</td>"

####################### KPI status (22.4 GA)####################
if kpi_open_ga3 == 0:
        kpi_op3="<td align=\"center\">-</td>"
else:
        kpi_op3="<td align=\"center\">"+str(kpi_open_ga3)+"</td>"

if kpi_inprog_ga3 == 0:
        kpi_inpr3="<td align=\"center\">-</td>"
else:
        kpi_inpr3="<td align=\"center\">"+str(kpi_inprog_ga3)+"</td>"

if kpi_hold_ga3 == 0:
        kpi_ho3="<td align=\"center\">-</td>"
else:
        kpi_ho3="<td align=\"center\">"+str(kpi_hold_ga3)+"</td>"

if kpi_resolve_ga3 == 0:
        kpi_reso3="<td align=\"center\">-</td>"
else:
        kpi_reso3="<td align=\"center\">"+str(kpi_resolve_ga3)+"</td>"

#################### Netan status (overall GA) ##################
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

#################### Netan status (22.3 GA) ##################
if netan_open_ga2 == 0:
        netan_op2="<td align=\"center\">-</td>"
else:
        netan_op2="<td align=\"center\">"+str(netan_open_ga2)+"</td>"

if netan_inprog_ga2 == 0:
        netan_inpr2="<td align=\"center\">-</td>"
else:
        netan_inpr2="<td align=\"center\">"+str(netan_inprog_ga2)+"</td>"

if netan_hold_ga2 == 0:
        netan_ho2="<td align=\"center\">-</td>"
else:
        netan_ho2="<td align=\"center\">"+str(netan_hold_ga2)+"</td>"

if netan_resolve_ga2 == 0:
        netan_reso2="<td align=\"center\">-</td>"
else:
        netan_reso2="<td align=\"center\">"+str(netan_resolve_ga2)+"</td>"

#################### Netan status (22.4 GA) ##################
if netan_open_ga3 == 0:
        netan_op3="<td align=\"center\">-</td>"
else:
        netan_op3="<td align=\"center\">"+str(netan_open_ga3)+"</td>"

if netan_inprog_ga3 == 0:
        netan_inpr3="<td align=\"center\">-</td>"
else:
        netan_inpr3="<td align=\"center\">"+str(netan_inprog_ga3)+"</td>"

if netan_hold_ga3 == 0:
        netan_ho3="<td align=\"center\">-</td>"
else:
        netan_ho3="<td align=\"center\">"+str(netan_hold_ga3)+"</td>"

if netan_resolve_ga3 == 0:
        netan_reso3="<td align=\"center\">-</td>"
else:
        netan_reso3="<td align=\"center\">"+str(netan_resolve_ga3)+"</td>"

##################### BO/OCS status (overall GA)######################
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

##################### BO/OCS status 22.3 GA ######################
if bo_open_ga2 == 0:
        bo_op2="<td align=\"center\">-</td>"
else:
        bo_op2="<td align=\"center\">"+str(bo_open_ga2)+"</td>"

if bo_inprog_ga2 == 0:
        bo_inpr2="<td align=\"center\">-</td>"
else:
        bo_inpr2="<td align=\"center\">"+str(bo_inprog_ga2)+"</td>"

if bo_hold_ga2 == 0:
        bo_ho2="<td align=\"center\">-</td>"
else:
        bo_ho2="<td align=\"center\">"+str(bo_hold_ga2)+"</td>"

if bo_resolve_ga2 == 0:
        bo_reso2="<td align=\"center\">-</td>"
else:
        bo_reso2="<td align=\"center\">"+str(bo_resolve_ga2)+"</td>"

##################### BO/OCS status 22.4 GA ######################
if bo_open_ga3 == 0:
        bo_op3="<td align=\"center\">-</td>"
else:
        bo_op3="<td align=\"center\">"+str(bo_open_ga3)+"</td>"

if bo_inprog_ga3 == 0:
        bo_inpr3="<td align=\"center\">-</td>"
else:
        bo_inpr3="<td align=\"center\">"+str(bo_inprog_ga3)+"</td>"

if bo_hold_ga3 == 0:
        bo_ho3="<td align=\"center\">-</td>"
else:
        bo_ho3="<td align=\"center\">"+str(bo_hold_ga3)+"</td>"

if bo_resolve_ga3 == 0:
        bo_reso3="<td align=\"center\">-</td>"
else:
        bo_reso3="<td align=\"center\">"+str(bo_resolve_ga3)+"</td>"

########################### Infra status overall GA #########################
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

########################### Infra status 22.3 GA #########################
if infra_open_ga2 == 0:
        infra_op2="<td align=\"center\">-</td>"
else:
        infra_op2="<td align=\"center\">"+str(infra_open_ga2)+"</td>"

if infra_inprog_ga2 == 0:
        infra_inpr2="<td align=\"center\">-</td>"
else:
        infra_inpr2="<td align=\"center\">"+str(infra_inprog_ga2)+"</td>"

if infra_hold_ga2 == 0:
        infra_ho2="<td align=\"center\">-</td>"
else:
        infra_ho2="<td align=\"center\">"+str(infra_hold_ga2)+"</td>"

if infra_resolve_ga2 == 0:
        infra_reso2="<td align=\"center\">-</td>"
else:
        infra_reso2="<td align=\"center\">"+str(infra_resolve_ga2)+"</td>"

########################### Infra status 22.4 GA #########################
if infra_open_ga3 == 0:
        infra_op3="<td align=\"center\">-</td>"
else:
        infra_op3="<td align=\"center\">"+str(infra_open_ga3)+"</td>"

if infra_inprog_ga3 == 0:
        infra_inpr3="<td align=\"center\">-</td>"
else:
        infra_inpr3="<td align=\"center\">"+str(infra_inprog_ga3)+"</td>"

if infra_hold_ga3 == 0:
        infra_ho3="<td align=\"center\">-</td>"
else:
        infra_ho3="<td align=\"center\">"+str(infra_hold_ga3)+"</td>"

if infra_resolve_ga3 == 0:
        infra_reso3="<td align=\"center\">-</td>"
else:
        infra_reso3="<td align=\"center\">"+str(infra_resolve_ga3)+"</td>"

######################## Security status GA (overall) ############################
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

######################## Security status 22.3 GA ############################
if sec_open_ga2 == 0:
        sec_op2="<td align=\"center\">-</td>"
else:
        sec_op2="<td align=\"center\">"+str(sec_open_ga2)+"</td>"

if sec_inprog_ga2 == 0:
        sec_inpr2="<td align=\"center\">-</td>"
else:
        sec_inpr2="<td align=\"center\">"+str(sec_inprog_ga2)+"</td>"

if sec_hold_ga2 == 0:
        sec_ho2="<td align=\"center\">-</td>"
else:
        sec_ho2="<td align=\"center\">"+str(sec_hold_ga2)+"</td>"

if sec_resolve_ga2 == 0:
        sec_reso2="<td align=\"center\">-</td>"
else:
        sec_reso2="<td align=\"center\">"+str(sec_resolve_ga2)+"</td>"

######################## Security status 22.4 GA ############################
if sec_open_ga3 == 0:
        sec_op3="<td align=\"center\">-</td>"
else:
        sec_op3="<td align=\"center\">"+str(sec_open_ga3)+"</td>"

if sec_inprog_ga3 == 0:
        sec_inpr3="<td align=\"center\">-</td>"
else:
        sec_inpr3="<td align=\"center\">"+str(sec_inprog_ga3)+"</td>"

if sec_hold_ga3 == 0:
        sec_ho3="<td align=\"center\">-</td>"
else:
        sec_ho3="<td align=\"center\">"+str(sec_hold_ga3)+"</td>"

if sec_resolve_ga3 == 0:
        sec_reso3="<td align=\"center\">-</td>"
else:
        sec_reso3="<td align=\"center\">"+str(sec_resolve_ga3)+"</td>"

#################### total status overall GA ###################
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

#################### total status 22.3 GA ###################
if total_inprog_ga2 == 0:
        total_inpr2="<td align=\"center\">-</td>"
else:
        total_inpr2="<td align=\"center\">"+str(total_inprog_ga2)+"</td>"

if total_open_ga2 == 0:
        total_op2="<td align=\"center\">-</td>"
else:
        total_op2="<td align=\"center\">"+str(total_open_ga2)+"</td>"

if total_hold_ga2 == 0:
        total_ho2="<td align=\"center\">-</td>"
else:
        total_ho2="<td align=\"center\">"+str(total_hold_ga2)+"</td>"

if total_resolve_ga2 == 0:
        total_reso2="<td align=\"center\">-</td>"
else:
        total_reso2="<td align=\"center\">"+str(total_resolve_ga2)+"</td>"

#################### total status 22.4 GA ###################
if total_inprog_ga3 == 0:
        total_inpr3="<td align=\"center\">-</td>"
else:
        total_inpr3="<td align=\"center\">"+str(total_inprog_ga3)+"</td>"

if total_open_ga3 == 0:
        total_op3="<td align=\"center\">-</td>"
else:
        total_op3="<td align=\"center\">"+str(total_open_ga3)+"</td>"

if total_hold_ga3 == 0:
        total_ho3="<td align=\"center\">-</td>"
else:
        total_ho3="<td align=\"center\">"+str(total_hold_ga3)+"</td>"

if total_resolve_ga3 == 0:
        total_reso3="<td align=\"center\">-</td>"
else:
        total_reso3="<td align=\"center\">"+str(total_resolve_ga3)+"</td>"

###########################################################################
if nmi_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106181\"><font color=\"red\">"+str(nmi_ga)+"</font></a></td>"+nmi_op+" "+nmi_inpr+" "+nmi_ho+" "+nmi_reso+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106181\"><font color=\"blue\">"+str(nmi_ga)+"</font></a></td>"+nmi_op+" "+nmi_inpr+" "+nmi_ho+" "+nmi_reso+"</font></tr>\n")

if nmisap_ga >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI-SAP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106415\"><font color=\"red\">"+str(nmisap_ga)+"</font></a></td>"+nmi_sap_op+" "+nmi_sap_inpr+" "+nmi_sap_ho+" "+nmi_sap_reso+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI-SAP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106415\"><font color=\"blue\">"+str(nmisap_ga)+"</font></a></td>"+nmi_sap_op+" "+nmi_sap_inpr+" "+nmi_sap_ho+" "+nmi_sap_reso+"</font></tr>\n")

if ddc_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>DDC/DDP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106182\"><font color=\"red\">"+str(ddc_ga)+"</font></a></td>"+ddc_op+" "+ddc_inpr+" "+ddc_ho+" "+ddc_reso+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>DDC/DDP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106182\"><font color=\"blue\">"+str(ddc_ga)+"</font></a></td>"+ddc_op+" "+ddc_inpr+" "+ddc_ho+" "+ddc_reso+"</font></tr>\n")

if pf_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>PF</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106180\"><font color=\"red\">"+str(pf_ga)+"</font></a></td>"+pf_op+" "+pf_inpr+" "+pf_ho+" "+pf_reso+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>PF</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106180\"><font color=\"blue\">"+str(pf_ga)+"</font></a></td>"+pf_op+" "+pf_inpr+" "+pf_ho+" "+pf_reso+"</font></tr>\n")

if tp_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>TP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106183\"><font color=\"red\">"+str(tp_ga)+"</font></a></td>"+tp_op+" "+tp_inpr+" "+tp_ho+" "+tp_reso+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>TP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106183\"><font color=\"blue\">"+str(tp_ga)+"</font></a></td>"+tp_op+" "+tp_inpr+" "+tp_ho+" "+tp_reso+"</font></tr>\n")

if kpi_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>KPI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107191\"><font color=\"red\">"+str(kpi_ga)+"</font></a></td>"+kpi_op+" "+kpi_inpr+" "+kpi_ho+" "+kpi_reso+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>KPI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107191\"><font color=\"blue\">"+str(kpi_ga)+"</font></a></td>"+kpi_op+" "+kpi_inpr+" "+kpi_ho+" "+kpi_reso+"</font></tr>\n")

if netan_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NetAn</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106184\"><font color=\"red\">"+str(netan_ga)+"</font></a></td>"+netan_op+" "+netan_inpr+" "+netan_ho+" "+netan_reso+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NetAn</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106184\"><font color=\"blue\">"+str(netan_ga)+"</font></a></td>"+netan_op+" "+netan_inpr+" "+netan_ho+" "+netan_reso+"</font></tr>\n")

if bo_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>BO/OCS</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106185\"><font color=\"red\">"+str(bo_ga)+"</font></a></td>"+bo_op+" "+bo_inpr+" "+bo_ho+" "+bo_reso+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>BO/OCS</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106185\"><font color=\"blue\">"+str(bo_ga)+"</font></a></td>"+bo_op+" "+bo_inpr+" "+bo_ho+" "+bo_reso+"</font></tr>\n")

if infra_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Infra</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106186\"><font color=\"red\">"+str(infra_ga)+"</font></a></td>"+infra_op+" "+infra_inpr+" "+infra_ho+" "+infra_reso+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Infra</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106186\"><font color=\"blue\">"+str(infra_ga)+"</font></a></td>"+infra_op+" "+infra_inpr+" "+infra_ho+" "+infra_reso+"</font></tr>\n")

if sec_ga >= 1:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Security</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106187\"><font color=\"red\">"+str(sec_ga)+"</font></a></td>"+sec_op+" "+sec_inpr+" "+sec_ho+" "+sec_reso+"</font></tr>\n")
else:
	f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Security</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106187\"><font color=\"blue\">"+str(sec_ga)+"</font></a></td>"+sec_op+" "+sec_inpr+" "+sec_ho+" "+sec_reso+"</font></tr>\n")

if total_ga > 0:
	f.write("<tr align=\"center\" style='background-color:#fcdfff;'><font style='font-family:arial;'><b><td>Total</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106189\"><font color=\"red\">"+str(total_ga)+"</font></a></td>"+total_op+" "+total_inpr+" "+total_ho+" "+total_reso+"</b></font></tr>\n")
else:
	f.write("<tr align=\"center\" style='background-color:#fcdfff;'><font style='font-family:arial;'><b><td>Total</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106189\"><font color=\"blue\">"+str(total_ga)+"</font></a></td>"+total_op+" "+total_inpr+" "+total_ho+" "+total_reso+"</b></font></tr>\n")

f.write("</table>\n</br></td>\n")

f.write("<td><b><font size=\"4\">22.3 GA Blockers</b></font>\n")
#f.write("<table><tr align=\"center\"><td><b><font size=\"4\">GA Blocker 2</b></font>\n")
f.write("<table border=\"2\" style=\'width:200\'><tr style='background-color:#e0ff44;'><b><font style='font-family:arial;'><th rowspan='2'>Team</th><th rowspan='2'>GA Blocker</th><th rowspan='13'></th><th colspan='4'>Status</th></font></b></tr>\n")

f.write("<tr align=\"center\"><b><font style='font-family:arial;'><td style='background-color:#e0ff44;'>Open</td><td style='background-color:#e0ff44;'>In-Progress</td><td style='background-color:#e0ff44;'>On-Hold</td><td style='background-color:#e0ff44;'>Resolved</td></font></b></tr>\n")

if nmi_ga2 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106181\"><font color=\"red\">"+str(nmi_ga2)+"</font></a></td>"+nmi_op2+" "+nmi_inpr2+" "+nmi_ho2+" "+nmi_reso2+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106181\"><font color=\"blue\">"+str(nmi_ga2)+"</font></a></td>"+nmi_op2+" "+nmi_inpr2+" "+nmi_ho2+" "+nmi_reso2+"</font></tr>\n")

if nmisap_ga2 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI-SAP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106415\"><font color=\"red\">"+str(nmisap_ga2)+"</font></a></td>"+nmi_sap_op2+" "+nmi_sap_inpr2+" "+nmi_sap_ho2+" "+nmi_sap_reso2+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI-SAP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106415\"><font color=\"blue\">"+str(nmisap_ga2)+"</font></a></td>"+nmi_sap_op2+" "+nmi_sap_inpr2+" "+nmi_sap_ho2+" "+nmi_sap_reso2+"</font></tr>\n")

if ddc_ga2 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>DDC/DDP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106182\"><font color=\"red\">"+str(ddc_ga2)+"</font></a></td>"+ddc_op2+" "+ddc_inpr2+" "+ddc_ho2+" "+ddc_reso2+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>DDC/DDP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106182\"><font color=\"blue\">"+str(ddc_ga2)+"</font></a></td>"+ddc_op2+" "+ddc_inpr2+" "+ddc_ho2+" "+ddc_reso2+"</font></tr>\n")

if pf_ga2 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>PF</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106180\"><font color=\"red\">"+str(pf_ga2)+"</font></a></td>"+pf_op2+" "+pf_inpr2+" "+pf_ho2+" "+pf_reso2+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>PF</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106180\"><font color=\"blue\">"+str(pf_ga2)+"</font></a></td>"+pf_op2+" "+pf_inpr2+" "+pf_ho2+" "+pf_reso2+"</font></tr>\n")

if tp_ga2 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>TP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106183\"><font color=\"red\">"+str(tp_ga2)+"</font></a></td>"+tp_op2+" "+tp_inpr2+" "+tp_ho2+" "+tp_reso2+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>TP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106183\"><font color=\"blue\">"+str(tp_ga2)+"</font></a></td>"+tp_op2+" "+tp_inpr2+" "+tp_ho2+" "+tp_reso2+"</font></tr>\n")

if kpi_ga2 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>KPI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107191\"><font color=\"red\">"+str(kpi_ga2)+"</font></a></td>"+kpi_op2+" "+kpi_inpr2+" "+kpi_ho2+" "+kpi_reso2+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>KPI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107191\"><font color=\"blue\">"+str(kpi_ga2)+"</font></a></td>"+kpi_op2+" "+kpi_inpr2+" "+kpi_ho2+" "+kpi_reso2+"</font></tr>\n")

if netan_ga2 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NetAn</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106184\"><font color=\"red\">"+str(netan_ga2)+"</font></a></td>"+netan_op2+" "+netan_inpr2+" "+netan_ho2+" "+netan_reso2+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NetAn</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106184\"><font color=\"blue\">"+str(netan_ga2)+"</font></a></td>"+netan_op2+" "+netan_inpr2+" "+netan_ho2+" "+netan_reso2+"</font></tr>\n")

if bo_ga2 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>BO/OCS</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106185\"><font color=\"red\">"+str(bo_ga2)+"</font></a></td>"+bo_op2+" "+bo_inpr2+" "+bo_ho2+" "+bo_reso2+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>BO/OCS</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106185\"><font color=\"blue\">"+str(bo_ga2)+"</font></a></td>"+bo_op2+" "+bo_inpr2+" "+bo_ho2+" "+bo_reso2+"</font></tr>\n")

if infra_ga2 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Infra</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106186\"><font color=\"red\">"+str(infra_ga2)+"</font></a></td>"+infra_op2+" "+infra_inpr2+" "+infra_ho2+" "+infra_reso2+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Infra</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106186\"><font color=\"blue\">"+str(infra_ga2)+"</font></a></td>"+infra_op2+" "+infra_inpr2+" "+infra_ho2+" "+infra_reso2+"</font></tr>\n")

if sec_ga2 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Security</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106187\"><font color=\"red\">"+str(sec_ga2)+"</font></a></td>"+sec_op2+" "+sec_inpr2+" "+sec_ho2+" "+sec_reso2+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Security</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106187\"><font color=\"blue\">"+str(sec_ga2)+"</font></a></td>"+sec_op2+" "+sec_inpr2+" "+sec_ho2+" "+sec_reso2+"</font></tr>\n")

if total_ga2 > 0:
        f.write("<tr align=\"center\" style='background-color:#fcdfff;'><font style='font-family:arial;'><b><td>Total</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106189\"><font color=\"red\">"+str(total_ga2)+"</font></a></td>"+total_op2+" "+total_inpr2+" "+total_ho2+" "+total_reso2+"</b></font></tr>\n")
else:
        f.write("<tr align=\"center\" style='background-color:#fcdfff;'><font style='font-family:arial;'><b><td>Total</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106189\"><font color=\"blue\">"+str(total_ga2)+"</font></a></td>"+total_op2+" "+total_inpr2+" "+total_ho2+" "+total_reso2+"</b></font></tr>\n")

f.write("</table>\n</br></td>\n")

f.write("<td><b><font size=\"4\">22.4 GA Blockers</b></font>\n")
f.write("<table border=\"2\" style=\'width:200\'><tr style='background-color:#e0ff44;'><b><font style='font-family:arial;'><th rowspan='2'>Team</th><th rowspan='2'>GA Blocker</th><th rowspan='13'></th><th colspan='4'>Status</th></font></b></tr>\n")

f.write("<tr align=\"center\"><b><font style='font-family:arial;'><td style='background-color:#e0ff44;'>Open</td><td style='background-color:#e0ff44;'>In-Progress</td><td style='background-color:#e0ff44;'>On-Hold</td><td style='background-color:#e0ff44;'>Resolved</td></font></b></tr>\n")

if nmi_ga3 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106181\"><font color=\"red\">"+str(nmi_ga3)+"</font></a></td>"+nmi_op3+" "+nmi_inpr3+" "+nmi_ho3+" "+nmi_reso3+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106181\"><font color=\"blue\">"+str(nmi_ga3)+"</font></a></td>"+nmi_op3+" "+nmi_inpr3+" "+nmi_ho3+" "+nmi_reso3+"</font></tr>\n")

if nmisap_ga3 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI-SAP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106415\"><font color=\"red\">"+str(nmisap_ga3)+"</font></a></td>"+nmi_sap_op3+" "+nmi_sap_inpr3+" "+nmi_sap_ho3+" "+nmi_sap_reso3+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NMI-SAP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106415\"><font color=\"blue\">"+str(nmisap_ga3)+"</font></a></td>"+nmi_sap_op3+" "+nmi_sap_inpr3+" "+nmi_sap_ho3+" "+nmi_sap_reso3+"</font></tr>\n")

if ddc_ga3 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>DDC/DDP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106182\"><font color=\"red\">"+str(ddc_ga3)+"</font></a></td>"+ddc_op3+" "+ddc_inpr3+" "+ddc_ho3+" "+ddc_reso3+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>DDC/DDP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106182\"><font color=\"blue\">"+str(ddc_ga3)+"</font></a></td>"+ddc_op3+" "+ddc_inpr3+" "+ddc_ho3+" "+ddc_reso3+"</font></tr>\n")

if pf_ga3 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>PF</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106180\"><font color=\"red\">"+str(pf_ga3)+"</font></a></td>"+pf_op3+" "+pf_inpr3+" "+pf_ho3+" "+pf_reso3+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>PF</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106180\"><font color=\"blue\">"+str(pf_ga3)+"</font></a></td>"+pf_op3+" "+pf_inpr3+" "+pf_ho3+" "+pf_reso3+"</font></tr>\n")

if tp_ga3 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>TP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106183\"><font color=\"red\">"+str(tp_ga3)+"</font></a></td>"+tp_op3+" "+tp_inpr3+" "+tp_ho3+" "+tp_reso3+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>TP</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106183\"><font color=\"blue\">"+str(tp_ga3)+"</font></a></td>"+tp_op3+" "+tp_inpr3+" "+tp_ho3+" "+tp_reso3+"</font></tr>\n")

if kpi_ga3 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>KPI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107191\"><font color=\"red\">"+str(kpi_ga3)+"</font></a></td>"+kpi_op3+" "+kpi_inpr3+" "+kpi_ho3+" "+kpi_reso3+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>KPI</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107191\"><font color=\"blue\">"+str(kpi_ga3)+"</font></a></td>"+kpi_op3+" "+kpi_inpr3+" "+kpi_ho3+" "+kpi_reso3+"</font></tr>\n")

if netan_ga3 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NetAn</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106184\"><font color=\"red\">"+str(netan_ga3)+"</font></a></td>"+netan_op3+" "+netan_inpr3+" "+netan_ho3+" "+netan_reso3+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>NetAn</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106184\"><font color=\"blue\">"+str(netan_ga3)+"</font></a></td>"+netan_op3+" "+netan_inpr3+" "+netan_ho3+" "+netan_reso3+"</font></tr>\n")

if bo_ga3 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>BO/OCS</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106185\"><font color=\"red\">"+str(bo_ga3)+"</font></a></td>"+bo_op3+" "+bo_inpr3+" "+bo_ho3+" "+bo_reso3+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>BO/OCS</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106185\"><font color=\"blue\">"+str(bo_ga3)+"</font></a></td>"+bo_op3+" "+bo_inpr3+" "+bo_ho3+" "+bo_reso3+"</font></tr>\n")

if infra_ga3 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Infra</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106186\"><font color=\"red\">"+str(infra_ga3)+"</font></a></td>"+infra_op3+" "+infra_inpr3+" "+infra_ho3+" "+infra_reso3+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Infra</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106186\"><font color=\"blue\">"+str(infra_ga3)+"</font></a></td>"+infra_op3+" "+infra_inpr3+" "+infra_ho3+" "+infra_reso3+"</font></tr>\n")

if sec_ga3 >= 1:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Security</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106187\"><font color=\"red\">"+str(sec_ga3)+"</font></a></td>"+sec_op3+" "+sec_inpr3+" "+sec_ho3+" "+sec_reso3+"</font></tr>\n")
else:
        f.write("<tr align=\"left\"><font style='font-family:arial;'><td style='background-color:#93c1f6;'>Security</td><td align=\"center\"><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106187\"><font color=\"blue\">"+str(sec_ga3)+"</font></a></td>"+sec_op3+" "+sec_inpr3+" "+sec_ho3+" "+sec_reso3+"</font></tr>\n")

if total_ga3 > 0:
        f.write("<tr align=\"center\" style='background-color:#fcdfff;'><font style='font-family:arial;'><b><td>Total</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106189\"><font color=\"red\">"+str(total_ga3)+"</font></a></td>"+total_op3+" "+total_inpr3+" "+total_ho3+" "+total_reso3+"</b></font></tr>\n")
else:
        f.write("<tr align=\"center\" style='background-color:#fcdfff;'><font style='font-family:arial;'><b><td>Total</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106189\"><font color=\"blue\">"+str(total_ga3)+"</font></a></td>"+total_op3+" "+total_inpr3+" "+total_ho3+" "+total_reso3+"</b></font></tr>\n")

f.write("</table>\n</br></td>\n")

###Threshold check############

#for security 
if sec_total_team <= 1:
		sec_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
		sec_threshold="<td style='background-color:red'>Yes</td>"	
if Bsec_total_team <= 1:
                Bsec_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
                Bsec_threshold="<td style='background-color:red'>Yes</td>"
if Csec_total_team <= 1:
                Csec_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
                Csec_threshold="<td style='background-color:red'>Yes</td>"

#for ddc_ddp  
if ddc_ddp_total_team <= 1:
		ddc_ddp_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
		ddc_ddp_threshold="<td style='background-color:red'>Yes</td>"
if Bddc_ddp_total_team <= 1:
                Bddc_ddp_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
                Bddc_ddp_threshold="<td style='background-color:red'>Yes</td>"
if Cddc_ddp_total_team <= 1:
                Cddc_ddp_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
                Cddc_ddp_threshold="<td style='background-color:red'>Yes</td>"

#for infra 
if infra_total_team <= 2:
		infra_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
		infra_threshold="<td style='background-color:red'>Yes</td>"
if Binfra_total_team <= 2:
                Binfra_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
                Binfra_threshold="<td style='background-color:red'>Yes</td>"
if Cinfra_total_team <= 2:
                Cinfra_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
                Cinfra_threshold="<td style='background-color:red'>Yes</td>"

#for tp 
tp_kpi_total = tp_total_team + kpi_total_team
Btp_kpi_total = Btp_total_team + Bkpi_total_team
Ctp_kpi_total = Ctp_total_team + Ckpi_total_team
if tp_kpi_total <= 3:
		tp_threshold="<td style='background-color:#98FF98;' rowspan='2'>No</td>"
else:
		tp_threshold="<td style='background-color:red' rowspan='2'>Yes</td>"
if Btp_kpi_total <= 3:
                Btp_threshold="<td style='background-color:#98FF98;' rowspan='2'>No</td>"
else:
                Btp_threshold="<td style='background-color:red' rowspan='2'>Yes</td>"
if Ctp_kpi_total <= 3:
                Ctp_threshold="<td style='background-color:#98FF98;' rowspan='2'>No</td>"
else:
                Ctp_threshold="<td style='background-color:red' rowspan='2'>Yes</td>"

#for nmi
nmi_nmisap_total = nmi_total_team + nmisap_total_team
Bnmi_nmisap_total = Bnmi_total_team + Bnmisap_total_team
Cnmi_nmisap_total = Cnmi_total_team + Cnmisap_total_team
if nmi_nmisap_total <= 3:
		nmi_threshold="<td style='background-color:#98FF98;' rowspan='2'>No</td>"
else:
		nmi_threshold="<td style='background-color:red' rowspan='2'>Yes</td>"
if Bnmi_nmisap_total <= 3:
                Bnmi_threshold="<td style='background-color:#98FF98;' rowspan='2'>No</td>"
else:
                Bnmi_threshold="<td style='background-color:red' rowspan='2'>Yes</td>"
if Cnmi_nmisap_total <= 3:
                Cnmi_threshold="<td style='background-color:#98FF98;' rowspan='2'>No</td>"
else:
                Cnmi_threshold="<td style='background-color:red' rowspan='2'>Yes</td>"

#for netan 
if netan_total_team <= 2:
		netan_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
		netan_threshold="<td style='background-color:red'>Yes</td>"
if Bnetan_total_team <= 2:
                Bnetan_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
                Bnetan_threshold="<td style='background-color:red'>Yes</td>"
if Cnetan_total_team <= 2:
                Cnetan_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
                Cnetan_threshold="<td style='background-color:red'>Yes</td>"

#for bo_ocs
if bo_ocs_total_team <= 2:
		bo_ocs_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
		bo_ocs_threshold="<td style='background-color:red'>Yes</td>"
if Bbo_ocs_total_team <= 2:
                Bbo_ocs_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
                Bbo_ocs_threshold="<td style='background-color:red'>Yes</td>"
if Cbo_ocs_total_team <= 2:
                Cbo_ocs_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
                Cbo_ocs_threshold="<td style='background-color:red'>Yes</td>"

#for pf 
if pf_total_team <= 2:
		pf_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
		pf_threshold="<td style='background-color:red'>Yes</td>"
if Bpf_total_team <= 2:
                Bpf_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
                Bpf_threshold="<td style='background-color:red'>Yes</td>"
if Cpf_total_team <= 2:
                Cpf_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
                Cpf_threshold="<td style='background-color:red'>Yes</td>"

#for total teams 
if total_uniq <= 15:
		total_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
		total_threshold="<td style='background-color:red'>Yes</td>"		
if Btotal_uniq <= 15:
                Btotal_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
                Btotal_threshold="<td style='background-color:red'>Yes</td>"
if Ctotal_uniq <= 15:
                Ctotal_threshold="<td style='background-color:#98FF98;'>No</td>"
else:
                Ctotal_threshold="<td style='background-color:red'>Yes</td>"

########################## NMI status main table #############
if nmi_open == 0:
        nmi_op1="<td align=\"center\">-</td>"
else:
        nmi_op1="<td align=\"center\">"+str(nmi_open)+"</td>"
if nmi_open2 == 0:
	Bnmi_op1="<td align=\"center\">-</td>"
else:
	Bnmi_op1="<td align=\"center\">"+str(nmi_open2)+"</td>"
if nmi_open3 == 0:
	Cnmi_op1="<td align=\"center\">-</td>"
else:
	Cnmi_op1="<td align=\"center\">"+str(nmi_open3)+"</td>"

if nmi_inprog == 0:
        nmi_inpr1="<td align=\"center\">-</td>"
else:
        nmi_inpr1="<td align=\"center\">"+str(nmi_inprog)+"</td>"
if nmi_inprog2 == 0:
	Bnmi_inpr1="<td align=\"center\">-</td>"
else:
	Bnmi_inpr1="<td align=\"center\">"+str(nmi_inprog2)+"</td>"
if nmi_inprog3 == 0:
	Cnmi_inpr1="<td align=\"center\">-</td>"
else:
	Cnmi_inpr1="<td align=\"center\">"+str(nmi_inprog3)+"</td>"

if nmi_hold == 0:
        nmi_ho1="<td align=\"center\">-</td>"
else:
        nmi_ho1="<td align=\"center\">"+str(nmi_hold)+"</td>"
if nmi_hold2 == 0:
	Bnmi_ho1="<td align=\"center\">-</td>"
else:
	Bnmi_inpr1="<td align=\"center\">"+str(nmi_hold2)+"</td>"
if nmi_hold3 == 0:
	Cnmi_ho1="<td align=\"center\">-</td>"
else:
	Cnmi_inpr1="<td align=\"center\">"+str(nmi_hold3)+"</td>"

if nmi_resolve == 0:
        nmi_reso1="<td align=\"center\">-</td>"
else:
        nmi_reso1="<td align=\"center\">"+str(nmi_resolve)+"</td>"
if nmi_resolve2 == 0:
	Bnmi_reso1="<td align=\"center\">-</td>"
else:
	Bnmi_reso1="<td align=\"center\">"+str(nmi_resolve2)+"</td>"
if nmi_resolve3 == 0:
	Cnmi_reso1="<td align=\"center\">-</td>"
else:
	Cnmi_reso1="<td align=\"center\">"+str(nmi_resolve3)+"</td>"

############################ NMI-SAP status main table ###################
if nmi_sap_open == 0:
        nmi_sap_op1="<td align=\"center\">-</td>"
else:
        nmi_sap_op1="<td align=\"center\">"+str(nmi_sap_open)+"</td>"
if nmi_sap_open2 == 0:
	Bnmi_sap_op1="<td align=\"center\">-</td>"
else:
	Bnmi_sap_op1="<td align=\"center\">"+str(nmi_sap_open2)+"</td>"
if nmi_sap_open3 == 0:
	Cnmi_sap_op1="<td align=\"center\">-</td>"
else:
	Cnmi_sap_op1="<td align=\"center\">"+str(nmi_sap_open3)+"</td>"

if nmi_sap_inprog == 0:
        nmi_sap_inpr1="<td align=\"center\">-</td>"
else:
        nmi_sap_inpr1="<td align=\"center\">"+str(nmi_sap_inprog)+"</td>"
if nmi_sap_inprog2 ==0:
	Bnmi_sap_inpr1="<td align=\"center\">-</td>"
else:
	Bnmi_sap_inpr1="<td align=\"center\">"+str(nmi_sap_inprog2)+"</td>"
if nmi_sap_inprog3 == 0:
	Cnmi_sap_inpr1="<td align=\"center\">-</td>"
else:
	Cnmi_sap_inpr1="<td align=\"center\">"+str(nmi_sap_inprog3)+"</td>"

if nmi_sap_hold == 0:
        nmi_sap_ho1="<td align=\"center\">-</td>"
else:
        nmi_sap_ho1="<td align=\"center\">"+str(nmi_sap_hold)+"</td>"
if nmi_sap_hold2 == 0:
	Bnmi_sap_ho1="<td align=\"center\">-</td>"
else:
	Bnmi_sap_ho1="<td align=\"center\">"+str(nmi_sap_hold2)+"</td>"
if nmi_sap_hold3 == 0:
	Cnmi_sap_ho1="<td align=\"center\">-</td>"
else:
	Cnmi_sap_ho1="<td align=\"center\">"+str(nmi_sap_hold3)+"</td>"

if nmi_sap_resolve == 0:
        nmi_sap_reso1="<td align=\"center\">-</td>"
else:
        nmi_sap_reso1="<td align=\"center\">"+str(nmi_sap_resolve)+"</td>"
if nmi_sap_resolve2 == 0:
	Bnmi_sap_reso1="<td align=\"center\">-</td>"
else:
	Bnmi_sap_reso1="<td align=\"center\">"+str(nmi_sap_resolve2)+"</td>"
if nmi_sap_resolve3 == 0:
	Cnmi_sap_reso1="<td align=\"center\">-</td>"
else:
	Cnmi_sap_reso1="<td align=\"center\">"+str(nmi_sap_resolve3)+"</td>"
######################### DDC/DDP status main table #######################
if ddc_open == 0:
        ddc_op1="<td align=\"center\">-</td>"
else:
        ddc_op1="<td align=\"center\">"+str(ddc_open)+"</td>"
if ddc_open2 == 0:
	Bddc_op1="<td align=\"center\">-</td>"
else:
	Bddc_op1="<td align=\"center\">"+str(ddc_open2)+"</td>"
if ddc_open3 == 0:
	Cddc_op1="<td align=\"center\">-</td>"
else:
	Cddc_op1="<td align=\"center\">"+str(ddc_open3)+"</td>"

if ddc_inprog == 0:
        ddc_inpr1="<td align=\"center\">-</td>"
else:
        ddc_inpr1="<td align=\"center\">"+str(ddc_inprog)+"</td>"
if ddc_inprog2 == 0:
	Bddc_inpr1="<td align=\"center\">-</td>"
else:
	Bddc_inpr1="<td align=\"center\">"+str(ddc_inprog2)+"</td>"
if ddc_inprog3 == 0:
	Cddc_inpr1="<td align=\"center\">-</td>"
else:
	Cddc_inpr1="<td align=\"center\">"+str(ddc_inprog3)+"</td>"

if ddc_hold == 0:
        ddc_ho1="<td align=\"center\">-</td>"
else:
        ddc_ho1="<td align=\"center\">"+str(ddc_hold)+"</td>"
if ddc_hold2 == 0:
	Bddc_ho1="<td align=\"center\">-</td>"
else:
	Bddc_ho1="<td align=\"center\">"+str(ddc_hold2)+"</td>"
if ddc_hold3 == 0:
	Cddc_ho1="<td align=\"center\">-</td>"
else:
	Cddc_ho1="<td align=\"center\">"+str(ddc_hold3)+"</td>"

if ddc_resolve == 0:
        ddc_reso1="<td align=\"center\">-</td>"
else:
        ddc_reso1="<td align=\"center\">"+str(ddc_resolve)+"</td>"
if ddc_resolve2 == 0:
	Bddc_reso1="<td align=\"center\">-</td>"
else:
	Bddc_reso1="<td align=\"center\">"+str(ddc_resolve2)+"</td>"
if ddc_resolve3 == 0:
	Cddc_reso1="<td align=\"center\">-</td>"
else:
	Cddc_reso1="<td align=\"center\">"+str(ddc_resolve3)+"</td>"

################################### PF status main table #############################
if pf_open == 0:
        pf_op1="<td align=\"center\">-</td>"
else:
        pf_op1="<td align=\"center\">"+str(pf_open)+"</td>"
if pf_open2 == 0:
	Bpf_op1="<td align=\"center\">-</td>"
else:
	Bpf_op1="<td align=\"center\">"+str(pf_open2)+"</td>"
if pf_open3 == 0:
	Cpf_op1="<td align=\"center\">-</td>"
else:
	Cpf_op1="<td align=\"center\">"+str(pf_open3)+"</td>"

if pf_inprog == 0:
        pf_inpr1="<td align=\"center\">-</td>"
else:
        pf_inpr1="<td align=\"center\">"+str(pf_inprog)+"</td>"
if pf_inprog2 == 0:
	Bpf_inpr1="<td align=\"center\">-</td>"
else:
	Bpf_inpr1="<td align=\"center\">"+str(pf_inprog2)+"</td>"
if pf_inprog3 == 0:
	Cpf_inpr1="<td align=\"center\">-</td>"
else:
	Cpf_inpr1="<td align=\"center\">"+str(pf_inprog3)+"</td>"

if pf_hold == 0:
        pf_ho1="<td align=\"center\">-</td>"
else:
        pf_ho1="<td align=\"center\">"+str(pf_hold)+"</td>"
if pf_hold2 == 0:
	Bpf_ho1="<td align=\"center\">-</td>"
else:
	Bpf_ho1="<td align=\"center\">"+str(pf_hold2)+"</td>"
if pf_hold3 == 0:
	Cpf_ho1="<td align=\"center\">-</td>"
else:
	Cpf_ho1="<td align=\"center\">"+str(pf_hold3)+"</td>"

if pf_resolve == 0:
        pf_reso1="<td align=\"center\">-</td>"
else:
        pf_reso1="<td align=\"center\">"+str(pf_resolve)+"</td>"
if pf_resolve2 == 0:
	Bpf_reso1="<td align=\"center\">-</td>"
else:
	Bpf_reso1="<td align=\"center\">"+str(pf_resolve2)+"</td>"
if pf_resolve3 == 0:
	Cpf_reso1="<td align=\"center\">-</td>"
else:
	Cpf_reso1="<td align=\"center\">"+str(pf_resolve3)+"</td>"

########################################## TP status main table ##########################
if tp_open == 0:
        tp_op1="<td align=\"center\">-</td>"
else:
        tp_op1="<td align=\"center\">"+str(tp_open)+"</td>"
if tp_open2 == 0:
	Btp_op1="<td align=\"center\">-</td>"
else:
	Btp_op1="<td align=\"center\">"+str(tp_open2)+"</td>"
if tp_open3 == 0:
	Ctp_op1="<td align=\"center\">-</td>"
else:
	Ctp_op1="<td align=\"center\">"+str(tp_open3)+"</td>"

if tp_inprog == 0:
        tp_inpr1="<td align=\"center\">-</td>"
else:
        tp_inpr1="<td align=\"center\">"+str(tp_inprog)+"</td>"
if tp_inprog2 == 0:
	Btp_inpr1="<td align=\"center\">-</td>"
else:
	Btp_inpr1="<td align=\"center\">"+str(tp_inprog2)+"</td>"
if tp_inprog3 == 0:
	Ctp_inpr1="<td align=\"center\">-</td>"
else:
	Ctp_inpr1="<td align=\"center\">"+str(tp_inprog3)+"</td>"

if tp_hold == 0:
        tp_ho1="<td align=\"center\">-</td>"
else:
        tp_ho1="<td align=\"center\">"+str(tp_hold)+"</td>"
if tp_hold2 == 0:
	Btp_ho1="<td align=\"center\">-</td>"
else:
	Btp_ho1="<td align=\"center\">"+str(tp_hold2)+"</td>"
if tp_hold3 == 0:
	Ctp_ho1="<td align=\"center\">-</td>"
else:
	Ctp_ho1="<td align=\"center\">"+str(tp_hold3)+"</td>"

if tp_resolve == 0:
        tp_reso1="<td align=\"center\">-</td>"
else:
        tp_reso1="<td align=\"center\">"+str(tp_resolve)+"</td>"
if tp_resolve2 == 0:
	Btp_reso1="<td align=\"center\">-</td>"
else:
	Btp_reso1="<td align=\"center\">"+str(tp_resolve2)+"</td>"
if tp_resolve3 == 0:
	Ctp_reso1="<td align=\"center\">-</td>"
else:
	Ctp_reso1="<td align=\"center\">"+str(tp_resolve3)+"</td>"

################################## KPI status main table #########################
if kpi_open == 0:
        kpi_op1="<td align=\"center\">-</td>"
else:
        kpi_op1="<td align=\"center\">"+str(kpi_open)+"</td>"
if kpi_open2 == 0:
	Bkpi_op1="<td align=\"center\">-</td>"
else:
	Bkpi_op1="<td align=\"center\">"+str(kpi_open2)+"</td>"
if kpi_open3 == 0:
	Ckpi_op1="<td align=\"center\">-</td>"
else:
	Ckpi_op1="<td align=\"center\">"+str(kpi_open3)+"</td>"

if kpi_inprog == 0:
        kpi_inpr1="<td align=\"center\">-</td>"
else:
        kpi_inpr1="<td align=\"center\">"+str(kpi_inprog)+"</td>"
if kpi_inprog2 == 0:
	Bkpi_inpr1="<td align=\"center\">-</td>"
else:
	Bkpi_inpr1="<td align=\"center\">"+str(kpi_inprog2)+"</td>"
if kpi_inprog3 == 0:
	Ckpi_inpr1="<td align=\"center\">-</td>"
else:
	Ckpi_inpr1="<td align=\"center\">"+str(kpi_inprog3)+"</td>"

if kpi_hold == 0 or kpi_hold2 == 0 or kpi_hold3 == 0:
        kpi_ho1="<td align=\"center\">-</td>"
else:
        kpi_ho1="<td align=\"center\">"+str(kpi_hold)+"</td>"
if kpi_hold2 == 0:
	Bkpi_ho1="<td align=\"center\">-</td>"
else:
	Bkpi_ho1="<td align=\"center\">"+str(kpi_hold2)+"</td>"
if kpi_hold3 == 0:
	Ckpi_ho1="<td align=\"center\">-</td>"
else:
	Ckpi_ho1="<td align=\"center\">"+str(kpi_hold3)+"</td>"

if kpi_resolve == 0:
        kpi_reso1="<td align=\"center\">-</td>"
else:
        kpi_reso1="<td align=\"center\">"+str(kpi_resolve)+"</td>"
if kpi_resolve2 == 0:
	Bkpi_reso1="<td align=\"center\">-</td>"
else:
	Bkpi_reso1="<td align=\"center\">"+str(kpi_resolve2)+"</td>"
if kpi_resolve3 == 0:
	Ckpi_reso1="<td align=\"center\">-</td>"
else:
	Ckpi_reso1="<td align=\"center\">"+str(kpi_resolve3)+"</td>"

############################ Netam status main table ######################
if netan_open == 0:
        netan_op1="<td align=\"center\">-</td>"
else:
        netan_op1="<td align=\"center\">"+str(netan_open)+"</td>"
if netan_open2 == 0:
	Bnetan_op1="<td align=\"center\">-</td>"
else:
	Bnetan_op1="<td align=\"center\">"+str(netan_open2)+"</td>"
if netan_open3 == 0:
	Cnetan_op1="<td align=\"center\">-</td>"
else:
	Cnetan_op1="<td align=\"center\">"+str(netan_open3)+"</td>"

if netan_inprog == 0:
        netan_inpr1="<td align=\"center\">-</td>"
else:
        netan_inpr1="<td align=\"center\">"+str(netan_inprog)+"</td>"
if netan_inprog2 == 0:
	Bnetan_inpr1="<td align=\"center\">-</td>"
else:
	Bnetan_inpr1="<td align=\"center\">"+str(netan_inprog2)+"</td>"
if netan_inprog3 == 0:
	Cnetan_inpr1="<td align=\"center\">-</td>"
else:
	Cnetan_inpr1="<td align=\"center\">"+str(netan_inprog3)+"</td>"

if netan_hold == 0:
        netan_ho1="<td align=\"center\">-</td>"
else:
        netan_ho1="<td align=\"center\">"+str(netan_hold)+"</td>"
if netan_hold2 == 0:
	Bnetan_ho1="<td align=\"center\">-</td>"
else:
	Bnetan_ho1="<td align=\"center\">"+str(netan_hold2)+"</td>"
if netan_hold3 == 0:
	Cnetan_ho1="<td align=\"center\">-</td>"
else:
	Cnetan_ho1="<td align=\"center\">"+str(netan_hold3)+"</td>"

if netan_resolve == 0:
        netan_reso1="<td align=\"center\">-</td>"
else:
        netan_reso1="<td align=\"center\">"+str(netan_resolve)+"</td>"
if netan_resolve2 == 0:
	Bnetan_reso1="<td align=\"center\">-</td>"
else:
	Bnetan_reso1="<td align=\"center\">"+str(netan_resolve2)+"</td>"
if netan_resolve3 == 0:
	Cnetan_reso1="<td align=\"center\">-</td>"
else:
	Cnetan_reso1="<td align=\"center\">"+str(netan_resolve3)+"</td>"

###################################### BO/OCS status main table ###########################
if bo_open == 0:
        bo_op1="<td align=\"center\">-</td>"
else:
        bo_op1="<td align=\"center\">"+str(bo_open)+"</td>"
if bo_open2 == 0:
	Bbo_op1="<td align=\"center\">-</td>"
else:
	Bbo_op1="<td align=\"center\">"+str(bo_open2)+"</td>"
if bo_open3 == 0:
	Cbo_op1="<td align=\"center\">-</td>"
else:
	Cbo_op1="<td align=\"center\">"+str(bo_open3)+"</td>"

if bo_inprog == 0:
        bo_inpr1="<td align=\"center\">-</td>"
else:
        bo_inpr1="<td align=\"center\">"+str(bo_inprog)+"</td>"
if bo_inprog2 == 0:
	Bbo_inpr1="<td align=\"center\">-</td>"
else:
	Bbo_inpr1="<td align=\"center\">"+str(bo_inprog2)+"</td>"
if bo_inprog3 == 0:
	Cbo_inpr1="<td align=\"center\">-</td>"
else:
	Cbo_inpr1="<td align=\"center\">"+str(bo_inprog3)+"</td>"

if bo_hold == 0:
        bo_ho1="<td align=\"center\">-</td>"
else:
        bo_ho1="<td align=\"center\">"+str(bo_hold)+"</td>"
if bo_hold2 == 0:
	Bbo_ho1="<td align=\"center\">-</td>"
else:
	Bbo_ho1="<td align=\"center\">"+str(bo_hold2)+"</td>"
if bo_hold3 == 0:
	Cbo_ho1="<td align=\"center\">-</td>"
else:
	Cbo_ho1="<td align=\"center\">"+str(bo_hold3)+"</td>"

if bo_resolve == 0:
        bo_reso1="<td align=\"center\">-</td>"
else:
        bo_reso1="<td align=\"center\">"+str(bo_resolve)+"</td>"
if bo_resolve2 == 0:
	Bbo_reso1="<td align=\"center\">-</td>"
else:
	Bbo_reso1="<td align=\"center\">"+str(bo_resolve2)+"</td>"
if bo_resolve3 == 0:
	Cbo_reso1="<td align=\"center\">-</td>"
else:
	Cbo_reso1="<td align=\"center\">"+str(bo_resolve3)+"</td>"

############################### Infra status main table ###################
if infra_open == 0:
        infra_op1="<td align=\"center\">-</td>"
else:
        infra_op1="<td align=\"center\">"+str(infra_open)+"</td>"
if infra_open2 == 0:
	Binfra_op1="<td align=\"center\">-</td>"
else:
	Binfra_op1="<td align=\"center\">"+str(infra_open2)+"</td>"
if infra_open3 == 0:
	Cinfra_op1="<td align=\"center\">-</td>"
else:
	Cinfra_op1="<td align=\"center\">"+str(infra_open3)+"</td>"

if infra_inprog == 0:
        infra_inpr1="<td align=\"center\">-</td>"
else:
        infra_inpr1="<td align=\"center\">"+str(infra_inprog)+"</td>"
if infra_inprog2 == 0:
	Binfra_inpr1="<td align=\"center\">-</td>"
else:
	Binfra_inpr1="<td align=\"center\">"+str(infra_inprog2)+"</td>"
if infra_inprog3 == 0:
	Cinfra_inpr1="<td align=\"center\">-</td>"
else:
	Cinfra_inpr1="<td align=\"center\">"+str(infra_inprog3)+"</td>"

if infra_hold == 0:
        infra_ho1="<td align=\"center\">-</td>"
else:
        infra_ho1="<td align=\"center\">"+str(infra_hold)+"</td>"
if infra_hold2 == 0:
	Binfra_ho1="<td align=\"center\">-</td>"
else:
	Binfra_ho1="<td align=\"center\">"+str(infra_hold2)+"</td>"
if infra_hold3 == 0:
	Cinfra_ho1="<td align=\"center\">-</td>"
else:
	Cinfra_ho1="<td align=\"center\">"+str(infra_hold3)+"</td>"

if infra_resolve == 0:
        infra_reso1="<td align=\"center\">-</td>"
else:
        infra_reso1="<td align=\"center\">"+str(infra_resolve)+"</td>"
if infra_resolve2 == 0:
	Binfra_reso1="<td align=\"center\">-</td>"
else:
	Binfra_reso1="<td align=\"center\">"+str(infra_resolve2)+"</td>"
if infra_resolve3 == 0:
	Cinfra_reso1="<td align=\"center\">-</td>"
else:
	Cinfra_reso1="<td align=\"center\">"+str(infra_resolve3)+"</td>"

############################# security status main table ##################
if sec_open == 0:
        sec_op1="<td align=\"center\">-</td>"
else:
        sec_op1="<td align=\"center\">"+str(sec_open)+"</td>"
if sec_open2 == 0:
	Bsec_op1="<td align=\"center\">-</td>"
else:
	Bsec_op1="<td align=\"center\">"+str(sec_open2)+"</td>"
if sec_open3 == 0:
	Csec_op1="<td align=\"center\">-</td>"
else:
	Csec_op1="<td align=\"center\">"+str(sec_open3)+"</td>"

if sec_inprog == 0:
        sec_inpr1="<td align=\"center\">-</td>"
else:
        sec_inpr1="<td align=\"center\">"+str(sec_inprog)+"</td>"
if sec_inprog2 == 0:
	Bsec_inpr1="<td align=\"center\">-</td>"
else:
	Bsec_inpr1="<td align=\"center\">"+str(sec_inprog2)+"</td>"
if sec_inprog3 == 0:
	Csec_inpr1="<td align=\"center\">-</td>"
else:
	Csec_inpr1="<td align=\"center\">"+str(sec_inprog3)+"</td>"

if sec_hold == 0:
        sec_ho1="<td align=\"center\">-</td>"
else:
        sec_ho1="<td align=\"center\">"+str(sec_hold)+"</td>"
if sec_hold2 == 0:
	Bsec_ho1="<td align=\"center\">-</td>"
else:
	Bsec_ho1="<td align=\"center\">"+str(sec_hold2)+"</td>"
if sec_hold3 == 0:
	Csec_ho1="<td align=\"center\">-</td>"
else:
	Csec_ho1="<td align=\"center\">"+str(sec_hold3)+"</td>"

if sec_resolve == 0:
        sec_reso1="<td align=\"center\">-</td>"
else:
        sec_reso1="<td align=\"center\">"+str(sec_resolve)+"</td>"
if sec_resolve2 == 0:
	Bsec_reso1="<td align=\"center\">-</td>"
else:
	Bsec_reso1="<td align=\"center\">"+str(sec_resolve2)+"</td>"
if sec_resolve3 == 0:
	Csec_reso1="<td align=\"center\">-</td>"
else:
	Csec_reso1="<td align=\"center\">"+str(sec_resolve3)+"</td>"

data_uri2 = base64.b64encode(open('/proj/eiffel013_config_fem7s11/eiffel_home/slaves/ComputeFarm1/workspace/Weekly_BUG_Report/eniq3_bugs.png', 'rb').read()).decode('utf-8')
#f.write("<img src='data:image/png;base64,{0}'>".format(data_uri2))
graph1 = "<img width='600' height='300' src='data:image/png;base64,{0}'>".format(data_uri2)

f.write("<table cellspacing=\"26\"><tr align=\"left\"><td><b><font size=\"4\"><u>Overall BUGs Status</u></b></font><br>\n")
f.write("<br><table border=\"2\"><tr style='background-color:#e0ff44;'><b><font style='font-family:arial;'><th rowspan='2'>Team</th><th colspan='3'>BUGs Opened in</th><th rowspan='13'></th><th colspan='3'>BUGs Closed in</th><th rowspan='13'></th><th rowspan='2'>Open BUGs</th><th colspan='4'>Status</th><th rowspan='13'></th><th rowspan='2'>Above Threshold</th><th rowspan='13'>"+graph1+"</th></font></b></tr>\n")

f.write("<tr align=\"center\"><b><font style='font-family:arial;'><td style='background-color:#e0ff44;'>Wk"+str(week_num-2)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num-1)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num-2)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num-1)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num)+"</td><td style='background-color:#e0ff44;'>Open</td><td style='background-color:#e0ff44;'>In-Progress</td><td style='background-color:#e0ff44;'>On-Hold</td><td style='background-color:#e0ff44;'>Resolved</td></font></b></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">NMI</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102827\">"+str(nmi_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102747\">"+str(nmi_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102227\">"+str(nmi_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102828\">"+str(nmi_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102748\">"+str(nmi_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102228\">"+str(nmi_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105059\">"+str(nmi_total_team)+"</a></td>"+nmi_op1+" "+nmi_inpr1+" "+nmi_ho1+" "+nmi_reso1+" "+nmi_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">NMI-SAP</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106411\">"+str(nmisap_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106410\">"+str(nmisap_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106409\">"+str(nmisap_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106414\">"+str(nmisap_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106413\">"+str(nmisap_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106412\">"+str(nmisap_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=106416\">"+str(nmisap_total_team)+"</a></td>"+nmi_sap_op1+" "+nmi_sap_inpr1+" "+nmi_sap_ho1+" "+nmi_sap_reso1+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">DDC/DDP</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102839\">"+str(ddc_ddp_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102762\">"+str(ddc_ddp_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102244\">"+str(ddc_ddp_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102840\">"+str(ddc_ddp_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102763\">"+str(ddc_ddp_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102245\">"+str(ddc_ddp_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105060\">"+str(ddc_ddp_total_team)+"</a></td>"+ddc_op1+" "+ddc_inpr1+" "+ddc_ho1+" "+ddc_reso1+" "+ddc_ddp_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">PF</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102835\">"+str(pf_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102758\">"+str(pf_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102235\">"+str(pf_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102836\">"+str(pf_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102759\">"+str(pf_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102236\">"+str(pf_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105061\">"+str(pf_total_team)+"</a></td>"+pf_op1+" "+pf_inpr1+" "+pf_ho1+" "+pf_reso1+" "+pf_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">TP</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102825\">"+str(TP_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102745\">"+str(TP_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102225\">"+str(TP_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102826\">"+str(TP_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102746\">"+str(TP_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102226\">"+str(TP_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105062\">"+str(tp_total_team)+"</a></td>"+tp_op1+" "+tp_inpr1+" "+tp_ho1+" "+tp_reso1+" "+tp_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">KPI</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107188\">"+str(kpi_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107187\">"+str(kpi_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107186\">"+str(kpi_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107185\">"+str(kpi_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107184\">"+str(kpi_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107183\">"+str(kpi_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=107189\">"+str(kpi_total_team)+"</a></td>"+kpi_op1+" "+kpi_inpr1+" "+kpi_ho1+" "+kpi_reso1+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">NetAn</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102829\">"+str(netan_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102749\">"+str(netan_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102229\">"+str(netan_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102830\">"+str(netan_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102750\">"+str(netan_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102230\">"+str(netan_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105063\">"+str(netan_total_team)+"</a></td>"+netan_op1+" "+netan_inpr1+" "+netan_ho1+" "+netan_reso1+" "+netan_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">BO/OCS</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102831\">"+str(bo_ocs_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102753\">"+str(bo_ocs_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102231\">"+str(bo_ocs_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102832\">"+str(bo_ocs_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102754\">"+str(bo_ocs_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102232\">"+str(bo_ocs_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105064\">"+str(bo_ocs_total_team)+"</a></td>"+bo_op1+" "+bo_inpr1+" "+bo_ho1+" "+bo_reso1+" "+bo_ocs_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">Infra</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102833\">"+str(infra_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102755\">"+str(infra_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102233\">"+str(infra_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102834\">"+str(infra_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102756\">"+str(infra_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102234\">"+str(infra_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105065\">"+str(infra_total_team)+"</a></td>"+infra_op1+" "+infra_inpr1+" "+infra_ho1+" "+infra_reso1+" "+infra_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">Security</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102841\">"+str(sec_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102764\">"+str(sec_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102246\">"+str(sec_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102842\">"+str(sec_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102765\">"+str(sec_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=102247\">"+str(sec_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105066\">"+str(sec_total_team)+"</a></td>"+sec_op1+" "+sec_inpr1+" "+sec_ho1+" "+sec_reso1+" "+sec_threshold+"</font></tr>\n")

f.write("<tr align=\"center\" style='background-color:#fcdfff;'><font color=\"black\" style='font-family:arial;'><td><b>Total Count<b></font></td><td><a><b>"+str(uni_open_last3)+"</b></a></td><td><a><b>"+str(uni_open_last2)+"</b></a></td><td><a><b>"+str(uni_open_last)+"</b></a></td><td><a><b>"+str(uni_closed_last3)+"</b></a></td><td><a><b>"+str(uni_closed_last2)+"</b></a></td><td><a><b>"+str(uni_closed_last)+"</b></a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105058\"><b>"+str(total_uniq)+"</b></a></td><td>"+str(total_open)+"</td><td>"+str(total_inprog)+"</td><td>"+str(total_hold)+"</td><td>"+str(total_resolve)+"</td>"+total_threshold+"</font></tr>\n")

f.write("</table>\n</br></td>\n")

data_uri = base64.b64encode(open('/proj/eiffel013_config_fem7s11/eiffel_home/slaves/ComputeFarm1/workspace/Weekly_BUG_Report/eniq1_bugs.png', 'rb').read()).decode('utf-8')
#f.write("<img src='data:image/png;base64,{0}'>".format(data_uri))
graph2 = "<img width='600' height='300' src='data:image/png;base64,{0}'>".format(data_uri)

f.write("<tr align=\"left\"><td><b><font size=\"4\"><u>22.3 Bugs Status</u></b></font><br>\n")
f.write("<br><table border=\"2\"><tr style='background-color:#e0ff44;'><b><font style='font-family:arial;'><th rowspan='2'>Team</th><th colspan='3'>BUGs Opened in</th><th rowspan='13'></th><th colspan='3'>BUGs Closed in</th><th rowspan='13'></th><th rowspan='2'>Open BUGs</th><th colspan='4'>Status</th><th rowspan='13'></th><th rowspan='2'>Above Threshold</th><th rowspan='13'>"+graph2+"</th></font></b></tr>\n")

f.write("<tr align=\"center\"><b><font style='font-family:arial;'><td style='background-color:#e0ff44;'>Wk"+str(week_num-2)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num-1)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num-2)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num-1)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num)+"</td><td style='background-color:#e0ff44;'>Open</td><td style='background-color:#e0ff44;'>In-Progress</td><td style='background-color:#e0ff44;'>On-Hold</td><td style='background-color:#e0ff44;'>Resolved</td></font></b></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">NMI</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109255\">"+str(Bnmi_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109256\">"+str(Bnmi_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109275\">"+str(Bnmi_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109285\">"+str(Bnmi_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109295\">"+str(Bnmi_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109296\">"+str(Bnmi_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109225\">"+str(Bnmi_total_team)+"</a></td>"+Bnmi_op1+" "+Bnmi_inpr1+" "+Bnmi_ho1+" "+Bnmi_reso1+" "+Bnmi_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">NMI-SAP</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109254\">"+str(Bnmisap_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109257\">"+str(Bnmisap_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109274\">"+str(Bnmisap_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109284\">"+str(Bnmisap_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109294\">"+str(Bnmisap_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109297\">"+str(Bnmisap_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109226\">"+str(Bnmisap_total_team)+"</a></td>"+Bnmi_sap_op1+" "+Bnmi_sap_inpr1+" "+Bnmi_sap_ho1+" "+Bnmi_sap_reso1+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">DDC/DDP</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109253\">"+str(Bddc_ddp_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109258\">"+str(Bddc_ddp_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109273\">"+str(Bddc_ddp_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109283\">"+str(Bddc_ddp_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109293\">"+str(Bddc_ddp_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109298\">"+str(Bddc_ddp_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109227\">"+str(Bddc_ddp_total_team)+"</a></td>"+Bddc_op1+" "+Bddc_inpr1+" "+Bddc_ho1+" "+Bddc_reso1+" "+Bddc_ddp_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">PF</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109252\">"+str(Bpf_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109259\">"+str(Bpf_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109272\">"+str(Bpf_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109282\">"+str(Bpf_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109292\">"+str(Bpf_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109299\">"+str(Bpf_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109228\">"+str(Bpf_total_team)+"</a></td>"+Bpf_op1+" "+Bpf_inpr1+" "+Bpf_ho1+" "+Bpf_reso1+" "+Bpf_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">TP</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109251\">"+str(BTP_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109260\">"+str(BTP_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109271\">"+str(BTP_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109281\">"+str(BTP_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109291\">"+str(BTP_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109300\">"+str(BTP_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109193\">"+str(Btp_total_team)+"</a></td>"+Btp_op1+" "+Btp_inpr1+" "+Btp_ho1+" "+Btp_reso1+" "+Btp_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">KPI</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109250\">"+str(Bkpi_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109261\">"+str(Bkpi_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109270\">"+str(Bkpi_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109280\">"+str(Bkpi_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109290\">"+str(Bkpi_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109301\">"+str(Bkpi_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109192\">"+str(Bkpi_total_team)+"</a></td>"+Bkpi_op1+" "+Bkpi_inpr1+" "+Bkpi_ho1+" "+Bkpi_reso1+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">NetAn</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109249\">"+str(Bnetan_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109262\">"+str(Bnetan_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109269\">"+str(Bnetan_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109279\">"+str(Bnetan_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109289\">"+str(Bnetan_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109302\">"+str(Bnetan_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109229\">"+str(Bnetan_total_team)+"</a></td>"+Bnetan_op1+" "+Bnetan_inpr1+" "+Bnetan_ho1+" "+Bnetan_reso1+" "+Bnetan_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">BO/OCS</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108940\">"+str(Bbo_ocs_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108939\">"+str(Bbo_ocs_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108936\">"+str(Bbo_ocs_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108797\">"+str(Bbo_ocs_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108796\">"+str(Bbo_ocs_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108795\">"+str(Bbo_ocs_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108967\">"+str(Bbo_ocs_total_team)+"</a></td>"+Bbo_op1+" "+Bbo_inpr1+" "+Bbo_ho1+" "+Bbo_reso1+" "+Bbo_ocs_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">Infra</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108848\">"+str(Binfra_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108847\">"+str(Binfra_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108846\">"+str(Binfra_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108804\">"+str(Binfra_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108803\">"+str(Binfra_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108802\">"+str(Binfra_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109190\">"+str(Binfra_total_team)+"</a></td>"+Binfra_op1+" "+Binfra_inpr1+" "+Binfra_ho1+" "+Binfra_reso1+" "+Binfra_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">Security</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108865\">"+str(Bsec_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108864\">"+str(Bsec_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108866\">"+str(Bsec_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108832\">"+str(Bsec_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108831\">"+str(Bsec_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=108830\">"+str(Bsec_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109191\">"+str(Bsec_total_team)+"</a></td>"+Bsec_op1+" "+Bsec_inpr1+" "+Bsec_ho1+" "+Bsec_reso1+" "+Bsec_threshold+"</font></tr>\n")

f.write("<tr align=\"center\" style='background-color:#fcdfff;'><font color=\"black\" style='font-family:arial;'><td><b>Total Count<b></font></td><td><a><b>"+str(Buni_open_last3)+"</b></a></td><td><a><b>"+str(Buni_open_last2)+"</b></a></td><td><a><b>"+str(Buni_open_last)+"</b></a></td><td><a><b>"+str(Buni_closed_last3)+"</b></a></td><td><a><b>"+str(Buni_closed_last2)+"</b></a></td><td><a><b>"+str(Buni_closed_last)+"</b></a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105058\"><b>"+str(Btotal_uniq)+"</b></a></td><td>"+str(Btotal_open)+"</td><td>"+str(Btotal_inprog)+"</td><td>"+str(Btotal_hold)+"</td><td>"+str(Btotal_resolve)+"</td>"+Btotal_threshold+"</font></tr>\n")

f.write("</table>\n</br></td>\n")

data_uri1 = base64.b64encode(open('/proj/eiffel013_config_fem7s11/eiffel_home/slaves/ComputeFarm1/workspace/Weekly_BUG_Report/eniq2_bugs.png', 'rb').read()).decode('utf-8')
#f.write("<img src='data:image/png;base64,{0}'>".format(data_uri1))
graph3 = "<img width='600' height='300' src='data:image/png;base64,{0}'>".format(data_uri1)

f.write("<tr align=\"left\"><td><b><font size=\"4\"><u>22.4 Bugs Status</u></b></font><br>\n")
f.write("<br><table border=\"2\"><tr align=\"center\" style='background-color:#e0ff44;'><b><font style='font-family:arial;'><th rowspan='2'>Team</th><th colspan='3'>BUGs Opened in</th><th rowspan='13'></th><th colspan='3'>BUGs Closed in</th><th rowspan='13'></th><th rowspan='2'>Open BUGs</th><th colspan='4'>Status</th><th rowspan='13'></th><th rowspan='2'>Above Threshold</th><th rowspan='13'>"+graph3+"</th></font></b></tr>\n")

f.write("<tr align=\"center\"><b><font style='font-family:arial;'><td style='background-color:#e0ff44;'>Wk"+str(week_num-2)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num-1)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num-2)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num-1)+"</td><td style='background-color:#e0ff44;'>Wk"+str(week_num)+"</td><td style='background-color:#e0ff44;'>Open</td><td style='background-color:#e0ff44;'>In-Progress</td><td style='background-color:#e0ff44;'>On-Hold</td><td style='background-color:#e0ff44;'>Resolved</td></font></b></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">NMI</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109255\">"+str(Cnmi_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109256\">"+str(Cnmi_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109275\">"+str(Cnmi_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109285\">"+str(Cnmi_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109295\">"+str(Cnmi_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109296\">"+str(Cnmi_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109225\">"+str(Cnmi_total_team)+"</a></td>"+Cnmi_op1+" "+Cnmi_inpr1+" "+Cnmi_ho1+" "+Cnmi_reso1+" "+Cnmi_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">NMI-SAP</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109254\">"+str(Cnmisap_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109257\">"+str(Cnmisap_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109274\">"+str(Cnmisap_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109284\">"+str(Cnmisap_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109294\">"+str(Cnmisap_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109297\">"+str(Cnmisap_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109226\">"+str(Cnmisap_total_team)+"</a></td>"+Cnmi_sap_op1+" "+Cnmi_sap_inpr1+" "+Cnmi_sap_ho1+" "+Cnmi_sap_reso1+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">DDC/DDP</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109253\">"+str(Cddc_ddp_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109258\">"+str(Cddc_ddp_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109273\">"+str(Cddc_ddp_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109283\">"+str(Cddc_ddp_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109293\">"+str(Cddc_ddp_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109298\">"+str(Cddc_ddp_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109227\">"+str(Cddc_ddp_total_team)+"</a></td>"+Cddc_op1+" "+Cddc_inpr1+" "+Cddc_ho1+" "+Cddc_reso1+" "+Cddc_ddp_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">PF</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109252\">"+str(Cpf_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109259\">"+str(Cpf_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109272\">"+str(Cpf_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109282\">"+str(Cpf_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109292\">"+str(Cpf_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109299\">"+str(Cpf_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109228\">"+str(Cpf_total_team)+"</a></td>"+Cpf_op1+" "+Cpf_inpr1+" "+Cpf_ho1+" "+Cpf_reso1+" "+Cpf_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">TP</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109251\">"+str(CTP_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109260\">"+str(CTP_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109271\">"+str(CTP_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109281\">"+str(CTP_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109291\">"+str(CTP_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109300\">"+str(CTP_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109193\">"+str(Ctp_total_team)+"</a></td>"+Ctp_op1+" "+Ctp_inpr1+" "+Ctp_ho1+" "+Ctp_reso1+" "+Ctp_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">KPI</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109250\">"+str(Ckpi_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109261\">"+str(Ckpi_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109270\">"+str(Ckpi_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109280\">"+str(Ckpi_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109290\">"+str(Ckpi_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109301\">"+str(Ckpi_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109192\">"+str(Ckpi_total_team)+"</a></td>"+Ckpi_op1+" "+Ckpi_inpr1+" "+Ckpi_ho1+" "+Ckpi_reso1+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">NetAn</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109249\">"+str(Cnetan_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109262\">"+str(Cnetan_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109269\">"+str(Cnetan_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109279\">"+str(Cnetan_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109289\">"+str(Cnetan_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109302\">"+str(Cnetan_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109229\">"+str(Cnetan_total_team)+"</a></td>"+Cnetan_op1+" "+Cnetan_inpr1+" "+Cnetan_ho1+" "+Cnetan_reso1+" "+Cnetan_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">BO/OCS</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109246\">"+str(Cbo_ocs_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109263\">"+str(Cbo_ocs_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109268\">"+str(Cbo_ocs_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109278\">"+str(Cbo_ocs_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109288\">"+str(Cbo_ocs_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109303\">"+str(Cbo_ocs_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109231\">"+str(Cbo_ocs_total_team)+"</a></td>"+Cbo_op1+" "+Cbo_inpr1+" "+Cbo_ho1+" "+Cbo_reso1+" "+Cbo_ocs_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">Infra</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109248\">"+str(Cinfra_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109264\">"+str(Cinfra_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109267\">"+str(Cinfra_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109277\">"+str(Cinfra_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109287\">"+str(Cinfra_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109304\">"+str(Cinfra_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109195\">"+str(Cinfra_total_team)+"</a></td>"+Cinfra_op1+" "+Cinfra_inpr1+" "+Cinfra_ho1+" "+Cinfra_reso1+" "+Cinfra_threshold+"</font></tr>\n")

f.write("<tr align=\"center\"><font style='font-family:arial;'><td style='background-color:#93c1f6;' align=\"left\">Security</td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109247\">"+str(Csec_open_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109265\">"+str(Csec_open_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109266\">"+str(Csec_open_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109276\">"+str(Csec_closed_jiras3)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109286\">"+str(Csec_closed_jiras2)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109305\">"+str(Csec_closed_jiras)+"</a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=109194\">"+str(Csec_total_team)+"</a></td>"+Csec_op1+" "+Csec_inpr1+" "+Csec_ho1+" "+Csec_reso1+" "+Csec_threshold+"</font></tr>\n")

f.write("<tr align=\"center\" style='background-color:#fcdfff;'><font color=\"black\" style='font-family:arial;'><td><b>Total Count<b></font></td><td><a><b>"+str(Cuni_open_last3)+"</b></a></td><td><a><b>"+str(Cuni_open_last2)+"</b></a></td><td><a><b>"+str(Cuni_open_last)+"</b></a></td><td><a><b>"+str(Cuni_closed_last3)+"</b></a></td><td><a><b>"+str(Cuni_closed_last2)+"</b></a></td><td><a><b>"+str(Cuni_closed_last)+"</b></a></td><td><a href=\"https://jira-oss.seli.wh.rnd.internal.ericsson.com/issues/?filter=105058\"><b>"+str(Ctotal_uniq)+"</b></a></td><td>"+str(Ctotal_open)+"</td><td>"+str(Ctotal_inprog)+"</td><td>"+str(Ctotal_hold)+"</td><td>"+str(Ctotal_resolve)+"</td>"+Ctotal_threshold+"</font></tr>\n")

f.write("</table>\n</br></td>\n")

#f.write("<td><b><font size=\"4\"><u>MRs F Status</u></b></font>\n")

MR_Data = base64.b64encode(open('/proj/eiffel013_config_fem7s11/eiffel_home/slaves/ComputeFarm1/workspace/Weekly_BUG_Report/MR1.png', 'rb').read()).decode('utf-8')
MR_Data2 = base64.b64encode(open('/proj/eiffel013_config_fem7s11/eiffel_home/slaves/ComputeFarm1/workspace/Weekly_BUG_Report/MR2.png', 'rb').read()).decode('utf-8')
f.write("<br><table><tr align=\"left\"><td><img src='data:image/png;base64,{0}'/ width='700' height='400'>".format(MR_Data))
f.write("<td><img src='data:image/png;base64,{0}'/ width='700' height='400'>".format(MR_Data2))
f.write("</td></tr></table>")

f.write("<br><br><br><b>Thanks & Regards,</b>")
f.write("<br><b>Eniq Stats DM CI Team</b>")

f.write("</body></html>")
f.close()


