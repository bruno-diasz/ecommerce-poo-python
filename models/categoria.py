class Categoria:
    #Construtor
    def __init__(self,id:int, d:str): 
        self.id = id #Chamando setter
        self.descricao = d #Chamando setter
        
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
    def descricao(self) ->str:
        return self.__descricao
    @descricao.setter
    def descricao(self, d:str):
        if not isinstance(d, str):
            raise TypeError("O descricao deve ser uma string")
        self.__descricao = d

    #Metodos
    def __str__(self)->str:
        return f"{self.id}. {self.descricao}"
    
    def to_dict(self):
        return {"id":self.id,"descricao":self.descricao}
    

