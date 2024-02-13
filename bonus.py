import json
import datetime

def loadList():
    """this function will load existing to-do list."""
    try:
        with open("todo_list.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def saveList(todo_list):
    """this function will save the updated to-do list."""
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file, indent=4)

def addToDo():
    """this function will add items to the To-Do list"""
    title = input("Enter the task title: ")
    date_str = input("Enter the due date (YYYY-MM-DD HH:MM:SS): ")
    try:
        due_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")
        return

    todo_item = {
        "title": title,
        "due_date": due_date.strftime("%Y-%m-%d %H:%M:%S"),
        "done": False
    }

    todo_list = loadList()
    todo_list.append(todo_item)
    saveList(todo_list)
    print(f"Task '{title}' added successfully!")

def showList():
    """this function will show the items in To-Do list"""
    todo_list = loadList()
    for index, item in enumerate(todo_list, start=1):
        status = "DONE" if item["done"] else "NOT DONE"
        print(f"{index}- {item['title']} - {item['due_date']} - {status}")

def done():
    """this function will mark a task in the list as done."""
    todo_list = loadList()
    showList()
    try:
        task_index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_index < len(todo_list):
            todo_list[task_index]["done"] = True
            saveList(todo_list)
            print(f"Task '{todo_list[task_index]['title']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def searchList():
    """Search for tasks by title."""
    search_term = input("Enter the title to search for: ")
    todo_list = loadList()
    matching_tasks = [item for item in todo_list if search_term.lower() in item["title"].lower()]
    if matching_tasks:
        print("Matching tasks:")
        for task in matching_tasks:
            print(f"- {task['title']} - {task['due_date']}")
    else:
        print("No matching tasks found.")

def main():
    while True:
        print("type 1 to add an item to the list")
        print("type 2 to show the items in the list")
        print("type 3 mark an item as done")
        print("type 4 to search by title")
        print("type 5 to terminate the program")
        choice = input("Choice: ")

        if choice == "1":
            addToDo()
        elif choice == "2":
            showList()
        elif choice == "3":
            done()
        elif choice == "4":
            searchList()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
