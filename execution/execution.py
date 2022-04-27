"""
Module responsible for collect the whole information and process it.
"""

import sys
import requests
from report import report
from config import config

# Reading the token information
TOKEN = config.read_token()


def query_url(url):
    """
    Def responsible for check if the customer is using the token and
    also responsible for all the queries on the Jira API endpoint
    """

    # Checking the current user info, just to guarantee that the token is
    # still valid
    url_user = "https://issues.redhat.com/rest/api/2/myself"
    req_user = requests.get(url_user, headers={"Authorization": "Bearer {}".format(TOKEN)})

    if (TOKEN is None) or (req_user.status_code != 200):
        print("TOKEN not set. Please, do it.")
        print("Access https://issues.redhat.com/secure/ViewProfile.jspa, click on")
        print("'Personal Access Tokens' and then 'Create token'. Use it to set the token")
        print("in this tool.")
        sys.exit(1)
    req = requests.get(url, headers={"Authorization": "Bearer {}".format(TOKEN)})
    return req.json()


def list_all_projects():
    """
    Def responsible for list all the projects available in jira
    """

    stage_lst = []
    url = "https://issues.redhat.com/rest/api/2/project/"
    response = query_url(url)
    print("project_id      - Project Description")
    for project in response:
        aux = project['key'] + "," + project['name']
        stage_lst.append(aux)

    stage_lst.sort()

    for element in stage_lst:
        key = element.split(",")[0]
        desc = element.split(",")[1]
        print("{:15} - {}".format(key, desc))


def export_by_project():
    """
    Def responsible for export the project
    """

    print("export by project")
    project_name = input("Please, type the name of the project that you would like to export the infos (e.g. SAT): ")

    if project_name is "":
        print("Project name it's mandatory")
        sys.exit()

    url = "https://issues.redhat.com/rest/api/2/search?jql=project=" + project_name

    num_of_entries = query_url(url)['total']
    print("Num of records: {}".format(num_of_entries))

    # load_data,bz_id,product,component,status,resolution,summary,version,keywords,creator,severity,create_time,close_time,customer_case_attached

    stage_lst = []
    final_lst = []

    final_lst.append([
                    "jira_key",
                    "project_name",
                    "status",
                    "summary",
                    "resolution",
                    "resolution_name",
                    "created",
                    "resolutiondate",
                    "priority",
                    "reporter",
                    "assignee",
                    "type",
                    "sub_task",
                    "customer_cases"
                ])

    for items_per_page in range(0, num_of_entries, 50):
        url = "https://issues.redhat.com/rest/api/2/search?jql=project=" + project_name + "&startAt=" + str(items_per_page)
        response = query_url(url)

        for element in response['issues']:
            jira_key = element['key']

            project_name = element['fields']['project']['key']
            # component = element['']
            status = element['fields']['status']['name']
            # resolution = check_value(element, {"key": "['fields']['resolution']['description']"})
            # resolution_name = check_value(element, {"key":"['fields']['resolution']['name']"})

            summary = element['fields']['summary'].rstrip().replace("\t", " ")

            try:
                resolution = element['fields']['resolution']['description'].rstrip().replace("\t", " ")
                # resolution = element['fields']['resolution']
            except:
                resolution = None

            try:
                resolution_name = element['fields']['resolution']['name'].rstrip().replace("\t", " ")
            except:
                resolution_name = None

            # resolution = element['fields']['resolution']
            # resolution_name = element['fields']['resolution']

            # version = element['']
            # keywords = element['']
            # creator = element['']
            # severity = element['']
            created = element['fields']['created']
            resolutiondate = element['fields']['resolutiondate']

            try:
                priority = element['fields']['priority']['name']
            except:
                priority = None                # customer_case_attached = element['']

            reporter = element['fields']['creator']['displayName']

            try:
                assignee = element['fields']['assignee']['displayName']
            except:
                assignee = None

            type = element['fields']['issuetype']['name']
            sub_task = element['fields']['issuetype']['subtask']

            customer_cases = len(element['fields']['customfield_12313441'].split())

            stage_lst.append(jira_key)
            stage_lst.append(project_name)
            stage_lst.append(status)
            stage_lst.append(summary)
            stage_lst.append(resolution)
            stage_lst.append(resolution_name)
            stage_lst.append(created)
            stage_lst.append(resolutiondate)
            stage_lst.append(priority)
            stage_lst.append(reporter)
            stage_lst.append(assignee)
            stage_lst.append(type)
            stage_lst.append(sub_task)
            stage_lst.append(customer_cases)

            final_lst.append(stage_lst)
            stage_lst = []

    report.project_export(final_lst, project_name)
