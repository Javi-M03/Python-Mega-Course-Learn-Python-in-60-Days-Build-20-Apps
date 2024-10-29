import FreeSimpleGUI as sg

sg.theme("Dark")
label_feet = sg.Text("Enter Feet:")
input_box_feet = sg.InputText(tooltip="Enter Feet:", key= "feet")
label_inches = sg.Text("Enter inches:")
input_box_inches = sg.InputText(tooltip="Enter innches:", key="inches")
add_button = sg.Button("Convert")
output_label = sg.Text("", key="output")
exit_button = sg.Button("Exit")


window = sg.Window('Convertor',layout=[[label_feet,input_box_feet],
                                       [label_inches,input_box_inches],
                                       [add_button,output_label],
                                       [exit_button]])
while True:
    event,values=window.read()

    feet_to_meter = float(values['feet'])*0.3048
    inches_to_m = float(values['inches'])*0.0254
    meter = feet_to_meter + inches_to_m
    window["output"].update(value=f"{meter} m", text_color="white")

    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break


window.close()

