import PySimpleGUI as sg
import pyperclip
from crypto_functions import encrypt, decrypt

sg.theme("DarkBlue")

layout = [
    [sg.Text("When Encrypting, leaving key blank will generate a random one, when giving a key make sure it is legit.", font=("Helvetica", 10))],
    [sg.Text("Enter a string to encrypt or decrypt:", font=("Helvetica", 14))],
    [sg.Input(key="string_input", font=("Helvetica", 14))],
    [sg.Text("Enter a key:", font=("Helvetica", 14))],
    [sg.Input(key="key_input", font=("Helvetica", 14))],
    [sg.Button("Encrypt",button_color=("mint cream", "slate blue"), font=("Helvetica", 14)), sg.Button("Decrypt",button_color=("slate blue", "mint cream"), font=("Helvetica", 14))],
    [sg.Text("Result:", font=("Helvetica", 14))],
    [sg.Output(key="result_output", font=("Helvetica", 14),size=(100,10))],
    [sg.Button("Copy String",button_color=("mint cream", "slate blue"), font=("Helvetica", 14)), sg.Button("Copy Key",button_color=("slate blue", "mint cream"), font=("Helvetica", 14))]

]


window = sg.Window("Encrypt/Decrypt", layout, size=(800,600))


#for text copy buttons
Copy_String =""
Copy_Key =""


while True:

    event, values = window.read()
    
    string_input = values["string_input"]
    key_input = values["key_input"]
    
    if event == "Encrypt":
        if (string_input != ""):
            result, key = encrypt(string_input)

            Copy_String=result
            Copy_Key=key

            window["result_output"].update(f"Encrypted string:{result}\nKey:{key}")
        else:
            sg.popup_ok('No String Entered!')

    elif event == "Decrypt":
        if (string_input != ""):
            result = decrypt(string_input, key_input)

            Copy_String=result
            Copy_Key=""

            window["result_output"].update(f"Decrypted string:{result}")
        else:
            sg.popup_ok('No String Entered!')



    elif event == "Copy String":
        if(Copy_String ==""):
            sg.popup_ok('No String To Copy!')
        else:    
            pyperclip.copy(Copy_String)
            sg.popup_ok('String copied to clipboard!')
        
     
    elif event == "Copy Key":
        if(Copy_Key ==""):
            sg.popup_ok('No Key To Copy!')
        else:    
            pyperclip.copy(Copy_Key)
            sg.popup_ok('Key copied to clipboard!')

window.close()