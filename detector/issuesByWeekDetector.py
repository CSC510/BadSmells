__author__ = 'fred'
import math
import gitable as gt
import base

def issuesDetect(issues):
    avg_val = base.avg(issues)
    std_dev = base.stdDeviation(issues)
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
    doNext = gitable.dump('https://api.github.com/repos/'+project+'/issues/events?page=' + str(page), issues,labels,duration,create)
    page += 1
    if not doNext : break
  issues_nums = gitable.divideByTime(create)
  issuesDetect(issues_nums)
