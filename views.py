from dao.clientes import Cliente, Clientes
from dao.produtos import Produto, Produtos
from dao.categorias import Categoria, Categorias
from dao.vendas import Venda, Vendas
from dao.vendaitems import VendaItem, VendaItems

class View:

    #==== Classe Clientes ====
    @staticmethod
    def cliente_inserir(nome:str, email:str, fone:str, senha:str) -> None: #Create
        x = Cliente(0, nome, email, fone, senha)
        Clientes.inserir(x)

    @staticmethod
    def cliente_listar() -> list[Cliente]: #Read
        return Clientes.listar()

    @staticmethod
    def cliente_atualizar(id:int, nome:str, email:str, fone:str) -> None:  #Update
        x = Cliente(id, nome, email, fone)
        Clientes.atualizar(x)

    @staticmethod
    def cliente_excluir(id:int) -> None: #Delete
        x = Clientes.listar_id(id)
        Clientes.excluir(x)

    def cliente_autenticar(email:str, senha:str)-> Cliente: 
        clientes = Clientes.listar()
        for c in clientes:
            if c.email == email and c.senha == senha:
                return c

    #===== Classe Produtos ======
    @staticmethod
    def produto_inserir(desc:str, preco:float, estoq:int) -> None: #Create
        x = Produto(0,desc,preco,estoq)
        Produtos.inserir(x)

    @staticmethod
    def produto_listar() -> list[Produtos]: #Read
        return Produtos.listar()

    @staticmethod
    def produto_atualizar(id:int, desc:str, preco:float, estoq:int) -> None : #Update
        x = Produto(id,desc,preco,estoq)
        Produtos.atualizar(x)

    @staticmethod
    def produto_excluir(id:int) -> None: #Delete
        x = Produtos.listar_id(id)
        Produtos.excluir(x)


    #===== Classe Categorias ======
    @staticmethod
    def categoria_inserir(desc:str)->None: #Create
        x = Categoria(0, desc)
        Categorias.inserir(x)

    @staticmethod
    def categoria_listar() -> list[Categoria]: #Read
        return Categorias.listar()

    @staticmethod
    def categoria_atualizar(id:int, desc:str) -> None: #Update
        x = Categoria(id,desc)
        Categorias.atualizar(x)

    @staticmethod
    def categoria_excluir(id:int) -> None: #Delete
        x = Categorias.listar_id(id)
        Categorias.excluir(x)


    #===== Classe Vendas =====
    @staticmethod
    def venda_listar() -> list[Venda]:
        return Vendas.listar()
    

    
    #===== Classe VendasItem =====
    @staticmethod
    def vendaitem_listar() -> list[VendaItem]:
        return VendaItems.listar() 
    
    #===== Venda Operações ======
    @staticmethod
    def venda_iniciar() -> Venda:

        x =  Venda(0) #Cria um carrinho
        Vendas.inserir(x) #Joga na lista
        return x #Retorna um carrinho para por no contexto

    @staticmethod
    def venda_inserir_item(item_id:int, qtd:int, id_carrinho:int) -> None:

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
    def venda_confirmar(carrinho_id:int) -> None:
        items = VendaItems.listar() #Listando items
        carrinho = Vendas.listar_id(carrinho_id) #Pegando carrinho pelo id

        for i in items:
            if carrinho_id == i.idVenda: #Verifica se o item pertence aquela compra
                prod = Produtos.listar_id(i.idProduto) #Pega o produto a partir do item venda
                prod.estoque -=  i.qtd #Remove do estoque
                Produtos.atualizar(prod) #Salva na memoria

        carrinho.carrinho = False #Finaliza o carrinho
        Vendas.atualizar(carrinho) #Joga na memoria
        return None #Retorna vazio para aplicar novamente no carrinho
