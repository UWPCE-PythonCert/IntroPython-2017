
def make_bricks(num_small, num_big, goal):
    """ can i make the goal with the number of bricks supplied """
    optimal_big = int(goal / 5)
    if num_big >= optimal_big:
        used_big = optimal_big
    else:
        used_big = num_big
    big_dist=used_big * 5
    big_shortfall = goal - big_dist
    if big_shortfall <= num_small:
        print("reached goal! ")
    else:
        print("too few!")
    #print(locals())
    



    print("num_small:",num_small,"num_big:",num_big,"goal:",goal)
    print("optimal_big:",optimal_big,"used_big:",used_big)
    print("")


#assert make_bricks(3,1,9) is False
make_bricks(3,1,10)
make_bricks(3,5,10)
make_bricks(3,5,11)

#print(globals())    
