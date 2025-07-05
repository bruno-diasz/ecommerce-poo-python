from dao.usuarios import Usuario, Usuarios
from dao.produtos import Produto, Produtos
from dao.categorias import Categoria, Categorias
from dao.vendas import Venda, Vendas
from dao.vendaitems import VendaItem, VendaItems
import base64

class View:

    #==== Classe Usuarios ====
    @staticmethod
    def usuario_inserir(nome:str, email:str, fone:str, senha:str,senha2:str, funcao:str) -> None: #Create
        #Regras do nome
        if nome.strip() == "":
            raise ValueError("Preencher o nome é obrigatorio")
        
        #Regras email
        if email.strip() == '':
            raise ValueError("Preecher o email é obrigatório!")
        for c in Usuarios.listar():
            if c.email == email:
                raise ValueError("O email já está em uso!")
            
        #Regras senha
        if senha == '':
            raise ValueError("Preencher a senha é obrigatório!")
        tamanho = len(senha) 
        if tamanho < 4:
            raise ValueError("A senha deve ter pelo menos 4 caracteres")
        if senha != senha2:
            raise ValueError("As senhas não correspondem")
        
            
       
        #Criação e adição do objeto
        x = Usuario(0, nome, email, fone, senha,funcao)
        Usuarios.inserir(x)

    @staticmethod
    def usuario_listar() -> list[Usuario]: #Read
        return Usuarios.listar()

    @staticmethod
    def usuario_atualizar(id:int, nome:str, email:str, fone:str, senha:str,senha2:str, funcao:str) -> None:  #Update
        c = Usuarios.listar_id(id)

        #Regra de atualização
        if c is None:
            raise ValueError("Id de usuario não encontrado")
        
         #Regras do nome
        if nome.strip() == "":
            raise ValueError("Preencher o nome é obrigatorio")
        
        #Regras email
        if email.strip() == '':
            raise ValueError("Preecher o email é obrigatório!")
        
        for c in Usuarios.listar():
            if email == c.email and email != Usuarios.listar_id(id).email:
                raise ValueError("O email já está em uso!")
            
        #Regras senha
        if senha == '':
            raise ValueError("Preencher a senha é obrigatório!")
        tamanho = len(senha) 
        if tamanho < 4:
            raise ValueError("A senha deve ter pelo menos 4 caracteres")
        if senha != senha2:
            raise ValueError("As senhas não correspondem")
        
       
        
        x = Usuario(id, nome, email, fone, senha, funcao)
        Usuarios.atualizar(x)
        

    @staticmethod
    def usuario_excluir(id:int) -> None: #Delete
        x = Usuarios.listar_id(id)

        #Regra de exclusão
        if x is None:
            raise ValueError("Id de usuario não encontrado")
        
        Usuarios.excluir(x)
        
    @staticmethod
    def usuario_autenticar(email:str, senha:str)-> Usuario: 
        for c in Usuarios.listar():
            if c.email == email and c.senha == senha:
                return c
        
        raise ValueError("Credenciais inválidas!")
    
    @staticmethod
    def admin_criar():
        for usuario in Usuarios.listar():
            if usuario.funcao == "admin" : return
        View.usuario_inserir("admin", "admin", "","admin","admin")    
     



    #===== Classe Produtos ======
    @staticmethod
    def produto_inserir(desc:str, preco:float, estoq:int, imagem:object, categoriaID:int) -> None: #Create
        #Transformando imagem em texto
        if imagem is not None:
            imagem_bytes = imagem.read()
            imagem_b64 = base64.b64encode(imagem_bytes).decode('utf-8')
        else:
            #caso nao selecione nenhuma foto poe uma foto padrao para nao quebrar o layout
            caminho_imagem = "assets/no_image.jpg"
            with open(caminho_imagem, "rb") as imagem_df:
                imagem_bytes = imagem_df.read()
                imagem_b64 = base64.b64encode(imagem_bytes).decode('utf-8')

        #Erros
        if desc.strip() == "":
            raise ValueError("O produto deve ter um nome")


        #Criando objeto
        x = Produto(0,desc.title(),round(preco,2),estoq,imagem_b64, categoriaID)
        Produtos.inserir(x)

    @staticmethod
    def produto_listar() -> list[Produtos]: #Read
        return Produtos.listar()
    
    @staticmethod
    def produto_listar_id(produto_id) -> Produtos: 
        return Produtos.listar_id(produto_id)
    
    @staticmethod
    def produto_listar_categoria(categoria_id) -> list[Produto]:
        if categoria_id == 0:
            pass
        elif not Categorias.listar_id(categoria_id) :
            raise ValueError("Categoria não encontrada")
        
        produto_categoria = []
        for prod in Produtos.listar():
            if prod.idCategoria == categoria_id:
                produto_categoria.append(prod)
        
        return produto_categoria

    @staticmethod
    def produto_atualizar(id:int, desc:str, preco:float, estoq:int, imagem:object, categoriaID:int) -> None: #Update

        c = Produtos.listar_id(id)
        if c is None:
            raise ValueError("Produto não encontrado")
        
        #Tranformando imagem em texto
        if imagem is not None:
            imagem_bytes = imagem.read()
            imagem_b64 = base64.b64encode(imagem_bytes).decode('utf-8')
        else:
            imagem_b64 = c.imagem

         
        if desc.strip() == "":
            raise ValueError("O produto deve ter um nome")
        
        #Aumentando o preço dos produtos que estão no carrinho
      
        for item in VendaItems.listar():
            venda = Vendas.listar_id(item.idVenda)
            if item.idProduto == id:
                if venda.carrinho:
                    venda.total -= (item.preco)*item.qtd
                    venda.total += (preco)*item.qtd
                    venda.total = round(venda.total,2)
                    Vendas.atualizar(venda)

                    item.preco = preco
                    item.preco = round( item.preco,2)
                    VendaItems.atualizar(item)

        #Criando objeto
        x = Produto(id,desc.title(),round(preco,2),estoq, imagem_b64, categoriaID)
        
        Produtos.atualizar(x)

       

    @staticmethod
    def produto_excluir(id:int) -> None: #Delete
        x = Produtos.listar_id(id)
        if x is None:
            raise ValueError("Produto não encontrado")
        Produtos.excluir(x)
        

    @staticmethod
    def produto_reajuste(percentual:float)-> None:

        if percentual < -100:
            raise ValueError("A porcentagem de desconto não pode ser maior que 100%")
        if percentual == 0:
            raise ValueError("A porcentagem de reajustes não pode ser igual a 0%")
        
        for p in Produtos.listar():
            p.preco += percentual/100*p.preco
            p.preco = round(p.preco, 2)
            Produtos.atualizar(p)

        #Aumentando o preço dos produtos que estão no carrinho
        for item in VendaItems.listar():
            venda = Vendas.listar_id(item.idVenda)
            if venda.carrinho:
                venda.total += (percentual/100*item.preco)*item.qtd
                venda.total = round(venda.total,2)
                Vendas.atualizar(venda)
                item.preco += percentual/100*item.preco
                item.preco = round( item.preco,2)
                VendaItems.atualizar(item)

    @staticmethod
    def produto_vincular_categoria(id_produto:int, id_categoria:int)-> None:
        prod = Produtos.listar_id(id_produto)
        cat = Categorias.listar_id(id_categoria)
        
        if prod is None:
            raise TypeError("Produto não encontrado")
        if cat is None:
            raise TypeError("Categoria não encontrado")
        prod.idCategoria = id_categoria
        Produtos.atualizar(prod)
    


    #===== Classe Categorias ======
    @staticmethod
    def categoria_inserir(desc:str)->None: #Create
        #Validações
        if desc == "":
            raise ValueError("A descrição da categoria não pode estar vazia")
        for categoria in Categorias.listar():
            if categoria.descricao.strip().lower() == desc.strip().lower():
                raise ValueError("Ja existe uma categoria com esse nome!")
        x = Categoria(0, desc.capitalize())
        Categorias.inserir(x)

    @staticmethod
    def categoria_listar() -> list[Categoria]: #Read
        return Categorias.listar()

    @staticmethod
    def categoria_atualizar(id:int, desc:str) -> None: #Update
        x = Categoria(id,desc.capitalize())
        c = Categorias.listar_id(id)

        #Validações
        if desc == "":
            raise ValueError("A descrição da categoria não pode estar vazia")
        
        for categoria in Categorias.listar():
            if categoria.descricao.strip().lower() == desc.strip().lower():
                raise ValueError("Ja existe uma categoria com esse nome!")

        if c is None:
            raise ValueError("Categoria não encontrado")
        if id == 0:
            raise ValueError('A categoria padrão, "Sem Categoria" não pode ser editada')
        Categorias.atualizar(x)
        
    @staticmethod
    def categoria_excluir(id:int) -> None: #Delete
        x = Categorias.listar_id(id)

        #Validações 
        if x is None:
            raise ValueError("Categoria não encontrado")
        if id == 0:
            raise ValueError('A categoria padrão, "Sem Categoria" não pode ser excluida')

        for produto in View.produto_listar():
            if produto.idCategoria == id:
                raise ValueError("Não é possivel apagar a categoria, existem produtos associados a ela!")
        
        Categorias.excluir(x)
    
    @staticmethod
    def sem_categoria_criar():
        if Categorias.listar_id(0) is None:
            x = Categoria(0,"Sem Categoria")
            Categorias.inserir(x)


  
        

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
    def venda_inserir_item(item_id:int, qtd:int, id_carrinho:int) -> None:
        
        item = Produtos.listar_id(item_id) #Pegando o produto da lista de produtos

        #Verificação de erros
        if item is None:
            raise ValueError("Id do produto não encontrado")
        if qtd <= 0:
            raise ValueError("A quantidade deve ser maior que zero!")
        if qtd > item.estoque:
            raise ValueError("Estoque insuficiente para compra")
        
        
        carrinho = Vendas.listar_id(id_carrinho) #Pegando o carrinho
        preco = item.preco #Pegando o preço do vendaitem

        
        #Verifica se o item ja está no carrinho caso esteja ele não cria um itemvenda novo so acrescenta
        for i in VendaItems.listar():
            if i.idProduto == item_id and i.idVenda == id_carrinho:
                if qtd + i.qtd > item.estoque:
                    raise ValueError(f"Estoque insuficiente para compra do {item.descricao}") #Verifica se tem o item em estoque
                i.qtd += qtd
                VendaItems.atualizar(i)#Atualiza o itemvenda na persistencia 

                carrinho.total += preco*qtd #Adicionando valor ao total no carrinho
                Vendas.atualizar(carrinho)#SAlvando valor na persistencia
                return

        #Caso contrario Adiciona um novo item
        venda = VendaItem(0,qtd,preco) #Montando o item de venda
        venda.idProduto = item.id #Associando itemvenda ao produto
        venda.idVenda = carrinho.id #Associando ao carrinho

        VendaItems.inserir(venda) #Adicionando item ao carrinho

        carrinho.total += preco*qtd #Adicionando valor ao total no carrinho
        Vendas.atualizar(carrinho)#SAlvando valor na persistencia

    @staticmethod
    def venda_excluir_item(item_id:int, qtd:int, id_carrinho:int) -> None:

        item = Produtos.listar_id(item_id) #Pegando o produto da lista de produtos
        carrinho = Vendas.listar_id(id_carrinho) #Pegando o carrinho

        if item is None:
            raise ValueError("Id do produto não encontrado")
        if qtd <= 0:
            raise ValueError("A quantidade deve ser maior que zero!")
        
        preco = item.preco #Calculando o preço do vendaitem

        for i in VendaItems.listar():
            if i.idProduto == item_id and i.idVenda == id_carrinho:
                if i.qtd < qtd:
                    raise ValueError(f"Você está tentando remover mais itens do que há no carrinho.") #Verifica se tem o item em estoque
                
                i.qtd -= qtd #Reduz a quantidade do produto

                if i.qtd <= 0:
                    VendaItems.excluir(i) #Se tiver menos que 1 remove o item
                else:
                    VendaItems.atualizar(i)#Atualiza o itemvenda na persistencia 

                carrinho.total -= preco*qtd #Adicionando valor ao total no carrinho
                Vendas.atualizar(carrinho)#SAlvando valor na persistencia 
                return
        
        raise ValueError("Id do produto não encontrado no carrinho")
            
        

      
        

    @staticmethod
    def venda_confirmar(carrinho_id:int) -> None:
        items = VendaItems.listar() #Listando items
        carrinho = Vendas.listar_id(carrinho_id) #Pegando carrinho pelo id
        items_do_carrinho= []
        #Verifica compra completa antes de remover do estoque: Para o caso do produto estar no carrinho mas alguem ter comprado o produto
        for i in items:
            if carrinho_id == i.idVenda: #Verifica se o item pertence aquela compra
                prod = Produtos.listar_id(i.idProduto) #Pega o produto a partir do item venda
                items_do_carrinho.append(prod)
                if prod.estoque - i.qtd < 0:
                    raise ValueError(f"Estoque insuficiente para compra do {prod.descricao}")
                
        #Verifica se o carrinho está vazio
        if  not  items_do_carrinho:
            raise ValueError("Seu carrinho está vazio")
        
        #Sai removendo todas as compras do estoque
        for i in items:
            if carrinho_id == i.idVenda: #Verifica se o item pertence aquela compra
                prod = Produtos.listar_id(i.idProduto) #Pega o produto a partir do item venda
                prod.estoque -=  i.qtd #Remove do estoque
                Produtos.atualizar(prod) #Salva na memoria

        carrinho.carrinho = False #Finaliza o carrinho
        Vendas.atualizar(carrinho) #Joga na memoria
        return None 

    @staticmethod
    def carregar_carrinho(idCliente) -> Venda:
       #Verifica se o usuario tem um carrinho
        if idCliente == 0 :return #Se for o adm não faz nada
        for carrinho in Vendas.listar():
           if carrinho.idCliente == idCliente and carrinho.carrinho: #Verifica se a venda é do usuario e se a venda é um carrinho
               return carrinho
           
        #Se não tiver cria um novo
        x =  Venda(0) #Cria um carrinho
        x.idCliente = idCliente #associa o usuario ao carrinho
        Vendas.inserir(x) #Joga na lista
        return x #Retorna um carrinho para por no contexto
    @staticmethod
    def iniciar_entrega(idEntregador:int, idVenda:int):
        venda = Vendas.listar_id(idVenda)
        if venda is None:
            raise ValueError("Venda não encontrada")
        entregadores = [entregador for entregador in View.usuario_listar() if entregador.funcao == "entregador"]
        if idEntregador not in [e.id for e in entregadores]:
            raise ValueError("Entregador não encontrado")
        venda.idEntregador = idEntregador
        venda.entrega = "enviado"
        Vendas.atualizar(venda)
    
    @staticmethod
    def finalizar_entrega(idVenda:int):
        venda = Vendas.listar_id(idVenda)
        if venda is None:
            raise ValueError("Venda não encontrada")
        venda.entrega = "entregue"
        Vendas.atualizar(venda)
        