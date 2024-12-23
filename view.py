from model.usuario import Usuario, Usuarios
from model.respostas import Resposta, Respostas
from model.questoes import Questao, Questoes

class View:
    @staticmethod
    def usuarioAdmin():
        for c in Usuarios.listar():
            if c.getEmail() == "admin":
                return None
        View.usuarioInserir("admin", "admin", "1234")

    @staticmethod
    def usuarioAutenticar(email, senha):
        for c in Usuarios.listar():
            if c.getEmail() == email and c.getSenha() == senha:
                return {"id": c.getId(), "nome": c.getNome()}
        return None
    
    @staticmethod
    def usuarioListar():
        return Usuarios.listar()
    
    @staticmethod
    def usuarioInserir(nome, email, senha):
        c = Usuario(0, nome, email, senha)
        Usuarios.inserir(c)

    @staticmethod
    def usuarioAtualizar(id, nome, email, senha):
        c = Usuario(id, nome, email, senha)
        Usuarios.atualizar(c)

    @staticmethod
    def usuarioExcluir(id):
        c = Usuario(id, "", "", "")
        Usuarios.excluir(c)

    @staticmethod
    def questaoListar():
        return Questoes.listar()
    
    @staticmethod
    def questaoInserir(nome, enunciado, casos_teste):
        c = Questao(0, nome, enunciado, casos_teste)
        Questoes.inserir(c)

    @staticmethod
    def questaoAtualizar(id, nome, enunciado, casos_teste):
        c = Questao(id, nome, enunciado, casos_teste)
        Questoes.atualizar(c)

    @staticmethod
    def questaoExcluir(id):
        c = Questao(id, "", "", "")
        Questoes.excluir(c)
