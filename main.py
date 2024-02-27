from cypher import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import sys



def on_input_type_change(widgetHide,widgetShow):
    hideWidget(widgetHide)
    showWidget(widgetShow)

def hideWidget(widget):
    widget.grid_remove()

def showWidget(widget):
    widget.grid(row=6, column=1, pady=15, ipadx = 40)

# def uploadFile(window, cypher): 
#     filename = filedialog.askopenfilename()
#     is_txt = True
    
#     if os.path.splitext(filename)[1] != ".txt":
#         is_txt = False

#     if not(is_txt):
#         if not(cypher == 'Extended Vigenere' or cypher == 'Autokey Vigenere'):
#             filename = "Error: Please upload a .txt file"

#     fileLabel = tk.Label(window, text=filename)
#     fileLabel.grid(row=7, column=1, pady=15, ipadx = 40)

#     return filename

def reset_label(window):
    fileLabel = tk.Label(window, text='                                                                                              ')
    fileLabel.grid(row=7, column=1, pady=15, ipadx = 40)

def start_encrypting(target, cypherType, inputType, input, key):
    cyphertext = "ERROR"
    fileContent = "ERROR"
    if inputType == 'Text': #["Vigenere","Extended Vigenere","Playfair","Product","Affine","Autokey Vigenere"]
        match cypherType:
            case "Vigenere":
                cyphertext = vigenere.vigenere_encrypt(input,key) 
            case "Extended Vigenere":
                cyphertext = vigenere_extended.string_to_base64(vigenere_extended.plaintext_encrypt_extended(input,key))
            case "Playfair":
                cyphertext = playfair.playfair_encrypt(input,key)
            case "Product":
                cyphertext = product.product_encrypt(input,key)
            case "Affine":
                cyphertext = affine.affine_encrypt(input,key)
            case "Autokey Vigenere":
                cyphertext =  vigenere_extended.string_to_base64(vigenere_autokey.plaintext_autokey_encrypt(input,key))
    else:
        if os.path.splitext(input)[1] == ".txt": #Berarti  -> enkripsi isinya, jangan filenya
            
            with open(input,"r") as inputFile:
                plainTextInput = inputFile.read()
            match cypherType:
                case "Vigenere":
                     cyphertext = vigenere.vigenere_encrypt(plainTextInput,key) 
                case "Extended Vigenere":
                    return
                case "Playfair":
                    cyphertext = playfair.playfair_encrypt(plainTextInput,key)
                case "Product":
                    cyphertext = product.product_encrypt(plainTextInput,key)
                case "Affine":
                    cyphertext = affine.affine_encrypt(plainTextInput,key)
                case "Autokey Vigenere":
                    return      


        else: 
            if (cypherType == 'Extended Vigenere' or cypherType == 'Autokey Vigenere'): #Bisa file biner
                print('idk')

            else:
                print('error')
    

    # THIS IS A PLACEHOLDER
    target.config(state='normal')
    target.delete(1.0, tk.END) 
    target.insert(tk.END, cyphertext)

    # BIAR GAK DIGANTI USER
    target.config(state=tk.DISABLED)

def start_decrypting(target, cypher, inputType, input, key):
    # if inputType == 'Text': #["Vigenere","Extended Vigenere","Playfair","Product","Affine","Autokey Vigenere"]
    #     match cypher:
    #         case "Vigenere":
                 
    #         case "Extended Vigenere":
    #             return
    #         case "Playfair":
    #             return
    #         case "Product":
    #             return
    #         case "Affine":
    #             return
    #         case "Autokey Vigenere":
    #             return
    # else:
    #     if os.path.splitext(input)[1] == ".txt": #Berarti  -> enkripsi isinya, jangan filenya
    #         print('idk')

    #     else: 
    #         if (cypher == 'Extended Vigenere' or cypher == 'Autokey Vigenere'): #Bisa file biner
    #             print('idk')

    #         else:
    #             print('error')
    # return 

    # THIS IS A PLACEHOLDER
    target.config(state='normal')
    target.delete(1.0, tk.END) 
    target.insert(tk.END, f"Selected Cipher: {cypher} {input}")

    # BIAR GAK DIGANTI USER
    target.config(state=tk.DISABLED)

    
