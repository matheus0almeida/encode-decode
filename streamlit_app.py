import cryptocode
import streamlit as st
from datetime import datetime,date
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

def clear_text():
    st.session_state["text"] = ""

st.set_page_config(
     page_title="Criptografar e Descriptografar",
     page_icon="lock"
 )
value = " "

st.title('Criptografar e Descriptografar')

with st.sidebar:
    st.write("")
    option = st.radio("Selecione a opção: ",('Criptografar', 'Descriptografar'))
    st.button("Limpar", on_click=clear_text)


with st.expander("Cripitografia Senha definida - Menos Seguro"):

    key = st.text_input('Senha', key="text")
    string = st.text_input('Texto', key="text")

    if st.button('Rodar'):
        if option == 'Criptografar' :
            st.text("Texto Criptografado")
            st.text_area("",encoded (key,string))
        if option == 'Descriptografar' :
            st.text("Texto Descriptografado")
            st.text_area("",decoded (key,string))

with st.expander("Cripitografia Senha aleatória - Mais Seguro"):

    if option == 'Criptografar' :
        key1 = st.text_input('Senha ', hash ())
        string1 = st.text_input('Texto ', key="text")
        if st.button('Rodar '):
            st.text("Texto Criptografado")
            st.text_area("",encoded (key1,string1))

    if option == 'Descriptografar' :
        key1 = st.text_input('Senha ', key="text")
        string1 = st.text_input('Texto ', key="text")
        if st.button('Rodar  '):
            st.text("Texto Descriptografado")
            st.text_area("",decoded (key1,string1))
