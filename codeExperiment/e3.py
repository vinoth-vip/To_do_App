import PySimpleGUI as sg
from converters import convert

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")
exit_button = sg.Button("Exit", key="Exit")

windows = sg.Window('Converter',
                    layout=[[feet_label, feet_input],
                            [inches_label, inches_input],
                            [button, exit_button, output_label]])


while True:
    event, values = windows.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    windows["output"].update(value=f"{result} m", text_color="Red")

windows.close()

