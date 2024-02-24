import transpose
import vignere

def formatText(text):
    finalText = ''
    for i in range(len(text)):
        if text[i].isalpha():
            finalText += text[i].upper()
    return finalText

def encrypt(plaintext, key):
    plaintext = formatText(plaintext)
    print(plaintext)
    cyphertext = vignere.encrypt(plaintext, key)
    print(cyphertext)
    return transpose.encrypt(cyphertext, key)

def decrypt(cyphertext, key):
    cyphertext = formatText(cyphertext)
    print(cyphertext)
    plaintext = transpose.decrypt(cyphertext, key)
    print(plaintext)
    return vignere.decrypt(plaintext, key)

print('encrypt')

txt = encrypt('KUCING MANIA MANTAP', 'KUCING')
print(txt)
print('decrypt')
print(decrypt(txt, 'KUCING'))
