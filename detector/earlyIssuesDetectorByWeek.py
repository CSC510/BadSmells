__author__ = 'fred'

import gitable as gt
import numpy as np

def earlyIssuesByWeekDetector():
    issues_nums=[]
    items = gt.launchDump()
    issues_nums = gt.divideByTime(items['create_at'])

    avg_val = np.mean(issues_nums[0:4])
    std_dev = np.std(issues_nums[0:4])
    val = std_dev
    data = issues_nums[0:4]
    print(data)
    sum = 0
    for i in range(len(data)):
        res = cmp(data[i], avg_val + val)    # when isssues number is greater than avg + 2 * stand deviation or less than avg - 2 * stand deviation
        res2 = cmp(data[i], avg_val - val)
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


earlyIssuesByWeekDetector()