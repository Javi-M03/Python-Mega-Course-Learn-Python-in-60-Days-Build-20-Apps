while True:
    user_action = input("Type add, show, edit, complete and exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('./ToDoApp/todos.txt','r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('./ToDoApp/todos.txt','w') as file:
                file.writelines(todos)

        case 'show':
            with open('./ToDoApp/todos.txt','r') as file:
                todos = file.readlines()

            for (index,item) in enumerate(todos):
                item =  item.strip('\n')
                row=f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number -1 
            with open('./ToDoApp/todos.txt','r') as file:
               todos =  file.readlines()

            new_todo = input("Enter new To Do: ")
            todos[number] = new_todo + '\n'
            
            with open('./ToDoApp/todos.txt','w') as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            with open('./ToDoApp/todos.txt','r') as file:
               todos =  file.readlines()
            index = number -1
            todoToRemove = todos[index].strip('\n')
            todos.pop(index)
            
            with open('./ToDoApp/todos.txt','w') as file:
                file.writelines(todos)
            
            message = f"Todo {todoToRemove} was remove from the list."
            print(message)

        case 'exit':
            break
print("Bye!")
