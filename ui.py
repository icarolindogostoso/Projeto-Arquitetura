from cliente import Cliente
import streamlit as st

st.header("Assembly")
codigo = st.text_area()
entrada = "8"
mensagem = Cliente.main(codigo, entrada)
st.write(mensagem)