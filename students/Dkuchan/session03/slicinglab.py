#slicinglab.py


asequence=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

def slicer1(asequence):  
    interimholder1=asequence[0]
    interimholder2=asequence[-1]
    asequence[0]=interimholder2
    asequence[-1]=interimholder1
    print(asequence)

    """class solution
    return sequence[-1:] +sequence[1:-2] + sequence[0]
    """

def slicer2(asequence):
    asequence=asequence[0:-1:2]
    print(asequence)

def slicer3(asequence):
    asequence2=asequence[5:-4]
    print(asequence2)

def slicer4(asequence):
    asequence3=asequence[::-1]
    print(asequence3)

def slicer5(asequence):
    sequencelen=len(asequence)
    sectionlen=sequencelen/3
    print(sectionlen)
    section1=asequence[0:sectionlen]
    section2=asequence[sectionlen:sectionlen*2]
    section3=asequence[sectionlen*2:sectionlen*3]
    asequence4=section2+section3+section1
    print(asequence4)







slicer1(asequence)
slicer2(asequence)
slicer3(asequence)
slicer4(asequence)
slicer5(asequence)