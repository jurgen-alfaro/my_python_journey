from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()
    due_date: Mapped[datetime] = mapped_column()
    priority: Mapped[int] = mapped_column(default=1)
    
    def __repr__(self):
        return f"<Task (id={self.id}, title={self.title}, priority={self.priority})>"

class TaskManager:
    def __init__(self, session):
        self.session = session
    
    def add_task(self, title, description, due_date, priority) -> Task:
        task = Task(title=title, description=description, due_date=due_date, priority=priority)
        self.session.add(task)
        self.session.commit()
        return task
    
    def list_all_tasks(self):
        return self.session.query(Task).all()
