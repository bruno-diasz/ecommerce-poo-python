from models.venda import Venda
from datetime import datetime
from dao.crud import CRUD
import json

class Vendas(CRUD):
    

    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []  
            with open("data/vendas.json", mode="r") as arquivo:
                vendas_json = json.load(arquivo)
                for obj in vendas_json:
                    x = Venda(obj["id"])
                    x.data = datetime.strptime(obj["data"],"%d/%m/%Y %H:%M:%S") 
                    x.carrinho= obj["carrinho"]
                    x.total= obj["total"]
                    x.idCliente= obj["idCliente"]
                    cls.objetos.append(x)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        lista_vendas = []
        for obj in cls.objetos:
            lista_vendas.append(obj.to_dict())
        with open ("data/vendas.json", mode="w") as arquivo:
            json.dump(lista_vendas, arquivo, indent =4)




