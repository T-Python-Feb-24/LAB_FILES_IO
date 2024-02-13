file =open ("to_do.txt", "+a", encoding="utf-8")
def main():
    while True:
        add_choice=input("Do you want to add a new To-Do item? y/n :")
        if add_choice=="y":
            ToDo_item=input("Enter TO-Do item :") 
            file.write(ToDo_item +"\n")
        elif add_choice=="n":
          print_items=input("Do you want to list your To-Do items? y/n :")
          if print_items =="y":
            file.seek(0)
            read = file.read()
            print(read)
        elif add_choice== "exit":
            print("Thank you for using the To-Do program, come back again soon")
            file.close()
           
            break
   
main()