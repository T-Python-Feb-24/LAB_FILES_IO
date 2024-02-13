to_do_file = open("To-Do list.txt", "a+", encoding="utf-8")
print("-------------------- Welcome to your To-Do list ---------------------")

while True: 
    try:
        # Q1. ask to add new task or exit
        user_choice_to_add = input("Do you want to add a new To-Do item (y:yes / n:no or e:exit)? ")

        if user_choice_to_add == "y" or user_choice_to_add == "Y": # yes to add new task

            # Q2. ask to insert the task
            add_item = input("Add new task to your list! \n  - ")
            to_do_file.write("✓ " + add_item + "\n")
        elif user_choice_to_add == "n" or user_choice_to_add == "N": # no to new task

            while True:
                try:
                    # Q3. ask to present the to-do list
                    show_items = input("Do you want to list your To-Do items(y:yes / n:no) ?") 
                    if show_items == "y" or show_items == "Y": # yes to show the to-do list
                        print("--------------------------- MY TO-DO LIST ---------------------------")
                        to_do_file.seek(0)
                        read_to_do_file = to_do_file.read()
                        #to_do_file.close()
                        print(read_to_do_file)
                        print("---------------------------------------------------------------------")   
                        break
                    elif show_items == "n" or show_items == "N": # no for pass 
                        break  # to back to the Q1
                    else:
                        raise Exception("Invalid choice. Try again!(y:yes / n:no)")
                        
                except Exception as e:
                    print(e)      
        elif user_choice_to_add == "e" or user_choice_to_add == "E": #to exit
            print("\n    Thank you for using the To-Do program, come back again soon    ")
            print("---------------------------------------------------------------------")
            break
        else:
            raise Exception("Invalid choice. Try again!(y:yes / n:no or e:exit)")
    except Exception as e:
        print(e)
to_do_file.close()




    


