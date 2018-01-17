
def parrot_trouble(parrot_talking=False, current_hour=0):
    if parrot_talking:
        return current_hour < 7 or current_hour > 20

    return False
        

print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))
#print(parrot_trouble(True, 21))
