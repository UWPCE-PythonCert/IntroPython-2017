#dictlab.py
#'name' : 'Chris' , 'city' : 'Seattle' , 'cake' : 'Chocolate'


#CREATE DICT
dandict = dict()
dandict['name'] = 'Chris'
dandict['city'] = 'Seattle'
dandict['cake'] = 'Chocolate'

#DISPLAY DICT
print(dandict)

print()
print()


#DELETE ENTRY FOR CAKE
del dandict['cake']

#DISPLAY DICT
print(dandict)

#add entry for fruit
dandict['fruit'] = 'Mango'


#DISPLAY DICT
print(dandict)

#display keys
print(dandict.keys())

print()
print()

#display values

#for i in dandict:
 #   print(dandict[i])

#OR MORE SIMPLY
print(dandict.values())


#in function for dicts
print("is 'cake' in the dictionary?")
print('cake' in dandict)

print("is 'mango' in the dictionary?")
print('Mango' in dandict.values())

