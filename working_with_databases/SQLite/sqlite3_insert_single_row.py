import sqlite3

connection = sqlite3.connect('movies.db') 
cursor = connection.cursor() 

# cursor.execute(''' INSERT INTO Movies VALUES('Taxi Driver', 'Martin Scorsese', 1976) ''') # Insert a row of data
cursor.execute(''' SELECT * FROM Movies ''') # Select all rows from the Movies table

print(cursor.fetchone()) # Fetch the first row

connection.commit()   
connection.close() 