import json #الحل ناقص برجع ابحث اكثر عن Json
from datetime import datetime 
with open("To_Do.json","a+")as file:
    while True:
        user_input=input("do you want to add a new To-Do item Answer by y for yes and n for no: ")
        if user_input=="y":
            title=input("Enter the name of task: ")
            date_time=float (input("Enter the date and time:ex yyyy-mm-dd  hh/mm: "))
            done=False
            with open("To_Do.json","a+")as file:
                toDo={"title:" ,title ,"date_time: ", date_time, "Done: " ,done}
                file.write("\n")
        elif user_input=="n":
            user1=input("do you want to list your To-Do items? answer y for yes and n for no: ")
            if user1=="y":
                with open("To_Do.json","r")as file:
                    read=file.read()
                    print(read)
        elif user_input == "exit":
          print("thank you for using the To-Do program, come back again soon")
        break




