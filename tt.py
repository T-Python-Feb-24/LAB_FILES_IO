while True:
    user_input=input("do you want to add a new To-Do item Answer by y for yes and n for no: ")
    if user_input=="y":
        user2=input("What is the type for ur to_do Item? ")
        with open("to_do.txt","a+")as file:
         file.write(user2 + "\n")
    elif user_input=="n":
        user1=input("do you want to list your To-Do items? answer y for yes and n for no: ")
        if user1=="y":
           with open("to_do.txt","r")as file:
              read=file.read()
              print(read)
    elif user_input == "exit":
        print("thank you for using the To-Do program, come back again soon")
        break
    

    


