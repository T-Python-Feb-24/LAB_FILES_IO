



      
while True:
    response=input("Do you want to add a new To-Do items?(y\n):")
    if response.lower()=="y":
        To_Do_item=open("to_do.txt","a+",encoding="utf-8")
        new_item=input("Enter your new-To Do item :")
        To_Do_item.write(new_item)
        To_Do_item.close()
    elif response.lower()== "n":
        response=input("Do you want to list your To-Do items?(y\n):")
    if response.lower()=="y":
         To_Do_item=open("to_do.txt","r",encoding="utf-8")
         task = To_Do_item.read()
         To_Do_item.close()
         print(task)
    else:
         print("Thank you for using the To-Do program. Came back agine soon")
         break
