def vignere_extended_encrypt(plainText:str, key:str):
    keyLength = len(key)
    plainTextLength = len(plainText)
    result = ["" for i in range(plainTextLength)]
    for i in range(plainTextLength):
        result[i] = chr((ord(plainText[i]) + ord(key[(i % keyLength)])) % 255)
    return "".join(result)

def vignere_extended_decrypt(encryptedText:str, key:str):
    keyLength = len(key)
    encryptedTextLength = len(encryptedText)
    result = ["" for i in range(encryptedTextLength)]
    for i in range(encryptedTextLength):
        result[i] = chr((ord(encryptedText[i]) - ord(key[i % keyLength])) % 255)
    return "".join(result)

