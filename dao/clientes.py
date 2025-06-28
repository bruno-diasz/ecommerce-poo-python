from models.cliente import Cliente
from dao.crud import CRUD
import json

class Clientes(CRUD):

    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []    
            with open("data/clientes.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"] )
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
        
    @classmethod
    def salvar(cls):
        lista_clientes = []
        for obj in cls.objetos:
            lista_clientes.append(obj.to_dict())
        with open("data/clientes.json", mode="w") as arquivo:
            json.dump(lista_clientes , arquivo, indent=4)


