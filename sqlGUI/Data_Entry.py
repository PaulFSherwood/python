import PySimpleGUI as sg
import pandas as pd

# Add some color to the window
sg.theme('DarkTeal9')

EXCEL_FILE = 'Data_Entry.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')],
    [sg.Text('City', size=(15,1)), sg.InputText(key='City')],
    [sg.Text('Favorite Color', size=(15,1)), sg.Combo(['Green', 'Blue', 'Red'], key='Favorite Color')],
    [sg.Text('I speak', size=(15,1)),
                            sg.Checkbox('German', key='German'),
                            sg.Checkbox('Spanish', key='Spanish'),
                            sg.Checkbox('English', key='English')],
    [sg.Text('No. of Children', size=(15,1)), sg.Spin([i for i in range(0, 16)],
                                                        initial_value=0, key='Children')],
    [sg.Submit(), sg.Exit()]
]
form_layout = [
    [sg.Text("Enter Name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(20,1))],
    [sg.Text("Enter Address:"), sg.Input(key='-ADDRESS-', do_not_clear=True, size=(20,1))],
    [sg.Text("Enter Phone Number:"), sg.Input(key='-PHONE_NUMBER-', do_not_clear=True, size=(20,1))],
    [sg.Button('Submit Contact Info')]    
]

window = sg.Window('Simple data entry form', layout)

# clears all the text fields
def clear_input():
    for key in values:
        window[key]('')
    return None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        #print(event, values)
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data Saved!')
        clear_input()

window.close()