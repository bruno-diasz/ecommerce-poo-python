from models.vendaitem import VendaItem
from dao.crud import CRUD
import json

class VendaItems(CRUD):
    
    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []  
            with open("data/vendaitems.json", mode="r") as arquivo:
                vendas_json = json.load(arquivo)
                for obj in vendas_json:
                    x = VendaItem(obj["id"], obj["qtd"], obj["preco"])
                    x.idVenda = obj["idVenda"]
                    x.idProduto = obj["idProduto"]
                    cls.objetos.append(x)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        lista_vendasitems = []
        for obj in cls.objetos:
            lista_vendasitems.append(obj.to_dict())
        with open ("data/vendaitems.json", mode="w") as arquivo:
            json.dump(lista_vendasitems, arquivo, indent =4)




