
def array123(array=[]):
    #print("array:",array)
    for i in range(0, len(array)-2):
        subset=array[i:i+3]
        #print(i,"subset:",subset)
        if subset==[1,2,3]:
            return True
    return False

print(array123([1,1,2,3,1]))
print(array123([1,1,2,4,1]))
print(array123([1,1,2,1,2,3]))
