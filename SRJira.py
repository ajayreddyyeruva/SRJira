from jira.client import JIRA
import sys

class SRJira:
    
    def __init__(self, server, userName, password):
        server = 'https://snapdeal.atlassian.net'
        userName = 'sandeep.rawat@jasperindia.com'
        password = 'sandeep'
        options = {
            'server': server
        }
        self.jira = JIRA(options)

        self.jira = JIRA(basic_auth=(userName, password))
        
    def verifyIssueOwner(self, issueId, emailId):
        jiraIssue = self.jira.issue(issueId)
        if jiraIssue.fields.assignee.emailAddress == emailId:
            print 'Issue ', issueId , ' belongs to correct owner ', emailId
        else:
            print 'Issue ', issueId , ' correct owner is ', jiraIssue.fields.assignee.emailAddress, 'please check!'
            sys.exit(1)

    def verifyIssueState(self, issueId, issueState):
        jiraIssue = self.jira.issue(issueId)
        if jiraIssue.fields.status.name == issueState:
            print 'Issue ', issueId , ' is in correct state ', issueState
        else:
            print 'Issue ', issueId , ' state is ', jiraIssue.fields.status.name, 'please check!'
            sys.exit(1)
            
    def updateIssue(self, issueId, commitMessage):
        jiraIssue = self.jira.issue(issueId)
        comment = 'A commit with %s is done using this JIRA' % commitId
        print comment
        self.jira.add_comment(jiraIssue, comment)
            
            
srJira = SRJira('https://snapdeal.atlassian.net', 'sandeep.rawat@jasperindia.com', 'sandeep')
srJira.verifyIssueOwner('SNAPDEALTECH-7830', 'sandeep.rawat@jasperindia.com',);
#srJira.verifyIssueState('SNAPDEALTECH-7830','Open')
commitId = '8693e3fe4c3669f5c88caf1e6036aab964f94c27'
commitMessage = 'A commit with %s is done using this JIRA' % commitId
srJira.updateIssue('SNAPDEALTECH-7830', commitMessage)