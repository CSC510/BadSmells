import gitable as gt
import base
from numpy import *
import matplotlib.pyplot as plt

def issueDurationDetector():
    zeroCount=0
    values=gt.launchDump()['duration']
    print (values)
    print ("Method 1")
    values.sort()
    for i in values:
        if i <=0.1:
            zeroCount+=1
        else:
            break
    hv=base.high(values)['value']
    hp=base.high(values)['pos']
    mv=base.median(values)['value']
    mp=base.median(values)['pos']
    lv=base.low(values)['value']
    lp=base.low(values)['pos']
    print ('low val',lv,'median val',mv,'high val',hv)
    print ('low pos',lp,'median pos',mp,'high pos',hp)
    k= float((hv-mv)*(mp-lp)/((hp-mp)*(mv-lv)))
    if k>5 or 20*zeroCount>len(values):
        print ('BadSmell found in issue Duration')
    elif k==5:
        print ('Probably have smells in issue length')
    else:
        print ('Issue Duration Detector Passed')

def issueDurationDetector2():
    print ("Method 2")
    zeroCount=0
    data=gt.launchDump()['duration']
    data.sort()
    for i in data:
        if i <=0.1:
            zeroCount+=1
        else:
            break
    data=data[1:len(data)-1]
    stddeviation= std(data)
    avg= mean(data)
    high=avg+stddeviation
    if avg-stddeviation>0:
        low=avg-stddeviation
    else:
        low=0
    lowCount=0
    highCount=0
    for i in data:
        if i < low:
            lowCount+=1
        if i>high:
            highCount+=1
    print ("avg",avg,"std",stddeviation)
    print ("strange small count=",lowCount,"strange large count=",highCount,"none issue count",zeroCount)
    if 20*(lowCount+highCount) > len(data) or 20*zeroCount>len(data):
        print ("BadSmell found in issue Duration")
    else:
        print ("Issue Duration Detector Passed")
issueDurationDetector()
issueDurationDetector2()

