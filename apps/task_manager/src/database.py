from os import path
from sqlalchemy import create_engine, text
from models import Base, Task

curr_dir = path.dirname(path.abspath(__file__))
db_path = f"sqlite:///{path.join(curr_dir, '../db/task_manager.db')}"

engine = create_engine(db_path, echo=True)

with engine.connect() as connection:
    result = connection.execute(text("SELECT 'Connected to database...'"))
    print(result.all())


# Create tables
print("Creating tables...")
Base.metadata.create_all(bind=engine)
