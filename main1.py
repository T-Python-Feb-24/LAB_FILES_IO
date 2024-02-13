file2=open("todo1.txt" , "a+" , encoding="utf-8")

while True:
 print("\n Do you want to add a new To-Do task ? ")
 userinput=input("Please enter 'y' for yes or 'n' for no or write 'q' to exit : ")

 match userinput:
    case "y":
        task=input("Type your new To-Do task : ")
        file2.writelines( "\n" + task)
    case "n":
        print("\n Do you want to list your To-Do items ?")
        todolist=input(" y for yes n for no :")
        
        if todolist == "Y" or todolist == "y":
            file2.seek(0)
            v=file2.read()
            file2.close()
            print(v) 
    case "q":
        print(" \n List closed , good bye ")
        break
    case _:
        print("\n invalid value")
  
   
