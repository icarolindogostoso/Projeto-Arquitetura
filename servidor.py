import socket
import sistema
class Servidor:
    soc : socket
    def __init__(self, ip:str, porta:int):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.bind((ip, porta))
    
    def ligar(self):
        self.soc.listen()
        while True:
            cliente, address = self.soc.accept()
            msg = cliente.recv(1024).decode("utf-8")

            try:
                codigo,entrada = msg.split("~",1)
                retorno = sistema.Sistema.comando(codigo,entrada)
                cliente.send(bytes(retorno,"utf-8"))

            except ValueError:
                cliente.send(b"Erro")

            cliente.close()
def main():
    server = Servidor("127.0.0.1",8888)
    server.ligar()

if __name__ == "__main__":
    main()
        
