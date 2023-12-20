import sqlite3

connection = sqlite3.connect('movies.db') 
cursor = connection.cursor() 

famousFilms = [('Pulp Fiction', 'Quentin Tarantino', 1994),
               ('Back to the Future', 'Steven Spielberg', 1985),
               ('Moonrise Kingdom', 'Wes Anderson', 2012)]

cursor.executemany('INSERT INTO Movies VALUES(?, ?, ?)', famousFilms) # Insert multiple rows of data

cursor.execute(''' SELECT * FROM Movies ''') # Select all rows from the Movies table

print(cursor.fetchall()) # Fetch all rows of a query result, returning a list

connection.commit()   
connection.close() 

# Remember that the cursor resets after each commit() and closes after each close().