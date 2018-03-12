


def Get_PCs():
    party_list = []
    while True:
        pc = input("What level is the Player Character between 1 and 20? (enter blank value to end)\n>")

        if pc == "" and len(party_list) == 0:
            print("You must enter at least PC level to continue")
        elif pc == "" and len(party_list)> 0:
            break
        else:
            try:
                pc = int(pc)
            except ValueError:
                print("Invalid level choice. Please enter an integer between 1 and 20")
                continue
            else:
                if (1 <= pc <= 20):
                    party_list.append(pc)
                else:
                    print("Invalid level choice. Please enter an integer between 1 and 20")

        # print(pc,'value')

    print("Your party consists of ")
    for y in range(1, 20+1):
        if party_list.count(y) > 0:
            print("{PC_count} PCs at level {pcLvl}".format(PC_count=party_list.count(y), pcLvl=y))


    return party_list

# def Get_Budgets():

def monster_types(group_size):
    split = 1
    if group_size > 1:
        while True:
            split = input("How many types of monsters do you want? (Must be less or equal to {})\n>".format(group_size))
            try:
                split = int(split)
                if split > group_size:
                    print("Please enter a value less than {}".format(group_size))
                else:
                    print('split return', split)
                    return split
                    # break
            except ValueError:
                print("Please enter an integer")
                pass
            except TypeError:
                print("Please enter an integer")
                pass

    return split

def enemy_force_size():
    while True:
        size = input("How many enemies should the party face?\n>")
        try:
            size = int(size)
            return size
        except ValueError:
            print("Please enter an integer")
            pass
        except TypeError:
            print("Please enter an integer")
            pass

def choose_difficulty():
    while True:
        difficulty = input("What difficulty of encounter do you want?\n"
                     "1. Easy\n"
                     "2. Medium\n"
                     "3. Hard\n"
                     "4. Deadly\n>")


        try:
            difficulty = int(difficulty)
            if 1 <= difficulty <= 4:
                return difficulty
            else:
                print("Please enter a value 1 through 4")
                pass
        except ValueError:
            print("Please enter a value 1 through 4")
            pass
        except TypeError:
            print("Please enter a value 1 through 4")
            pass


if __name__ == "__main__":
    Get_PCs()
    # Get_Budgets()

