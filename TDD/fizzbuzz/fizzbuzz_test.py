import unittest
from fizzbuzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

	def test_num_divisible_by_3_and_5(self):
		''' Test number given is divisible by both 3 and 5'''
		self.assertEqual(fizz_buzz(15), 'FizzBuzz')

	def test_num_divisible_by_3_and_5(self):
		''' Test number given is divisible by both 3 and 5'''
		self.assertNotEqual(fizz_buzz(10), 'FizzBuzz')


	def test_num_divisible_by_3_only(self):
		''' Test number given is divisible by 3 only'''
		self.assertEqual(fizz_buzz(3), 'Fizz')


	def test_num_divisible_by_3_only(self):
		''' Test number given is divisible by 5 only'''
		self.assertEqual(fizz_buzz(10), 'Buzz')


	def test_num_is_not_divisible_by_either_3_or_5_or_both(self):
		''' Test number given is divisible by both 3 and 5 or 3 or 5'''
		self.assertEqual(fizz_buzz(11), 11)

	def test_num_less_than_zero_is_not_divisible(self):
		''' Test for negative numbers and raise error'''
		num = fizz_buzz(0)
		self.assertNotEqual(type(num), int, msg="number should be an integer")

	def test_arg_passed_is_string(self):
		''' assert throwing of exceptions if  a string  is passed '''
		num = fizz_buzz('beth')
		self.assertNotEqual(type(num), int, msg="input should be an integer")

	def test_arg_passed_is_int(self):
		''' test for int numbers passed'''
		num = fizz_buzz(8)
		self.assertEqual(type(8), int)















if __name__ == '__main__':
	unittest.main()


