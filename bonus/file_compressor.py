import FreeSimpleGUI as sg
from modules import zip_creator

label1 = sg.Text("Select Files to compress")
input1 = sg.InputText()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select Destination folder")
input2 = sg.InputText()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")

output = sg.Text(key="output", text_color="green")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output]])

while True:
    event, values = window.read()
    # print(event)
    # print(values)
    match event:
        case "Compress":
            filepaths = values["files"].split(";")
            dest_dir = values["folder"]
            zip_creator.make_archive(filepaths, dest_dir)
            window["output"].update(value="Compression successful")
        case sg.WIN_CLOSED:
            break

window.close()