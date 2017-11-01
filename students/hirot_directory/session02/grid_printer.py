
'''
Dev: Hiro Takechi
Subject: Grid printer
Date: 10-15-2017
'''

plus = '+'
minus = '-'
space = ' '
bar = '|'

def h_line(x):
	x = int((x-1)/2)
	print(plus + minus * x + plus + minus * x + plus)

def v_line(x):
	x = int((x-1)/2)
	print(bar + space * x+ bar + space * x + bar)

def h_line2(x,y):
	print((plus + minus * y) * x + plus)

def v_line2(x,y):
	for i in range(y):
		print((bar + space * y) * x + bar)

def grid_printer2(x,y):
	print("grid printer2",'(', x, ',', y, ')')
	for i in range(x):
		h_line2(x,y)
		v_line2(x,y)
	h_line2(x,y)

def grid_printer(x):
	print("grid printer", '(', x, ')')
	h_line(x)
	for i in range(int((x-1)/2)):
		v_line(x)
	h_line(x)
	for i in range(int((x-1)/2)):
		v_line(x)
	h_line(x)

if __name__ == "__main__":
	grid_printer(3)
	grid_printer(15)
	grid_printer2(3,4)
	grid_printer2(5,3)