def main():
    # Main Window
    window = tk.Tk()
    window.title("Crypto GUI")

    fileLabel = tk.Label(window, text='')
    fileLabel.grid(row=7, column=1, pady=15, ipadx = 40)

    # Cipher Selection
    cipherLabel = tk.Label(window, text="Cipher : ")
    cipherLabel.grid(row=0, column=0, pady=5)
    selectedCipher = tk.StringVar() 
    cipherList = ["Vigenere","Extended Vigenere","Playfair","Product","Affine","Autokey Vigenere"]
    cipherSelection = ttk.OptionMenu(window, selectedCipher, "Vigenere",*cipherList, command=lambda event: reset_label(window))
    cipherSelection.grid(row=0, column=1, pady=10)

    # Key
    keyLabel = tk.Label(window, text="Key : ")
    keyLabel.grid(row=1, column=0, pady=10)
    key = tk.StringVar()
    keyField = ttk.Entry(window, textvariable=key)
    keyField.grid(row=1, column=1, pady=5)

    currentFile = "Error"

    def uploadFile(cypher): 
        nonlocal currentFile
        nonlocal window
        filename = filedialog.askopenfilename()
        is_txt = True
        
        if os.path.splitext(filename)[1] != ".txt":
            is_txt = False

        if not(is_txt):
            if not(cypher == 'Extended Vigenere' or cypher == 'Autokey Vigenere'):
                filename = "Error"

        fileLabel = tk.Label(window, text=filename)
        fileLabel.grid(row=7, column=1, pady=15, ipadx = 40)

        currentFile = filename

    def handle_input(inputType):
        nonlocal currentFile
        if inputType == 'Text':
            return inputText.get()
        else:
            return currentFile

    # Input Text
    inputText = tk.StringVar()
    inputTextField = ttk.Entry(window, textvariable=inputText)

    # Input File
    inputUploadButton = ttk.Button(window,text= "Upload", command=lambda:uploadFile(selectedCipher.get()))

    # Input Selection
    inputLabel = tk.Label(window, text="Input Type :")
    inputLabel.grid(row=4, column=0, pady=10)
    inputSelected = tk.StringVar()
    inputList = ["Text", "File" ]
    inputSelection1 = ttk.Radiobutton(window, text=inputList[0], variable= inputSelected, value=inputList[0], command=lambda: (on_input_type_change(inputUploadButton,inputTextField), reset_label(window)))
    inputSelection1.grid(row=4, column=1, pady=10)
    inputSelection2 = ttk.Radiobutton(window, text=inputList[1], variable= inputSelected, value=inputList[1], command=lambda: (on_input_type_change(inputTextField,inputUploadButton), inputUploadButton.grid(row=6, column=1, pady=15, ipadx = 40)))
    inputSelection2.grid(row=5, column=1, pady=15)


    inputLabel = tk.Label(window, text="Input:")
    inputLabel.grid(row=6, column=0, pady=15, ipadx = 40)

    textLabel = tk.Label(window, text="Your Encrypted/Decrypted Text:")
    textLabel.grid(row=9, column=0, pady=15, ipadx = 40)

    textBox = tk.Text(window, state=tk.DISABLED, height=5, width=40)
    textBox.grid(row=10, column=1, columnspan=2, pady=15, ipadx=40)

    encryptButton = ttk.Button(window, text="Encrypt", command=lambda: start_encrypting(textBox, selectedCipher.get(), inputSelected.get(), handle_input(inputSelected.get()), key.get()))
    encryptButton.grid(row=8, column=1, pady=10)

    decryptButton = ttk.Button(window, text="Decrypt", command=lambda: start_decrypting(textBox, selectedCipher.get(), inputSelected.get(), handle_input(inputSelected.get()), key.get()))
    encryptButton.grid(row=9, column=1, pady=10)

    print(sys.version)
    #RUN 
    window.mainloop()

if __name__ == '__main__':
    main()
