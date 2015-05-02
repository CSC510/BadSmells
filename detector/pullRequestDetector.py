import gitable as gt
import base
from numpy import *



def pullRequestDetector():
    time= gt.dumpPulls()['processTime']
    file= gt.dumpPulls()['changedfiles']
    commitNum= gt.dumpCommitsNum()['length']
    
    print ("Process Time",time)
    print ("Changed Files",file)
    print ("Pull request Number",len(time),"Commits number",commitNum)
    if len(time)<0.05*commitNum:
        print ("Too few pull request! BadSmell Detected")
    else:
        if ~pullTimeDetector(time) and ~pullFileDetector(file):
            print ("Pull Request Detector Passed")
        elif pullTimeDetector(time):
            print ("BadSmell found in pull request process Time")
        elif pullFileDetector(file):
            print ("BadSmell found in pull request File changed")
        else:
            print ("BadSmell found in process time and file changed ")
            

def pullTimeDetector(data):
    print ("\nProcess Time")
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
    print ("avg",avg,"std",stddeviation)
    print ("number of strange small time",lowCount,"number of strange large time",highCount)
    if 10*(lowCount+highCount)> len(data) or high(data)>72:
        return True
    else:
        return False
        
def pullFileDetector(data):
    print ("\n File Changed")
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
    print ("avg",avg,"std",stddeviation)
    print ("number of strange large file changed",highCount)
    if 8*highCount/len(data)>1:
        return True
    else:
        return False
pullRequestDetector()