def remove_fruit():
    '''remove last or user specified fruit from list'''
    fruits = ['Apples','Pears','Oranges','Peaches']
    print(fruits)
    del fruits[-1]
    print(fruits)
    choice = input("Which fruit should be removed? > ")
    ## this works in ipython but not here...?
    ## should remove all instances of choice
    fruits2 = [x for x in fruits if x!= choice]
    print(fruits2)

if __name__ == "__main__":
    remove_fruit()
