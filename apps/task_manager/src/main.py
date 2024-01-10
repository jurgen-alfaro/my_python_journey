from database import *
from sqlalchemy.orm import Session 
from models import TaskManager
from datetime import datetime

session = Session(bind=engine)
task_manager = TaskManager(session)

def main():
    
    while True:
        print_menu()
        option = int(input("Enter your choice: "))
            
        if option == 0: 
            print("Closing program... Bye 👋")
            exit(0)
        elif option == 1:
            print_add_task_menu()
        elif option == 4:
            print_all_tasks()
        
        
def print_menu():
    print("""
Choose an operation from the list:
1. Add a task
2. Edit a task
3. Delete a task
4. List all tasks
5. List all tasks by priority
6. List all tasks by due date
0. Exit
""")
    
def print_add_task_menu():
    print("Add task menu")
    title: str = input("Enter title: ")
    description: str = input("Enter description: ")
    due_date = datetime.strptime(input("Enter due date (YYYY-MM-DD): "), "%Y-%m-%d")
    priority = int(input("Enter priority: "))
    
    task_manager.add_task(title, description, due_date, priority)
    print("Task added successfully!")
    

def print_all_tasks():
    tasks = task_manager.list_all_tasks()
    for task in tasks:
        print(task)

if __name__ == "__main__":
    main()