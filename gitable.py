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
import math
from datetime import timedelta
from datetime import date

token="5f1dcfbcc9c3b7a61f49a7225990bc7f2eccf029"
#project="SuperCh-SE-NCSU/ProjectScraping"
#project="CSC510/SQLvsNOSQL"
project ="bighero4/MarkParser"
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

def dump3(u, milestones,  dtime,  issues):  # add dtime and issues
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
    issues_num = open_issues + closed_issues
    issues.append(issues_num)
    if closed_at != None:
        duration=secs(closed_at)-secs(created_at)
        dtime.append(duration/3600)
    else:
         duration = float("inf")
    
    due_on = milestone['due_on']
    if due_on>closed_at:
        late=True
    else:
        late=False
    milestoneObj = L( # what = title,
                   open_issues= open_issues,
                   closed_issues =closed_issues,
                   # created_at = secs(created_at),
                   # closed_at = secs(closed_at),
                   duration = duration/3600,
                   # due_on = secs(due_on),
                   late= late,
                   total_issues= int(closed_issues)+int(open_issues)
                      )
    all_milestones =  milestones.get(title)
    if not all_milestones:
        all_milestones = []
    all_milestones.append(milestoneObj)
    milestones[title] = all_milestones
    return True
    
def dump4(u, pulls):
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
    pullObj = L( # what = title,
                 # created_at = secs(created_at),
                 # closed_at = secs(closed_at),
                 # merged_at =secs(merged_at),
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
def dumpM(u,milestones,  dtime,  issues):
    try:
        return dump3(u,milestones,  dtime,  issues)
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
def dump1(u,issues,labels,dur,create):
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
    if labels.has_key(label_name) and action==("labeled"):
        labels[label_name]+=1
    else:
        labels[label_name]=1
    all_events = issues.get(issue_id)
    if not all_events: 
      all_events = []
      issue = event['issue']
      created_at = secs(issue['created_at'])
      closed_at = secs(issue['closed_at'])
      if closed_at!=None:
          duration = secs(issue['closed_at'])-secs(issue['created_at'])
      else:
          duration = float("inf")
      issueObj = L( state = issue['state'],
                    user =  issue['user']['login'],
                    comments =issue['comments'],
                     #add more attributes here: attr_name = issue['attr'] , json response described here:https://developer.github.com/v3/issues/events/
                    created_at = secs(issue['created_at']),
                    closed_at = secs(issue['closed_at']),
                    duration =duration
                    #duration = closed_at- created_at
                   )
      all_events.append(issueObj)
      dur.append(int(duration/3600))        
      create.append(created_at)
    all_events.append(eventObj)
    issues[issue_id] = all_events
  return True

def dump(u,issues,labels,duration,create):
  try:
    return dump1(u, issues,labels,duration,create)
  except Exception as e: 
    print(e)
    print("Contact TA")
    return False

def launchDump():
  page = 1
  issues = dict()
  labels={}
  duration=[]
  create=[]
  while(True):
    doNext = dump('https://api.github.com/repos/'+project+'/issues/events?page=' + str(page), issues,labels,duration,create)
    # print("page "+ str(page))
    page += 1
    if not doNext : break
  # for issue, events in issues.iteritems():
  #   print("ISSUE " + str(issue))
  #   for event in events: print(event.show())
  #   print('')
  
  print ("labels used Times",labels)
  print ("duration in hours",duration)
  print ("Issue created by weeks",divideByTime(create))

def dumpCommits():
    page = 1
    commits= dict()
    time=[];
    while(True):
       doNext =  dumpC('https://api.github.com/repos/'+project+'/commits?page='+str(page), commits,time)
       # print("page "+str(page))
       page += 1
       if not doNext : break
    # for author,commits in commits.iteritems():
#         print("AUTHOR "+ author)
#         # print(len(commits))
#         for commit in commits:
#             print(commit.show())
#         print('')
    print (divideByTime(time))
def divideByTime(time):
    time.sort();
    newDate= datetime.datetime.utcfromtimestamp(0)+timedelta(seconds=time[0])
    weekday=newDate.weekday()
    start=newDate-datetime.timedelta(days=weekday,weeks=0)
    print ("start week",start)
    std=secs(str(start))
    count=0;
    countTime=[]
    for i in time:
        if i <= std+604800:
            count+=1
        else:
            countTime.append(count)
            count=1
            std+=604800
    countTime.append(count)
    print ("total Num",sum(countTime))
    return countTime
    
def dumpCommitsNum():  # count each user's commits numbers
    page = 1
    commits= dict()
    times=[]
    user_count = 0
    while(True):
       doNext =  dumpC('https://api.github.com/repos/'+project+'/commits?page='+str(page), commits,  times)
       print("page "+str(page))
       page += 1
       if not doNext : break
    for author, commits in commits.iteritems():	
        print("user"+ str(user_count) + ": " + str(len(commits)))
        user_count += 1
        print('')

    
def dumpMilestones():
    page=1
    dtime=[]
    issues=[]
    milestones=dict()
    while(True):
        doNext=dumpM('https://api.github.com/repos/'+project+'/milestones/'+str(page),  milestones,  dtime,  issues)
        # print("page "+str(page))
        page+=1
        if not doNext :break
    for title,milestone in milestones.iteritems():
        for item in milestone:
            print (item.show())
        print('')
        
def dumpPulls():
    page=1
    pulls=dict()
    doNext=dumpP('https://api.github.com/repos/'+project+'/pulls?state=closed', pulls)
    # for author, pulls in pulls.iteritems():
    #     print("AUTHOR "+ author)
    #     # print(len(commits))
    #     # for commit in commits: print(commit.show())
    #     print('')

#avg  threshold
#g1[19, 9, 6, 4, 6, 1, 5, 13]=7, 5.41987084717
#g6[3, 19, 4, 5, 1, 1, 1, 14]=6, 6.34428877022
#g8[10, 9, 7, 1, 1, 1, 1, 18, 20]=7, 7.04745817062
def avg(data):
    sum = 0
    length = len(data)
    for x in data:
        sum += x
    avg = sum / length
    return avg
def stdDeviation(data):
    avg_val = avg(data)
   # print (avg_val)
    total = 0
    length = len(data)
    for x in data:
        temp = math.fabs(x - avg_val)
        total += math.pow(temp,  2)
    std_dev = math.sqrt(total/length)
   # print (std_dev)
    return std_dev
def issuesDetect(issues):
    avg_val = avg(issues) 
    std_dev = stdDeviation(issues)
    val = 2*std_dev
    for x in issues:
        res = cmp(x,  avg_val+val)    # when isssues number is greater than avg + 2 * stand deviation or less than avg - 2 * stand deviation
        res2 = cmp(x,  avg_val - val)
        if res > 0:
            print ('Badsmells: This week has too many issues.')
        elif res2 < 0:
            print ('Badsmells: This week has too less issues.')
        else:
            print ('Issues numbers are normal')

    
def issuesByWeekDetector():
  page = 1
  issues = dict()
  labels={}
  duration=[]
  create=[]
  issues_nums=[]
  while(True):
    doNext = dump('https://api.github.com/repos/'+project+'/issues/events?page=' + str(page), issues,labels,duration,create)
    page += 1
    if not doNext : break
  issues_nums = divideByTime(create)
  issuesDetect(issues_nums)

# g1[65.42333333333333, 1069.7225, 1310.9583333333333, 304.98833333333334, 1310.2811111111112] avg=812.274722222, std=524.995531997
# g6 [186.93472222222223, 596.8102777777777, 652.6475, 620.1069444444445, 264.0052777777778] avg=464.100944444, std=197.159241914
# g8 [876.8580555555556, 987.67, 987.4355555555555] avg=950.654537037, std=52.1820802596
def milestoneDurationDetector():
    page = 1
    dtime=[]
    issues=[]
    milestones=dict()
    while(True):
        doNext=dumpM('https://api.github.com/repos/'+project+'/milestones/'+str(page), milestones,  dtime,  issues)
        page += 1
        if not doNext :break
    milestoneDurationDetect(dtime)
    #print(issues)

def milestoneDurationDetect(dtime):
    avg_val = avg(dtime)
    std_dev = stdDeviation(dtime)
    val = std_dev
    for x in dtime:
        res = cmp(x,  avg_val + val)    # when isssues number is greater than avg + 2 * stand deviation or less than avg - 2 * stand deviation
        res2 = cmp(x,  avg_val - val)
        if res > 0:
            print ('Badsmell: This milestone has Xlong time.')
        elif res2 < 0:
            print ('Badsmell: This milestone has Xsmall time.')
        else:
            print ('Milestone time is normal')

# g1[1, 13, 6, 13, 6] avg=7, std=4.69041575982
# g6 [14, 19, 8, 7, 8] avg=11, std=4.62601340249
# g8 [23, 4, 14, 23, 0] avg=12, std=9.52890339966
def milestoneIssuesDetector():
    page = 1
    dtime=[]
    issues=[]
    milestones=dict()
    while(True):
        doNext=dumpM('https://api.github.com/repos/'+project+'/milestones/'+str(page), milestones,  dtime,  issues)
        page += 1
        if not doNext :break
    milestoneIssuesDetect(issues)
    #print(issues)

def milestoneIssuesDetect(issues):
    avg_val = avg(issues)
    std_dev = stdDeviation(issues)
#    print (avg_val)
#    print (std_dev)
    val = std_dev
    for x in issues:
        res = cmp(x,  avg_val + val)    # when isssues number is greater than avg + 2 * stand deviation or less than avg - 2 * stand deviation
        res2 = cmp(x,  avg_val - val)
        if res > 0:
            print ('Badsmell: This milestone has too many issues.')
        elif res2 < 0:
            print ('Badsmell: This milestone has too less issues.')
        else:
            print ('Issue number in this milestone is normal')
    
print ("pull request")
dumpPulls()
print ("milestone")
dumpMilestones()
print ("commit")
dumpCommits()
dumpCommitsNum()
print ("issues")
launchDump()
issuesByWeekDetector()
milestoneDurationDetector()
milestoneIssuesDetector()

  
   
 


  
   
 
