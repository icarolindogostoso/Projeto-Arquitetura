import streamlit as st
from view import View

class LoginUI:
    @staticmethod
    def main():
        st.title("Entrar no Sistema")
        email = st.text_input("Informe o email:")
        senha = st.text_input("Informe a senha:")
        if st.button("Entrar"):
            c = View.usuarioAutenticar(email, senha)
            if c == None:
                st.write("Email ou senha inválidos")
            else:
                st.session_state["clienteId"] = c["id"]
                st.session_state["clienteNome"] = c["nome"]
                st.rerun()