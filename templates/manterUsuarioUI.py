import streamlit as st
from view import View
import time

class ManterUsuarioUI:
    @staticmethod
    def main():
        st.title("Manter Usuarios")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterUsuarioUI.listar()
        with tab2:
            ManterUsuarioUI.inserir()
        with tab3:
            ManterUsuarioUI.atualizar()
        with tab4:
            ManterUsuarioUI.excluir()

    @staticmethod
    def listar():
        usuarios = View.usuarioListar()

        if len(usuarios) == 0:
            st.write("Nenhum usuario cadastrado")
        else:
            for usuario in usuarios:
                with st.container(border=True):
                    st.header(f"{usuario.getId()}. {usuario.getNome()}")
                    st.subheader(f"Email: {usuario.getEmail()}")
                    st.write(f"Senha: {usuario.getSenha()}")

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome:")
        email = st.text_input("Informe o email:")
        senha = st.text_input("Informe a senha:")
        if st.button("Cadastrar"):
            if nome == "" or email == "" or senha == "":
                st.error("Preencha todos os campos")
            else:
                View.usuarioInserir(nome, email, senha)
                st.success("Cadastrado com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def atualizar():
        usuarios = View.usuarioListar()
        if len(usuarios) == 0:
            st.write("Nenhum usuario cadastrado")
        else:
            op = st.selectbox("Selecione o usuario", [f"{u.getId()}. {u.getNome()}" for u in usuarios])
            nome = st.text_input("Informe o nome:", key="nome-atualizar")
            email = st.text_input("Informe o email:", key="email-atualizar")
            senha = st.text_input("Informe a senha:", key="senha-atualizar")
            if st.button("Atualizar"):
                if nome == "" or email == "" or senha == "":
                    st.error("Preencha todos os campos")
                else:
                    View.usuarioAtualizar(op.split(".")[0], nome, email, senha)
                    st.success("Atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()

    @staticmethod
    def excluir():
        usuarios = View.usuarioListar()
        if len(usuarios) == 0:
            st.write("Nenhum usuario cadastrado")
        else:
            op = st.selectbox("Selecione o usuario", [f"{u.getId()}. {u.getNome()}" for u in usuarios], key="op-excluir")
            if st.button("Excluir"):
                View.usuarioExcluir(op.split(".")[0])
                st.success("Excluido com sucesso")
                time.sleep(2)
                st.rerun()