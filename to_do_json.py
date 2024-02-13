import json
task_data = {
    'title':'title',
    'due_date':'1212-12-12 10:00:00',
    'done':False
}
def add_task(title, due_date, done):
    if title in task_data:
        try:
            with open('todo.json', mode='r', encoding='utf-8') as todo_file:
                task_data = json.load(todo_file)

            todo_file.append(title, due_date, done)

            with open('todo.json', 'w') as todo_file:
                json.dump(task_data, todo_file, indent=4)

            print(f"User data appended to {todo_file} successfully!")

        except FileNotFoundError:
            with open(todo_file, mode='w', encoding='utf-8') as todo_file:
                json.dump([task_data], todo_file, indent=4)

            print(f"New {todo_file} created with user data.")





while True:
    print('Do you want to perform an action? Enter "add", "mark", "search", or "exit".')
    choice = input('Write your answer here: ')

    if choice.lower() == 'add':
        title:str = input('enter your task: ')
        due_date:str = input('Enter the due date and time (YYYY-MM-DD HH:MM:SS): ')
        done = False
    elif choice.lower() == 'mark':
        pass
    elif choice.lower() == 'search':
        pass
    elif choice.lower() == 'exit':
        print('Thank you for using the To-Do program. Come back again soon!')
        break
    else:
        print('Invalid choice. Please try again.')