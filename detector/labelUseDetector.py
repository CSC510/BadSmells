import base
import matplotlib.pyplot as plt
def labelUseDetector(labels):
    values=labels.values()
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
    k= float((hv-mv)*(mp-lp)/((hp-mp)*(mv-lv)))
    if k>3:
        print ('bad smells in label usage')
    elif k==3:
        print ('probably have smells in label usage')
    else:
        print ('no smells in label detected')
    print ("k",k)
    plt.plot(values)
    plt.show()
