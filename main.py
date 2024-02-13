def addToDO():
    """this function will add items to the To-Do list"""
    file = open("to-do.txt", "a", encoding = "utf-8")
    list_input = input("please enter the item you want to add: ")
    file.write(list_input + "\n")
    file.close()

def showList():
    """this function will show the items in To-Do list"""
    file = open("to-do.txt", "r", encoding = "utf-8")
    todo_list = file.read()
    print(todo_list)
    file.close()

def main():
    while True:
        print("type 1 to add an item to the list")
        print("type 2 to show the items in the list")
        print("type exit to terminate the programe")
        userInput = input("Choice: ")
        if userInput.upper() == "1":
            print(addToDO())
            

        elif userInput.upper() == "2":
            print("type 1 to show the list")
            print("type 2 to go back to the first choise")
            refuse = input("Choice: ")
            if refuse.upper() == "1":
                 print(showList())
            
            elif refuse.upper() == "2":
                print("Good bye.")

            else:
                print("please use one of the options.")

        
        elif userInput.lower() == "exit":
            break

        else:
            print("please use one of the options (1), (2) or (exit).")

print(main())