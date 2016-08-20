import unittest
from datatype import data_type

class TestDataType(unittest.TestCase):
	"""docstring for TestDataType"""
	
	# def test_if_arg_is_typeof_str(self):
	# 	self.assertIsInstance(type('myarg'), str, "the arg passed is a string")

	def test_for_bool_value(self):
		myarg = True
		self.assertTrue(myarg, "arg gave back a True")

	def test_for_bool_value(self):
		myarg = False
		self.assertFalse(myarg, "arg gave back a False")

	def test_for_bool_value(self):
		self.assertIsNotNone(data_type(''), "No value")








if __name__ == '__main__':
	unittest.main()
		