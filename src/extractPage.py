from hashlib import sha256
import streamlit as st
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from extract import genKey


def extractPage():
    coverFile = st.file_uploader("Cover File")
    password = st.text_input("Password",type="password")
    if st.button("Extract", type="primary") and coverFile and password:
        begin = coverFile.read(4)
        if begin == b'\x7fELF' or begin == "MZ":
            coverFile.seek(0)
            data = coverFile.read()
            location = data.find(sha256(bytes(password, 'utf-8')).digest())
            if location == -1:
                st.error("Wrong Password or no hidden data")
            else:
                location += 32
                coverFile.seek(location)
                alldata = coverFile.read()
                iv = alldata[:AES.block_size]
                enc_data = alldata[AES.block_size:]
                key = genKey(password)
                aes_decrypt = AES.new(key, AES.MODE_CBC, iv)

                st.download_button(
                    "download", unpad(aes_decrypt.decrypt(enc_data), AES.block_size), "hidden_data")
                st.success("Success")
        else:
            st.error("Given File is not a binary")
    else:
        st.warning("Please select Files")
