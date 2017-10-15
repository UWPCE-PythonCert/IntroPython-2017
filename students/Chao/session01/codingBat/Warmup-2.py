def string_times(str, n):
    return str*n

def front_times(str, n):
    return(str[:3]*n)

def string_bits(str):
    n = ""
    for i in range(len(str)):
        if i%2 == 0:
            n += str[i]
    return n

def string_splosion(str):
    n = ""
    for i in range(len(str)):
        n += str[:i+1]
    return n

def last2(str):
    count = 0
    n = str[-2:]
    for i in range(len(str)-2):
        if str[i:i+2] == n:
            count += 1
    return count

def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1
    return count

def array_front9(nums):
    if len(nums) > 4:
        for i in range(4):
            if nums[i] == 9:
                return True
    else:
        for i in nums:
            if i == 9:
                return True
    return False

def array123(nums):
    if len(nums) >= 3:
        for i in range(len(nums)-2):
            if nums[i:i+3] == [1, 2, 3]:
                return True
    return False

def string_match(a, b):
    count = 0
    if (len(a) >= 2) and (len(b) >= 2):
        j = ""
        if a <= b:
            for i in range(len(a)-1):
                if a[i:i+2] == b[i:i+2]:
                    count += 1
        else:
            for i in range(len(b)-1):
                if a[i:i+2] == b[i:i+2]:
                    count += 1
    return count



