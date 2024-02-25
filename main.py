from cypher import *
import tkinter as tk
from tkinter import ttk



def main():
    # Create the main window
    window = tk.Tk()
    window.title("Crypto GUI")

    # Cipher Selection
    selectedCipher = tk.StringVar() 
    cipherList = ["Vigenere","Extended Vigenere","Playfair","Product","Affine","Autokey Vigenere"]
    cipherSelection = ttk.OptionMenu(window, selectedCipher, "Vigenere",*cipherList)
    cipherSelection.pack(pady=10)
    # Input Selection

    window.mainloop()
if __name__ == '__main__':
    main()
