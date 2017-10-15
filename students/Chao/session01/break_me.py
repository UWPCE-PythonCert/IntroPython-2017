# Function 1: Produce NameError.
def fun1():
    print(non_existing_name)

# Function 2: Produce TypeError.
def fun2():
    a = 1 + '2'

# Function 3: Produce SyntaxError.
def fun3():
    eval('1***3')

# Function 4: AttributeError.
def fun4():
    c = 0
    c.append(1)

# Main Function
def main():
    option = input("What error do you want? (NameError press '1', TypeError press '2', SyntaxError press '3', AttributeError press'4') ")
    if option == '1':
        fun1()
    elif option == '2':
        fun2()
    elif option == '3':
        fun3()
    elif option == '4':
        fun4()
    else:
        print("Try again.")

main()