#  gitabel
#  the world's smallest project management tool
#  reports relabelling times in github (time in seconds since epoch)
#  thanks to dr parnin
#  todo:
#    - ensure events sorted by time
#    - add issue id
#    - add person handle

"""
You will need to add your authorization token in the code.
Here is how you do it.

1) In terminal run the following command

curl -i -u <your_username> -d '{"scopes": ["repo", "user"], "note": "OpenSciences"}' https://api.github.com/authorizations

2) Enter ur password on prompt. You will get a JSON response. 
In that response there will be a key called "token" . 
Copy the value for that key and paste it on line marked "token" in the attached source code. 

3) Run the python file. 

     python gitable.py

"""
 
from __future__ import print_function
import urllib2
import json
import re,datetime
import sys
 
class L():
  "Anonymous container"
  def __init__(i,**fields) : 
    i.override(fields)
  def override(i,d): i.__dict__.update(d); return i
  def __repr__(i):
    d = i.__dict__
    name = i.__class__.__name__
    return name+'{'+' '.join([':%s %s' % (k,pretty(d[k])) 
                     for k in i.show()])+ '}'
  def show(i):
    lst = [str(k)+" : "+str(v) for k,v in i.__dict__.iteritems() if v != None]
    return ',\t'.join(map(str,lst))

  
def secs(d0):
  if d0==None:
      return d0;
  d     = datetime.datetime(*map(int, re.split('[^\d]', d0)[:-1]))
  epoch = datetime.datetime.utcfromtimestamp(0)
  delta = d - epoch
  return delta.total_seconds()



def dump2(u, commits,time):
  token = "INSERT TOKEN HERE" # <===
  request = urllib2.Request(u, headers={"Authorization" : "token "+token})
  v = urllib2.urlopen(request).read()
  w = json.loads(v)
  if not w: return False
  for commit in w:
    author = commit['author']['login']
    message = commit['commit']['message']
    created_at = commit['commit']['committer']['date']
    time.append(secs(created_at))
    commitObj = L( what = repr(message),
                   when = secs(created_at)
                      )
    all_commits =  commits.get(author)
    if not all_commits:
        all_commits = []
    all_commits.append(commitObj)
    commits[author] = all_commits
  return True

def dump3(u, milestones):
    token = "INSERT TOKEN HERE" # <===
    request = urllib2.Request(u, headers={"Authorization" : "token "+token})
    v = urllib2.urlopen(request).read()
    milestone = json.loads(v)
    if not milestone: return False
    title = milestone['title']
    open_issues = milestone['open_issues']
    closed_issues = milestone['closed_issues']
    created_at = milestone['created_at']
    updated_at = milestone['updated_at']
    closed_at = milestone['closed_at']
    if closed_at != None:
        duration=secs(closed_at)-secs(created_at)
    else:
         duration = inf
    due_on = milestone['due_on']
    milestoneObj = L( what = title,
                   open_issues= open_issues,
                   closed_issues =closed_issues,
                   created_at = secs(created_at),
                   closed_at = secs(closed_at),
                   duration = duration/3600,
                   due_on = secs(due_on),
                   total_issues= int(closed_issues)+int(open_issues)
                      )
    all_milestones =  milestones.get(title)
    if not all_milestones:
        all_milestones = []
    all_milestones.append(milestoneObj)
    milestones[title] = all_milestones
    return True
    
def dump4(u, pulls):
  token = "INSERT TOKEN HERE" # <===
  request = urllib2.Request(u, headers={"Authorization" : "token "+token})
  v = urllib2.urlopen(request).read()
  w = json.loads(v)
  if not w: return False
  for pull in w:
    title = pull['title']
    number = pull['number']
    created_at = pull['created_at']
    closed_at = pull['closed_at']
    merged_at = pull['merged_at']
    if merged_at != None:
        process_duration=secs(merged_at)-secs(created_at)
    elif closed_at != None:
        process_duration=secs(closed_at)-secs(created_at)
    else:
        process_duration=inf
    request2 = urllib2.Request('https://api.github.com/repos/CSC510/SQLvsNOSQL/pulls/'+str(number), headers={"Authorization" : "token "+token})
    v2= urllib2.urlopen(request2).read()
    w2 = json.loads(v2)
    mergeable = w2['mergeable']
    changed_files= w2['changed_files']
    pullObj = L( what = title,
                 created_at = secs(created_at),
                 closed_at = secs(closed_at),
                 merged_at =secs(merged_at),
                 mergeable =mergeable,
                 process_duration = process_duration,
                 changed_files=changed_files
                      )
    print (pullObj.show())
    all_pulls =  pulls.get(title)
    if not all_pulls:
        all_pulls = []
    all_pulls.append(pullObj)
    pulls[title] = all_pulls
  return True
