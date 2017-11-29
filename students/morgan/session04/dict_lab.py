# $ ./dict_lab.py
# $ chmod +x dict_lab.py

# Dictionaries 1



merp = {'name': 'Chris', 'city':'Seattle', 'cake':'Chocolate'}
print(merp)

del merp['cake']

print(merp, 'no cake')

merp['fruit'] = 'Mango'

print(merp,'add fruit')



for key in merp:
	print(key)

for value in merp:
	print(merp[value])

if 'cake' in merp:
	print('Cake is real')
else:
	print('Cake is a lie')

if 'fruit' in merp:
	print('i have fruit')
else:
	print('i have no fruit')

input('')


# Dictionaries 2

derp = dict(merp)

for key in derp:
	derp[key] = merp[key].count('t') + merp[key].count('T')
print(merp)
print(derp)

# Sets 1

s2 =set()
s3 =set()
s4 =set()

i = 0
while i <=20:
	if i % 2 == 0:
		s2.add(i)
	if i % 3 == 0:
		s3.add(i)
	if i % 4 == 0:
		s4.add(i)
	i+=1


print(s2)
print(s3)
print(s4)

print('3 in 2?', s3.issubset(s2) )
print('4 in 2?', s4.issubset(s2))

# sets 2

hrmp = {'p','y','t','h','o','n'}
hrmp.add('i')

nert = frozenset({'m','a','r','a','t','h','o','n'})
print(hrmp)
print(nert)

print(nert.union(hrmp))
print(nert.intersection(hrmp))