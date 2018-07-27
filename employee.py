from __future__ import print_function
import sys

class Employee(object):
	def __init__(self):
		return None

	def display(self, library):
		for each in library.list_contents():
			print(each)

	def add_book(self, item, library):
		print("THE BOOK ID IS {0}".format(library.add(item)))


	def select_year(self, year1, year2, library):
		if int(year1) <= int(year2):
			for eachbook in library.list_contents():
				if int(eachbook[4]) >= int(year1) and int(eachbook[4])<=int(year2):
					print(eachbook)
		else:
			print("Please input a valid range.")

	def select_ISBN(self, ISBN, library):
		for eachbook in library.list_contents():
			if eachbook[2] == ISBN:
				print(eachbook)

	def on_loan(self, ISBN, library):
		print(library.book_on_loan(ISBN))

	def not_on_loan(self, ISBN, library):
		print(library.book_not_on_loan(ISBN))
