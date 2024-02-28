from cypher import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import sys
import base64

def str_to_base64(input_str):
    input_str_bytes = input_str.encode('utf-8')
    base64_bytes = base64.b64encode(input_str_bytes)
    base64_str = base64_bytes.decode('utf-8')
    return base64_str

def on_input_type_change(widgetHide,widgetShow):
    hideWidget(widgetHide)
    showWidget(widgetShow)

def hideWidget(widget):
    widget.grid_remove()

def showWidget(widget):
    widget.grid(row=6, column=1, pady=15, ipadx = 40)

def reset_label(window):
    fileLabel = tk.Label(window, text='                                                                                              ')
    fileLabel.grid(row=7, column=1, pady=15, ipadx = 40)

def start_encrypting(target, target64, cypherType, inputType, input, key, encodingUsed):
    cyphertext = "ERROR"
    fileContent = cyphertext
    fileContentIsBinary = False

    if (len(input) == 0 or len(key) == 0):
        return fileContent, fileContentIsBinary
    
    if inputType == 'Text': #["Vigenere","Extended Vigenere","Playfair","Product","Affine","Autokey Vigenere"]
        match cypherType:
            case "Vigenere":
                cyphertext = vigenere.vigenere_encrypt(input,key) 
                fileContent = cyphertext
            case "Extended Vigenere":
                fileContent = vigenere_extended.plaintext_encrypt_extended(input,key)
                cyphertext = vigenere_extended.string_to_base64(fileContent)
                fileContent = fileContent.encode(encodingUsed)
                fileContentIsBinary = True
            case "Playfair":
                cyphertext = playfair.playfair_encrypt(input,key)
                fileContent = cyphertext
            case "Product":
                cyphertext = product.product_encrypt(input,key)
                fileContent = cyphertext
            case "Affine":
                cyphertext = affine.affine_encrypt(input,key)
                fileContent = cyphertext
            case "Autokey Vigenere":
                fileContent = vigenere_autokey.plaintext_autokey_encrypt(input,key)
                cyphertext =  vigenere_extended.string_to_base64(fileContent)
                fileContent = fileContent.encode(encodingUsed)
                fileContentIsBinary = True
    else:
        if os.path.splitext(input)[1] == ".txt": #Berarti  -> enkripsi isinya, jangan filenya
            
            with open(input,"r") as inputFile:
                plainTextInput = inputFile.read()
            match cypherType:
                case "Vigenere":
                     cyphertext = vigenere.vigenere_encrypt(plainTextInput,key) 
                     fileContent = cyphertext
                case "Extended Vigenere":
                    fileContent = vigenere_extended.plaintext_encrypt_extended(plainTextInput,key)
                    cyphertext = vigenere_extended.string_to_base64(fileContent)
                    fileContent = fileContent.encode(encodingUsed)
                    fileContentIsBinary = True
                case "Playfair":
                    cyphertext = playfair.playfair_encrypt(plainTextInput,key)
                    fileContent = cyphertext
                case "Product":
                    cyphertext = product.product_encrypt(plainTextInput,key)
                    fileContent = cyphertext
                case "Affine":
                    cyphertext = affine.affine_encrypt(plainTextInput,key)
                    fileContent = cyphertext
                case "Autokey Vigenere":
                    fileContent = vigenere_autokey.plaintext_autokey_encrypt(plainTextInput,key)
                    cyphertext =  vigenere_extended.string_to_base64(fileContent)
                    fileContent = fileContent.encode(encodingUsed)
                    fileContentIsBinary = True



        else: 
            if (cypherType == 'Extended Vigenere' or cypherType == 'Autokey Vigenere'): #Bisa file biner
                with open(input,"rb") as inputFile:
                    binaryInput = inputFile.read()
                fileContentIsBinary = True
                if (cypherType == 'Extended Vigenere'):
                    fileContent = vigenere_extended.vignere_extended_encrypt(binaryInput, key)
                    cyphertext = vigenere_extended.binary_to_base64(fileContent)
                else :
                    fileContent = vigenere_autokey.vignere_autokey_encrypt(binaryInput, key)
                    cyphertext = vigenere_extended.binary_to_base64(fileContent.decode(encodingUsed))
            else:
                print('error')
    

    # DIMUNCULIN DI TEXTBOX
    target.config(state='normal')
    target.delete(1.0, tk.END) 

    target64.config(state='normal')
    target64.delete(1.0, tk.END) 

    if not(fileContentIsBinary):
        target.insert(tk.END, cyphertext)
        target64.insert(tk.END, str_to_base64(cyphertext))
    else:
        target.insert(tk.END, fileContent.decode(encodingUsed))
        target64.insert(tk.END, cyphertext)  

    # BIAR GAK DIGANTI USER
    target.config(state=tk.DISABLED)
    target64.config(state=tk.DISABLED)

    return fileContent, fileContentIsBinary

