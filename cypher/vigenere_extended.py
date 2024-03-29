import base64

def vignere_extended_encrypt(plainBytes:bytes, key:str):
    keyLength = len(key)
    plainText = list(plainBytes)
    plainTextLength = len(plainText)
    result = [0 for i in range(plainTextLength)]
    for i in range(plainTextLength):
        result[i] = (((plainText[i]) + ord(key[i % keyLength])) % 256)
    return bytes(result)

def vignere_extended_decrypt(encryptedBytes:bytes, key:str):
    keyLength = len(key)
    encryptedText = list(encryptedBytes)
    encryptedTextLength = len(encryptedText)
    result = [0 for i in range(encryptedTextLength)]
    for i in range(encryptedTextLength):
        result[i] = ((encryptedText[i] - ord(key[i % keyLength])) % 256)

    return bytes(result)

def file_encrypt_extended(plainFileName:str, encryptedFileName:str ,key:str):
    plainFile = open(plainFileName, "rb")
    plainBinary = plainFile.read()
    plainFile.close()
    encryptedBinary = vignere_extended_encrypt(plainBinary, key)
    encryptedFile = open(encryptedFileName, "wb")
    encryptedFile.write(encryptedBinary)
    encryptedFile.close()
    return encryptedBinary
def file_decrypt_extended(encryptedFileName:str, plainFileName:str ,key:str):
    encryptedFile = open(encryptedFileName, "rb")
    encryptedBinary = encryptedFile.read()
    encryptedFile.close()
    plainBinary = vignere_extended_decrypt(encryptedBinary, key)
    plainFile = open(plainFileName, "wb")
    plainFile.write(plainBinary)
    plainFile.close()
    return plainBinary

def plaintext_encrypt_extended(plainText:str, key:str):
    keyLength = len(key)
    plainTextLength = len(plainText)
    result = ["" for i in range(plainTextLength)]
    for i in range(plainTextLength):
        result[i] = chr(( ord(plainText[i]) + ord(key[i % keyLength])) % 256)
    return "".join(result)

def plaintext_decrypt_extended(encryptedText:str, key:str):
    keyLength = len(key)
    plainTextLength = len(encryptedText)
    result = ["" for i in range(plainTextLength)]
    for i in range(plainTextLength):
        result[i] = chr(( ord(encryptedText[i]) - ord(key[i % keyLength])) % 256)
    return "".join(result)

def binary_to_base64(binary:bytes):
    return(base64.b64encode(binary))

def string_to_base64(string:str):
    return(base64.b64encode(string.encode("utf-8")))

