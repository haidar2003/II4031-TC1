import random

def keyGen(seed, range):
    random.seed(seed)
    return random.randint(1, range)  

def formatText(text):
    finalText = ''
    for i in range(len(text)):
        if text[i].isalpha():
            finalText += text[i].upper()
    return finalText

def encrypt(plaintext, key):
    cyphertext = ''

    plaintext = formatText(plaintext)
    
    key = keyGen(key, len(plaintext))

    print(key)

    while len(plaintext) % key != 0:
        plaintext += '_'

    matrix = [['.' for i in range(key)] for j in range(len(plaintext)//key)]

    currentIdx = 0

    for i in range(len(plaintext)//key):
        for j in range(key):
            if currentIdx < len(plaintext):
                matrix[i][j] = plaintext[currentIdx]
                currentIdx += 1

    for row in matrix:
        print(' '.join(row))

    for i in range(key):
        for j in range(len(plaintext)//key):
            if matrix[j][i] != '_':
                cyphertext += matrix[j][i]

    return cyphertext


def decrypt(cyphertext, key):
    plaintext = ''

    cyphertext = formatText(cyphertext)
    
    key = keyGen(key, len(cyphertext))

    print(key)

    print(cyphertext)

    matrix = [['.' for i in range(len(cyphertext)//key)] for j in range(key)]

    currentIdx = 0

    for i in range(key):
        for j in range(len(cyphertext)//key):
            if currentIdx < len(cyphertext):
                matrix[i][j] = cyphertext[currentIdx]
                currentIdx += 1

    for row in matrix:
        print(' '.join(row))

    for i in range(len(cyphertext)//key):
        for j in range(key):
            if matrix[j][i] != '_':
                plaintext += matrix[j][i]

    return plaintext

# print('Encrypt')
# print(encrypt('KUCING MANIA MANTAP MUHAMMAD RAFI HAIDAR MISAL MMM', 'KUCING'))

print('Decrypt')
print(decrypt(encrypt('KUCING MANIA', 'KUCING'), 'KUCING'))
