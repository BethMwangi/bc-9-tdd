def super_sum(*args):
	'''
	Takes in elements 
	in a list and returns
	total  sum
	'''

	total = 0 #initialize the total for elements in a list
	

	for element in args: # loops through each element passed
		if type(element) is list: #test if the element is a list
			for i in element:
				if type(i) is int:
					total = i + total # adds the elements in an individual list
				else:
					return ' You have entered a non integer'
		else:
			if type(element) is int: #test if the element passed is an integer
				total += element
			else:
				return 'you entered a non integer item'

	
	return total

	


















