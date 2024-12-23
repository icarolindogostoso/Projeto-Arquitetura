import streamlit as st
from view import View
import time

class AbrirContaUI:
    @staticmethod
    def main():
        st.title("Abrir Conta no Sistema")
        AbrirContaUI.inserir()

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome:")
        email = st.text_input("Informe o email:")
        senha = st.text_input("Informe a senha:")
        if st.button("Cadastrar"):
            View.usuarioInserir(nome, email, senha)
            st.success("Cadastrado com sucesso")
            time.sleep(2)
            st.rerun()