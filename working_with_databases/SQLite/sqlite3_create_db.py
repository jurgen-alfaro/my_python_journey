import sqlite3

connection = sqlite3.connect('movies.db') # Create a connection object if the database exists, if not, create a new database
cursor = connection.cursor() # Create a cursor object to execute SQL statements

cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Year INT)''') # Create a table if it does not exist

connection.commit() # Commit the changes to the database   
connection.close() # Close the connection to the database