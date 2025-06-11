class Cliente:
    def __init__(self, id:int, nome:str, email:str, fone:str, senha:str):
        self.id = id #Chamando setter
        self.nome = nome #Chamando setter
        self.email= email #Chamando setter
        self.fone = fone #Chamando setter
        self.senha = senha #Chamando setter
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
    def nome(self, nome):
        if not isinstance(nome, str):
             raise TypeError("O nome de ser uma string")
        self.__nome = nome.strip().title()
    
    @property
    def email(self) -> str:
        return self.__email
    @email.setter
    def email(self, valor):
        if not isinstance(valor, str):
             raise TypeError("O email de ser uma string")
        if "@" not in valor and valor != "admin":
            raise ValueError("Formato de email inválido!")
        self.__email = valor.strip().lower()

    @property
    def fone(self) -> str:
        return self.__fone
    @fone.setter
    def fone(self, valor):
        if not isinstance(valor, str):
             raise TypeError("O fone de ser uma string")
        self.__fone = valor.strip()

    @property
    def senha(self) -> str:
        return self.__senha
    
    @senha.setter 
    def senha(self, senha:str):
        if not isinstance(senha, str):
            raise TypeError("O fone de ser uma string")
        self.__senha = senha.strip()

    #Metodos da instancia
    def __str__(self):
        return f"{self.id}. {self.nome:<18} {self.email:<20} {self.fone}"
    
    def to_dict(self):
        return {"id":self.id, "nome":self.nome, "email":self.email, "fone":self.fone, "senha":self.senha}