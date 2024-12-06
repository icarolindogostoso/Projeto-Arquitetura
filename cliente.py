import socket

class Cliente:
    @staticmethod
    def main(codigo, entrada):
        while True:

            if codigo.lower() == "sair":
                break

            comando = f"{codigo}~{entrada}"

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("127.0.0.1", 8888))

            s.send(comando.encode("utf-8"))

            msg = s.recv(1024)
            return f"{msg.decode("utf-8")}"
        
# codigo = ""
# while True:
#     linha = input()
#     if linha == "":
#         break
#     codigo += linha + "\n"

# entrada = "8"

# resposta = Cliente.main(codigo, entrada)

# print(resposta)