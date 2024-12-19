import FreeSimpleGUI as sg

label1 = sg.Text("Enter Feet")
input1 = sg.InputText()

label2 = sg.Text("Enter Feet")
input2 = sg.InputText()

convert_button = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button]])

window.read()
window.close()