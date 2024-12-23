import streamlit as st
from view import View

class ListarQuestaoUI:
    @staticmethod
    def main():
        if 'page' not in st.session_state:
            st.session_state['page'] = 'pagina1'
        
        if st.session_state['page'] == 'pagina1':
            st.title("Listar Questoes")
            questao = View.questaoListar()

            if len(questao) == 0:
                st.write("Nenhuma questão cadastrada")
            else:
                for q in questao:
                    with st.container(border=True):
                        col1, col2 = st.columns([5,1])
                        with col1:
                            st.header(f"{q.getId()}. {q.getNome()}")
                        with col2:
                            if st.button("Responder", key=q.getId()):
                                st.session_state['page'] = 'pagina2'
                                st.session_state['questaoId'] = q.getId()
                                st.rerun()

        if st.session_state['page'] == 'pagina2':
            st.title("Responder Questao")
