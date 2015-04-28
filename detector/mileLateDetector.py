import gitable as gt
import base


def mileLateDetector():
    data=gt.dumpMilestones()['late']
    if sum(data)>0.2* len(data):
        print ('bad smell in fullfilling milestones')
    else:
        print ('no smell detected')
        
        
mileLateDetector()