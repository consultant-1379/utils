from jira import JIRA, JIRAError
import getpass
#get JIRA credentials
import sys

# Check if the user provided an argument
if len(sys.argv) < 3:
    print("Please provide an argument")
else:
	# Retrieve the argument and store it in a variable
	job_name = sys.argv[1]
	print("Job name", job_name)
	build_url = sys.argv[2]
	print("build url is ", build_url)
	



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
    'project': {'key': 'CIS'},
    'summary': job_name+' Test case failure ',
    'description': job_name+' Test cases have failed, Please check the build url: '+build_url+'for more details',
    'issuetype': {'name': 'Spike'},
    'customfield_15706': 'DM/CI',
    'components': [{'name': 'CDB/Main Track'}],
    'customfield_16801': {'value':'ENIQ Stats'},
    'customfield_16800':{'value': 'India/Wipro'}
}

print(new_issue)


# Create issue
issue = jira.create_issue(fields=new_issue)

# Print issue key
#print(f'Created issue {issue.key}')
print('Created issue {0}'.format(issue.key))