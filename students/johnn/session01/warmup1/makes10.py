
def makes10(num1, num2):
    num_sum = num1 + num2
    if num1 == 10 or num2 == 10 or num_sum == 10:
        return True
    else:
        return False


print(makes10(9,10))
print(makes10(9,9))
print(makes10(1,9))
