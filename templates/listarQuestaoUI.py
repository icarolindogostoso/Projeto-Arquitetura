import streamlit as st

class ListarQuestaoUI:
    @staticmethod
    def main():
        st.title("Listar Questoes")
        questao = View.questaoListar()

        if len(questao) == 0:
            st.write("Nenhuma questão cadastrada")
        else:
            for q in questao:
                with st.container(border=True):
                    st.header(f"{q.getId()}. {q.getNome()}")