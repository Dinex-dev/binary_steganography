from hashlib import sha256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def genKey(password):
    salt = b'\x14\x82\nN\xd9\xc4\x00\xc6\xbd\xd3\xf6\x0bu`*G\xd0\xe81Q\x13\xb4\x91\x1d\nJ\xf5\x93\x01\x93\xa4\xdc'
    key = PBKDF2(password, salt, dkLen=32)
    return key


def decrypt(filename, password):
    file = open(filename, 'rb')

    data = file.read()
    location = data.find(sha256(bytes(password, 'utf-8')).digest())
    if location == -1:
        print("Wrong Password or no hidden data")
        exit(0)
    location += 32
    file.seek(location)
    alldata = file.read()
    iv = alldata[:AES.block_size]
    encrypted_data = alldata[AES.block_size:]
    key = genKey(password)
    aes_decrypt = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes_decrypt.decrypt(encrypted_data), AES.block_size)


def extract(filename, password, outputfile):
    try:
        file = open(outputfile, 'wb')
        if not (file.read(4) != b'\x7fELF' or file.read(4) != "MZ"):
            print("Given file is not a executable binary")
            exit(0)
    except FileNotFoundError:
        return "File not found"
    file.write(decrypt(filename, password))
    return "Successful"


if __name__ == "__main__":
    filename = input("File name : ")
    password = input("Password : ")
    outputfile = input("Output file : ")
    extract(filename, password, outputfile)
