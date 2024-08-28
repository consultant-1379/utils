from jira import JIRA
from datetime import datetime

#jira = JIRA(auth=('esjkadm100', 'Naples!0512'), options={'server': 'https://jira-oss.seli.wh.rnd.internal.ericsson.com/'})
#jira = JIRA(auth=('esjkadm100', 'Naples!0512'), options={'server': 'https://eteamproject.internal.ericsson.com'})
jira = JIRA(auth=('esjkadm100', 'Naples!0512'), options={'server': 'https://eteamproject.internal.ericsson.com/'})
output_list = []  # Use a list to store information about all issues

# Perform the Jira search
issues = jira.search_issues('project = EQEV AND issuetype = MR AND status not in (Closed,Cancelled, "MR Cancelled") AND "MR Status"="In Refinement"', startAt=0, maxResults=100)
##issues = jira.search_issues('project = EQEV AND issuetype = MR AND status not in (Closed, "MR Cancelled") AND labels = ENIQ-ReadyForRefinement', startAt=0, maxResults=100)
#issues = jira.search_issues('project = "Continuous Integration Services" AND assignee = zhshees AND status = "In Progress"', startAt=0, maxResults=100)
total_issues = len(issues)  # to get the length of ResultList as per the filter

# Generate HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body style="font-family: Arial, sans-serif;">
    <h1></h1>
"""

if total_issues > 0:
    print(f"Total Number of Issues: {total_issues}")

    # Iterate over the retrieved issues
    for result in issues:
        issue = jira.issue(result.key)

        print(f"Processing Issue: {issue.key}")

        # Check if there are any comments before processing
        if issue.fields.comment.total > 0:
            # Get the last comment
            last_comment = issue.fields.comment.comments[-1]

            # Create dictionary for the issue and its last comment
            issue_data = {
                'Key': f'<a href="https://jira-oss.seli.wh.rnd.internal.ericsson.com/browse/{issue.key}">{issue.key}</a>',
                'Summary': issue.fields.summary,
                'Issue Type': issue.fields.issuetype.name,
                'Assignee': issue.fields.assignee.displayName if issue.fields.assignee else "Unassigned",
                'status': issue.fields.status,
                'Comment': last_comment.body
            }

            output_list.append(issue_data)
        else:
            # If there are no comments, create a dictionary with empty comment fields and display as None
            issue_data = {
                'Key': f'<a href="https://jira-oss.seli.wh.rnd.internal.ericsson.com/browse/{issue.key}">{issue.key}</a>',
                'Summary': issue.fields.summary,
                'Issue Type': issue.fields.issuetype.name,
                'Assignee': issue.fields.assignee.displayName if issue.fields.assignee else "Unassigned",
                'status': issue.fields.status,
                'Comment': None
            }

            output_list.append(issue_data)

    html_content += """
    <p>Hi All,<br><br>Please find below the list of MR for refinement : <br><br></p>
    <table style="border-collapse: collapse; border: 1px solid #000; width: 100%;">
        <tr>
            <th style="border: 1px solid #000;" bgcolor="DodgerBlue">Issue Type</th>
            <th style="border: 1px solid #000;" bgcolor="DodgerBlue">Key</th>
            <th style="border: 1px solid #000;" bgcolor="DodgerBlue">Summary</th>
            <th style="border: 1px solid #000;" bgcolor="DodgerBlue">status</th>
            <th style="border: 1px solid #000;" bgcolor="DodgerBlue">Assignee</th>
            <th style="border: 1px solid #000;" bgcolor="DodgerBlue">Last Comment</th>
        </tr>
    """

    for output in output_list:
        html_content += f"""
        <tr>
            <td style="border: 1px solid #000;">{output['Issue Type']}</td>
            <td style="border: 1px solid #000;">{output['Key']}</td>
            <td style="border: 1px solid #000;">{output['Summary']}</td>
            <td style="border: 1px solid #000;">{output['status']}</td>
            <td style="border: 1px solid #000;">{output['Assignee']}</td>
            <td style="border: 1px solid #000;">{output['Comment']}</td>
        </tr>
        """

    html_content += """
    </table>
    <p><br>Regards,<br>Technical Management Scope Team<br>ENIQ_S</p>
"""

else:
    print("Hi All,\nNo MR for discussion this Week.")
    html_content += "<p>Hi All,<br><br>No MR for discussion this Week.<br><br>Regards,<br>Technical Management Scope Team<br>ENIQ_S</p>"

html_content += """
    </body>
</html>
"""

# Write HTML content to a file
file_name = f"/home/esjkadm100/zhshees/Assure_Jira_Report.html"
with open(file_name, 'w') as html_file:
    html_file.write(html_content)

print(f"HTML report saved to {file_name}")

