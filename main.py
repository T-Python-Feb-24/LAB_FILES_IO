def addToDO():
    while True:
        userInput = input("do you want to add a new To-Do item? if yes enter (Y) if no enter (N), and (exit) to exit the program: ")
        if userInput.upper() == "Y":
            file = open("to-do.txt", "a", encoding = "utf-8")
            list_input = input("please enter your to-do list: ")
            file.write(list_input + "\n")
            file.close()
        
        elif userInput.upper() == "N":
            showList()
        
        elif userInput.lower() == "exit":
            break

        else:
            print("please use one of the options (Y), (N) or (exit).")

def showList():
    
    refuse = input("do you want to list your To-Do items ?if yes enter (Y) if no enter (N): ")
    if refuse.upper() == "Y":
        file = open("to-do.txt", "r", encoding = "utf-8")
        todo_list = file.read()
        print(todo_list)
        file.close()

    elif refuse.upper() == "N":
        print("Good bye.")

    else:
        print("please use one of the options (Y) or (N).")

def main():
    try:
        print(addToDO())
    except FileNotFoundError:
        print("the file does not exist.")
print(main())