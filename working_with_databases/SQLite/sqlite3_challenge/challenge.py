import sqlalchemy

database_url = 'sqlite:///challenge.db'
engine = sqlalchemy.create_engine(database_url, echo=True)

users_to_insert = [
    {"Name": "John", "Last_Name": "Smith", "Email_Address": "john_smith@gmail.com"},
    {"Name": "Jane", "Last_Name": "Doe", "Email_Address": "jane_doe@gmail.com"},
    {"Name": "Kevin", "Last_Name": "Gomez", "Email_Address": "kev_gom@hotmail.com"},
    {"Name": "Linda", "Last_Name": "Johnson", "Email_Address": "lin_johnson@yahoo.com"},
    {"Name": "Peter", "Last_Name": "Williams", "Email_Address": "p_williams@hotmail.com"}
]

metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table("Users", metadata,
                               sqlalchemy.Column("User_Id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
                               sqlalchemy.Column("Name", sqlalchemy.String),
                               sqlalchemy.Column("Last_Name", sqlalchemy.String),
                               sqlalchemy.Column("Email_Address", sqlalchemy.String))

metadata.create_all(engine)

with engine.connect() as conn:
    conn.execute(sqlalchemy.insert(users_table).values(users_to_insert))
    for row in conn.execute(sqlalchemy.select(users_table)):
        print(row)
    conn.commit()