#

def make_bricks(num_small, num_big, goal):
	if num_small * 1 + num_big * 5 < goal:
		return False
	needed_large = goal // 5
	if needed_large > num_big:
		return False
	needed_small = goal % 5
	if needed_small > num_small:
		return False

	print('needed_large:', needed_large)
	print('needed_small:', needed_small)

	return True

assert make_bricks(3, 2, 8)
assert make_bricks(10, 0, 8)



if goal % 5 > num_small:
	return False
