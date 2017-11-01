#!/usr/bin/env python

def list_fruit():
    '''Manipualte and print lists of fruit'''
    fruits = ['Apples','Pears','Oranges','Peaches']
    print(fruits)
    fruits += [input("Specify another fruit >")]
    print(fruits)
    index = int(input("Specify an index to see fruit > "))
    if (index-1) > len(fruits) or index < 1:
        index = int(input("Specify index between 1..# of fruit >"))
    else:
        print(index,": ",fruits[index-1])
    fruits = ["Mangos"] + fruits
    print(fruits)
    fruits.insert(0,"Cherries")
    print(fruits)
    [print(fruit) for fruit in fruits if fruit[0].lower()=='p']
    return fruits


def remove_fruit():
    '''remove last and user specified fruit from list'''
    fruits = ['Apples','Pears','Oranges','Peaches']
    print(fruits)
    del fruits[-1]
    print(fruits)
    choice = input("Which fruit should be removed? > ")
    ## remove all instances of choice
    fruits2 = [x for x in fruits if x!= choice]
    print(fruits2)


def remove_disliked_fruit():
    '''remove fruit if user dislikes it'''
    fruits = ['Apples','Pears','Oranges','Peaches']
    i = 0
    stop = len(fruits)
    while i < len(fruits):
        like = input("Do you like {}, yes or no? ".format(fruits[i].lower()))
        if like.lower() == "no":
            del fruits[i]
        elif like.lower() == "yes":
            i += 1
        else:
            print("Enter yes or no *only*")
            continue
    print(fruits)



def rev_fruitnames():
    '''copy list and reverse letters of each fruit
    then delete the last item of original list'''
    fruits = ['Apples','Pears','Oranges','Peaches']
    fruits_copy = fruits[:]
    fruits_copy = [x[::-1] for x in fruits_copy]
    del fruits[-1]
    print(fruits)
    print(fruits_copy)


if __name__=="__main__":
    print("running list_fruit")
    list_fruit()
    print("running remove_fruit")
    remove_fruit()
    print("running remove_disliked_fruit")
    remove_disliked_fruit()
    print("running rev_fruitnames")
    rev_fruitnames()