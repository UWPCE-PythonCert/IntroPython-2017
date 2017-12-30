#dictlab2.py
#create a program which outputs the number of t's in the original dictionary from dictlab.py

#CREATE STARTING DICT
dandict = dict()
dandict['name'] = 'Chris'
dandict['city'] = 'Seattle'
dandict['cake'] = 'Chocolate'

def updatedT():
    for i in dandict:
        valstring=dandict[i]
        tcount=0
        for j in range(0,len(valstring)):   #this might also be doable by saying for j in valstring: if j=='t' etc etc
            if valstring[j]=='t':
                tcount+=1
        dandict[i]=tcount


updatedT()
print(dandict)