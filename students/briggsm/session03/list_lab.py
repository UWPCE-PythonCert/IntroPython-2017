'''This is the session two list lab.'''

stuff = ["Apples", "Pears", "Oranges", "Peaches"]
print(stuff)

morestuff = input("Please add another fruit. >")
print("You added: {}".format(morestuff))
stuff.append(morestuff)
print(stuff)

def displayitem(x, alist):
    '''Take a list and an index and display an item.'''
    x = int(x)
    max = len(alist)
    ind = x-1
    if max <= ind:
        return "Index out of range."
    else:
        return "You choose: [{}] {}".format(x, alist[ind])

choose = input("Pick an item in the list its index (starting with 1) > ")
print (displayitem(choose, stuff))

stuff = ["Strawberry"] + stuff
print (stuff)

stuff.insert(0,"Banana")
print (stuff)

for i in stuff:
    if i[0] == "P":
        print (i)
