#make a row that is goal inches long 
#using 1" bricks and 5" bricks

#I dont really know what we are trying to solve here.


#can you make a wall with x number of different bricks

num_small=1
num_big=1
goal=6

def make_bricks(num_small,num_big,goal):

    nec_big=goal/5
    nec_small=goal%5

    if nec_big>=num_big and nec_small>=num_small:
        print("YES")
    else:
        print("NO")


make_bricks(num_small,num_big,goal)

"""
print("num_big: ",num_big)
print("num_small: ",num_small)

#should be devide goal by 5 for num_large
#get remainder using goal%5 for num_small



assert make_bricks(3,1,8) is True
assert make_bricks(3,1,9) is False
"""