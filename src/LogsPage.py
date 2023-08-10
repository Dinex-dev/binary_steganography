import pickle 
import streamlit as st
import time
from datetime import datetime



def newLog(username,fileName):
    with open('logs.log','ab') as log:
        pickle.dump({'username':username,"time":str(datetime.now().strftime("%d %b %Y %H:%M:%S")),"file":fileName},log)

def getLog(userName):
    userLogs = []
    with open('logs.log','rb') as log:
        while True:
            try:
                data = pickle.load(log)
                if data['username'] == userName:
                    userLogs.append(data)
            except EOFError:
                break
        return userLogs



def LogsPage(username):
    logs = getLog(username)
    for i in logs:
        col1,col2,col3 = st.columns(3)
        with col1:
            st.write(i['username'])
        with col2:
            st.write(i['time'])
        with col3:
            with open(i['file'],'rb') as file:
                st.download_button(i['file'].split('/')[-1],file)
    