
def array_front9(list=[]):
    range_num = 4
    list_len = len(list)
    #print("list:",list)
    #print("len:",list_len)
    if list_len < 4:
        range_num = list_len
    #print("range: 0 -",range_num)
    for entry in range(0, range_num):
        #print("entry:",entry,"value=",list[entry])
        if list[entry] == 9:
            return True
    
    return False


#print(array_front9([1,2,9,3]))
#print(array_front9([1,9,3]))
#print(array_front9([9,3]))
#print(array_front9([9]))
#print(array_front9([3]))
#print(array_front9([]))
#
print(array_front9([1,2,9,3,4]))
print(array_front9([1,2,3,4,9]))
print(array_front9([1,2,3,4,5]))

