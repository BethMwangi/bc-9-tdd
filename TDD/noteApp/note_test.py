import unittest
from note import NotesApplication 

class TestNoteApplication(unittest.TestCase):

	def test_int_type_notecontent(self):
		''' pass test for integer inputs'''
		author = NotesApplication('author')
		author.create('note_content')
		self.assertEqual(type(val), int)
		

	def test_string_type_notecontent(self):
		''' pass test for string inputs'''
		author = NotesApplication('author')
		author.create('note_content')
		self.assertEqual(type(val), str)
		







	

