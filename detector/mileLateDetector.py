def mileLateDetector(data):
    print (data)
    if sum(data)>0.2* len(data):
        print ('bad smell in fullfilling milestones')
    else:
        print ('no smell detected')
