# Pyro4-Remote-Object-Control
read_csv.py
A python document for reading the CSV and determining the branch of tasks.
employee.py
A python document for displaying books, adding books, selecting books by year range, select books by ISBN, setting the book on loan and setting the book not on loan.
library.py
A python document which is a remote object for storing books in library, adding books in library and changing the book on/not on loan status.
test.text
A CSV file contains tasks commands.

How To Run and Test:
1. Start a name server
Open a console window and execute the following command to start a name server:
python -m Pyro4.naming (or simply: pyro4-ns)
The name server will start and it prints something like:
Not starting broadcast server for localhost.
NS running on localhost:9090 (127.0.0.1)
Warning: HMAC key not set. Anyone can connect to this server! URI = PYRO:Pyro.NameServer@localhost:9090
2. Start the remote object
Open a new terminal in the dictionary and enter the following command to start the remote object.
python library.py
Object <__main__.Library object at 0x7f950f0a9dd8>:
uri = PYRO:obj_3425c2a0528b4c93b85317bc0cbe739f@localhost:34823 name = example.library
Pyro daemon running.
3. Run the tasks
Open a new terminal in the dictionary and enter the following command:
python read_csv.py tasks.txt
