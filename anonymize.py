# Anonymize username and milestone description
# Run python file: python anonymize.py input.txt output.txt (eg: python anonymize.py group8.txt output8.txt)
def reader(inputFile, outputFile):
    fd = open(inputFile, 'r')
    wd = open(outputFile, 'w')
    userDict = {};
    user = "user";
    milestoneDict = {};
    milestone = "milestone";
    userCount = 0;
    milestoneCount = 0;
    for line in fd:
        index1=line.find("user :")
	index2=line.find("milestone :")
        if index1!=-1:
	    if index2 != -1:   # get username from line
            	res = line[index1+7:index2-2];
	    else:
		res = line[index1+7:index2];
	    #print res;
	    if res in userDict:  # change username using hashtable
		userRes = userDict[res];
            else:
		str1 = user + str(userCount);
                userDict[res] = str1;
		userRes = userDict[res];
		userCount = userCount + 1;

	    if index2 != -1:	# change milestone using hashtable
	        res2 = line[index2+11:len(line)];
	        if res2 in milestoneDict:
		    milestoneRes = milestoneDict[res2];
	        else:
		    str2 = milestone + str(milestoneCount);
		    milestoneDict[res2] = str2;
		    milestoneRes = milestoneDict[res2];
		    milestoneCount = milestoneCount + 1;
	    else:
		milestoneRes = "";
            
	    string = line[0:index1+7] + userRes + line[index2-2:index2+12] + milestoneRes; # conbine string
	    #print userRes;
	    #print milestoneRes;
	    #print string;
	    wd.write(string+'\n');
	else:
	    #print line;
            wd.write(line);
	    #print;
    fd.closed
    wd.closed
if __name__ == '__main__':
    import sys
    reader(sys.argv[1],sys.argv[2])
