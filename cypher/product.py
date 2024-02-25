from . import transpose
from .  import vignere

def formatText(text):
    finalText = ''
    for i in range(len(text)):
        if text[i].isalpha():
            finalText += text[i]
    return finalText

def encrypt(plaintext, key):
    plaintext = formatText(plaintext)
    print(plaintext)
    cyphertext = transpose.encrypt(plaintext, key)
    print(cyphertext)
    return vignere.encrypt(cyphertext, key)

def decrypt(cyphertext, key):
    cyphertext = formatText(cyphertext)
    plaintext = vignere.decrypt(cyphertext, key)
    return transpose.decrypt(plaintext, key)


