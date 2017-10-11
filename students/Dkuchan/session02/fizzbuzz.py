#fizzbuzz


"""
this is how you do block commenting
"""

""" What I Wrote
def fizzbuzzer():
    count=0
    for count in range(100):
        if count % 3==0 and count % 5==0:
            print("FizzBuzz")
        elif count % 3==0 or count % 5==0:
            if count % 3==0:
                print("Fizz")
            elif count % 5==0:
                print("Buzz")   
        else:
            print(count)
        count+=1
"""

#this is the simpler way...
def fizzbuzzer():
    count=0
    for count in range(100):
        if count % 3==0 and count % 5==0:
            print("FizzBuzz")
        elif count % 3==0:
                print("Fizz")
        elif count % 5==0:
                print("Buzz")   
        else:
            print(count)
        count+=1

fizzbuzzer()
print("I'm Done")

