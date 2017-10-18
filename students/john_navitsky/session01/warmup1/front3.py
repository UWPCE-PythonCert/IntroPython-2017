
def front3(string):
    index = 3
    length = len(string)
    if length <= 3:
      index = length
    front = string[0:index]
    return front

print(front3("Java"))
print(front3("Chocolate"))
print(front3("abc"))
#print(front3("a"))
#print(front3("ab"))