def dumpC(u,commits,time):
    try:
       return  dump2(u, commits,time)
    except Exception as e:
        print("problem when dump commits")
        print(e)
        return False
def dumpM(u,milestones):
    try:
        return dump3(u,milestones)
    except Exception as e:
        print("problem when dump milestones")
        print(e)
        return False;
def dumpP(u,pulls):
    try:
        return dump4(u,pulls)
    except Exception as e:
        print("problem when dump pull requests")
        print(e)
        return False;
def dump1(u,issues):
  token = "INSERT TOKEN HERE" 
  request = urllib2.Request(u, headers={"Authorization" : "token "+token})
  v = urllib2.urlopen(request).read()
  w = json.loads(v)
  if not w: return False
  for event in w:
    issue_id = event['issue']['number']
    if not event.get('label'): continue
    created_at = secs(event['created_at'])
    action = event['event']
    label_name = event['label']['name']
    user = event['actor']['login']
    milestone = event['issue']['milestone']
    if milestone != None : milestone = milestone['title']
    eventObj = L(when=created_at,
                 action = action,
                 what = label_name,
                 user = user,
                 milestone = milestone)
    all_events = issues.get(issue_id)
    if not all_events: 
      all_events = []
      issue = event['issue']
      issueObj = L( state = issue['state'],
                    user =  issue['user']['login'],
                    comments =issue['comments'],
                     #add more attributes here: attr_name = issue['attr'] , json response described here:https://developer.github.com/v3/issues/events/
                    created_at = secs(issue['created_at']),
                    closed_at = secs(issue['closed_at']),
                    #duration = closed_at- created_at
                   )
      all_events.append(issueObj)          
    all_events.append(eventObj)
    issues[issue_id] = all_events
  return True

def dump(u,issues):
  try:
    return dump1(u, issues)
  except Exception as e: 
    print(e)
    print("Contact TA")
    return False

def launchDump():
  page = 1
  issues = dict()
  while(True):
    doNext = dump('https://api.github.com/repos/CSC510/SQLvsNOSQL/issues/events?page=' + str(page), issues)
    print("page "+ str(page))
    page += 1
    if not doNext : break
  for issue, events in issues.iteritems():
    print("ISSUE " + str(issue))
    for event in events: print(event.show())
    print('')

def dumpCommits():
    page = 1
    commits= dict()
    time=[];
    while(True):
       doNext =  dumpC('https://api.github.com/repos/CSC510/SQLvsNOSQL/commits?page='+str(page), commits,time)
       print("page "+str(page))
       page += 1
       if not doNext : break
    for author,commits in commits.iteritems():
        print("AUTHOR "+ author)
        # print(len(commits))
        for commit in commits:
            print(commit.show())
        print('')
    print (time)
    
def dumpMilestones():
    page=1
    milestones=dict()
    while(True):
        doNext=dumpM('https://api.github.com/repos/CSC510/SQLvsNOSQL/milestones/'+str(page), milestones)
        print("page "+str(page))
        page+=1
        if not doNext :break
    for title,milestone in milestones.iteritems():
        for item in milestone:
            print (item.show())
        print('')
        
def dumpPulls():
    page=1
    pulls=dict()
    doNext=dumpP('https://api.github.com/repos/CSC510/SQLvsNOSQL/pulls?state=all', pulls)
    # for author, pulls in pulls.iteritems():
    #     print("AUTHOR "+ author)
    #     # print(len(commits))
    #     # for commit in commits: print(commit.show())
    #     print('')
# dumpPulls()
# dumpMilestones();
dumpCommits()
#launchDump()

  
   
 


  
   
 
