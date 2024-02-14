import json
import datetime 

'''
حلي ناقص باقي اكمله
'''

while True:
        try:
            print("type '1' to add new to-do item type '2' for no type '3' to show your list")
            ask=input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no or 'exit' for close the program: ")

            # If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
            if ask.lower()=="y":
                file=open("to_do","a+", encoding="utf-8")
                ask_user=input("type your new To-Do item:")
                
                file.write(ask_user+"\n")
                file.close()
            # If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.
            elif ask.lower()=="n":
                ask_user=input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for exit: ")
                # If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
                if ask_user.upper()=="Y":
                    file=open("to_do","r")
                    read=file.read()
                    print(read)
                elif ask_user.upper()=="N":
                    print("thank you for using the To-Do program, come back again soon")
                    break
                elif ask_user.upper()=="3":
                    file=open("to_do","r")
                    read=file.read()
                    print(read)
                else:
                    print("please enter between 'y' or 'n':")
            elif ask.lower()=="exit":
                print("thank you for using the To-Do program, come back again soon")
                break
            else:
                print("please enter between 'y' or 'n' or 'exit':")
        except Exception:
            print("some thing went worng")

        