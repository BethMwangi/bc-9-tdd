
class NotesApplication(object):


	def __init__(self, author):
		self.author = author
		self.notes = []

	def create(self, note_content):
		"""
		   This function takes the note content 
		   as the parameter and adds it to 
		   the notes list of the object.
		"""
		if type (note_content) == str or type(note_content) == int:
			self.notes.append(note_content)
		else:
			return 'None'


	def list(self):
		
		""" This function lists out 
		    each of the notes in the 
		    notes list in the following format. 
		"""

		if len(self.notes) > 0: #checks if note is empty
			for note in self.notes:
				print 'Note ID:' + self.notes.index(note)
				print 'note' 
				print 'By Author ' + self.author
		else:
			return 'None'

	def get(self, note_id):
		"""
		This function takes a note_id which refers 
		to the index of the note in the notes list and 
		returns th e content of that note as a string.
		"""
		
		if self.notes[note_id]:
			return self.notes[note_id]
		else:
			raise IndexError

	def search (self, search_text):
		"""
		This function take a search string, search_text 
		and returns all the notes with that text within 
		it in the following format
		"""
		for note in self.notes:
			for search_text in note:

				print 'Showing results for search' + search_text
				print 'Note ID' + self.notes.index(note)
				print 'By Author ' + self.author

	def delete(self, note_id):
		"""
		This function deletes the note 
		at the index note_id 
		of the notes list.
		"""
		if self.notes[note_id]:
			del(self.notes[note_id])
		else:
			return 'Does not exist'


	def edit(self, note_id, new_content):
		"""
		This function replaces the content in the
		 note at note_id with new_content.
		"""
		if self.notes[note_id]:
			self.notes[note_id] = new_content
		else:
			raise IndexError
		
				
b = NotesApplication('beth')
b.create ('Note one')
b.create ('Note Two')
b.create ('Note Three')
b.create ('Note Four')










			




