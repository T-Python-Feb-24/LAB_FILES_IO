def add_todo():
    todo_item = input("Enter your new To-Do item: ")
    with open('to_do.txt', 'a',encoding="utf-8") as file:
        file.write(todo_item + '\n')

def list_todo():
    with open('to_do.txt', 'r', encoding="utf-8") as file:
        todo_list = file.readlines()
        for item in todo_list:
            print(item.strip())

def main():
    while True:
        user_input = input("Do you want to add a new To-Do item? (y/n): ")
        if user_input.lower() == 'y':
            add_todo()
        elif user_input.lower() == 'n':
            user_input = input("Do you want to list your To-Do items? (y/n): ")
            if user_input.lower() == 'y':
                list_todo()
            else:
                exit_input = input(" press 'e' to exit, or Enter to continue: ")
                if exit_input.lower() == 'e' or exit_input.lower() == 'exit':
                    print("Thank you for using the To-Do program. Come back again soon!")
                    break

if __name__ == "__main__":
    main()

    