from cypher import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def on_input_type_change(widgetHide,widgetShow):
    hideWidget(widgetHide)
    showWidget(widgetShow)

def hideWidget(widget):
    widget.pack_forget()

def showWidget(widget):
    widget.pack(pady=15)

def uploadFile():
    return filedialog.askopenfile()

def main():
    # Main Window
    window = tk.Tk()
    window.title("Crypto GUI")

    # Cipher Selection
    cipherLabel = tk.Label(window, text="Cipher : ")
    cipherLabel.pack(pady=5)
    selectedCipher = tk.StringVar() 
    cipherList = ["Vigenere","Extended Vigenere","Playfair","Product","Affine","Autokey Vigenere"]
    cipherSelection = ttk.OptionMenu(window, selectedCipher, "Vigenere",*cipherList)
    cipherSelection.pack(pady=10)
    # Key
    cipherLabel = tk.Label(window, text="Key")
    cipherLabel.pack(pady=5)
    key = tk.StringVar()
    keyField = ttk.Entry(window, textvariable=key)
    keyField.pack(pady=5)

    # Input Text
    inputText = tk.StringVar()
    inputTextField = ttk.Entry(window, textvariable=inputText)
    # Input File
    inputUploadButton = ttk.Button(window,text= "Upload", command=uploadFile)

    # Input Selection
    inputLabel = tk.Label(window, text="Input : ")
    inputLabel.pack(pady=10)
    inputSelected = tk.StringVar()
    inputList = ["Text", "File" ]
    inputSelection1 = ttk.Radiobutton(window, text=inputList[0], variable= inputSelected, value=inputList[0], command=lambda: on_input_type_change(inputUploadButton,inputTextField)) 
    inputSelection2 = ttk.Radiobutton(window, text=inputList[1], variable= inputSelected, value=inputList[1], command=lambda: on_input_type_change(inputTextField,inputUploadButton))
    inputSelection1.pack(pady=10)
    inputSelection2.pack(pady=15)


    inputTextField.pack(pady=15, ipadx=50)
    inputUploadButton.pack(padx=15)


    #RUN 
    window.mainloop()
if __name__ == '__main__':
    main()
