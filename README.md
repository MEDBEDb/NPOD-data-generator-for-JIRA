NPOD - Nimble Propagator of Data for JIRA

NPOD - Nimble Propagator of Data for JIRA is a little python script to help generate JIRA projects, issues and filters... To run the script simply enter: python2.7 npod.py -j https://jira_url/ -e YWRtaW46YWRtaW4= -p 1 -i 7 -f 7 (where p, i, f - is number of issues, projects and filters, needed to be generated).
HOW TO
Requirements

    Administrator account for JIRA instance should be admin:admin
    pip2.7 install random_words

Usage examples
Generate 1 project, 5 issues and 3 filters on the default dev JIRA instance

python2.7 npod.py -j https://jira_url/ -e YWRtaW46YWRtaW4= -p 1 -i 5 -f 3
# Note: YWRtaW46YWRtaW4= is admin:admin

Generate 1 project, 1337 issues and 0 filters on the custom dev/cloud JIRA instance

python2.7 npod.py -j https://jira_url/ -e YWRtaW46YWRtaW4= -p 1 -i 1337 -f 0

For help run "python npod.py -h" or "python npod.py --help"
