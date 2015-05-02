__author__ = 'fred'

import gitable as gt
import numpy as np


def issuesByWeekDetector():
    issues_nums=[]
    items = gt.launchDump()
    issues_nums = gt.divideByTime(items['create_at'])
    print(issues_nums)

    avg_val = np.mean(issues_nums)
    std_dev = np.std(issues_nums)
    val = std_dev
    sum = 0
    for i in range(len(issues_nums)):
        res = cmp(issues_nums[i], avg_val + val)    # when isssues number is greater than avg + 2 * stand deviation or less than avg - 2 * stand deviation
        res2 = cmp(issues_nums[i], avg_val - val)
        if (i > 0):
            sum = issues_nums[i-1] + issues_nums[i]
        if sum < avg_val and i > 0:
            print ('Badsmells: This week has too less issues.')
            sum = 0
        elif res > 0:
            print ('Badsmells: This week has too many issues.')
        elif res2 < 0:
            print ('Badsmells: This week has too less issues.')
        else:
            print ('Issues numbers are normal')


issuesByWeekDetector()