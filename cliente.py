class Cliente:
    def __init__(self, id:int, nome:str, email:str, fone:str):
        self.id = id #Chamando setter
        self.nome = nome #Chamando setter
        self.email= email #Chamando setter
        self.fone = fone #Chamando setter

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
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str):
             raise TypeError("O nome de ser uma string")
        self.__nome = valor
    
    @property
    def email(self) -> str:
        return self.__email
    @email.setter
    def email(self, valor):
        if not isinstance(valor, str):
             raise TypeError("O email de ser uma string")
        self.__email = valor

    @property
    def fone(self) -> str:
        return self.__fone
    @fone.setter
    def fone(self, valor):
        if not isinstance(valor, str):
             raise TypeError("O fone de ser uma string")
        self.__fone = valor

    #Metodos da instancia
    def __str__(self):
        return f"{self.id}. {self.nome} - {self.email} - {self.fone}"
    
    def to_dict(self):
        return {"id":self.id, "nome":self.nome, "email":self.email, "fone":self.fone}