def start_decrypting(target, target64, cypherType, inputType, input, key, encodingUsed):
    plaintext = "ERROR"
    fileContent = plaintext
    fileContentIsBinary = False

    if (len(input) == 0 or len(key) == 0):
        return fileContent, fileContentIsBinary
    
    if inputType == 'Text': #["Vigenere","Extended Vigenere","Playfair","Product","Affine","Autokey Vigenere"]
        match cypherType:
            case "Vigenere":
                plaintext = vigenere.vigenere_decrypt(input,key) 
                fileContent = plaintext
            case "Extended Vigenere":
                fileContent = vigenere_extended.plaintext_decrypt_extended(input,key)
                plaintext = vigenere_extended.string_to_base64(fileContent)
                fileContent = fileContent.encode(encodingUsed)
                fileContentIsBinary = True
            case "Playfair":
                plaintext = playfair.playfair_decrypt(input,key)
                fileContent = plaintext
            case "Product":
                plaintext = product.product_decrypt(input,key)
                fileContent = plaintext
            case "Affine":
                plaintext = affine.affine_decrypt(input,key)
                fileContent = plaintext
            case "Autokey Vigenere":
                fileContent = vigenere_autokey.plaintext_autokey_decrypt(input,key)
                plaintext =  vigenere_extended.string_to_base64(fileContent) 
                fileContent = fileContent.encode(encodingUsed)
                fileContentIsBinary = True
    else:
        if os.path.splitext(input)[1] == ".txt": #Berarti  -> enkripsi isinya, jangan filenya
            
            with open(input,"r") as inputFile:
                plainTextInput = inputFile.read()
            match cypherType:
                case "Vigenere":
                    plaintext = vigenere.vigenere_decrypt(plainTextInput,key) 
                    fileContent = plaintext
                case "Extended Vigenere":
                    fileContent = vigenere_extended.plaintext_decrypt_extended(plainTextInput,key)
                    plaintext = vigenere_extended.string_to_base64(fileContent)
                    fileContent = fileContent.encode(encodingUsed)
                    fileContentIsBinary = True
                case "Playfair":
                    plaintext = playfair.playfair_decrypt(plainTextInput,key)
                    fileContent = plaintext
                case "Product":
                    plaintext = product.product_decrypt(plainTextInput,key)
                    fileContent = plaintext
                case "Affine":
                    plaintext = affine.affine_decrypt(plainTextInput,key)
                    fileContent = plaintext
                case "Autokey Vigenere":
                    fileContent = vigenere_autokey.plaintext_autokey_decrypt(plainTextInput,key)
                    plaintext =  vigenere_extended.string_to_base64(fileContent)
                    fileContent = fileContent.encode(encodingUsed)
                    fileContentIsBinary = True                    

        else: 
            if (cypherType == 'Extended Vigenere' or cypherType == 'Autokey Vigenere'): #Bisa file biner
                with open(input,"rb") as inputFile:
                    binaryInput = inputFile.read()
                fileContentIsBinary = True
                if (cypherType == 'Extended Vigenere'):
                    fileContent = vigenere_extended.vignere_extended_decrypt(binaryInput, key)
                    plaintext = vigenere_extended.binary_to_base64(fileContent)
                else :
                    fileContent = vigenere_autokey.vignere_autokey_decrypt(binaryInput, key)
                    plaintext = vigenere_extended.binary_to_base64(fileContent)
            else:
                print('error')


    # DIMUNCULIN DI TEXTBOX
    target.config(state='normal')
    target.delete(1.0, tk.END) 

    target64.config(state='normal')
    target64.delete(1.0, tk.END) 

    if not(fileContentIsBinary):
        target.insert(tk.END, plaintext)
        target64.insert(tk.END, str_to_base64(plaintext))
    else:
        target.insert(tk.END, fileContent.decode(encodingUsed))
        target64.insert(tk.END, plaintext)  

    # BIAR GAK DIGANTI USER
    target.config(state=tk.DISABLED)
    target64.config(state=tk.DISABLED)

    return fileContent, fileContentIsBinary

    
