import FreeSimpleGUI as sg
import time

sg.theme('DarkAmber')

clock = sg.Text('',key="clock")

label1 = sg.Text("Enter feet: ")
input1 = sg.InputText(tooltip="Enter feet", key="feetData")
feet_button = sg.Button("Add", key="feet")

label2 = sg.Text("Enter inches: ")
input2 = sg.InputText(tooltip="Enter inches", key="inchesData")
inches_button = sg.Button("Add", key="inches")


convert_button = sg.Button("Convert", key="convert")
output_label = sg.Text(key="output", text_color="green")

exit_button = sg.Button("Exit")

window = sg.Window("Convertor", 
                   layout=[[clock], [label1, input1, feet_button], 
                           [label2, input2, inches_button],
                           [convert_button, exit_button, output_label]])
while True:
        event, values = window.read()
        
        if event in (sg.WINDOW_CLOSED, None):
            break
        else:
            window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
        try:
            if event == "Exit":
                break
            if event == "feet":
                feet = float(values['feetData'])
            if event == "inches":
                inches = float(values['inchesData'])
            if event == "convert":
                feet = float(values['feetData'])
                inches = float(values['inchesData'])
                total_inches = (feet * 12) + inches
                cm = total_inches * 2.54
                window['output'].update(value=f"{cm} cm")
            if not values['feetData'] or not values['inchesData']:
                raise ValueError
        except ValueError:
            sg.popup("Please enter a number.", font=('Helvetica', 16))
window.close()