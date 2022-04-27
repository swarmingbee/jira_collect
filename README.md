# jira_collect

This project will help you to collect Jira information via API.

You can download the binary version in the Releases area (right side). In this case, no virtual environment or additional steps will be necessary.

About the use, please, proceed as below

 - Download the Jira API key from [here](https://issues.redhat.com/secure/ViewProfile.jspa)
 - Download the latest version of the binary [here](https://github.com/waldirio/jira_collect/releases/latest)
 - Execute the command `./jira_collect.py setup set-token` and inform your `token` when requested

 At this moment, you will be good to go and run the app.

 ```
 $ ./jira_collect
 ```
 and it will result in an output as below
 ```
$ ./jira_collect
Usage: jira_collect.py [OPTIONS] COMMAND [ARGS]...

  Main app to check/export the JIRA information

Options:
  --help  Show this message and exit.

Commands:
  export        Export a JIRA project information
  list-project  List all the projects available in JIRA
  setup         Setup and/or show the basic configuration
 ```

The first step is `list-project`. This option will bring back the whole products available on Jira.
```
$ ./jira_collect.py list-project
project_id      - Project Description
AA              - Automation Analytics
AAH             - Automation Hub
AAJIT           - Agile and Jira Integration Templates
AAP             - Ansible Automation Platform
...
YUPANA          - Yupana
ZANATA          - Zanata
ZIPOC           - Forge: FUSE ZI POC
ZUUL            - Zuul
```
Keep in mind that you can copy/paste the `project_id` from the above list, after that, the next step will be to export the data.

From now, let's run the command `./jira_collect.py export by-project` which will ask you the project name that you would like to export.
```
$ ./jira_collect.py export by-project
export by project
Please, type the name of the project that you would like to export the infos (e.g. SAT):
```
Note. Type the name as you saw in the previous list. Here as example, let's check the `YUPANA` project.

```
$ ./jira_collect.py export by-project
export by project
Please, type the name of the project that you would like to export the infos (e.g. SAT): YUPANA
Num of records: 103
Saving the file '/tmp/YUPANA.csv'
```

As we can see above, the project has 103 issues and it was exported to `/tmp/YUPANA.csv`

Now, let's check the content of the file
```
$ cat /tmp/YUPANA.csv
jira_key,project_name,status,summary,resolution,resolution_name,created,resolutiondate,priority,reporter,assignee,type,sub_task,customer_cases
YUPANA-104,YUPANA,New,[tracker] YUPANA (Subscriptions) EBS to orgid,,,2022-04-27T11:47:59.000+0000,,Normal,Kavita Gaikwad,,Story,False,0
YUPANA-103,YUPANA,New,Emit event notification on host rejection,,,2022-04-26T18:52:17.000+0000,,Normal,Kavita Gaikwad,,Task,False,0
YUPANA-102,YUPANA,New,run_delegate test case failing,,,2022-04-22T19:50:50.000+0000,,Major,Suraj Patil,Suraj Patil,Bug,False,0
...
```
After that, you can import this data in your best SpreadSheet and play with it.


If you would like to play with the code and/or contribute, I really recommend you to prepare a virtual environment, install all the python modules according to the `requirement.txt` file and then voilá, you will be able to run it.


I really hope you enjoy it.

Waldirio
