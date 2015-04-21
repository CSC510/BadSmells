# Call it from terminal by running 
# python fileReader.py inputfile outputfile
from datetime import timedelta
from datetime import datetime
from datetime import date
import matplotlib.pyplot as plt
def reader(inputFile,outputFile):
    f=open(inputFile,'r')
    w=open(outputFile,'w')
    durationArray=[]
    for line in f:
        dateArray=[]
        while(line.find(": 14")!=-1):
            index=line.find(": 14")
            end=line.find(".0")
            if index!=-1:
                for i in range(index+2,end+1):
                    if(line[i]<'0' or line[i]>'9'):
                        break;
                num=int(line[index+2:i]);
                # print num;
                newDate= datetime(1970,1,1,0,0,0)+timedelta(seconds=num)
                dateArray.append(newDate)
                # newDate= date(1970,1,1)+timedelta(num/86400)
                line=line[0:index+2]+str(newDate)+line[i+2:len(line)]
                # print line;
                # w.write(line);
        
        if len(dateArray)>1:
            duration = dateArray[0]-dateArray[1]
            durationArray.append(duration.days*24+duration.seconds/3600)
            hours= "duration: "+str(duration.days*24+duration.seconds/3600)+" hours \n"
            line=line+str(hours);
        # print line
        w.write(line)
    durationArray.sort();
    print durationArray;
    tarArray=[]
    tarArray.append(durationArray[int(len(durationArray)*0.1)]);
    tarArray.append(durationArray[int(len(durationArray)*0.3)]);
    tarArray.append(durationArray[int(len(durationArray)*0.5)]);
    tarArray.append(durationArray[int(len(durationArray)*0.9)]);
    print tarArray;
    # plt.plot(durationArray)
    # plt.show()
    w.closed
    f.closed
if __name__ == '__main__':
    import sys
    reader(sys.argv[1],sys.argv[2])
# reader("group8.txt","output8.txt")
