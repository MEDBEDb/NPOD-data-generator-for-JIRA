#!/usr/bin/python
# coding=UTF-8

import argparse
import json
import string
import subprocess, shlex
import sys
import time
import random
from random_words import RandomWords

### Usage: 
# pip2.7 install random_words
# python2.7 npod.py -j https://jira_url/ -e YWRtaW46YWRtaW4= -p 1 -i 7 -f 7
# Note: YWRtaW46YWRtaW4= is admin:admin

parser=argparse.ArgumentParser()
parser = argparse.ArgumentParser(description="NPOD - Nimble Propagator of Data for JIRA is a little python script to help generate JIRA projects, issues and filters... To run the script simply enter: python2.7 npod.py -j https://jira_url/ -e YWRtaW46YWRtaW4= -p 1 -i 7 -f 7 (where p, i, f - is number of issues, projects and filters, needed to be generated).")

parser.add_argument("-j", "--jira", action="store", dest="jira", 
					default=False, help="JIRA instance URL")
parser.add_argument("-e", "--encoded_credentials",
                    type = str, dest="encoded_credentials", default=True,
                    help="Your JIRA instance username and password user:pass encoded into base64")
parser.add_argument("-p", "--projects",
                    type = int, dest="projects", default=True,
                    help="Number of pojects to be generated")
parser.add_argument("-i", "--issues",
                    type = int, dest="issues", default=True,
                    help="Number of issues to be generated")
parser.add_argument("-f", "--filters",
                    type = int, dest="filters", default=True,
                    help="Number of filters to be generated")
args = parser.parse_args()



if args.jira in sys.argv:
 	jira_url = sys.argv[2]
else:
 	jira_url = 'http://localhost:8090/jira'

print("Your JIRA URL is: " +  jira_url)
print("Number of projects to be generated: " + str(args.projects))
print("Number of issues to be generated: " + str(args.issues))
print("Number of filters to be generated: " + str(args.filters))

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
args=parser.parse_args()


langs = ["provë", "písemná", "prøve", "δοκιμή", "próf", "scrúdú", "pārbaude",
"контрольная", "פּרובירן", "փորձարկում", "sınaq", "পরীক্ষা", "测试", "測試",
"ტესტი", "ટેસ્ટ", "कसौटी", "xeem", "テスト", "ಟೆಸ್ಟ್", "сынақ", "ការ​ធ្វើ​តេ​ស្ត",
"테스트", "ການທົດ​ສອບ", "ടെസ്റ്റ്", "चाचणी", "စမ်းသပ်မှု", "परीक्षण", "ටෙස්ට්",
"озмоиш", "சோதனை", "పరీక్ష", "ทดสอบ", "ٹیسٹ", "sinov", "thử",
"اختبار", "מבחן", "تست", "tès"]

#auth_curl = 'curl -u ' + str(args.user) + ':' + str(args.password) + ' -H "Content-Type: application/json" -H "ATL-CloudId: default"'
auth_curl = 'curl -D- -X GET -H "Authorization: Basic "' + str(args.encoded_credentials) + " " + '-H "Content-Type: application/json" -H "ATL-CloudId: default"'


jql = "type = Task and resolution is empty"
filter_favourited = "true"

rw = RandomWords()
project = str(rw.random_words(count=3)).replace("u'", "").replace("u'", "").replace("'", "").replace("[", "").replace("]", "").replace(",", "").capitalize()

first = project[0][0].capitalize()
second = project[1][0].capitalize()
last = project[2][0].capitalize()
project_key = first + second + last

with open('data/project_key.txt', 'w') as the_file:
    the_file.write(project_key)

### Generate a project
for i in xrange(int(args.projects)):

	unix_timestamp = time.time()
	project = { "key": project_key,
	"name": project,
	"projectTypeKey": "software",
	"projectTemplateKey": "com.pyxis.greenhopper.jira:basic-software-development-template",
	"description": "Example Project description",
	"lead": "admin",
	"url": "http://atlassian.com",
	"assigneeType": "PROJECT_LEAD",
	"avatarId": 10200 }
	with open('data/project.json', 'w') as outfile:
		json.dump(project, outfile, sort_keys=True, indent=4, separators=(',', ':'))
	generate_project = auth_curl + ' -X POST --data @data/project.json ' + jira_url + '/rest/api/2/project'
	call_params_project = shlex.split(generate_project)
	print call_params_project
	subprocess.call(call_params_project)

### Generate issues
## Generate random English words for summary and description
project_key_from_file = lines = open('data/project_key.txt').read()
for i in xrange(args.issues):
	rw = RandomWords()
	summary = rw.random_words(count=7)
	description = rw.random_words(count=150)
	issue ={"fields": { 
	 "project": { "key": project_key_from_file }, 
	 "summary": str(summary).replace("u'", "").replace("u'", "").replace("'", "").replace("[", "").replace("]", "").replace(",", "").capitalize(),
	 "description": str(description).replace("u'", "").replace("u'", "").replace("'", "").replace("[", "").replace("]", "").replace(",", "").capitalize(),
	 "issuetype": { "name": "Bug" } } } 
	with open('data/issue.json', 'w') as outfile:
		json.dump(issue, outfile, sort_keys=True, indent=4, separators=(',', ':'))
	generate_issues =  auth_curl + ' -X POST --data @data/issue.json ' + jira_url + '/rest/api/2/issue'
 	call_params_issues = shlex.split(generate_issues)
 	print call_params_issues
 	subprocess.call(call_params_issues)

### Generate filters
for i in xrange(args.filters):
	unix_timestamp = time.time()
	filter = {"name": str(i + 1) + " " + random.choice(langs) + " " + str(unix_timestamp) + " " + random.choice(langs),
	 "description": str(i + 1) + " " + random.choice(langs) + " description " + random.choice(langs), 
	 "jql": jql, 
	 "favourite": filter_favourited }
	with open('data/filter.json', 'w') as outfile:
		json.dump(filter, outfile, sort_keys=True, indent=4, separators=(',', ':'))
	generate_filters = auth_curl + ' -X POST --data @data/filter.json ' + jira_url + '/rest/api/2/filter'
	call_params_filters = shlex.split(generate_filters)
	print call_params_filters
	subprocess.call(call_params_filters)
