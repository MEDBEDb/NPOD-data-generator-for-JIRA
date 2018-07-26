NPOD - Nimble Propagator of Data for JIRA

NPOD is a little python script to help generate filters in JIRA... To run the script simply enter: python npod.py n (where n - is number of issues and filters needed to be generated), it will also create 1 project by default for you. Optionally, if you have a custom jira intsance running in cloud - you could specify it as an optional param -jira yourinstance.yourdomain.com, only thing to make sure - the auth should be admin:admin for that instance. If -jira param is not specified, the script will call a default instance on http://localhost:8090/jira/"
HOW TO
Requirements

    Administrator account for JIRA instance should be admin:admin

Usage examples
Generate 1 project, 5 issues and 5 filters on the default dev JIRA instance

python npod.py 5 # defaults to http://localhost:8090/jira

Generate 1 project, 1337 issues and 1337 filters on the custom dev/cloud JIRA instance

python npod.py 1337 -jira https://yourinstance.jira-dev.com

For help run "python npod.py -h" or "python npod.py --help"
In order to generate multiple projects, comment out issues and filters methods (optionally) and modify line 40:

number_of_projects = N, where N is the number of project needed (currently it's hardcoded to 1)
