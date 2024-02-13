import json
from datetime import datetime

def load_todo_list():
    try:
        with open("to_do.json", mode="r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_todo_list(todo_list):
    with open("to_do.json", mode="w", encoding="utf-8") as file:
        json.dump(todo_list, file, indent=4)

def display_todo_list(todo_list):
    for index, task in enumerate(todo_list, start=1):
        status = "DONE" if task["done"] else "NOT DONE"
        print(f"{index}- {task['title']} - {task['date_time']} - {status}")

def mark_task_as_done(todo_list, task_index):
    if 0 < task_index <= len(todo_list):
        todo_list[task_index - 1]["done"] = True
        save_todo_list(todo_list)
        print("Task marked as done.")
    else:
        print("Invalid task index.")

def search_task_by_title(todo_list, title):
    found_tasks = [task for task in todo_list if title.lower() in task["title"].lower()]
    if found_tasks:
        print("Found tasks:")
        display_todo_list(found_tasks)
    else:
        print("No tasks found with that title.")

def add_task(todo_list):
    title = input("Enter the title of the task: ")
    date_time = input("Enter the date & time (YYYY-MM-DD HH:MM:SS): ")
    done = False
    todo_list.append({"title": title, "date_time": date_time, "done": done})
    save_todo_list(todo_list)
    print("Task added.")

def main():
    todo_list = load_todo_list()
    
    while True:
        print("\n1- Add a new task")
        print("2- Display To-Do list")
        print("3- Mark a task as done")
        print("4- Search for a task by title")
        print("5- Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            display_todo_list(todo_list)
        elif choice == "3":
            task_index = int(input("Enter the index of the task to mark as done: "))
            mark_task_as_done(todo_list, task_index)
        elif choice == "4":
            title = input("Enter the title to search for: ")
            search_task_by_title(todo_list, title)
        elif choice == "5":
            print("Thank you for using the To-Do program, come back again soon.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
