import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

clock =sg.Text('',key="clock")

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo",key="todo")
add_button = sg.Button(size=5,image_source="add.png",
                       mouseover_colors="LightBlue2",
                       tooltip="Add Todo",key="Add")
list_box = sg.Listbox(values=functions.get_todos(),key='todos',
                      enable_events=True,size=[45,10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

window = sg.Window('My-To-do',
                   layout= [[clock],[label],[add_button,input_box],
                            [list_box,edit_button,complete_button]],
                            font=('Helvetica',20))

while True:
    event, values = window.read (timeout=10)
    # print("Hello")
    window["clock"].update (value=time.strftime ("%b %d, %Y %H:%M:%S"))
    # print(1,event)
    # print(2, values)
    # print(3, values['todos'])
    match event:
            case "Add":
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update (values=todos)

            case "Edit":
                try:
                    todos_to_edit = values['todos'][0]
                    new_todo = values['todo']

                    todos = functions.get_todos ()
                    index = todos.index (todos_to_edit)
                    todos[index] = new_todo
                    functions.write_todos (todos)
                    window['todos'].update (values=todos)
                except IndexError:
                    sg.Popup ("please select an item first")


            case 'Complete':
              try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos (todos)
                window['todos'].update (values=todos)
                window['todo'].update (value='')
              except IndexError:
                sg.Popup ("please select an item first")
            case "Exit":
                      break
            case 'todos':
                window['todo'].update (value=values['todos'][0])

            case sg.WIN_CLOSED:
                break





window.close()
