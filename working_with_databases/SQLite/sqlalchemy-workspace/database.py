import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///movies.db', echo=True) # echo=True -> show all SQL commands

with engine.connect() as conn:
    result = conn.execute(sqlalchemy.text("SELECT * FROM Movies"))
    for row in result:
        print(row)
    