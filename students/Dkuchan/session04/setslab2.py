# setslab2.py
unionset = set()
interset = set()
inputstring = 'P,y,t,h,o,n'
inputstring2 = 'M,a,r,a,t,h,o,n'
danset = set([inputstring])
frostyset = frozenset([inputstring2])
#danset.remove()    need to figure out how to remove the single quote
danset.add('i')
danset.add(frostyset)
unionset = danset.union(frostyset)
interset = danset.intersection(frostyset)


print(danset)
print()
print(unionset)
print()
print(interset)
