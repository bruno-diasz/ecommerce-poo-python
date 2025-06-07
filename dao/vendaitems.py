from vendaitem import VendaItem
import json

class VendaItems:
    objetos= []
    
    @classmethod
    def inserir(cls,obj:VendaItem):
        cls.abrir()
        i = 0
        for elemento in cls.objetos:
            if elemento.id > i:
                i = elemento.id
        obj.id = i + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list[VendaItem]:
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls,id:int):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj:VendaItem):
        old_obj = cls.listar_id(obj.id)
        if old_obj is not None: 
            cls.objetos.remove(old_obj)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj:VendaItem):
        if obj is not None:
            cls.objetos.remove(obj)
            cls.salvar()

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




