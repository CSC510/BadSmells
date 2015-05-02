import base
import gitable as gt
import matplotlib.pyplot as plt
from numpy import *

def labelUseDetector():
    data=gt.launchDump()['labels'].values()
    # print (data)
    data.sort()
    data=data[0:len(data)-1]
    stddeviation= std(data)
    avg= mean(data)
    high=avg+stddeviation
    if avg-stddeviation>0:
        low=avg-stddeviation
    else:
        low=0
    lowCount=0
    highCount=0
    print ("avg",avg)
    print ("std",stddeviation)
    for i in data:
        if i < low:
            lowCount+=1
        if i>high:
            highCount+=1
    print ("number of strange low data",lowCount)
    print ("number of strange high data",highCount)
    if 10*(lowCount+highCount)/len(data) > 1:
        print ("BadSmell found in Label Use")
    else:
        print ("Label Use Detector Passed")

labelUseDetector()
