while True:
    user_action = input("Type add, show, edit, complete and exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        with open('./ToDoApp/todos.txt','r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('./ToDoApp/todos.txt','w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('./ToDoApp/todos.txt','r') as file:
            todos = file.readlines()

        for (index,item) in enumerate(todos):
            item =  item.strip('\n')
            row=f"{index+1}-{item}"
            print(row)
    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number -1 
        with open('./ToDoApp/todos.txt','r') as file:
            todos =  file.readlines()

        new_todo = input("Enter new To Do: ")
        todos[number] = new_todo + '\n'
        
        with open('./ToDoApp/todos.txt','w') as file:
            file.writelines(todos)
    elif 'complete' in user_action:
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

    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid!")
print("Bye!")
