"""
Week 4 Lab 1
Write a script to perform the following actions:

1. Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
2. Display the dictionary.
3. Delete the entry for “cake”.
4. Add an entry for “fruit” with “Mango” and display the dictionary.

    Display the dictionary keys.
    Display the dictionary values.
    Display whether or not “cake” is a key in the dictionary.
    Display whether or not “Mango” is a value in the dictionary.

5. Using the dictionary from item 1, make a dictionary using the same keys but with the number of ‘t’s in each value.
"""

dic = {'name': 'Chris', 'city':'Seattle', 'cake': 'Chocolate'}  #create a dictionary
dic2 = dic.copy()  #making copy of dic
print('\nDisplay dic:\n', dic)  #display dic
del dic['cake']   #del key
dic['fruit'] = 'Mango'   #adding key and value to dic
print("\nDisplay new dic after adding new key(fruit) & value(mango)':\n", dic)    #display dic
print("\nDisplay dic's key:\n", dic.keys())    #printing dic keys
print("\nDisplay dic's value:\n", dic.values())    #printing dic values
print("\nCheck if cake is in dic's key:\n", 'cake' in dic.items())    #is cake in dic key
print("\nCheck if mango is in dic's key:\n", 'Mango' in dic.values())     #is mango in dic value


def getValue():
    """ counting 't' in each value, but keeping key the same """
    dd = {}
    for key, value in dic2.items():
        dd[key] = (value.count('t'))
    return dd

print("\nNumber of 't' in each value:")
print(getValue())