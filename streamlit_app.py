import cryptocode
import streamlit as st

def encoded (key,string):
    str_encoded = cryptocode.encrypt(string, key)
    return (str_encoded)

def decoded (key,string):
    str_decoded = cryptocode.decrypt(string, key)
    return (str_decoded)


st.set_page_config(
     page_title="Criptografar e Descriptografar",
     page_icon="lock"
 )


st.title('Criptografar e Descriptografar')

option = st.radio("Selecione a opção: ",('Criptografar', 'Descriptografar'))

key = st.text_input('Chave', '')
string = st.text_input('Texto', '')

if st.button('Rodar'):
    if option == 'Criptografar' :
        st.text(option)
        st.text(encoded (key,string))
    if option == 'Descriptografar' :
        st.text(option)
        st.text(decoded (key,string))
