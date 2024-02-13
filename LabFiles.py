def write_toDO_item (new):
    with open("to_do.txt","a+",encoding="utf-8") as file :
        writeFile = file.write(f"{new} \n")
    return writeFile

def read_toDo_items():
    with open("to_do.txt","a+",encoding="utf-8") as file :
        file.seek(0)
        readFile = print(file.read())
    return readFile

 
def main():
    print("Welcome to the to-do list program !")
    while True:
            askUser = input("Do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no.")
            if askUser == 'n':
                askTOcheck = input("Do you want to list your To-Do items ?answer 'y' for yes and 'n' for no")
                if askTOcheck == 'n':
                    exit = input("pleas write exit !")
                    if exit == 'exit':
                        print("thank you for using the To-Do program, come back again soon")
                        break
                    else: 
                        print("Pleas Enter Valid Value!")
                elif askTOcheck == 'y':
                    read_toDo_items()
                else : 
                    print("Pleas Enter Valid Value !!")       
            elif askUser == 'y':     
                appendNew = input("write your To Do item !")
                write_toDO_item(appendNew) 
                print("A new to-do item has been added successfully!")    
            else : 
                    print("Pleas Enter Valid Value!!!") 
        

main() 

                
