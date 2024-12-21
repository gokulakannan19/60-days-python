import FreeSimpleGUI as sg
from modules import functions

label = sg.Text("Type in a Todo")
input_text = sg.InputText(tooltip="Enter a Todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_text, add_button]],
                   font=("Helvitica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()