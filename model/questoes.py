import json

class Questao:
    def __init__(self, id, nome, enunciado, casos_teste):
        self.setId(id)
        self.setNome(nome)
        self.setEnunciado(enunciado)
        self.setCasosTeste(casos_teste)

    def setId(self, id):
        if id >= 0:
            self.__id = id
        else:
            raise ValueError("Id da questão inválido")
        
    def setNome(self, nome):
        if len(nome) >= 0:
            self.__nome = nome
        else:
            raise ValueError("Nome da questão inválido")

    def setEnunciado(self, enunciado):
        if len(enunciado) >= 0:
            self.__enunciado = enunciado
        else:
            raise ValueError("Enunciado da questão inválido")

    def setCasosTeste(self, casos_teste):
        if len(casos_teste) >= 0:
            self.__casos_teste = casos_teste        
        else:
            raise ValueError("Casos de teste da questão inválido")

    def getId(self):
        return self.__id
    
    def getNome(self):
        return self.__nome
    
    def getEnunciado(self):
        return self.__enunciado
    
    def getCasosTeste(self):
        return self.__casos_teste
    
    def __str__ (self):
        return f"Id: {self.__id}\nNome: {self.__nome}\nEnunciado: {self.__enunciado}\nCasos de teste: {self.__casos_teste}"
    
class Questoes:
    objetos = []

    @classmethod
    def inserir (cls, obj):
        cls.abrir()

        id = 0
        for questao in cls.objetos:
            if questao.getId() > id:
                id = questao.getId()

        obj.setId(id + 1)
        cls.objetos.append(obj)

        cls.salvar()

    @classmethod
    def listar (cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listarId (cls, id):
        cls.abrir()

        for questao in cls.objetos:
            if questao.getId() == id:
                return questao

        return None
    
    @classmethod
    def atualizar (cls, obj):
        questao = cls.listarId(obj.getId())
        if questao != None:
            questao.setEnunciado(obj.getEnunciado())
            questao.setCasosTeste(obj.getCasosTeste())
            cls.salvar()
    
    @classmethod
    def excluir (cls, obj):
        questao = cls.listarId(obj.getId())
        if questao != None:
            cls.objetos.remove(questao)
            cls.salvar()

    @classmethod
    def abrir (cls):
        cls.objetos = []

        try:
            with open("model/questoes.json", mode="r") as arquivo:
                questoes_json = json.load(arquivo)
                for obj in questoes_json:
                    c = Questao(obj["id"], obj["nome"], obj["enunciado"], obj["casos_teste"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar (cls):
        with open("model/questoes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)