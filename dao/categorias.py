from categoria import Categoria
import json

class Categorias:
    objetos= []
    
    @classmethod
    def inserir(cls,obj:Categoria):
        cls.abrir()
        i = 0
        for elemento in cls.objetos:
            if elemento.id > i:
                i = elemento.id
        obj.id = i + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list[Categoria]:
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls,id:int):
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj:Categoria):
        old_obj = cls.listar_id(obj.id)
        if old_obj is not None: 
            cls.objetos.remove(old_obj)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj:Categoria):
        if obj is not None:
            cls.objetos.remove(obj)
            cls.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []  
            with open("comercio/data/categorias.json", mode="r") as arquivo:
                categorias_json = json.load(arquivo)
                for obj in categorias_json:
                    x = Categoria(obj["id"],obj["descricao"])
                    cls.objetos.append(x)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        lista_categorias = []
        for obj in cls.objetos:
            lista_categorias.append(obj.to_dict())
        with open ("comercio/data/categorias.json", mode="w") as arquivo:
            json.dump(lista_categorias, arquivo, indent =4)




