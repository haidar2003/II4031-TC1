import random

lowerCase = 'abcdefghijklmnopqrstuvwxyz'
upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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


def vignere_encrypt(plaintext, key):
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

        else:
            cyphertext += plaintext[i]

    return cyphertext
def vignere_encrypt(plaintext, key):
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

        else:
            cyphertext += plaintext[i]

    return cyphertext


def vignere_decrypt(cyphertext, key):
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
    cyphertext = vignere_encrypt(plaintext, key)
    decryption = vignere_decrypt(cyphertext, key)

    print(f'\nEncryption: {cyphertext}\nDecryption: {decryption}')

if __name__ == '__main__':
    main()