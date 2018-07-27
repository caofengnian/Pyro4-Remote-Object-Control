import csv
import sys
import Pyro4
import Pyro4.util
from  employee import Employee

sys.excepthook = Pyro4.util.excepthook
library = Pyro4.Proxy("PYRONAME:example.library")
employee = Employee()

f = open('./tasks.txt', 'r')
try:
	reader = csv.reader(f)
	for row in reader:
		print(row)
		if(row[0] == 'a'):
			employee.add_book(row, library) #add book

		elif(row[0] == 'sy'):
			employee.select_year(row[1], row[2], library) #select book by year 

		elif(row[0] == 'd'):
			employee.display(library) #display all the book

		elif(row[0] == 'si'):
			employee.select_ISBN(row[1],library) #select book by ISBN

		elif(row[0] == 'ol'):
			employee.on_loan(row[1],library) #set book on loan by ISBN

		elif(row[0] == 'nol'):
			employee.not_on_loan(row[1],library) #set book not on loan by ISBN
finally:
    f.close()