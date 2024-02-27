def vignere_autokey_encrypt(plainBytes:bytes, key:str):
    keyLength = len(key)
    plainText = list(plainBytes)
    plainTextLength = len(plainText)
    result = [0 for i in range(plainTextLength)]
    for i in range(plainTextLength):
        if i < keyLength:
            result[i] = (((plainText[i]) + ord(key[i % keyLength])) % 256)
        else:
            result[i] = (((plainText[i]) + plainText[i-keyLength]) % 256)
    return bytes(result)

def vignere_autokey_decrypt(encryptedBytes:bytes, key:str):
    keyLength = len(key)
    encryptedText = list(encryptedBytes)
    encryptedTextLength = len(encryptedText)
    result = [0 for i in range(encryptedTextLength)]
    for i in range(encryptedTextLength):
        if (i < keyLength):
            result[i] = ((encryptedText[i] - ord(key[i % keyLength])) % 256)
        else:
            result[i] = ((encryptedText[i] - result[i-keyLength]) % 256)
    return bytes(result)

def file_encrypt_autokey(plainFileName:str, encryptedFileName:str ,key:str):
    plainFile = open(plainFileName, "rb")
    plainBinary = plainFile.read()
    plainFile.close()
    encryptedBinary = vignere_autokey_encrypt(plainBinary, key)
    encryptedFile = open(encryptedFileName, "wb")
    encryptedFile.write(encryptedBinary)
    encryptedFile.close()
    return list(plainBinary)
def file_decrypt_autokey(encryptedFileName:str, plainFileName:str ,key:str):
    encryptedFile = open(encryptedFileName, "rb")
    encryptedBinary = encryptedFile.read()
    encryptedFile.close()
    plainBinary = vignere_autokey_decrypt(encryptedBinary, key)
    plainFile = open(plainFileName, "wb")
    plainFile.write(plainBinary)
    plainFile.close()
    return list(plainBinary)

def plaintext_autokey_encrypt(plainText:str, key:str):
    keyLength = len(key)
    plainTextLength = len(plainText)
    result = [0 for i in range(plainTextLength)]
    for i in range(plainTextLength):
        if i < keyLength:
            result[i] = chr((ord(plainText[i]) + ord(key[i % keyLength])) % 256)
        else:
            result[i] = chr((ord(plainText[i]) + ord(plainText[i-keyLength])) % 256)
    return "".join(result)

def plaintext_autokey_decrypt(encryptedBytes:str, key:str):
    keyLength = len(key)
    encryptedText = list(encryptedBytes)
    encryptedTextLength = len(encryptedText)
    result = [0 for i in range(encryptedTextLength)]
    for i in range(encryptedTextLength):
        if (i < keyLength):
            result[i] = chr((ord(encryptedText[i]) - ord(key[i % keyLength])) % 256)
        else:
            result[i] = chr((ord(encryptedText[i]) - ord(result[i-keyLength])) % 256)
    return "".join(result)
