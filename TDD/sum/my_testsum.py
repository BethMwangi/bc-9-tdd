import unittest
from my_sum import my_sum

class TestSum(unittest.TestCase):

	def test_sum_of_digits(self):
		''' Test sum of 5 and 10 is 15'''		
		self.assertEqual(my_sum(5,10), 15)

	def test_sum2(self):
		''' Test sum of 9 and 3 can only be 12'''
		self.assertNotEqual(my_sum(9,3), 12)


	def test_sum2(self):
		''' Test sum of negative numbers '''
		self.assertEqual(my_sum(-1,-2), -3)

	
	def test_string(self):
		'''assert throwing of exceptions if it is a string '''
		result = my_sum('','')
		self.assertNotEqual(type(result), int , msg= 'Type Error')


	def test_no_arguments(self):
		'''assert no arguments passed have been passed'''
		result = my_sum()
		self.assertIsNone(result, msg='No arguments passed')
	
	

if __name__ == '__main__':
	unittest.main()
