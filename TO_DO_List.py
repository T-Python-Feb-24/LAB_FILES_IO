
to_do_items = open("to_do.txt" ,"a+", encoding="utf_8" )


while True: 
    user_choice = input("Do you want to add a new To-Do item? (answer \"y\" for yes and \"n\" for no.) ")
    if user_choice == "y":
        task = input("Type in your new To-Do item please : ")
        to_do_items.writelines(task + "\n")
    elif user_choice == "n":
        choice =  input("Do you want to list your To-Do items ? ")
        if choice =="y":
            to_do_items.seek(0)
            tasks = to_do_items.read()
            to_do_items.close()
            print(tasks)
    elif user_choice == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break
    else:
        print("invalid")


# # (to_do_items == "y")
# # to_do_items.close()

#     #   print(file) 
# # i think i should use while loop for this quastion since it's a multiple options 

# input("Do you want to add a new To-Do item? (answer \"y\" for yes and \"n\" for no.) ")