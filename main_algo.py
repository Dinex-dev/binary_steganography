from fileinput import filename
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def genKey(password):
    salt = b'\x14\x82\nN\xd9\xc4\x00\xc6\xbd\xd3\xf6\x0bu`*G\xd0\xe81Q\x13\xb4\x91\x1d\nJ\xf5\x93\x01\x93\xa4\xdc'
    key = PBKDF2(password,salt,dkLen=32)
    return key

def encrypt(data , password):
    key = genKey(password)
    aes_cipher = AES.new(key,AES.MODE_CBC)
    encrypted_data = aes_cipher.encrypt(pad(data,AES.block_size))
    return encrypted_data,aes_cipher.iv

def writefile(fileName,data):
    fileNameArray = fileName.split('.')
    fileExtention = fileNameArray[1:]
    fileName = fileNameArray[0]
    outputFile = open(fileName+"Encryted"+"."+'.'.join(fileExtention),'wb')
    outputFile.write(data)

fileName = input("Enter file to encrypt : ")
password = input("Enter Password : ")
file = open(fileName,'rb')
data = file.read()

(enc_data , iv) = encrypt(data,password)

writefile(fileName,iv+enc_data)