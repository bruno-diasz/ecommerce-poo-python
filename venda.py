from datetime import datetime
class Venda:

    def __init__(self,id:int):
        self.id = id #Chamando setter

        self.__data = datetime.now()
        self.__carrinho = True
        self.__total = 0
        self.__idCliente = 0

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
    def data(self) -> datetime:
        return self.__data 
    @data.setter
    def data(self,valor:datetime):
        if not isinstance(valor, datetime):
            raise TypeError("O valor da data deve ser um do tipo date")
        self.__data = valor

    @property
    def carrinho(self) -> int:
        return self.__carrinho
    @carrinho.setter
    def carrinho(self,valor:int):
        if not isinstance(valor, bool):
            raise TypeError("O valor o carrinho deve ser um verdadeiro ou falso")
        self.__carrinho= valor

    @property
    def total(self) ->float:
        return self.__total
    @total.setter
    def total(self, valor:float):
        if not isinstance(valor, (float,int)):
            raise TypeError("O valor o total deve ser um número")
        if valor < 0:
            raise ValueError("O valor deve ser maior ou igual a zero")
        self.__total= valor

    @property
    def idCliente(self) -> int:
        return self.__idCliente
    
    @idCliente.setter
    def idCliente(self,valor:int):
        if not isinstance(valor, int):
            raise TypeError("O valor o idCliente deve ser um número inteiro")
        if valor < 0:
            raise ValueError("O idCliente deve ser maior ou igual a zero")
        self.__idCliente= valor

    #Metodos de instancia
    def __str__(self):
        data = self.data.strftime("%d/%m/%Y %H:%M:%S")
        return f"{self.id}. {data} - Total: R$ {self.total:.2f}"
    
    def to_dict(self):
        data = self.data.strftime("%d/%m/%Y %H:%M:%S")
        return {"id":self.id, "data":data, "carrinho":self.carrinho, "total":self.total, "idCliente":self.idCliente}
    



    