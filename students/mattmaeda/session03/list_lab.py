#!/usr/bin/env python3

def series1(fruits):
    print(fruits)

    response = input("Input a fruit: ")
    fruits.append(response)
    print(fruits)

    valid_num = False
    max_num = len(fruits)
    index = -1

    while not valid_num:
        response = input("Input a number between 1 and {}: ".format(max_num))

        try:
            index = int(response)

            if index > 0 and index <= max_num:
                valid_num = True

        except ValueError:
            print("Not a valid number")

    print(fruits[index-1])

    response = input("Input a fruit: ")
    fruits = [response] + fruits
    print(fruits)

    response = input("Input a fruit: ")
    fruits.insert(0, response)
    print(fruits)

    print("Print all fruits that begin with 'P'")
    p_fruits = []
    for f in fruits:
        if f.startswith("P") or f.startswith("p"):
            p_fruits.append(f)
    print(p_fruits)


def series2(fruits):
    print(fruits)
    del fruits[-1]
    print(fruits)

    exit_loop = False
    while not exit_loop and len(fruits) != 0:
        response = input("Input a fruit to delete (Enter to exit): ")

        if response != "" and response in fruits:
            delete_indexes = []
            for i in range(len(fruits)):
                if fruits[i] == response:
                    delete_indexes.append(i)

            for i in delete_indexes:
                del fruits[i]

            print(fruits)
        elif response != "":
            print("Fruit '{}' not found".format(response))
        else:
            exit_loop = True


def series3(fruits):
    tmp_copy = fruits.copy()
    hated_fruit = []
    for f in tmp_copy:
        response = ""

        while response != "yes" and response != "no":
            response = input("Do you like {}?".format(f.lower()))

        if response == "no":
            hated_fruit.append(f)


    for x in hated_fruit:
        del fruits[fruits.index(x)]

    print("Here are the fruits you like:")
    print(fruits)


def series4(fruits):
    fruit_copy = fruits.copy()
    for i in range(len(fruit_copy)):
        fruit_copy[i] = fruit_copy[i][::-1]
    del fruits[-1]
    print("Original: {}".format(fruits))
    print("Copy: {}".format(fruit_copy))


if __name__ == "__main__":
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]

    # Series 1
    print("#" * 10)
    print("Series 1")
    series1(fruits.copy())


    # Series 2
    print("#" * 10)
    print("Series 2")
    series2(fruits.copy())

    # Series 3
    print("#" * 10)
    print("Series 3")
    series3(fruits.copy())

    # Series 4
    print("#" * 10)
    print("Series 4")
    series4(fruits.copy())
