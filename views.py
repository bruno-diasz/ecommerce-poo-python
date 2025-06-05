from dao.clientes import Cliente, Clientes

class View:

    #==== Classe Cliente ====
    @staticmethod
    def cliente_listar():
        return Clientes.listar()

    @staticmethod
    def cliente_inserir(id, nome, email, fone):
        x = Cliente(id, nome, email, fone)
        Clientes.inserir(x)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        x = Cliente(id, nome, email, fone)
        Clientes.atualizar(x)

    @staticmethod
    def cliente_excluir(id):
        x = Clientes.listar_id(id)
        Clientes.excluir(x)

    #===== Classe Produto ======
    @staticmethod
    def produto_listar():
        pass

    @staticmethod
    def produto_inserir():
        pass

    @staticmethod
    def produto_atualizar():
        pass

    @staticmethod
    def produto_excluir():
        pass
  
    #===== Classe Categoria ======
    @staticmethod
    def categoria_listar():
        pass

    @staticmethod
    def categoria_inserir():
        pass

    @staticmethod
    def categoria_atualizar():
        pass

    @staticmethod
    def categoria_excluir():
        pass