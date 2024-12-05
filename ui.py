from cliente import Cliente
import streamlit as st
import streamlit.components.v1 as components

st.header("Assembly")
codigo = st.text_area("Escreva", height=300)

components.html("""
    <html>
    <head>
        <script type="text/javascript">
            function send_input() {
                var input_value = document.getElementById('nome_input').value;
                // Envia o valor para o Streamlit utilizando sessionStorage
                window.parent.postMessage({type: 'input_value', value: input_value}, '*');
            }
        </script>
    </head>
    <body>
        <input type="text" id="nome_input" placeholder="Digite seu nome" />
        <button onclick="send_input()">Enviar</button>
    </body>
    </html>
""")

nome = st.text_input("Nome", key="nome_input")

if st.button("enviar"):
    st.write(nome[0])

# entrada = "8"
# if st.button("submeter"):
#     mensagem = Cliente.main(codigo, entrada)
#     st.write(mensagem)