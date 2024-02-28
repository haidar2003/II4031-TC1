import random

lowerCase = 'abcdefghijklmnopqrstuvwxyz'
upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def formatText(text):
    finalText = ''
    for i in range(len(text)):
        if text[i].isalpha():
            finalText += text[i]
    return finalText.replace(" ", "")

def getOrder(alphabet):
    if alphabet.isalpha():
        for i in range(len(lowerCase)):
            if alphabet.lower() == lowerCase[i]:
                return i
    else: 
        return 0

def repeat(word, target):
    repeatedWord = word
    wordLength = len(word)
    idx = 0
    while (len(repeatedWord) < target):
        repeatedWord += word[idx]
        if idx == wordLength - 1:
            idx = 0
        else:
            idx += 1
    return repeatedWord

def vigenere_encrypt(plaintext, key):
    plaintext = formatText(plaintext)
    key = formatText(key)
    cyphertext = ''

    if len(key) < len(plaintext):
        key = repeat(key, len(plaintext))
    else:
        key = key[:len(plaintext)]

    for i in range(len(plaintext)):
        if (plaintext[i].isalpha()):
            encryptedChar = (getOrder(plaintext[i]) + getOrder(key[i])) % 26

            if plaintext[i].islower():
                cyphertext += lowerCase[encryptedChar]
            else:
                cyphertext += upperCase[encryptedChar]

        # else:
        #     cyphertext += plaintext[i]

    return cyphertext

def vigenere_decrypt(cyphertext, key):
    cyphertext = formatText(cyphertext)
    key = formatText(key)
    plaintext = ''

    if len(key) < len(cyphertext):
        key = repeat(key, len(cyphertext))
    else:
        key = key[:len(cyphertext)]

    for i in range(len(cyphertext)):
        if (cyphertext[i].isalpha()):
            decryptedChar = (getOrder(cyphertext[i]) - getOrder(key[i])) % 26

            if cyphertext[i].islower():
                plaintext += lowerCase[decryptedChar]
            else:
                plaintext += upperCase[decryptedChar]

        else:
            plaintext += cyphertext[i]

    return plaintext


def main():
    plaintext = str(input("Plaintext: "))
    key = str(input("Key: "))
    cyphertext = vigenere_encrypt(plaintext, key)
    decryption = vigenere_decrypt(cyphertext, key)

    print(f'\nEncryption: {cyphertext}\nDecryption: {decryption}')

if __name__ == '__main__':
    main()