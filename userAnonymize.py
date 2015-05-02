# count issues for each user
# Run python file: python userDetector.py input.txt output.txt (eg: python userDetector.py group8.txt output8.txt)
def reader(inputFile, outputFile):
    fd = open(inputFile, 'r')
    wd = open(outputFile, 'w')
    userDict = {};  # record each user's issue number
    issueCount = 0;  # count issue numbers
    previousUser = "";
    for line in fd:
        index1=line.find("ISSUE");
	index2=line.find("user :");
	index3=line.find("milestone :");    
        if index1 != -1:
	    issueCount += 1;
        if index2 != -1:	# change user using hashtable
            curUser = line[index2+7:index2+12];
	    #print curUser;
	    if curUser != previousUser:
		if previousUser in userDict:
		    userDict[previousUser] = userDict[previousUser] + issueCount - 1;
		    issueCount = 1;
		else:
		    if previousUser != "":
		    	userDict[previousUser] = issueCount - 1;
		    issueCount = 1;
		    
	    previousUser = curUser;	  

    # output the last user's issue number.
    if previousUser in userDict:
	userDict[previousUser] = userDict[previousUser] + issueCount;
    else:
	print issueCount;
	if previousUser != "":
	    userDict[previousUser] = issueCount;
    # output the results
    print "{:<15} {:<10}".format('Users: ','IssueNumbers: ')
    for key, v in userDict.items():
	#label, num = v;
        print "{:<15} {:<10}".format(key, v);

    fd.closed
    wd.closed
if __name__ == '__main__':
    import sys
    reader(sys.argv[1],sys.argv[2])
