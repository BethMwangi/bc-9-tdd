def super_sum(*args):
	'''
	Takes in elements 
	in a list and returns
	total  sum
	'''

	total = 0 #initialize the total for elements in a list
	float_num = 0.0

	for element in args: # loops through each element passed
		if isinstance(element,list): #test if the element is a list
			for i in element:
				if isinstance(i, int):
					total = i + total # adds the elements in an individual list
				elif isinstance(i, float):
					float_num = i + float_num
				else:
					return ' You have entered a non integer'
		else:
			if type(element) is int: #test if the element passed is an integer
				total += element
			else:
				return 'you entered a non integer item'

	super_sum = float_num + total
	return super_sum




	


















