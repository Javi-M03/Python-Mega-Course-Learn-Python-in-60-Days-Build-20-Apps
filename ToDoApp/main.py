while True:
    user_action = input("Type add, show, edit, complete and exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        with open('./ToDoApp/todos.txt','r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('./ToDoApp/todos.txt','w') as file:
            file.writelines(todos)

    elif  user_action.startswith('show'):
        with open('./ToDoApp/todos.txt','r') as file:
            todos = file.readlines()

        for (index,item) in enumerate(todos):
            item =  item.strip('\n')
            row=f"{index+1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number -1 
            with open('./ToDoApp/todos.txt','r') as file:
                todos =  file.readlines()

            new_todo = input("Enter new To Do: ")
            todos[number] = new_todo + '\n'
            
            with open('./ToDoApp/todos.txt','w') as file:
                file.writelines(todos)
        except ValueError:
            print('Your command is not valid')
            continue


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            with open('./ToDoApp/todos.txt','r') as file:
                todos =  file.readlines()
            index = number -1
            todoToRemove = todos[index].strip('\n')
            todos.pop(index)
            
            with open('./ToDoApp/todos.txt','w') as file:
                file.writelines(todos)
            
            message = f"Todo {todoToRemove} was remove from the list."
            print(message)
        except IndexError:
            print('There is no item with that number')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid!")
print("Bye!")
