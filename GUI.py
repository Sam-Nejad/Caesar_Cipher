import PySimpleGUI as sg

from Caesar_Cipher import encrypt, decipher

sg.theme('SystemDefault')

layout = [[sg.Text("Do you want to encrypt, decipher or brute force a message?")],
          [sg.Text("String: "), sg.Input(key='-STRING-')],
          [sg.Text("Shift:   "), sg.Input(key='-SHIFT-')],
          [sg.Text(size=(15, 1), key='-OUTPUT-')],
          [sg.Button('Encrypt'), sg.Button('Decipher'), sg.Button('Brute Force'), sg.Button('Exit')]]

window = sg.Window('Caesar_Cipher', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    text = values['-STRING-']
    shift = int(values['-SHIFT-'])
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Encrypt':
        window['-OUTPUT-'].update(encrypt(text, shift))
    if event == 'Decipher':
        window['-OUTPUT-'].update(decipher(text, shift))
    if event == 'Brute Force':
        alphabet = 26
        for key in range(1, alphabet + 1):
            print(key, decipher(text, key))
        print("")
        #window['-OUTPUT-'].update(values['-IN-'])

window.close()

