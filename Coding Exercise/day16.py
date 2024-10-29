import FreeSimpleGUI as sg

label_feet = sg.Text("Enter Feet:")
input_box_feet = sg.InputText(tooltip="Enter Feet:")
label_inches = sg.Text("Enter inches:")
input_box_inches = sg.InputText(tooltip="Enter innches:")
add_button = sg.Button("Convert")

window = sg.Window('Convertor',layout=[[label_feet,input_box_feet],[label_inches,input_box_inches] ,[add_button]])
window.read()
window.close()

