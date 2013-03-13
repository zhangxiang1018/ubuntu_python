from os.path  import join

class FileObject:
	def __init__(self, filepath='~', filename='sample.txt'):
		self.file = open(join(filepath, filename), 'r+')
    def __del__(self):
    	self.file.close()
    	del self.filen