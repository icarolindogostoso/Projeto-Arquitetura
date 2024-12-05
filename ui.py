from cliente import Cliente
import streamlit as st

st.header("Assembly")
codigo = st.text_area("Escreva")
entrada = "8"
if st.button("submeter"):
    mensagem = Cliente.main(codigo, entrada)
    st.write(mensagem)