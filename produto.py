class Produto:
    #Construtor
    def __init__(self, id:int, desc:str, preco:float,estoq:int):
        self.id = id #Chamando setter
        self.descricao = desc #Chamando setter
        self.preco = preco #Chamando setter
        self.estoque = estoq #Chamando setter
        
        self.__idCategoria = 0

    @property
    def id(self) -> int:
        return self.__id
    @id.setter
    def id(self,valor:int):
        if not isinstance(valor, int):
            raise TypeError("O valor o id deve ser um número inteiro")
        if valor < 0:
            raise ValueError("O id deve ser maior ou igual a zero")
        self.__id= valor

    @property
    def descricao(self) ->str:
        return self.__descricao
    @descricao.setter
    def descricao(self, d:str):
        if not isinstance(d, str):
            raise TypeError("O descricao deve ser uma string")
        self.__descricao = d

    @property
    def preco(self) ->float:
        return self.__preco
    @preco.setter
    def preco(self, valor:float):
        if not isinstance(valor, (float,int)):
            raise TypeError("O valor o preco deve ser um número")
        if valor < 0:
            raise ValueError("O valor deve ser maior ou igual a zero")
        self.__preco= valor

    @property
    def estoque(self) -> int:
        return self.__estoque
    @estoque.setter
    def estoque(self,valor:int):
        if not isinstance(valor, int):
            raise TypeError("O estoque deve ser um número inteiro")
        if valor < 0:
            raise ValueError("O estoque deve ser maior ou igual a zero")
        self.__estoque = valor

    @property
    def idCategoria(self) -> int:
        return self.__idCategoria
    
    @idCategoria.setter
    def idCategoria(self,valor:int):
        if not isinstance(valor, int):
            raise TypeError("O valor o idCategoria deve ser um número inteiro")
        if valor < 0:
            raise ValueError("O idCategoria deve ser positivo")
        self.__idCategoria= valor

    #Metodos
    def __str__(self):
        
        return f"{self.id}. {self.descricao:<15}R$ {self.preco} - Estoque:{self.estoque} - categoriaID:{self.idCategoria} "
    
    def to_dict(self):
        return {"id": self.id, "desc":self.descricao, "preco":self.preco, "estoque":self.estoque, "categoriaID":self.idCategoria}
    