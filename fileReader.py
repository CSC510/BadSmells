# Call it from terminal by running 
# python fileReader.py inputfile outputfile

from datetime import timedelta
from datetime import datetime
from datetime import date
def reader(inputFile,outputFile):
    f=open(inputFile,'r')
    w=open(outputFile,'w')
    for line in f:
        index=line.find("when")
        if index!=-1:
            for i in range(index+7,len(line)):
                if(line[i]<'0' or line[i]>'9'):
                    break;
            num=int(line[index+7:i]);
        
            newDate= datetime(1970,1,1,0,0,0)+timedelta(seconds=num)
            # newDate= date(1970,1,1)+timedelta(num/86400)
            string=line[0:index+6]+str(newDate)+line[i+2:len(line)]
            # print string;
            # print line;
            w.write(string);
    f.closed
if __name__ == '__main__':
    import sys
    reader(sys.argv[1],sys.argv[2])
# reader("group4.txt","output4.txt")
