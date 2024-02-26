lowerCase = 'abcdefghijklmnopqrstuvwxyz'

import random

def keyGen(seed, range):
    random.seed(seed)
    return random.randint(1, range)  

def formatText(text):
    finalText = ''
    for i in range(len(text)):
        if text[i]:
            finalText += text[i]
    return finalText

def transpose_encrypt(plaintext, key):
    cyphertext = ''

    plaintext = formatText(plaintext)
    
    key = keyGen(key, len(plaintext))

    dummy = 0

    while len(plaintext) % key != 0:
        plaintext += lowerCase[dummy % 26]
        dummy += 1

    matrix = [['.' for i in range(key)] for j in range(len(plaintext)//key)]

    currentIdx = 0

    for i in range(len(plaintext)//key):
        for j in range(key):
            if currentIdx < len(plaintext):
                matrix[i][j] = plaintext[currentIdx]
                currentIdx += 1

    for i in range(key):
        for j in range(len(plaintext)//key):
            cyphertext += matrix[j][i]

    return cyphertext


def transpose_decrypt(cyphertext, key):
    plaintext = ''

    cyphertext = formatText(cyphertext)
    
    key = keyGen(key, len(cyphertext))

    matrix = [['.' for i in range(len(cyphertext)//key)] for j in range(key)]

    currentIdx = 0

    for i in range(key):
        for j in range(len(cyphertext)//key):
            if currentIdx < len(cyphertext):
                matrix[i][j] = cyphertext[currentIdx]
                currentIdx += 1

    for i in range(len(cyphertext)//key):
        for j in range(key):
            plaintext += matrix[j][i]

    return plaintext


def main():
    plaintext = str(input("Plaintext: "))
    key = str(input("Key: "))
    cyphertext = transpose_encrypt(plaintext, key)
    decryption = transpose_decrypt(cyphertext, key)

    print(f'\nEncryption: {cyphertext}\nDecryption: {decryption}')

if __name__ == '__main__':
    main()