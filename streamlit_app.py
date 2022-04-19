import cryptocode
import streamlit as st

def encoded (key,string):
    str_encoded = cryptocode.encrypt(string, key)
    return (str_encoded)

def decoded (key,string):
    str_decoded = cryptocode.decrypt(string, key)
    return (str_decoded)


st.set_page_config(
     page_title="Encode e Decode",
     page_icon="lock"
 )


st.title('Encode e Decode')

option = st.radio("Selecione a opção: ",('Encode', 'Decode'))

key = st.text_input('Chave', '')
string = st.text_input('Texto', '')

if st.button('Rodar'):
    if option == 'Encode' :
        st.text(option)
        st.text(encoded (key,string))
    if option == 'Decode' :
        st.text(option)
        st.text(decoded (key,string))
