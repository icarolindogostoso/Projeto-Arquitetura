import subprocess
import os

class Sistema:
    @staticmethod
    def comando (codigo, entrada):

        codigo_asm = codigo

        arquivo_asm = "c:/Users/icaroohomidopcgaymer/Desktop/TADS/Projeto-Arquitetura2/codigo.asm"
        with open(arquivo_asm, "w") as arquivo:
            arquivo.write(codigo_asm)

        caminho_jar = "c:/Users/icaroohomidopcgaymer/Desktop/TADS/Projeto-Arquitetura2/Mars4_5.jar"

        if not os.path.isfile(caminho_jar):
            return "nao foi possivel achar arquivo"
        else:

            comando = ["java", "-jar", caminho_jar, arquivo_asm]

            entradas = entrada + "\n"

            try:   
                resultado = subprocess.run(comando, input=entradas, capture_output=True, text=True, check=True)
                return f"{resultado.stdout}"

            except subprocess.CalledProcessError as e:
                return f"{e}"

            finally:
                if os.path.isfile(arquivo_asm):
                    os.remove(arquivo_asm)

# codigo = ""
# while True:
#     linha = input()
#     if linha == "":
#         break
#     codigo += linha + "\n"
# entrada = input("Insira as entradas: ")
# comando = f"{codigo}~{entrada}"
# codigo,entrada = comando.split("~",1)

# saida = Sistema.comando(codigo,entrada)
# print(saida)