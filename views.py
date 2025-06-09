from dao.clientes import Cliente, Clientes
from dao.produtos import Produto, Produtos
from dao.categorias import Categoria, Categorias
from dao.vendas import Venda, Vendas
from dao.vendaitems import VendaItem, VendaItems

class View:

    #==== Classe Clientes ====
    @staticmethod
    def cliente_inserir(nome:str, email:str, fone:str, senha:str) -> None: #Create
        #Regras email
        if email == '':
            raise ValueError("O email é obrigatório!")
        for c in Clientes.listar():
            if c.email == email:
                raise ValueError("O email já está em uso!")
            
        #Regras senha
        if senha == '':
            raise ValueError("O senha é obrigatório!")
        tamanho = len(senha) 
        if tamanho < 4:
            raise ValueError("A senha deve ter pelo menos 4 caracteres")
       
        #Criação e adição do objeto
        x = Cliente(0, nome, email, fone, senha)
        Clientes.inserir(x)

    @staticmethod
    def cliente_listar() -> list[Cliente]: #Read
        return Clientes.listar()

    @staticmethod
    def cliente_atualizar(id:int, nome:str, email:str, fone:str, senha:str) -> None:  #Update
        c = Clientes.listar_id(id)

        #Regra de atualização
        if c is None:
            raise ValueError("Id de cliente não encontrado")
        
        x = Cliente(id, nome, email, fone, senha)
        Clientes.atualizar(x)
        

    @staticmethod
    def cliente_excluir(id:int) -> None: #Delete
        x = Clientes.listar_id(id)

        #Regra de exclusão
        if x is None:
            raise ValueError("Id de cliente não encontrado")
        
        Clientes.excluir(x)
        
    @staticmethod
    def cliente_autenticar(email:str, senha:str)-> Cliente: 
        for c in Clientes.listar():
            if c.email == email and c.senha == senha:
                return c
        
        raise ValueError("Credenciais inválidas!")
    
    @staticmethod
    def admin_criar():
        for cliente in Clientes.listar():
            if cliente.email == "admin" : return
        View.cliente_inserir("#", "admin", "#","admin")    
     



    #===== Classe Produtos ======
    @staticmethod
    def produto_inserir(desc:str, preco:float, estoq:int) -> None: #Create
        x = Produto(0,desc,preco,estoq)
        Produtos.inserir(x)

    @staticmethod
    def produto_listar() -> list[Produtos]: #Read
        return Produtos.listar()

    @staticmethod
    def produto_atualizar(id:int, desc:str, preco:float, estoq:int) -> None: #Update
        x = Produto(id,desc,preco,estoq)
        c = Produtos.listar_id(id)
        if c is None:
            raise ValueError("Produto não encontrado")
        Produtos.atualizar(x)
       

    @staticmethod
    def produto_excluir(id:int) -> None: #Delete
        x = Produtos.listar_id(id)
        if x is None:
            raise ValueError("Produto não encontrado")
        Produtos.excluir(x)
        

    @staticmethod
    def produto_reajuste(percentual:float)-> None:
        for p in Produtos.listar():
            p.preco += percentual/100*p.preco
            Produtos.atualizar(p)

    


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
        c = Categorias.listar_id(id)
        if c is None:
            raise ValueError("Categoria não encontrado")
        Categorias.atualizar(x)
        
    @staticmethod
    def categoria_excluir(id:int) -> None: #Delete
        x = Categorias.listar_id(id)
        if x is None:
            raise ValueError("Categoria não encontrado")
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
    def venda_iniciar(idCliente:int) -> Venda:
        for carrinho in Vendas.listar():
           if carrinho.idCliente == idCliente and carrinho.carrinho: #Verifica se a venda é do cliente e se a venda está no carrinho
               raise ValueError("Você ja tem um carrinho iniciado!")
        x =  Venda(0) #Cria um carrinho
        x.idCliente = idCliente
        Vendas.inserir(x) #Joga na lista
        return x #Retorna um carrinho para por no contexto

    @staticmethod
    def venda_inserir_item(item_id:int, qtd:int, id_carrinho:int) -> None:
        
        item = Produtos.listar_id(item_id) #Pegando o produto da lista de produtos

        #Verificação de erros
        if item is None:
            raise ValueError("Id do produto não encontrado")
        if qtd < 0:
            raise ValueError("A quantidade não pode ser negativa")
        if qtd > item.estoque:
            raise ValueError("Estoque insuficiente para compra")
        
        carrinho = Vendas.listar_id(id_carrinho) #Pegando o carrinho
        preco = item.preco*qtd #Calculando o preço do vendaitem

        
        #Verifica se o item ja está no carrinho caso esteja ele não cria um itemvenda novo so acrescenta
        for i in VendaItems.listar():
            if i.idProduto == item_id and i.idVenda == id_carrinho:
                if qtd + i.qtd > item.estoque:
                    raise ValueError(f"Estoque insuficiente para compra do {item.descricao}") #Verifica se tem o item em estoque
                i.qtd += qtd
                i.preco += preco #Adiciona o valor ao itemvenda
                VendaItems.atualizar(i)#Atualiza o itemvenda na persistencia 

                carrinho.total += preco #Adicionando valor ao total no carrinho
                Vendas.atualizar(carrinho)#SAlvando valor na persistencia
                return

        #Caso contrario Adiciona um novo item
        venda = VendaItem(0,qtd,preco) #Montando o item de venda
        venda.idProduto = item.id #Associando itemvenda ao produto
        venda.idVenda = carrinho.id #Associando ao carrinho

        VendaItems.inserir(venda) #Adicionando item ao carrinho

        carrinho.total += preco #Adicionando valor ao total no carrinho
        Vendas.atualizar(carrinho)#SAlvando valor na persistencia

    @staticmethod
    def venda_excluir_item(item_id:int, qtd:int, id_carrinho:int) -> None:

        item = Produtos.listar_id(item_id) #Pegando o produto da lista de produtos
        carrinho = Vendas.listar_id(id_carrinho) #Pegando o carrinho

        if item is None:
            raise ValueError("Id do produto não encontrado")
        if qtd < 0:
            raise ValueError("A quantidade não pode ser negativa")
        
        preco = item.preco*qtd #Calculando o preço do vendaitem

        for i in VendaItems.listar():
            if i.idProduto == item_id and i.idVenda == id_carrinho:
                if i.qtd < qtd:
                    raise ValueError(f"Você está tentando remover mais itens do que há no carrinho.") #Verifica se tem o item em estoque
                i.qtd -= qtd
                i.preco -= preco #Adiciona o valor ao itemvenda

                if i.qtd <= 0:
                    VendaItems.excluir(i) #Se tiver menos que 1 remove o item
                else:
                    VendaItems.atualizar(i)#Atualiza o itemvenda na persistencia 

                carrinho.total -= preco #Adicionando valor ao total no carrinho
                Vendas.atualizar(carrinho)#SAlvando valor na persistencia
                return
        
        raise ValueError("Id do produto não encontrado no carrinho")
            
        

      
        

    @staticmethod
    def venda_confirmar(carrinho_id:int) -> None:
        items = VendaItems.listar() #Listando items
        carrinho = Vendas.listar_id(carrinho_id) #Pegando carrinho pelo id

        #Verifica compra completa antes de remover do estoque: Para o caso do produto estar no carrinho mas alguem ter comprado o produto
        for i in items:
            if carrinho_id == i.idVenda: #Verifica se o item pertence aquela compra
                prod = Produtos.listar_id(i.idProduto) #Pega o produto a partir do item venda
                if prod.estoque - i.qtd < 0:
                    raise ValueError(f"Estoque insuficiente para compra do {prod.descricao}")

        #Sai removendo todas as compras do estoque
        for i in items:
            if carrinho_id == i.idVenda: #Verifica se o item pertence aquela compra
                prod = Produtos.listar_id(i.idProduto) #Pega o produto a partir do item venda
                prod.estoque -=  i.qtd #Remove do estoque
                Produtos.atualizar(prod) #Salva na memoria

        carrinho.carrinho = False #Finaliza o carrinho
        Vendas.atualizar(carrinho) #Joga na memoria
        return None #Retorna vazio para aplicar novamente no carrinho

    @staticmethod
    def carregar_carrinho(clienteid) -> Venda:
       for carrinho in Vendas.listar():
           if carrinho.idCliente == clienteid and carrinho.carrinho: #Verifica se a venda é do cliente e se a venda está no carrinho
               return carrinho