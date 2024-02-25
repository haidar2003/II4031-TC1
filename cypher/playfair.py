letter = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

def formatKey(key):
    finalKey = ''
    for i in range(len(key)):
        if (key[i].isalpha() and not(key[i] in finalKey) and key[i].lower() != 'j'):
            finalKey += key[i].upper()
    for j in range(len(letter)):
        if not(letter[j] in finalKey):
            finalKey += letter[j].upper()
    return finalKey

def makeSquare(key):
    square = [['.' for i in range(5)] for j in range(5)]
    idx = 0
    for i in range(5):
        for j in range(5):
            square[i][j] = key[idx]
            idx += 1
    return square

def locate(letter, square):
    for i in range(5):
        for j in range(5):
            if square[i][j] == letter.upper():
                return (i, j)
            
def formatText(text):
    finalText = ''
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].upper() == 'J':
                finalText += 'I'
            else:
                finalText += text[i].upper()
    
    if len(finalText) == 1:
        finalText += 'X'
        return finalText
    else:
        currIdx = 0
        nextIdx = 1
        while nextIdx < len(finalText):
            if finalText[currIdx].upper() == finalText[nextIdx].upper():
                finalText = finalText[:currIdx + 1].upper() + 'X' + finalText[currIdx + 1:].upper()
            currIdx += 1
            nextIdx += 1
        if len(finalText) % 2 != 0:
            finalText += 'X'
        return finalText
    

            
def playfair_encrypt(plaintext, key):
    cyphertext = ''
    playfairSquare = makeSquare(formatKey(key))
    plaintext = formatText(plaintext)

    while len(plaintext) != 0:
        firstLetter = locate(plaintext[0], playfairSquare)
        secondLetter = locate(plaintext[1], playfairSquare)

        if firstLetter[0] == secondLetter[0]:
            cyphertext += playfairSquare[firstLetter[0]][(firstLetter[1] + 1) % 5] + playfairSquare[secondLetter[0]][(secondLetter[1] + 1) % 5]

        elif firstLetter[1] == secondLetter[1]:
            cyphertext += playfairSquare[(firstLetter[0] + 1) % 5][firstLetter[1]] + playfairSquare[(secondLetter[0] + 1) % 5][secondLetter[1]]

        else:
            cyphertext += playfairSquare[firstLetter[0]][secondLetter[1]] + playfairSquare[secondLetter[0]][firstLetter[1]]

        plaintext = plaintext[2:]
    
    return cyphertext


def playfair_decrypt(cyphertext, key):
    plaintext = ''
    playfairSquare = makeSquare(formatKey(key))
    cyphertext = formatText(cyphertext)

    while len(cyphertext) != 0:
        firstLetter = locate(cyphertext[0], playfairSquare)
        secondLetter = locate(cyphertext[1], playfairSquare)

        if firstLetter[0] == secondLetter[0]:
            plaintext += playfairSquare[firstLetter[0]][(firstLetter[1] - 1) % 5] + playfairSquare[secondLetter[0]][(secondLetter[1] - 1) % 5]

        elif firstLetter[1] == secondLetter[1]:
            plaintext += playfairSquare[(firstLetter[0] - 1) % 5][firstLetter[1]] + playfairSquare[(secondLetter[0] - 1) % 5][secondLetter[1]]

        else:
            plaintext += playfairSquare[firstLetter[0]][secondLetter[1]] + playfairSquare[secondLetter[0]][firstLetter[1]]

        cyphertext = cyphertext[2:]
    
    return plaintext 



print(formatKey('JALAN GANESHA SEPULUH'))

for row in makeSquare(formatKey('JALAN GANESHA SEPULUH')):
    print(' '.join(row))


print(encrypt('temui ibu nanti malam', 'JALAN GANESHA SEPULUH'))

print(decrypt(encrypt('temui ibu nanti malam', 'JALAN GANESHA SEPULUH'), 'JALAN GANESHA SEPULUH'))

