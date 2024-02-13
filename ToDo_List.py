'''
Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
   - Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
   - If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
   - If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.
   - If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
   - Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"
'''
print("------ Welcome to ToDo List Program ------")

while True:

   user_input = input("do you want to add a new To-Do item? (y/yes, n/no, exit): ")
   match user_input:
      case "y":
         note = input("Type your tasks: ")
         with open("to_do.txt", "a+", encoding="UTF-8") as todo:
            todo.writelines(note + "\n")
      case "n":
         note2 = input("do you want to list your To-Do items ? (y/n): ")
         if note2 == 'y':
            with open("to_do.txt", "r", encoding="UTF-8") as text:
               content = text.read()
               print(content)
         elif note2 == 'n':
            continue
      case _:
         print("--------------------------------")
         print("\nthank you for using the To-Do program, come back again soon")
         break