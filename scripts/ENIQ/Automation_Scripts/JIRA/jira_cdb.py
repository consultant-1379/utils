from jira import JIRA, JIRAError
import getpass
#get JIRA credentials
import sys

# Check if the user provided an argument
if len(sys.argv) < 9:
    print("Please provide an argument")
    print(" Job_name Build_Url Project Issue_type Fix_Version Components drop_version Eniq_Area")
    sys.exit(1)
else:
	# Retrieve the argument and store it in a variable
	job_name = sys.argv[1]
	print("Job name", job_name)
	build_url = sys.argv[2]
	print("build url is ", build_url)
	proj = sys.argv[3]
	print("Project is: ", proj)
	issue_type = sys.argv[4]
	print(" Issue type is: ", issue_type)
	fix = sys.argv[5]
	print("Fix Version is: ", fix)
	component = sys.argv[6]
	print(" Component is: ", component)
	drop = sys.argv[7]
	print("drop version is: ", drop)
	area = sys.argv[8]
	print(" ENIQ_Area is: ", area)
	


""" 
#For Interactive inputs
username = raw_input("Enter the zid :")
passwd = getpass.getpass("Enter the password")
"""

username = 'esjkadm100'
passwd = 'Naples!0512'


# Set up Jira API credentials
options = {
    'server': 'https://jira-oss.seli.wh.rnd.internal.ericsson.com'
}
#jira = JIRA(options, basic_auth=('username', 'api_token'))

#test connection
try:
    jira = JIRA(options=options, basic_auth=(username, passwd))
except JIRAError as e:
    if e.status_code == 401:
        print("Login to JIRA failed. Check your username and password")

#
#
print("Login Successfull...!!!")

# Define issue fields

new_issue = {
    'project': {'key': proj},
    'summary': job_name+' Test case failure ',
    'description': job_name+' Test cases have failed, Please check the build url: '+build_url+' for more details. Please do not close the Jira without resolving the issue.',
    'environment': 'CDB',
    'issuetype': {'name': issue_type},
    'components': [{'name': component}],
    'fixVersions':[{'name': fix}],
    'customfield_14801': {'value': drop},
    'customfield_24700': [{'value': area}],
    'labels': ["ci_pipeline_cdb" ]  	# label depends on the pipeline where jira is being raised.being used.
    
	
}

print(new_issue)


# Create issue
issue = jira.create_issue(fields=new_issue)

# Print issue key
#print(f'Created issue {issue.key}')
print('Created issue {0}'.format(issue.key))
#print('Issue url: {0}'.format(issue.self))

#issue_url = f"{server}/browse/{issue_key}"

print('Issue url: https://jira-oss.seli.wh.rnd.internal.ericsson.com/browse/{0}'.format(issue.key))
