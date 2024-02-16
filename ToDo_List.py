print("------ Welcome to ToDo List Program ------")
with open("to_do.txt", "a+", encoding="UTF-8") as todo:

   while True:

      user_input = input("do you want to add a new To-Do item? (y/yes, n/no, e/exit): ")
      match user_input:
         case "y":
            note = input("Type your tasks: ")
            todo.writelines(note + "\n")
         case "n":
            note2 = input("do you want to list your To-Do items ? (y/n): ")
            if note2 == 'y':
               todo.seek(0)
               content = todo.read()
               print(content)
            elif note2 == 'n':
               continue
         case "e":
            print("--------------------------------")
            print("\nthank you for using the To-Do program, come back again soon")
            break
         case _:
            print("Invalid input. please choose correct.")