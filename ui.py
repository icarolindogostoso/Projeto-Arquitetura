from cliente import Cliente
import streamlit as st

st.header("Assembly")

codigo = st.text_area("Digite seu código:", height=500)

entrada = "8"
if st.button("submeter"):
    mensagem = Cliente.main(codigo, entrada)
    st.write(mensagem)