def super_sum(*args):
	'''
	Takes in elements 
	in a list and returns
	total  sum
	'''

	total = 0 #initialize the total for elements in a list
	int_num = 0 #adds the integers passed 

	for element in args: # loops through each element passed
		if type(element) is list: #test if the element is a list
			for i in element:
				if type(i) is int:
					total = i + total # adds the elements in an individual list
				else:
					return ' You have entered a non integer'
		else:
			if type(element) is int: #test if the element passed is an integer
				int_num = element + int_num
			else:
				return 'you entered a non integer item'

	super_total = int_num + total #adds the super sum of all elements
	return super_total

	

	


















