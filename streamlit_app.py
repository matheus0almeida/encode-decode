import cryptocode
import streamlit as st
from datetime import datetime,date
import time
import hashlib

def encoded (key,string):
    str_encoded = cryptocode.encrypt(string, key)
    return (str_encoded)

def decoded (key,string):
    str_decoded = cryptocode.decrypt(string, key)
    return (str_decoded)

def hash ():
    t_today = datetime.now()
    s_today = t_today.strftime('%Y/%m/%d %H:%M*%S')
    crypto = hashlib.sha256(s_today.encode('utf-8')).hexdigest()
    return (crypto)

st.set_page_config(
     page_title="Criptografar e Descriptografar",
     page_icon="lock"
 )


st.title('Criptografar e Descriptografar')

with st.expander("Cripitografia Senha definida - Menos Seguro"):

    option = st.radio("Selecione a opção: ",('Criptografar', 'Descriptografar'))
    key = st.text_input('Senha', '')
    string = st.text_input('Texto', '')

    if st.button('Rodar'):
        if option == 'Criptografar' :
            st.text("Texto Criptografado")
            st.text_area("",encoded (key,string))
        if option == 'Descriptografar' :
            st.text("Texto Descriptografado")
            st.text_area("",decoded (key,string))

with st.expander("Cripitografia Senha aleatória - Mais Seguro"):

    if st.button('Criptografar'):
        key1 = st.text_input('Senha ', hash ())
        string1 = st.text_input('Texto ', '')
        if st.button('Rodar '):
            st.text("Texto Criptografado")
            st.text_area("",encoded (key1,string1))

    if st.button('Descriptografar'):
        key1 = st.text_input('Senha ', '')
        string1 = st.text_input('Texto ', '')
        if st.button('Rodar  '):
            st.text("Texto Descriptografado")
            st.text_area("",decoded (key1,string1))
