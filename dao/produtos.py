from models.produto import Produto
from dao.crud import CRUD
import json

class Produtos(CRUD):
   
    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []    
            with open("data/produtos.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Produto(obj["id"], obj["desc"], obj["preco"],obj["estoque"], obj["imagem"])
                    c.idCategoria = obj["categoriaID"]
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
        
    @classmethod
    def salvar(cls):
        lista_produtos = []
        for obj in cls.objetos:
            lista_produtos.append(obj.to_dict())
        with open("data/produtos.json", mode="w") as arquivo:
            json.dump(lista_produtos , arquivo, indent=4)



