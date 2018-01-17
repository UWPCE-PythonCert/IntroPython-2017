
def monkey_trouble(a_smile=False, b_smile=False):

    bool_monkey=a_smile + b_smile
    if bool_monkey in [2, 0]:
        return True
     
    return False


print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))
