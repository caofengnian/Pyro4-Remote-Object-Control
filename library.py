from __future__ import print_function
import Pyro4

@Pyro4.expose
class Library(object):
	def __init__(self):
		self.contents = []

	def list_contents(self):
		return self.contents

	def add(self, item): #add the book
		id = str(len(self.contents)) #id is the number of items in library
		item[0]=id
		item.append('no')
		self.contents.append(item)
		print("THE BOOK IS ADDED SUCCESSFULLY.THE BOOK ID IS {0}".format(id))
		return id

	def book_on_loan(self, ISBN): #set the book on loan
		for i in range(len(self.contents)):
			if self.contents[i][2] == ISBN:
				self.contents[i][5] = 'yes'
				print("{0} IS ON LOAN".format(ISBN))
				return self.contents[i]

	def book_not_on_loan(self, ISBN): #set the book not on loan
		for i in range(len(self.contents)):
			if self.contents[i][2] == ISBN:
				self.contents[i][5] = 'no'
				print("{0} IS NOT ON LOAN".format(ISBN))
				return self.contents[i]

def main():
	library = Library()
	Pyro4.Daemon.serveSimple(
		{
			library: "example.library"
		},
		ns=True)

if __name__ == "__main__":
	main()