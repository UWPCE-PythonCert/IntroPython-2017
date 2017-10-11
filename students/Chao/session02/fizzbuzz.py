def fibu():
    for i in range(100):
        x = i+1
        if x%3 == 0 and x%5==0:
            print('FizzBuzz')
        elif x%3 == 0:
            print('Fizz')
        elif x%5 == 0:
            print('Buzz')
        print(x)

fibu()