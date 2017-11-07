#!/usr/bin/env python3


def rev_str(str):
    return str[::-1]


def fruit_lst():
    '''
    Playing with list and fruit
    '''
    fruits = ['Apple', 'Pears', 'Orange', 'Peaches']
    print(fruits)

    new_fruit = input('Please, add a fruit to the list\n')
    fruits.append(new_fruit)
    print(fruits)

    bool = True
    nb_fruits = len(fruits)
    while bool:
        number = input('Please give a number between 1 and {}\n'.format(nb_fruits))
        try:
            number = int(number)
            if number <= nb_fruits:
                number -= 1
                bool = False
            else:
                print('Not enough fruits!\n')
        except:
            print('Wrong input !\n')

    print( '{} is fruit {}\n'.format(str(number + 1), fruits[number]) )

    fruits = ['Raspberry'] + fruits
    print(fruits)

    fruits.insert(0, 'Strawberry')
    print(fruits)

    for fruit in fruits:
        if fruit[0] == 'P':
            print(fruit)

    print(fruits)
    del fruits[-1]
    print(fruits)

    del_fruit = input('Please remove a fruit from the list\n')
    fruits = 2 * fruits
    fruits = list(filter(lambda fruit: fruit != del_fruit, fruits))
    print(fruits)

    new_fruits = list()
    for fruit in fruits:
        bool = True
        while bool:
            like_fruit = input('Do you like {}?\n'.format(fruit.lower()))
            if like_fruit == 'yes' or like_fruit == 'no':
                bool = False
                if like_fruit == 'yes':
                    new_fruits.append(fruit)
            else:
                print('Please type yes or no')

    fruits = new_fruits
    del new_fruits
    print(fruits)


if __name__ == '__main__':
    fruit_lst()
    print(rev_str('test'))
