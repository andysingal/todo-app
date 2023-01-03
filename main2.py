# todos = []
while True:
  # Get user input and strip space chars from it
       user_action = input("Type add,show,edit,complete or exit: ")
       user_action = user_action.strip()
       if "add" in user_action:
          todo = user_action[4:]

          # Reading and appending the file
          # file = open("file/todos.txt", 'r')
          # todos = file.readlines()
          # file.close()
          # context Manager
          with open("file/todos.txt", 'r') as file:
              todos = file.readlines()

          todos.append(todo + "\n")

          # writing to the file
          # file = open('file/todos.txt', 'w')
          # file.writelines(todos)
          # file.close()
          with open("file/todos.txt", 'w') as file:
              file.writelines(todos)

       elif "show" in user_action:
          # file = open('file/todos.txt', 'r')
          # todos = file.readlines()
          # file.close()

          with open("file/todos.txt", 'r') as file:
              todos = file.readlines()

          for index, item in enumerate(todos):
              item = item.strip("\n")
              row = f"{index}-{item}"
              print(row)
       elif "edit" in user_action:
          number = int(user_action[5:])
          number = number - 1

          with open("file/todos.txt", 'r') as file:
              todos = file.readlines()

          new_todo = input("Enter the new_item: ")
          todos[number] = new_todo + "\n"

          with open("file/todos.txt", 'w') as file:
                file.writelines(todos)

       elif "complete" in user_action:
            number = int(user_action[9:])
            with open("file/todos.txt", 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open("file/todos.txt", 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
       elif "exit" in user_action:
             break
       else:
           print("cannot be valid")
print("Bye")
