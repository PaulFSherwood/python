import PySimpleGUI as sg

# Add some color to the window
sg.theme('DarkTeal9')

layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')],
    [sg.Text('Favorite Color', size=(15,1)), sg.Combo(['Green', 'Blue', 'Red'], key='Favorite Color')],
    [sg.Text('I speak', size=(15,1)),
                            sg.Checkbox('German', key='German'),
                            sg.Checkbox('Spanish', key='Spanish'),
                            sg.Checkbox('English', key='English')],
    [sg.Text('No. of Children', size=(15,1)), sg.Spin([i for i in range(0, 16)],
                                                        initial_value=0, key='Children')],
    [sg.Submit(), sg.Exit()]
]

window = sg.Window('Simple data entry form', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        print(event, values)
window.close()