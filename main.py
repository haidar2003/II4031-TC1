from cypher import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

def on_input_type_change(widgetHide,widgetShow):
    hideWidget(widgetHide)
    showWidget(widgetShow)

def hideWidget(widget):
    widget.grid_remove()

def showWidget(widget):
    widget.grid(row=6, column=1, pady=15, ipadx = 40)



def uploadFile(window, cypher): 
    filename = filedialog.askopenfilename()
    is_txt = True
    
    if os.path.splitext(filename)[1] != ".txt":
        is_txt = False

    if not(is_txt):
        if not(cypher == 'Extended Vigenere' or cypher == 'Autokey Vigenere'):
            filename = "Error: Please upload a .txt file"

    fileLabel = tk.Label(window, text=filename)
    fileLabel.grid(row=7, column=1, pady=15, ipadx = 40)

    return filename

def reset_label(window):
    fileLabel = tk.Label(window, text='                                                 ')
    fileLabel.grid(row=7, column=1, pady=15, ipadx = 40)

def start_encrypting(cypher, inputType, input, key):
    if inputType == 'Text':
        print('idk')
        #enkripsi teks
    else:
        if os.path.splitext(input)[1] == ".txt": #Berarti  -> enkripsi isinya, jangan filenya
            print('idk')

        else:
            if (cypher == 'Extended Vigenere' or cypher == 'Autokey Vigenere'): #Bisa file biner
                print('idk')

            else:
                print('error')
    return 

#bikin tombol submit, sama fungsinya

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

    # Input Text
    inputText = tk.StringVar()
    inputTextField = ttk.Entry(window, textvariable=inputText)

    

    # Input File
    inputUploadButton = ttk.Button(window,text= "Upload", command=lambda: uploadFile(window, selectedCipher.get()))

    


    # Input Selection
    inputLabel = tk.Label(window, text="Input Type :")
    inputLabel.grid(row=4, column=0, pady=10)
    inputSelected = tk.StringVar()
    inputList = ["Text", "File" ]
    inputSelection1 = ttk.Radiobutton(window, text=inputList[0], variable= inputSelected, value=inputList[0], command=lambda: (on_input_type_change(inputUploadButton,inputTextField), reset_label(window)))
    inputSelection1.grid(row=4, column=1, pady=10)
    inputSelection2 = ttk.Radiobutton(window, text=inputList[1], variable= inputSelected, value=inputList[1], command=lambda: on_input_type_change(inputTextField,inputUploadButton))
    inputSelection2.grid(row=5, column=1, pady=15)

    inputLabel = tk.Label(window, text="Input:")
    inputLabel.grid(row=6, column=0, pady=15, ipadx = 40)

    textLabel = tk.Label(window, text="Your Text Here")
    textLabel.grid(row=8, column=0, pady=15, ipadx = 40)

    textBox = tk.Text()
    textBox.grid(row=8, column=1, pady=15, ipadx = 40)

    #RUN 
    window.mainloop()



# def main():
#     # Main Window
#     window = tk.Tk()
#     window.title("Crypto GUI")

#     # Cipher Selection
#     cipherLabel = tk.Label(window, text="Cipher : ")
#     cipherLabel.pack(pady=5)
#     selectedCipher = tk.StringVar() 
#     cipherList = ["Vigenere","Extended Vigenere","Playfair","Product","Affine","Autokey Vigenere"]
#     cipherSelection = ttk.OptionMenu(window, selectedCipher, "Vigenere",*cipherList)
#     cipherSelection.pack(pady=10)

#     # Key
#     keyLabel = tk.Label(window, text="Key : ")
#     keyLabel.pack(pady=10)
#     key = tk.StringVar()
#     keyField = ttk.Entry(window, textvariable=key)
#     keyField.pack(pady=5)

#     # Input Text
#     inputText = tk.StringVar()
#     inputTextField = ttk.Entry(window, textvariable=inputText)
#     # Input File
#     inputUploadButton = ttk.Button(window,text= "Upload", command=uploadFile)

#     # Input Selection
#     inputLabel = tk.Label(window, text="Input:")
#     inputLabel.pack(pady=10)
#     inputSelected = tk.StringVar()
#     inputList = ["Text", "File" ]
#     inputSelection1 = ttk.Radiobutton(window, text=inputList[0], variable= inputSelected, value=inputList[0], command=lambda: on_input_type_change(inputUploadButton,inputTextField)) 
#     inputSelection2 = ttk.Radiobutton(window, text=inputList[1], variable= inputSelected, value=inputList[1], command=lambda: on_input_type_change(inputTextField,inputUploadButton))
#     inputSelection1.pack(pady=10)
#     inputSelection2.pack(pady=15)

#     #RUN 
#     window.mainloop()

if __name__ == '__main__':
    main()
