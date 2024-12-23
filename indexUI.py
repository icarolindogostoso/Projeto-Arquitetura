from templates.abrirContaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.manterUsuarioUI import ManterUsuarioUI
from templates.manterQuestaoUI import ManterQuestaoUI
from templates.listarQuestaoUI import ListarQuestaoUI
from templates.responderQuestaoUI import ResponderQuestaoUI

from view import View

import streamlit as st

class IndexUI:
    def menuVisitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema":
            LoginUI.main()
        if op == "Abrir Conta":
            AbrirContaUI.main()

    def menuAdmin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Usuarios", "Cadastro de Questoes"])
        if op == "Cadastro de Usuarios":
            ManterUsuarioUI.main()
        if op == "Cadastro de Questoes":
            ManterQuestaoUI.main()

    def menuCliente():
        op = st.sidebar.selectbox("Menu", ["Listar Questoes", "Responder Questao"])
        if op == "Listar Questoes":
            ListarQuestaoUI.main()
        if op == "Responder Questao":
            ResponderQuestaoUI.main()

    def sairDoSistema():
        if st.sidebar.button("Sair"):
            del st.session_state["clienteId"]
            del st.session_state["clienteNome"]
            st.rerun()

    def sidebar():
        if "clienteId" not in st.session_state:
            IndexUI.menuVisitante()
        else:
            admin = st.session_state["clienteNome"] == "admin"
            st.sidebar.write(f"Olá, {st.session_state['clienteNome']}")
            if admin:
                IndexUI.menuAdmin()
            else:
                IndexUI.menuCliente()
            IndexUI.sairDoSistema()

    def main():
        View.usuarioAdmin()
        IndexUI.sidebar()

IndexUI.main()