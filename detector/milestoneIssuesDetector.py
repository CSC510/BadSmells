import gitable
import base

# g1[1, 13, 6, 13, 6] avg=7, std=4.69041575982
# g6 [14, 19, 8, 7, 8] avg=11, std=4.62601340249
# g8 [23, 4, 14, 23, 0] avg=12, std=9.52890339966
def milestoneIssuesDetector():
    page = 1
    dtime=[]
    issues=[]
    milestones=dict()
    while(True):
        doNext=gitable.dumpM('https://api.github.com/repos/'+project+'/milestones/'+str(page), milestones,  dtime,  issues)
        page += 1
        if not doNext :break
    milestoneIssuesDetect(issues)
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