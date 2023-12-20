import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///movies.db', echo=True) 
metadata = sqlalchemy.MetaData() # metadata object to store information about tables

movies_table = sqlalchemy.Table("Movies", metadata, # create table
                                sqlalchemy.Column("title", sqlalchemy.Text),
                                sqlalchemy.Column("director", sqlalchemy.Text),
                                sqlalchemy.Column("year", sqlalchemy.Integer))

metadata.create_all(engine) # create table in database

with engine.connect() as conn: 
    for row in conn.execute(sqlalchemy.select(movies_table)): # select all rows from table
        print(row)