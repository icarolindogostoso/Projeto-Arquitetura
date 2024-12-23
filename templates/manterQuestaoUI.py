import streamlit as st
from view import View
import time

class ManterQuestaoUI:
    @staticmethod
    def main():
        st.title("Manter Questoes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterQuestaoUI.listar()
        with tab2:
            ManterQuestaoUI.inserir()
        with tab3:
            ManterQuestaoUI.atualizar()
        with tab4:
            ManterQuestaoUI.excluir()

    @staticmethod
    def listar():
        questoes = View.questaoListar()

        if len(questoes) == 0:
            st.write("Nenhuma questão cadastrada")
        else:
            for questao in questoes:
                with st.container(border=True):
                    st.header(f"{questao.getId()}. {questao.getNome()}")
                    st.write(f"Enunciado: {questao.getEnunciado()}")
                    st.write(f"Casos de Teste:")
                    for caso in questao.getCasosTeste():
                        st.write(f"- {caso}")

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome:")
        enunciado = st.text_input("Informe o enunciado:")
        casos_teste_lista = []
        for i in range(5):
            casos_teste_lista.append(st.text_input(f"Informe o caso de teste {i + 1}:"))
        if st.button("Cadastrar"):
            if nome == "" or enunciado == "" or len(casos_teste_lista) == 0:
                st.error("Preencha todos os campos")
            else:
                casos_teste = []
                for caso in casos_teste_lista:
                    if caso != "":
                        casos_teste.append(caso)
                View.questaoInserir(nome, enunciado, casos_teste)
                st.success("Cadastrado com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def atualizar():
        questoes = View.questaoListar()
        if len(questoes) == 0:
            st.write("Nenhuma questão cadastrada")
        else:
            op = st.selectbox("Selecione a questão", [f"{q.getId()}. {q.getNome()}" for q in questoes])
            nome = st.text_input("Informe o novo nome:")
            enunciado = st.text_input("Informe o novo enunciado:")
            casos_teste_lista = []
            for i in range(5):
                casos_teste_lista.append(st.text_input(f"Informe o novo caso de teste {i + 1}:"))
            if st.button("Atualizar"):
                if nome == "" or enunciado == "" or len(casos_teste_lista) == 0:
                    st.error("Preencha todos os campos")
                else:
                    casos_teste = []
                    for caso in casos_teste_lista:
                        if len(caso) == 0:
                            casos_teste.append(caso)
                    View.questaoAtualizar(int(op.split(".")[0]), nome, enunciado, casos_teste)
                    st.success("Atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()

    @staticmethod
    def excluir():
        questoes = View.questaoListar()
        if len(questoes) == 0:
            st.write("Nenhuma questão cadastrada")
        else:
            op = st.selectbox("Selecione a questão", [f"{q.getId()}. {q.getNome()}" for q in questoes], key="op-excluir")
            if st.button("Excluir"):
                View.questaoExcluir(int(op.split(".")[0]))
                st.success("Excluido com sucesso")
                time.sleep(2)
                st.rerun()