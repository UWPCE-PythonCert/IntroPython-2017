import kwargs_ex

#pytest test_kwargs.py
#testing kwargs_ex.fun
def te():
	assert True

def test_just_keyword_arguments():
	result = kwargs_ex.fun(link_color='red', 
							back_color='blue')
	assert result == ('blue', 'blue', 'red', 'green')

def test_just_positional_arguements():
	result = kwargs_ex.fun('red', 'blue', 'yellow', 'chartreuse')
	assert result == ('red', 'blue', 'yellow', 'chartreuse')

def test_combination_postional_keyword():
	result = kwargs_ex.fun('purple', link_color='red', back_color='blue')
	assert result == ('purple', 'blue', 'red', 'green')

def test_tuple():
	tup = ('red', 'blue')
	result = kwargs_ex.fun(*tup, 'yellow1')
	assert result == ('red', 'blue', 'yellow1', 'green')

def test_dict():
	mydict = {'link_color':'white', 
	'fore_color':'purple',
	'visted_color':'bronze',
	'back_color':'blue'}
	result = kwargs_ex.fun(**mydict)
	assert result == ('purple', 'blue', 'white', 'bronze')

#testing kwargs_ex.fun2
def test_return_colors():
	mydict = {'link_color':'white', 
	'fore_color':'purple',
	'visted_color':'bronze',
	'back_color':'blue',
	'added':'why'}
	tup = ('red', 'blue')
	result = kwargs_ex.fun2(*tup, **mydict)
	print(result)
	assert result == (('red', 'blue'), 
		{'link_color':'white', 
		'fore_color':'purple',
		'visted_color':'bronze',
		'back_color':'blue',
		'added':'why'})




"""
fore_color='blue',
back_color='red',
link_color='yellow',
visted_color='green'

def test_kw():
	result = kwargs_ex.fun(fore_color='blue',
							back_color='red',
							visted_color='green',
							link_color='yellow'
							)
	assert result == ('blue', 'red','yellow','green')

def test_kw_new_orde():
	result = kwargs_ex.fun('green',
							'blue',
							'purple',
							'red')
	assert result == ('green','blue', 'purple','red')



def test_kw_combo():
	result = kwargs_ex.fun('green',
							'blue',
							visted_color='green',
							link_color='red')
	assert result == ('green','blue', 'yellow','red')


def test_kw_tup():
	tup =('blue',
			'red',
			'yellow',
			'green')
	result = kwargs_ex.fun(*tup)
	assert result == tup

def test_kw_dict():
	dic ={'fore_color':'blue',
		'back_color':'red',
		'link_color':'yellow',
		'visted_color':'green'}
	result = kwargs_ex.fun(**dic)
	assert result == dic

def test_kw_combo():
	tup = ('green',
			'blue')

	dic ={#'fore_color':'blue',
		#'back_color':'red',
		'link_color':'yellow',
		'visted_color':'green'}
	result = kwargs_ex.fun(*tup, **dic)
	assert result == ('green', 'blue', 'yellow', 'green'
		"""


"""
****THESE ARE FROM CLASS REMOVE DOCSTRING TO OBSERVE****
def test_fun2():
	result = kwargs_ex.fun2()
	assert result == ((), {})

def test_fun_pos():
	result = kwargs_ex.fun2(2,3)
	assert result == ((2,3), {})

def test_fun_kw():
	result = kwargs_ex.fun2(this=45)
	assert result == ((), {'this':45})


def test_fun_both():
	result = kwargs_ex.fun2(4,5,this=45)

	assert result[0] ==(4,5)
	assert result[1] == {'this':45}

def test_fun_args():
	t = (4,5,6,7)
	result = kwargs_ex.fun2(*t,this=45)

	assert result[0] ==t
	assert result[1] == {'this':45}


def test_fun_args2():
	t = (4,5,6,7)
	result = kwargs_ex.fun2(6,7,*t,this=45)

	assert result[0] ==t
	assert result[1] == {'this':45}
"""