import streamlit as st
from hide import encrypt, CombineData
import os
from LogsPage import newLog

def nextnonexistent(f):
    fnew = f
    root, ext = os.path.splitext(f)
    i = 0
    while os.path.exists(fnew):
        i += 1
        fnew = '%s_%i%s' % (root, i, ext)
    return fnew

def hidePage(username):
    with st.container():

        coverFile = st.file_uploader(
            "Cover file")
        dataFile = st.file_uploader("Data file")
        password = st.text_input("File Password",type="password")

        if st.button("Hide", type="primary") and coverFile and dataFile and password:
            with st.spinner("runnning"):
                begin = coverFile.read(4)
                if begin == b'\x7fELF' or begin == "MZ":
                    coverFile.seek(0)
                    coverData = coverFile.read()
                    data = dataFile.read()
                    (enc_data, iv) = encrypt(data, password)
                    password = bytes(password, 'utf-8')
                    hiddenData = CombineData(coverData, password, iv, enc_data)
                    if coverFile.name.split(".")[-1] == "exe":
                        st.download_button("Download "+coverFile.name + " with hidden data", hiddenData, coverFile.name.split('.')[0:-1]+"hidden.exe", mime="application/x-msdownload")
                    else:
                        st.download_button("Download File", hiddenData, "".join(coverFile.name)+"hidden", mime="application/x-elf")
                    st.success("Data hidden Successfully", icon="✅")
                    try:
                        os.mkdir(f'Files/{username}')
                    except FileExistsError:
                        pass
                    fileName = nextnonexistent(f'Files/{username}/{coverFile.name}')
                    with open(fileName,'wb') as file:
                        file.write(hiddenData)
                    newLog(username,fileName)
                else:
                    st.error(
                        "Cover file is not a executable binary", icon="🚨")
        else:
            st.warning("Please Select Files", icon="⚠️")
