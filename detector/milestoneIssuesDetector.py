import gitable as gt
import numpy as np

def milestoneIssuesDetector():

    items = gt.dumpMilestones()
    avg_val = np.mean(items['issueNum'])
    std_dev = np.std(items['issueNum'])
    #print(items['issueNum'])
    val = std_dev
    for x in items['issueNum']:
        res = cmp(x,  avg_val + val)    # when isssues number is greater than avg + 2 * stand deviation or less than avg - 2 * stand deviation
        res2 = cmp(x,  avg_val - val)
        if res > 0:
            print ('Badsmell: This milestone has too many issues.')
        elif res2 < 0:
            print ('Badsmell: This milestone has too less issues.')
        else:
            print ('Issue number in this milestone is normal')


milestoneIssuesDetector()