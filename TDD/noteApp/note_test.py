import unittest
from note import NotesApplication 

class TestNotesApplication(unittest.TestCase):

	def test_valid_note_content(self):
		# Test for valid note input
		#create(note) method
		note=NotesApplication("New note")
		self.assertEqual(note.create("New Note"), "Success", msg="Invalid Note Entry")

	def test_invalid_note_content(self):
		# Test for invalid note note_content e.g Empty String Input
		#create(note) method
		note=NotesApplication("New note")
		self.assertEqual(note.create(""), "None", msg="Invalid Note Entry")
	

	def test_if_noteid_does_not_exist(self):
		#Test for get(id) method for a note_id that does not exist
		author3 = NotesApplication('allan')
		with self.assertRaises(IndexError):
			author3.get(3)

	def test_when_noteid_exists(self):
		#Test for get(id) method for a note_id that exist
		author = NotesApplication('Qusai')
		author.create("new note")
		self.assertEqual(author.get(0), "new note", msg="Note Index not Found")

	def test_notes_search(self):
		#Test for search in empty list
		notes_list = NotesApplication("Beth")
		self.assertEqual(notes_list.search("Search Text"), "Empty Notes List", msg="List has Content")

	def test_notes_search2(self):
		#Test for search where the search text is found
		notes_list = NotesApplication("Beth")
		notes_list.create("This is my note")
		self.assertEqual(notes_list.search("note"), "Text Found", msg="Search text not Found")

	def test_note_deletion(self):
		#Test from delete function. Delete an indexthat does not exist
   		notes_list = NotesApplication("Beth")
   		with self.assertRaises(IndexError):
   			notes_list.delete(3)

   	def test_note_deletion2(self):
		#Test from delete function. Delete an index Exists
   		notes_list = NotesApplication("Beth")
   		notes_list.create("First Index")
   		self.assertEqual(notes_list.delete(0), "Deleted", msg="Deletion Failed")

   	def test_note_editting(self):
   		#Test fro edit fnction. Try to edit and Index that does not Exist
   		notes_list = NotesApplication("Beth")
   		with self.assertRaises(IndexError):
   			notes_list.edit(3, "New Content")

   	def test_note_editting2(self):
   		#Test fro edit fnction. Try to edit and Index that Exists
   		notes_list = NotesApplication("Beth")
   		notes_list.create("First Note")
   		self.assertEqual(notes_list.edit(0, "New Content"), "Editted", msg="Edittibg Failed")

   

if __name__ == '__main__':
	unittest.main()
     	






		







	

