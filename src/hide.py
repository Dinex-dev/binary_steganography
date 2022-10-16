from hashlib import sha256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def genKey(password):
    salt = b'\x14\x82\nN\xd9\xc4\x00\xc6\xbd\xd3\xf6\x0bu`*G\xd0\xe81Q\x13\xb4\x91\x1d\nJ\xf5\x93\x01\x93\xa4\xdc'
    key = PBKDF2(password, salt, dkLen=32)
    return key


def encrypt(data, password):
    key = genKey(password)
    aes_cipher = AES.new(key, AES.MODE_CBC)
    encrypted_data = aes_cipher.encrypt(pad(data, AES.block_size))
    return encrypted_data, aes_cipher.iv


def CombineData(coverData, password, iv, encryptedData):
    return coverData + sha256(password).digest() + iv + encryptedData


def decrypt(data, iv, key):
    aes_decrypt = AES.new(key, AES.MODE_CBC, iv)
    return aes_decrypt.decrypt(data)


def hide(DataFile, coverFile, outputFileName, password):
    try:
        cover = open(coverFile, 'rb')
        if not (cover.read(4) != b'\x7fELF' or cover.read(4) != "MZ"):
            print("Cover file is not a executable binary")
            exit(0)
    except FileNotFoundError:
        return "Cover file not found"
    else:
        coverData = cover.read()
    try:
        file = open(DataFile, 'rb')
    except FileNotFoundError:
        return "Data file not Found"
    else:
        data = file.read()
    try:
        outputFile = open(outputFileName, 'wb')
    except FileNotFoundError:
        return "Output file invalid"
    (enc_data, iv) = encrypt(data, password)
    password = bytes(password, 'utf-8')
    outputFile.write(CombineData(coverData, password, iv, enc_data))
    return "Successful"


def menudriven():
    coverFile = input("Cover file : ")
    dataFile = input("Data file : ")
    password = input("Password : ")
    outputFile = input("Output file : ")
    print(hide(dataFile, coverFile, outputFile, password))


if __name__ == "__main__":
    menudriven()
