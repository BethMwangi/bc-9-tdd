import unittest
from note import NotesApplication 

class TestNoteApplication(unittest.TestCase):

	def test_int_and_string_type_notecontent(self):
		''' pass test for string and integer inputs'''
		author = NotesApplication('author')
		author.create('note_content')
		self.assertEqual(type(val), str)
		self.assertEqual(type(val), int)





	

