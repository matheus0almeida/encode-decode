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
     page_icon="lock",
     layout="wide",
 )

st.title('Criptografar e Descriptografar')

with st.sidebar:
    st.subheader('Opções:')
    if st.button("Criptografar"):
        option=1
    if st.button("Descriptografar"):
        option=2
    st.button("Limpar", on_click=clear_text)


with st.expander("Cripitografia Senha definida - Menos Seguro"):

    key = st.text_input('Senha', key="text")
    string = st.text_input('Texto', key="text")

    if st.button('Rodar'):
        if option == 1 :
            st.text("Texto Criptografado")
            st.text_area("",encoded (key,string))
        if option == 2 :
            st.text("Texto Descriptografado")
            st.text_area("",decoded (key,string))

with st.expander("Cripitografia Senha aleatória - Mais Seguro"):

    if option == 1 :
        key1 = st.text_input('Senha ', hash ())
        string1 = st.text_input('Texto ', key="text")
        if st.button('Rodar '):
            st.text("Texto Criptografado")
            st.text_area("",encoded (key1,string1))

    if option == 2 :
        key1 = st.text_input('Senha ', key="text")
        string1 = st.text_input('Texto ', key="text")
        if st.button('Rodar  '):
            st.text("Texto Descriptografado")
            st.text_area("",decoded (key1,string1))
