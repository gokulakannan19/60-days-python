import FreeSimpleGUI as sg
from modules import functions

label = sg.Text("Type in a Todo")
input_text = sg.InputText(tooltip="Enter a Todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label], [input_text, add_button]])
window.read()
window.close()