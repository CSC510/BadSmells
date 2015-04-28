import gitable as gt
import base

def milestoneDurationDetector():
    page = 1
    dtime=[]
    issues=[]
    milestones=dict()
    items = gt.dumpMilestones()
    milestoneDurationDetect(items['duration'])
    #print(issues)

def milestoneDurationDetect(dtime):
    avg_val = base.avg(dtime)
    std_dev = base.stdDeviation(dtime)
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

milestoneDurationDetector()