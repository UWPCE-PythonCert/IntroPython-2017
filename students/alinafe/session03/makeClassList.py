#!/usr/bin/env python3
"""
1.1) Create a list that contains the names of 5 students of this class. (Do not ask for input to do that, simply create the list.) Print the list. Ask the user to input one more name and append it to the list. Print the list. Ask a user to input a number. Print the name that has that number as index. Add "John Smith" and "Mary Miller" at the beginning of the list (by using "+"). Print the list.
"""
students=['Briggsm','Eowyn','Hirot','Kegan','Morgan','Scott']
print(students)

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an number! Try again.")
       continue
    else:
       return userInput 
       break 

def inputName(message):
  while True:
    try:
       userInput = str(input(message))       
       userInput = userInput.capitalize()
    except ValueError:
       print("Not an string! Try again.")
       continue
    else:
       return userInput 
       break 

#while newStudentInput != 'quit' or 'q':
#newStudentInput = inputName("Enter another student name, or enter 'quit': ")
newStudentInput = inputName("Enter another student name: ")
    
#    if newStudentInput != 'quit':
students.append(newStudentInput)

print(students)
#while newStudentNumber != 'quit:
students= ["John Smith","Mary Miller"] +students

#newStudentNumber = inputNumber("Enter a number, or enter 'quit' : ")

#for idx,i in enumerate(range(len(students)-1)):
#    #if i < len(students)-1:
#    if i = students[-1:]:
#        print (idx)
#        break
#    else:
#        print (idx)

#def getIndexOfList(students, index):
#    for pos,t in enumerate(range(len(students))):
#        if t[index]:
#            return students[pos]

#    raise ValueError("list.index(x): x not in list")

while True:
    try:
        newStudentNumber = inputNumber("Enter a number equal to or less than {}: ".format(students.index(students[-1])))
        #getIndexOfList(students, newStudentNumber) 
    except ValueError:
	print("That number is out of Range!")
    else:
        if 0 <= newStudentNumber < students.index(students[-1]):
            print(newStudentNumber)
            break
        else:
            print("Out of range. Try Again.")

    
#    if newStudentNumber != 'quit':
#tuple_list = [("pineapple", 5), ("cherry", 7), ("kumquat", 3), ("plum", 11)]
#>>> [x for x, y in enumerate(tuple_list) if y[1] == 7]
#[1]
#>>> [x for x, y in enumerate(tuple_list) if y[0] == 'kumquat']
#print the list
print(students)
#remove the last name from the list
students.pop()
#print the list
print(students)

newStudentInput = inputName("Enter another student name: ")
if newStudentInput in students:
    print(students.index(newStudentInput))
    students.pop(students.index(newStudentInput))
else:
    students.append(newStudentInput)

studentsCopy = students[:]
studentsCopy.reverse()
print(students)
print(studentsCopy)

for idx,i in enumerate(range(len(students)-1)):
    if i < len(students)-1:
        print ("Hello {}, how are you? ".format(students[i]))
        #break
    else:
        print ("You don't have students.")
