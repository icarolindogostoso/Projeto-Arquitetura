from cliente import Cliente
import streamlit as st
import os

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:

    st.header("Assembly")

    codigo = st.text_area("Digite seu código:", height=500)

    entrada = "8"
    if st.button("submeter"):
        mensagem = Cliente.main(codigo, entrada)
        st.write(mensagem)

with col2:

    html_file = "index.html"

    if os.path.exists(html_file):
        with open(html_file, "r", encoding="utf-8") as file:
            html_content = file.read()
            st.components.v1.html(html_content, height=1000, width=800)  # Ajuste a altura conforme necessário
    else:
        st.error(f"O arquivo {html_file} não foi encontrado!")
