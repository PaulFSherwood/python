from json import tool
import PySimpleGUI as sg
# import pandas as pd

contact_information_array = [['Amith', '31 Main St.', '66679090']]
headings = ['Full Name', 'Address', 'Phone Number']

instructions_layout = [
    [sg.Text("Enter contact information in the 'New Contact' tab an dview all contacts in the 'Contacts Tab'.")]
]

form_layout = [
    [sg.Text("Enter Name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(20,1))],
    [sg.Text("Enter Address:"), sg.Input(key='-ADDRESS-', do_not_clear=True, size=(20,1))],
    [sg.Text("Enter Phone Number:"), sg.Input(key='-PHONE_NUMBER-', do_not_clear=True, size=(20,1))],
    [sg.Button('Submit Contact Info')]    
]

table_layout = [
    [sg.Table(values=contact_information_array, headings=headings, max_col_width=35,
            auto_size_columns=True,
            display_row_numbers=True,
            justification='right',
            num_rows=10,
            key='-TABLE-',
            row_height=35,
            tooltip='Conctacts Table')]
]

tab_group = [
                [sg.TabGroup(
                    [[
                        sg.Tab('Instructions',instructions_layout, background_color='Green', element_justification='right'),
                        sg.Tab('Contact Information', form_layout, background_color='Yellow'),
                        sg.Tab('All Contacts', table_layout, background_color='Pink')]],
                        tab_location='centertop',
                        title_color='White',
                        tab_background_color='Purple',
                        selected_title_color='Green',
                        selected_background_color='Yellow',
                        border_width=5),
                        sg.Button('Exit')
]]

window = sg.Window('Application Form', tab_group)

while True:
    event,values=window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Submit Contact Info":
        contact_information_array.append([values['-NAME-'],values['-ADDRESS-'],values['-PHONE_NUMBER-']])
        window['-TABLE-'].update(values=contact_information_array)

window.close()