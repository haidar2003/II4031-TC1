from . import transpose
from . import vigenere

def formatText(text):
    finalText = ''
    for i in range(len(text)):
        if text[i].isalpha():
            finalText += text[i]
    return finalText.replace(" ", "")

def product_encrypt(plaintext, key):
    plaintext = formatText(plaintext)
    cyphertext = transpose.transpose_encrypt(plaintext, key)
    return vigenere.vigenere_encrypt(cyphertext, key)

def product_decrypt(cyphertext, key):
    cyphertext = formatText(cyphertext)
    plaintext = vigenere.vigenere_decrypt(cyphertext, key)
    return transpose.transpose_decrypt(plaintext, key)


def main():
    plaintext = str(input("Plaintext: "))
    key = str(input("Key: "))
    cyphertext = product_encrypt(plaintext, key)
    decryption = product_decrypt(cyphertext, key)

    print(f'\nEncryption: {cyphertext}\nDecryption: {decryption}')

if __name__ == '__main__':
    main()