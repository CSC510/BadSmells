import gitable as gt
import base
from numpy import *

def pullFileDetector():
    data= gt.dumpPulls()['changedfiles']
    print (data)
    data.sort()
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
    if 8*lowCount/len(data) > 1 or 8*highCount/len(data)>1:
        print ("BadSmell found in Pull Request Files")
    else:
        print ("Pull Request Files Detector Passed")
    
pullFileDetector()