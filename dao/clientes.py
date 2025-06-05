from cliente import Cliente
import json

class Clientes:
    objetos = []

    @classmethod
    def inserir(cls, obj:object):
        cls.abrir()
        i = 0
        for elemento in cls.objetos:
            if elemento.id > i:
                i = elemento.id
        obj.id = i + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list[Cliente]:
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id:int):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x is not None: 
            cls.objetos.remove(x)
            cls.objetos.insert(obj.id-1,obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x is not None: 
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):
        lista_clientes = []
        for obj in cls.objetos:
            lista_clientes.append(obj.to_dict())
        with open("comercio/data/clientes.json", mode="w") as arquivo:
            json.dump(lista_clientes , arquivo, indent=4)

    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []    
            with open("comercio/data/clientes.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Cliente(obj["id"], obj["nome"], obj["email"],obj["fone"] )
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