def main():
    # Main Window
    window = tk.Tk()
    window.title("Crypto GUI")
    defaultEncoding = sys.getdefaultencoding()

    window_width =700
    window_height = 800
    
    window.minsize(window_width, window_height)
    window.maxsize(window_width, window_height)

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

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

    # Nested Functions (We're bad at programming)
    currentFile = "Error"
    resultContent = "Error"
    isResultBinary = False

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

    def handle_encrypt(target, target64, cypherType, inputType, input, key):
        nonlocal resultContent
        nonlocal isResultBinary
        nonlocal defaultEncoding
        resultContent , isResultBinary = start_encrypting(target, target64, cypherType, inputType, input, key,defaultEncoding)

    def handle_decrypt(target, target64, cypherType, inputType, input, key):
        nonlocal resultContent
        nonlocal isResultBinary
        nonlocal defaultEncoding
        resultContent , isResultBinary = start_decrypting(target, target64, cypherType, inputType, input, key,defaultEncoding)

        
    def on_save_button():
        nonlocal isResultBinary
        nonlocal resultContent
        if (isResultBinary):
            outputFile = filedialog.asksaveasfile(mode="wb",filetypes=[("All files","*.*")])
        else :
            outputFile = filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=[("Text files","*.txt*")])
        outputFile.write(resultContent)
        
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
    inputLabel.grid(row=6, column=0, pady=5, ipadx = 40)

    # Result
    textLabel = tk.Label(window, text="Your Encrypted/Decrypted Text:")
    textLabel.grid(row=10, column=0, pady=5, ipadx = 40)

    textBox = tk.Text(window, state=tk.DISABLED, height=10, width=20)
    textBox.grid(row=10, column=1, columnspan=2, pady=5, ipadx=40)

    # Result (Base64)
    textLabel = tk.Label(window, text="Your Encrypted/Decrypted Text (Base64):")
    textLabel.grid(row=11, column=0, pady=5, ipadx = 40)

    textBox64 = tk.Text(window, state=tk.DISABLED, height=10, width=20)
    textBox64.grid(row=11, column=1, columnspan=2, pady=5, ipadx=40)

    # Encrypt Button
    encryptButton = ttk.Button(window, text="Encrypt", command=lambda: handle_encrypt(textBox, textBox64, selectedCipher.get(), inputSelected.get(), handle_input(inputSelected.get()), key.get()))
    encryptButton.grid(row=8, column=1, pady=3)

    # Decrypt Button
    decryptButton = ttk.Button(window, text="Decrypt", command=lambda: handle_decrypt(textBox, textBox64, selectedCipher.get(), inputSelected.get(), handle_input(inputSelected.get()), key.get()))
    decryptButton.grid(row=9, column=1, pady=3)

    # Save Button
    saveButton = ttk.Button(window, text="Save File", command=lambda: on_save_button())
    saveButton.grid(row=12, column=1, pady=10)

    #RUN 
    window.mainloop()

if __name__ == '__main__':
    main()
