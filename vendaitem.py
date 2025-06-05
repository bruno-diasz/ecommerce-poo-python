from dao.produtos import Produtos
class VendaItem:
    #Contrutor
    def __init__(self, id:int, qtd:int, preco:float):
        self.id = id #Chamando setter
        self.qtd = qtd #Chamando setter
        self.preco = preco #Chamando setter
        
        self.__idVenda = 0
        self.__idProduto = 0

    #Getters e setters
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
    def qtd(self) -> int:
        return self.__qtd
    @qtd.setter
    def qtd(self,valor:int):
        if not isinstance(valor, int):
            raise TypeError("A quantidade deve ser um número inteiro")
        if valor < 0:
            raise ValueError("A quantidade deve ser maior que zero")
        self.__qtd = valor

    @property
    def idVenda(self) -> int:
        return self.__idVenda
    @idVenda.setter
    def idVenda(self,valor:int):
        if not isinstance(valor, int):
            raise TypeError("O valor o idVenda deve ser um número inteiro")
        if valor < 0:
            raise ValueError("O idVenda deve ser positivo")
        self.__idVenda= valor

    @property
    def idProduto(self) -> int:
        return self.__idProduto
    @idProduto.setter
    def idProduto(self,valor:int):
        if not isinstance(valor, int):
            raise TypeError("O valor o idProduto deve ser um número inteiro")
        if valor < 0:
            raise ValueError("O idProduto deve ser positivo")
        self.__idProduto= valor

    #Metodos de instancia
    def __str__(self):
        nomeprod = Produtos.listar_id(self.idProduto).descricao
        valorprod = Produtos.listar_id(self.idProduto).preco
    
        return f"{nomeprod:<18} R$ {valorprod:.2f} x Qtd:{self.qtd}     R$ {self.preco:.2f}"
    
    def to_dict(self):
        return {"id": self.id, "qtd":self.qtd, "preco":self.preco, "idVenda":self.idVenda, "idProduto":self.idProduto}
    

    