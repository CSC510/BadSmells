import gitable as gt
import base
from numpy import *
import matplotlib.pyplot as plt

def issueDurationDetector():
    values=gt.launchDump()['duration']
#     values.sort()
    print (values)
#     hv=base.high(values)['value']
#     hp=base.high(values)['pos']
#     mv=base.median(values)['value']
#     mp=base.median(values)['pos']
#     lv=base.low(values)['value']
#     lp=base.low(values)['pos']
#     print ('lv',lv,'mv',mv,'hv',hv)
#     print ('lp',lp,'mp',mp,'hp',hp)
#     k= float((hv-mv)*(mp-lp)/((hp-mp)*(mv-lv)))
#     if k>5:
#         print ('bad smells in issue length')
#     elif k==5:
#         print ('probably have smells in issue length')
#     else:
#         print ('no smells in issue length detected')
#
# def issueDurationDetector2():
#     data=gt.launchDump()['duration']
#     print (data)
#     data.sort()
#     data=data[1:len(data)-1]
#     stddeviation= std(data)
#     avg= mean(data)
#     high=avg+stddeviation
#     if avg-stddeviation>0:
#         low=avg-stddeviation
#     else:
#         low=0
#     lowCount=0
#     highCount=0
#     for i in data:
#         if i < low:
#             lowCount+=1
#         if i>high:
#             highCount+=1
#     print (lowCount,highCount)
#     if 40*lowCount/len(data) > 1 or 40*highCount/len(data)>1:
#         print ("BadSmell found in issue Duration")
#     else:
#         print ("issue Duration Detector Passed")
# issueDurationDetector()
# issueDurationDetector2()
if __name__ == '__main__':
    issueDurationDetector()
