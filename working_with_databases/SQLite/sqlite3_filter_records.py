import sqlite3

connection = sqlite3.connect('movies.db') 
cursor = connection.cursor() 

release_year = (1985,)
cursor.execute(''' SELECT * FROM Movies WHERE year=? ''', release_year) # Select all rows from the Movies table where the year is 1985

print(cursor.fetchall()) # Fetch all rows of a query result, returning a list

connection.commit()   
connection.close() 