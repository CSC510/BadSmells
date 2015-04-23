# count issues for each milestone
# Run python file: python milestoneDetector.py input.txt output.txt (eg: python milestoneDetector.py group8.txt output8.txt)
def reader(inputFile, outputFile):
    fd = open(inputFile, 'r')
    wd = open(outputFile, 'w')
    milestoneDict = {};  # record each milestone's issue number
    issueCount = 0;  # count issue numbers
    previousMilestone = "";
    for line in fd:
        index1=line.find("ISSUE")
	index2=line.find("milestone :")    
        if index1 != -1:
	    issueCount += 1;
        if index2 != -1:	# change milestone using hashtable
            curMilestone = line[index2+11:len(line)];
	    if curMilestone != previousMilestone:
		if previousMilestone in milestoneDict:
		    milestoneDict[previousMilestone] = milestoneDict[previousMilestone] + issueCount - 1;
		    issueCount = 1;
		else:
		    if previousMilestone != "":
		    	milestoneDict[previousMilestone] = issueCount - 1;
		    issueCount = 1;
		    
	    previousMilestone = curMilestone;	  

    # output the last milestone's issue number.
    if previousMilestone in milestoneDict:
	milestoneDict[previousMilestone] = milestoneDict[previousMilestone] + issueCount;
    else:
#	print issueCount;
	if previousMilestone != "":
	    milestoneDict[previousMilestone] = issueCount;
    # output the results
    print "{:<15} {:<10}".format('Milestone','IssueNumbers')
    for key, v in milestoneDict.items():
	#label, num = v;
        print "{:<2} {:<23}".format(key, v);

    fd.closed
    wd.closed
if __name__ == '__main__':
    import sys
    reader(sys.argv[1],sys.argv[2])
