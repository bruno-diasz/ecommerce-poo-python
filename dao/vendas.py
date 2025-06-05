from venda import Venda
from datetime import datetime
import json

class Vendas:
    objetos= []
    
    @classmethod
    def inserir(cls,obj:Venda):
        cls.abrir()
        i = 0
        for elemento in cls.objetos:
            if elemento.id > i:
                i = elemento.id
        obj.id = i + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list[Venda]:
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls,id:int):
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj:Venda):
        old_obj = cls.listar_id(obj.id)
        if old_obj is not None: 
            cls.objetos.remove(old_obj)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj:Venda):
        if obj is not None:
            cls.objetos.remove(obj)
            cls.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []  
            with open("comercio/data/vendas.json", mode="r") as arquivo:
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
        with open ("comercio/data/vendas.json", mode="w") as arquivo:
            json.dump(lista_vendas, arquivo, indent =4)




