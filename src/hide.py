from hashlib import sha256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from sys import argv


def genKey(password):
    salt = b'\x14\x82\nN\xd9\xc4\x00\xc6\xbd\xd3\xf6\x0bu`*G\xd0\xe81Q\x13\xb4\x91\x1d\nJ\xf5\x93\x01\x93\xa4\xdc'
    key = PBKDF2(password,salt,dkLen=32)
    return key

def encrypt(data , password):
    key = genKey(password)
    aes_cipher = AES.new(key,AES.MODE_CBC)
    encrypted_data = aes_cipher.encrypt(pad(data,AES.block_size))
    return encrypted_data,aes_cipher.iv

def CombineData(coverData,password,iv,encryptedData):
    return coverData+sha256(password).digest()+iv+encryptedData

def decrypt(data,iv,key):
    aes_decrypt = AES.new(key,AES.MODE_CBC,iv)
    return aes_decrypt.decrypt(data)

def writefile(fileName,data):
    outputFile = open(fileName,'wb')
    outputFile.write(data)


def hide(DataFile,coverFile,outputFileName,password):
    file = open(DataFile,'rb')
    data = file.read()

    cover = open(coverFile,'rb')
    coverData = cover.read()

    (enc_data , iv) = encrypt(data,password)
    password = bytes(password,'utf-8')
    writefile(outputFileName,CombineData(coverData,password,iv,enc_data))

def menudriven():
    coverFile = input("Cover file : ")
    dataFile = input("Abstract file : ")
    password = input("Password : ")
    outputFile = input("Output file : ")
    hide(dataFile,coverFile,outputFile,password)

if __name__ == "__main__":
    menudriven()