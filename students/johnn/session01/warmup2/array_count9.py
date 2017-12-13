
def array_count9(array=[]):
    nines=0
    #print(array)
    for i in range(0, len(array)):
        if array[i]==9:
            nines+=1
            #print(i,array[i])
    return nines

print(array_count9([1,2,9]))
print(array_count9([1,9,9]))
print(array_count9([1,9,9,3,9]))
#print(array_count9([1,1,1,1,1]))
