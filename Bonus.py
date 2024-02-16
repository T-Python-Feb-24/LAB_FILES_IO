import json
from datetime import datetime

def add_new_task():
    title = input("Type your task title: ")
    date_time = datetime.now().strftime("%d-%b-%Y %H:%M:%S")
    done = False
    new_task = {"title": title, "date_time": date_time, "done": done}
    with open("to_do.json", "r+", encoding="UTF-8") as todo:
        try:
            data = json.load(todo)
        except json.JSONDecodeError:
            data = []
        data.append(new_task)
        todo.seek(0)
        json.dump(data, todo, indent=4)
        print("New task added successfully.\n")

def list_tasks():
    with open("to_do.json", "r", encoding="UTF-8") as todo:
        data = json.load(todo)
        for i, task in enumerate(data, start=1):
            done_status = "DONE" if task["done"] else "NOT DONE"
            print(f"{i}- {task['title']} - {task['date_time']} - {done_status}\n")

def mark_as_done(title):
    with open("to_do.json", "r+", encoding="UTF-8") as todo:
        data = json.load(todo)
        for task in data:
            if task["title"] == title:
                task["done"] = True
                print("Task marked as done.\n")
                todo.seek(0)
                todo.truncate()
                json.dump(data, todo, indent=4)
                break
        else:
            print("Task not found.\n")

def search_task(title):
    with open("to_do.json", "r", encoding="UTF-8") as todo:
        data = json.load(todo)
        for task in data:
            if task["title"] == title:
                done_status = "DONE" if task["done"] else "NOT DONE"
                print(f"{task['title']} - {task['date_time']} - {done_status}\n")
                break
        else:
            print("Task not found.\n")

while True:
    print("------ Welcome to ToDo List Program ------")
    print("1. Add a new To-Do List")
    print("2. List your To-Do List")
    print("3. Mark a specific Task as Done")
    print("4. Search in your tasks using the title")
    print("5. Exit")

    user_input = input("Choose an option: ")
    match user_input:
        case "1":
            add_new_task()
        case "2":
            print("------ Your ToDo List ------")
            list_tasks()
        case "3":
            list_tasks()
            title = input("Enter the title of the task you want to mark as done: ")
            mark_as_done(title)
        case "4":
            title = input("Enter the title of the task you want to search: ")
            search_task(title)
        case "5":
            print("--------------------------------")
            print("thank you for using the To-Do program, come back again soon")
            break
        case _:
            print("Invalid input. Please choose correct.")