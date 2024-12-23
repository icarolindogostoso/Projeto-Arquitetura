import streamlit as st

class ResponderQuestaoUI:
    @staticmethod
    def main():
        if st.session_state['page'] == 'pagina2':
            st.session_state['page'] = 'pagina1'
        pass