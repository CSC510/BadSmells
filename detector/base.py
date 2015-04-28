import math

def avg(data):
    sum = 0
    length = len(data)
    for x in data:
        sum += x
    avg = sum / length
    return avg
def stdDeviation(data):
    avg_val = avg(data)
   # print (avg_val)
    total = 0
    length = len(data)
    for x in data:
        temp = math.fabs(x - avg_val)
        total += math.pow(temp,  2)
    std_dev = math.sqrt(total/length)
   # print (std_dev)
    return std_dev

def high(l):
    h={}
    h['pos']=int(0.9*len(l))
    h['value']=l[int(0.9*len(l))]
    return h
def median(l):
    m={}
    m['pos']=int(0.5*len(l))
    m['value']=l[int(0.5*len(l))]
    return m
def low(l):
    lw={}
    lw['pos']=int(0.1*len(l))
    lw['value']=l[int(0.1*len(l))]
    return lw
