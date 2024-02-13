while True:
    try:
        user_input = input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no and exit.")
        if user_input.lower()  == "y" :
            user_input = input("write your task:")
            file = open("to_do.txt", mode="a", encoding="utf-8")
            file.write(user_input + "\n")
            file.close()
        elif user_input.lower() == "n":
            user_input = input ("ok,do you want to see your liste ?")
            if user_input.lower()  =="y":
                file = open("to_do.txt", mode="r", encoding="utf-8")
                to_do = file.read()
                print(to_do)
            elif user_input.lower()=="n":
                print("good bay")
                break
                
        if user_input.lower() == "exit":
                print("thank you for using the To-Do program, come back again soon")
                break
        
    except Exception:
        print("some thing want wrong")