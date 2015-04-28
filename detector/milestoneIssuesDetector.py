import gitable as gt
import base

def milestoneIssuesDetector():
    page = 1
    dtime=[]
    issues=[]
    milestones=dict()
    items = gt.dumpMilestones()
    milestoneIssuesDetect(items['issueNum'])
    #print(issues)

def milestoneIssuesDetect(issues):
    avg_val = base.avg(issues)
    std_dev = base.stdDeviation(issues)
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

milestoneIssuesDetector()