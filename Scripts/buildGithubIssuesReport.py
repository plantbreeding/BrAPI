#! /usr/bin/env python

## Usage
## py buildGithubIssuesReport.py project_query_string [open_query_string]

import requests
import sys
from jsonschema._utils import indent
    
def go():
    project = ""
    isOpen = "closed"
    
    if len(sys.argv) > 2 :
        project = sys.argv[1]
        isOpen = sys.argv[2]
    elif len(sys.argv) > 1 :
        project = sys.argv[1]
    else:
        print('Usage:\n > py buildGithubIssuesReport.py project_query_string [open_query_string]')
        exit(1)
        
    issues = getIssues(project, isOpen)
    reportText = generateReport(issues)
    print(reportText)
    
def getIssues(project, isOpen):
    issues = []
    testURL = "https://api.github.com/search/issues?per_page=100&q=is:issue%20is:" + isOpen + "%20project:" + project
    response = requests.get(testURL)
    rawIssues = response.json()
    for rawIssue in rawIssues["items"]:
        newIssue = {
            "url": rawIssue["html_url"],
            "title": rawIssue["title"],
            "user": rawIssue["user"]["login"],
            "state":  rawIssue["state"],
            "body":  rawIssue["body"].replace("\n", "").replace("\r", "\n").replace("\t", "    ").replace("\"", "'").replace("-", " ").replace("\n\n", "\n"),
            "number":  str(rawIssue["number"]),
            }
        issues.append(newIssue)
    return issues

def generateReport(issues):
    sep = "\"\t\""
    newLine = "\" \n"
    indent = "\"" + sep + sep + sep + sep
    report = "\"Issue Number" + sep + "Status" + sep + "Author" + sep + "Title/URL" + sep + "Description"  + newLine
    for issue in issues:
        bodyText = issue["body"]
        if len(bodyText) > 600:
            bodyText = bodyText[0:600] + "... (continued)"
        bodyText = bodyText.replace("\n", "\"\n" + indent)
        
        report = report + "\"Issue #" + issue["number"] + sep + issue["state"] + sep + issue["user"] + sep + issue["title"] + newLine
        report = report + "\"" + sep + sep + sep + issue["url"] + newLine
        report = report + indent + bodyText + newLine
        report = report + "\"" + newLine
    
    return report
    
    
    
go()