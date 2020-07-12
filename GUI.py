import PySimpleGUI as sg

from Caesar_Cipher import encrypt, decipher

sg.theme('SystemDefault')

layout = [[sg.Text("Do you want to encrypt, decipher or brute force a message?")],
          [sg.Text("String: "), sg.Input(key='-STRING-')],
          [sg.Text("Shift:   "), sg.Input(key='-SHIFT-')],
          [sg.Text(size=(35, 1), key='-OUTPUT-')],
          [sg.Button('Encrypt'), sg.Button('Decipher'), sg.Button('Brute Force'), sg.Button('Exit')]]

window = sg.Window('Caesar_Cipher', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Encrypt' and values['-STRING-'] and values['-SHIFT-']:
        if values['-STRING-'].isalpha():
            if values['-SHIFT-'].isdigit():
                text = values['-STRING-']
                shift = int(values['-SHIFT-'])
                window['-OUTPUT-'].update(encrypt(text, shift))
            else:
                window['-OUTPUT-'].update("Given shift is not number.")
        else:
            window['-OUTPUT-'].update("Given string is not alphabetic.")
    if event == 'Decipher' and values['-STRING-'] and values['-SHIFT-']:
        if values['-STRING-'].isalpha():
            if values['-SHIFT-'].isdigit():
                text = values['-STRING-']
                shift = int(values['-SHIFT-'])
                window['-OUTPUT-'].update(decipher(text, shift))
            else:
                window['-OUTPUT-'].update("Given shift is not number.")
        else:
            window['-OUTPUT-'].update("Given string is not alphabetic.")
    if event == 'Brute Force' and values['-STRING-']:
        if values['-STRING-'].isalpha():
            text = values['-STRING-']
            alphabet = 26
            brute = ""
            for key in range(1, alphabet + 1):
                brute = brute + "\n" + str(key) + " " + decipher(text, key)
            sg.popup(brute)
        else:
            window['-OUTPUT-'].update("Given string is not alphabetic.")

window.close()
