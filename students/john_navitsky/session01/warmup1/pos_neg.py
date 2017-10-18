
def pos_neg(num1, num2, negative_check):

    negative_count = 0
    if num1 < 0:
        negative_count += 1
    if num2 < 0:
        negative_count += 1

    if negative_check:
        # only return true of both are negative
        return negative_count == 2
    else:
        if negative_count == 1:
            # only return true if one is negative
            return True
        else:
            return False
    

print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))
#print(pos_neg(1, -1, True))
#print(pos_neg(-11, -1, False))
