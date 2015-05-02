__author__ = 'fred'

import gitable as gt
import numpy as np

def milestoneDetector():

    issues_items = gt.dumpMilestones()
    issues_avg_val = np.mean(issues_items['issueNum'])
    issues_std_dev = np.std(issues_items['issueNum'])
    print('Issue number in each milestone: ', issues_items['issueNum'])
    issues_num = issues_items['issueNum']

    duration_time_items = gt.dumpMilestones()
    dtime_avg_val = np.mean(duration_time_items['duration'])
    dtime_std_dev = np.std(duration_time_items['duration'])
    dtime_num = duration_time_items['duration']

    print ('Duration time in each milestone: ', duration_time_items['duration'])

    for k in range(len(dtime_num)):
        issues_res = cmp(issues_num[k],  issues_avg_val + issues_std_dev)
        issues_res2 = cmp(issues_num[k],  issues_avg_val - issues_std_dev)

        dtime_res = cmp(dtime_num[k], dtime_avg_val + dtime_std_dev)
        dtime_res2 = cmp(dtime_num[k], dtime_avg_val - dtime_std_dev)

        if issues_res > 0 and dtime_res2 < 0:
            print ('Badsmell: Milestone has too many issues in short time!')
        elif issues_res2 < 0 and dtime_res > 0:
            print ('Badsmell: Milestone has too less issues in long time!')
        else:
            print ('Milestone duration time and issues number are normal')



milestoneDetector()
