import json

class Resposta:
    def __init__(self, id, respostas, tentativa, questao_id, usuario_id):
        self.setId(id)
        self.setResposta(respostas)
        self.setTentativa(tentativa)
        self.setQuestaoId(questao_id)
        self.setUsuarioId(usuario_id)

    def setId(self, id):
        if id >= 0:
            self.__id = id
        else:
            raise ValueError("Id da resposta inválido")

    def setResposta(self, respostas):
        for resposta in respostas:
            if len(resposta) < 0:
                raise ValueError("Resposta da questão inválido")
        self.__respostas = respostas

    def setTentativa(self, tentativa):
        if tentativa >= 0:
            self.__tentativa = tentativa
        else:
            raise ValueError("Tentativa da questão inválida")

    def setQuestaoId(self, questao_id):
        if questao_id >= 0:
            self.__questao_id = questao_id
        else:
            raise ValueError("Id da questão inválido")

    def setUsuarioId(self, usuario_id):
        if usuario_id >= 0:
            self.__usuario_id = usuario_id
        else:
            raise ValueError("Id do usuário inválido")
        
    def getId(self):
        return self.__id
    
    def getRespostas(self):
        return self.__respostas
    
    def getTentativa(self):
        return self.__tentativa
    
    def getQuestaoId(self):
        return self.__questao_id
    
    def getUsuarioId(self):
        return self.__usuario_id
        
    def __str__ (self):
        return f"Id: {self.__id}\nRespostas: {self.__respostas}\nTentativa: {self.__tentativa}\nId da questão: {self.__questao_id}\nId do usuário: {self.__usuario_id}"
    
class Respostas:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
            
        id = 0
        for resposta in cls.objetos:
            if resposta.getId() > id:
                id = resposta.getId()
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

        for resposta in cls.objetos:
            if resposta.getId() == id:
                return resposta
        return None
    
    @classmethod
    def atualizar (cls, obj):
        resposta = cls.listarId(obj.getId())
        if resposta != None:
            resposta.setResposta(obj.getRespostas())
            resposta.setQuestaoId(obj.getQuestaoId())
            resposta.setUsuarioId(obj.getUsuarioId())
            cls.salvar()

    @classmethod
    def excluir (cls, obj):
        resposta = cls.listarId(obj.getId())
        if resposta != None:
            cls.objetos.remove(resposta)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("model/respostas.json", mode="r") as arquivo:
                respostas_json = json.load(arquivo)
                for obj in respostas_json:
                    c = Resposta(obj["id"], obj["respostas"], obj["tentativa"], obj["questao_id"], obj["usuario_id"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("model/respostas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)