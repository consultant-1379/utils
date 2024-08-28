from jira import JIRA

jiraReport = open("/proj/eiffel004_config_fem167/slaves/RHEL_ENIQ_STATS/JIRA/jira_week.txt", 'w')
jira = JIRA(basic_auth=('statsjenki',"Nov#2021"), options={'server':'http://jira-oss.seli.wh.rnd.internal.ericsson.com'})
jira_raised = jira.search_issues('created >= -7d AND reporter in (zsampri,zpunvai,zpthvsh,zhshees,zbhopxx,zahgusn)')
jiraReport.write('Jiras raised in this week :   ')
if not jira_raised:
    jiraReport.write(" - ")
else:
    for issue in jira_raised:
        jiraReport.write(issue.key+"    ")
jiraReport.write('\nJiras open : ')
jira_opened = jira.search_issues('created >= -7d AND reporter in (zsampri,zpunvai,zpthvsh,zhshees,zbhopxx,zahgusn) and resolution = Unresolved')
if not jira_opened:
    jiraReport.write("  -  ")
else:
    for issue in jira_opened:
        jiraReport.write(issue.key+"    ")
jira_closed = jira.search_issues('created >= -7d AND reporter in (zsampri,zpunvai,zpthvsh,zhshees,zbhopxx,zahgusn) and status in (Closed,Resolved)')
jiraReport.write("\nJiras closed : ")
if not jira_closed:
    jiraReport.write("  -  ")
else:
    for issue in jira_closed:
        jiraReport.write(issue.key+"    ")

