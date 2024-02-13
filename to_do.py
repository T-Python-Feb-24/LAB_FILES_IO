while True:
    try:
        
        print('Do you want to add a new To-Do item? Answer "y" for yes and "n" for no, or enter "exit" to exit.')
        choice = input('Write your answer here: ')

        if choice.lower() == 'y':
            with open("todo.txt", mode="a+", encoding="utf-8") as todo_file:
                user_input = input('You can type your new To-Do item here: ')
                todo_file.write(user_input + '\n')

        elif choice.lower() == 'n':
            print('Do you want to list your To-Do items? Answer "y" for yes and "n" for no.')
            list_choice = input('Write your answer here: ')

            if list_choice.lower() == 'y':
                with open('todo.txt', mode='r', encoding='utf-8') as todo_file:
                    #                 .strip() removing white spaces and '\n' 
                    todo_items = [line.strip() for line in todo_file.readlines()]
                    for item in todo_items:
                        print(item)

            elif list_choice.lower() == 'n':
                pass
            else:
                print('Please enter a valid answer!')
        elif choice.lower() == 'exit':
            print('Thank you for using the To-Do program. Come back again soon!')
            break
        else:
            print('Wrong answer. Please try again.')
    except FileNotFoundError:
        print('the file is not found try again.. ')
