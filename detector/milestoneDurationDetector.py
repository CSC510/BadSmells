import gitable as gt
import numpy as np

def milestoneDurationDetector():

    items = gt.dumpMilestones()
    avg_val = np.mean(items['duration'])
    std_dev = np.std(items['duration'])
    val = std_dev
    print(items['duration'])
    for x in items['duration']:
        res = cmp(x,  avg_val + val)    # when isssues number is greater than avg + 2 * stand deviation or less than avg - 2 * stand deviation
        res2 = cmp(x,  avg_val - val)
        if res > 0:
            print ('Badsmell: This milestone has Xlong time.')
        elif res2 < 0:
            print ('Badsmell: This milestone has Xsmall time.')
        else:
            print ('Milestone time is normal')


milestoneDurationDetector()