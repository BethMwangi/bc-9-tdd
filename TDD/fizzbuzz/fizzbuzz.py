
def fizz_buzz(num):
	if num < 1:
		return "number should be an integer"
	elif type(num) is str:
		""" if a string is passed, should raise an error"""
		return "the input should be an integer"
	else:
		if num% 3 == 0 and num%5 == 0:  #checks visibilty of both 3 and 5
			return 'FizzBuzz'
		elif num % 3 == 0:  #checks visibilty of both 3 
			return 'Fizz'
		elif num % 5 == 0:   #checks visibilty of both  5
			return 'Buzz'
		else:
			return num 
           
          
          
         


# print fizz_buzz()