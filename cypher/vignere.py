import random

lowerCase = 'abcdefghijklmnopqrstuvwxyz'
upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def getOrder(alphabet):
    for i in range(len(lowerCase)):
        if alphabet.lower() == lowerCase[i]:
            return i

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


def encrypt(plaintext, key):
    ciphertext = ''

    if len(key) < len(plaintext):
        key = repeat(key, len(plaintext))
    else:
        key = key[:len(plaintext)]

    for i in range(len(plaintext)):
        if (plaintext[i].isalpha()):
            encryptedChar = (getOrder(plaintext[i]) + getOrder(key[i])) % 26

            if plaintext[i].islower():
                ciphertext += lowerCase[encryptedChar]
            else:
                ciphertext += upperCase[encryptedChar]

        else:
            ciphertext += plaintext[i]

    return ciphertext

def decrypt(cyphertext, key):
    plaintext = ''

    if len(key) < len(cyphertext):
        key = repeat(key, len(cyphertext))
    else:
        key = key[:len(cyphertext)]

    for i in range(len(cyphertext)):
        if (cyphertext[i].isalpha()):
            encryptedChar = (getOrder(cyphertext[i]) - getOrder(key[i])) % 26

            if cyphertext[i].islower():
                plaintext += lowerCase[encryptedChar]
            else:
                plaintext += upperCase[encryptedChar]

        else:
            plaintext += cyphertext[i]

    return plaintext