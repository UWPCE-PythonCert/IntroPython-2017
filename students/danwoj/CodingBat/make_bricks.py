def make_bricks(small, big, goal):
  if small * 1 + big * 5 < goal:
    return False
  needed_large = goal // 5
  if goal % 5 <= small and goal / 5 <= big
  	return True
  elif small > 5:
  	if large < big:
  		diff = goal - large*5
  		if diff <= small:
  			return True

  else:
  	leftover = goal - big*5
  	if leftover <= small:
  		
#  if needed_large > big:
#  	return False
#  needed_small = goal % 5
#  if needed_small > small:
#  	return False

  print('Needed Large: ', needed_large)
  print('Needed Small: ', needed_small)
  return True

assert make_bricks(3, 1, 8) is True
assert make_bricks(3, 1, 9) is False
assert make_bricks(0, 2, 8) is False
assert make_bricks(10, 1, 12) is True