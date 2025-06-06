from dao.clientes import Cliente, Clientes
from dao.produtos import Produto, Produtos
from dao.categorias import Categoria, Categorias
from dao.vendas import Venda, Vendas
from dao.vendaitems import VendaItem, VendaItems

class View:

    #==== Classe Clientes ====
    @staticmethod
    def cliente_inserir(id, nome, email, fone) -> None: #Create
        x = Cliente(id, nome, email, fone)
        Clientes.inserir(x)

    @staticmethod
    def cliente_listar() -> list[Cliente]: #Read
        return Clientes.listar()

    @staticmethod
    def cliente_atualizar(id, nome, email, fone) -> None:  #Update
        x = Cliente(id, nome, email, fone)
        Clientes.atualizar(x)

    @staticmethod
    def cliente_excluir(id) -> None: #Delete
        x = Clientes.listar_id(id)
        Clientes.excluir(x)

    #===== Classe Produtos ======
    @staticmethod
    def produto_inserir(id, desc, preco, estoq) -> None: #Create
        x = Produto(id,desc,preco,estoq)
        Produtos.inserir(x)

    @staticmethod
    def produto_listar() -> list[Produtos]: #Read
        return Produtos.listar()

    @staticmethod
    def produto_atualizar(id,desc,preco,estoq):
        x = Produto(id,desc,preco,estoq)
        Produtos.atualizar(x)

    @staticmethod
    def produto_excluir(id):
        x = Produtos.listar_id(id)
        Produtos.excluir(x)


    #===== Classe Categorias ======
    @staticmethod
    def categoria_listar():
        return Categorias.listar()

    @staticmethod
    def categoria_inserir(id, desc):
        x = Categoria(id, desc)
        Categorias.inserir(x)

    @staticmethod
    def categoria_atualizar(id, desc):
        x = Categoria(id,desc)
        Categorias.atualizar(x)

    @staticmethod
    def categoria_excluir(id):
        x = Categorias.listar_id(id)
        Categorias.excluir(x)


    #===== Classe Vendas =====
    @staticmethod
    def venda_listar():
        return Vendas.listar()
    

    
    #===== Classe VendasItem =====
    @staticmethod
    def vendaitem_listar():
        return VendaItems.listar()
    
    #===== Venda Operações ======
    @staticmethod
    def venda_iniciar(id):
        x =  Venda(id)
        Vendas.inserir(x)
        return x

    @staticmethod
    def venda_inserir_item(item_id, qtd, id_carrinho):

        item = Produtos.listar_id(item_id) #Pegando o produto da lista de produtos
        preco = item.preco*qtd #Escolhendo o preço
        venda = VendaItem(0,qtd,preco) #Montando o item de venda
        carrinho = Vendas.listar_id(id_carrinho) #Pegando o carrinho

        venda.idProduto = item.id #Associando itemvenda ao produto
        venda.idVenda = carrinho.id #Associando ao carrinho

        VendaItems.inserir(venda) #Adicionando item ao carrinho

        carrinho.total += preco #Adicionando valor ao total no carrinho
        Vendas.atualizar(carrinho)#SAlvando valor na persistencia

    @staticmethod
    def venda_confirmar(carrinho_id):
        items = VendaItems.listar()
        carrinho = Vendas.listar_id(carrinho_id)
        for i in items:
            if carrinho_id == i.idVenda:
                prod = Produtos.listar_id(i.idProduto)
                prod.estoque -=  i.qtd
                Produtos.atualizar(prod)
        carrinho.carrinho = False
        Vendas.atualizar(carrinho)
        return None
