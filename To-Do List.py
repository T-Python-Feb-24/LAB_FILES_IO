print("< Welocome to my To do list program > ")
while True:
    print("  do you want to add a new To-Do item?  ")
    choice=input("press 'y' for yes, press 'n' for no, press '0' to exit -> ") 
    if choice.lower() == "y":
        with open('to_do.txt', 'a') as file:
                todo_item = input("Enter your new To-Do item: ")
                file.write(todo_item + '\n')
        print("To-Do item added successfully.")
    elif choice.lower() =="n":
        choice2=input("do you want to list your To-Do items yes or no y/n -> ")
        if choice2 == "y":
            try:
                with open('to_do.txt', 'r') as file:
                    todo_items = file.readlines()
                    print("Your To-Do list:")
                    for item in todo_items:
                        print(item.strip())
            except FileNotFoundError:
                    print("To-Do list is empty.")
    elif choice == 0:
        print("Thank you for using the To-Do program. Come back again soon!")
        break
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")

