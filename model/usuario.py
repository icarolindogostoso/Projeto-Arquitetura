import json

class Usuario:
    def __init__(self, id, nome, email, senha):
        self.setId(id)
        self.setNome(nome)
        self.setEmail(email)
        self.setSenha(senha)

    def setId (self, id):
        if id >= 0:
            self.__id = id
        else:
            raise ValueError ("Id invalido")
        
    def setNome (self, n):
        if len(n) >= 0:
            self.__nome = n
        else:
            raise ValueError ("Nome invalido")
        
    def setEmail (self, e):
        if len(e) >= 0:
            self.__email = e
        else:
            raise ValueError ("Email invalido")
        
    def setSenha (self, s):
        if len(s) >= 0:
            self.__senha = s
        else:
            raise ValueError ("Senha invalida")
        
    def getSenha (self, s):
        if len(s) >= 0:
            self.__senha = s
        else:
            raise ValueError ("Senha invalida")
        
    def getId (self):
        return self.__id
    
    def getNome (self):
        return self.__nome
    
    def getEmail (self):
        return self.__email
    
    def getSenha (self):
        return self.__senha
        
    def __str__ (self):
        return f"Id: {self.getId()}\nNome: {self.getNome()}\nEmail: {self.getEmail()}\nSenha: {self.getSenha()}"
    
class Usuarios:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()

        for usuario in cls.objetos:
            if usuario.getEmail() == obj.getEmail():
                raise ValueError ("Email ja cadastrado")
            
        id = 0
        for usuario in cls.objetos:
            if usuario.getId() > id:
                id = usuario.getId()
        obj.setId(id + 1)

        cls.objetos.append(obj)

        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listarId(cls, id):
        cls.abrir()

        for usuario in cls.objetos:
            if usuario.getId() == id:
                return usuario
        return None
    
    @classmethod
    def atualizar (cls, obj):
        for usuario in cls.objetos:
            if usuario.getEmail() == obj.getEmail():
                raise ValueError ("Email ja cadastrado")

        usuario = cls.listarId(obj.getId())
        if usuario != None:
            usuario.setNome(obj.getNome())
            usuario.setEmail(obj.getEmail())
            cls.salvar()

    @classmethod
    def excluir (cls, obj):
        usuario = cls.listarId(obj.getId())
        if usuario != None:
            cls.objetos.remove(usuario)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("bee/model/usuarios.json", mode="r") as arquivo:
                usuarios_json = json.load(arquivo)
                for obj in usuarios_json:
                    c = Usuario(obj["_Usuario__id"], obj["_Usuario__nome"], obj["_Usuario__email"], obj["_Usuario__senha"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("bee/model/usuarios.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)