# todos = []
from functions import get_todos, write_todos
import time

now = time.strftime ("%b %d,%Y %H:%M:%S")
print(f"It is %s" % now)


while True:
    # Get user input and strip space chars from it
    user_action = input ("Type add,show,edit,complete or exit: ")
    user_action = user_action.strip ()
    if user_action.startswith ('add'):
        todo = user_action[4:]

        # Reading and appending the file
        # file = open("file/todos.txt", 'r')
        # todos = file.readlines()
        # file.close()
        # context Manager
        todos = get_todos ()

        todos.append (todo + "\n")

        # writing to the file
        # file = open('file/todos.txt', 'w')
        # file.writelines(todos)
        # file.close()
        write_todos (todos)

    elif user_action.startswith ("show"):
        # file = open('file/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = get_todos ()

        for index, item in enumerate (todos):
            item = item.strip ("\n")
            row = f"{index}-{item}"
            print (row)
    elif user_action.startswith ("edit"):
        try:
            number = int (user_action[5:])
            number = number - 1

            todos = get_todos ()

            new_todo = input ("Enter the new_item: ")
            todos[number] = new_todo + "\n"

            write_todos (todos)
        except ValueError:
            print ("Your command is not valid")
            continue
            # user_action = input("Type add,show,edit,complete or exit: ")
            # user_action = user_action.strip()


    elif user_action.startswith ("complete"):
        try:
            number = int (user_action[9:])
            todos = get_todos ()
            index = number - 1
            todo_to_remove = todos[index].strip ("\n")
            todos.pop (index)

            write_todos (todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print (message)
        except IndexError:
            print ("There is no item with that number: ")
            continue
    elif user_action.startswith ("exit"):
        break
    else:
        print ("cannot be valid")
print ("Bye")
