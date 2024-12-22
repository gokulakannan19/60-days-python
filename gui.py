import FreeSimpleGUI as sg
from modules import functions
import time

sg.theme("Black")

current_time = sg.Text("", key="clock")
label = sg.Text("Type in a Todo")
input_text = sg.InputText(tooltip="Enter a Todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[current_time],
                           [label], [input_text, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvitica", 20))

while True:
    event, values = window.read()
    print(event)
    window["clock"].update(value=time.strftime("%b, %d, %y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=functions.get_todos())

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=functions.get_todos())
            except IndexError:
                sg.popup("Select an item", font=("Helvitica", 20))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Select an item", font=("Helvitica", 20))
        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0].strip("\n"))

        case sg.WIN_CLOSED:
            break

window.close()