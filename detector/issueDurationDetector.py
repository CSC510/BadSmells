import base
def issueDurationDetector(data):
    values=data
    values.sort()
    print (values)
    hv=base.high(values)['value']
    hp=base.high(values)['pos']
    mv=base.median(values)['value']
    mp=base.median(values)['pos']
    lv=base.low(values)['value']
    lp=base.low(values)['pos']
    print ('lv',lv,'mv',mv,'hv',hv)
    print ('lp',lp,'mp',mp,'hp',hp)
    # plt.plot(values)
   #  plt.show()
    k= float((hv-mv)*(mp-lp)/((hp-mp)*(mv-lv)))
    if k>3:
        print ('bad smells in issue length')
    elif k==3:
        print ('probably have smells in issue length')
    else:
        print ('no smells in issue length detected')
    print ("k",k)