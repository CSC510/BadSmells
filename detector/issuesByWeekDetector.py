__author__ = 'fred'

import gitable as gt
import numpy as np


def issuesByWeekDetector():
    issues_nums=[]
    items = gt.launchDump()
    issues_nums = gt.divideByTime(items['create_at'])
    #print(issues_nums)

    avg_val = np.mean(issues_nums)
    std_dev = np.std(issues_nums)
    val = std_dev
    for x in issues_nums:
        res = cmp(x, avg_val + val)    # when isssues number is greater than avg + 2 * stand deviation or less than avg - 2 * stand deviation
        res2 = cmp(x, avg_val - val)
        if res > 0:
            print ('Badsmells: This week has too many issues.')
        elif res2 < 0:
            print ('Badsmells: This week has too less issues.')
        else:
            print ('Issues numbers are normal')


issuesByWeekDetector()