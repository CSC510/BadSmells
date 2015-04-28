import gitable as gt
import base
from numpy import *

def pullTimeDetector():
    data= gt.dumpPulls()['processTime']
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
    if lowCount/len(data) > 0.1 or highCount/len(data)>0.1:
        print ("BadSmell found in Pull Request Time")
    else:
        print ("Pull Request Time Detector Passed")
pullTimeDetector()