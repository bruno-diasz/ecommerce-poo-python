from views import View
from getpass import getpass

class UI:
    carrinho = None
    usr = None

    @classmethod
    def menu(cls) -> int:
       
        
        if cls.usr is None: #O usuario está deslogado!
            usr_op = "1"

            print("\n#================ MENU VISITANTE =================#")
            print("Bem vindo: \n")
            print("1. Entrar | 2. Criar conta | 9. Encerrar")
            op = usr_op + input("\n- Digite o número da opção desejada: ") 

            
            return int(op)

            
        if cls.usr.email == "admin": #O Usuario é o adm!
            usr_op = "2"

            print("\n#================== MENU ADMIN ===================#")
            print("Selecione o item que quer editar\n")
            print("1. Cliente | 2. Produto | 3. Categoria | 4. Pedidos | 9. Sair\n")
            op = usr_op + input("- Digite o número da opção desejada: ") 

            if op == "21":
                print("\n#====================== CLIENTE ======================#")
                print(f"Selecione uma das opções abaixo:\n")
                print("1. Listar | 2. Inserir | 3. Atualizar | 4. Excluir\n")
                op += input("- Digite o número da opção desejada: ")

            elif op == "22":
                print("\n#====================== PRODUTO ======================#")
                print("Selecione uma das opções abaixo:\n")
                print("1. Listar | 2. Inserir | 3. Atualizar | 4. Excluir")
                print("5. Reajustar preço\n")
                op += input("- Digite o número da opção desejada: ")

            elif op == "23":
                print("\n#===================== CATEGORIA =====================#")
                print("Selecione uma das opções abaixo:\n")
                print("1. Listar | 2. Inserir | 3. Atualizar | 4. Excluir\n")
                op += input("- Digite o número da opção desejada: ")

            elif op == "24":
                print("\n#===================== PEDIDOS =====================#")
                print("Selecione uma das opções abaixo:\n")
                print("1. Ver todas as compras\n")
                op += input("- Digite o número da opção desejada: ")


            return int(op)
        
        else:# está logado, e não é o adm
            usr_op = "3"

            print("\n#======================== MENU CLIENTE ========================#")
            print(f"Oi, {cls.usr.nome}! Que bom te ver por aqui 😄\n")
            print("1. Iniciar carrinho de compras | 2. Listar as compras")
            print("3. Listar carrinho de compras  | 4. Inserir produto no carrinho")
            print("5. Confirmar compra            | 9. Sair\n")

            op = usr_op + input("- Digite o número da opção desejada: ")

            return int(op)
        
        
        
    @staticmethod
    def main():
        while True:
            View.admin_criar()
            op = UI.menu()
            
            if op == 11: UI.cliente_autenticar()
            elif op== 29 or op == 39: UI.cliente_logout()

            elif op == 12 or op == 212 : UI.cliente_inserir(op)
            elif op == 211: UI.cliente_listar()
            elif op == 213: UI.cliente_atualizar()
            elif op == 214: UI.cliente_excluir()

            elif op == 221: UI.produto_listar()
            elif op == 222: UI.produto_inserir()
            elif op == 223: UI.produto_atualizar()
            elif op == 224: UI.produto_excluir()
            elif op == 225: UI.produto_reajuste()

            elif op == 231: UI.categoria_listar()
            elif op == 232: UI.categoria_inserir()
            elif op == 233: UI.categoria_atualizar()
            elif op == 234: UI.categoria_excluir()

            elif op == 241: UI.venda_listar()

            elif op == 31: UI.venda_iniciar()
            elif op == 32: UI.venda_listar_usr()
            elif op == 33: UI.venda_listar_carrinho()
            elif op == 34: UI.venda_inserir_item()
            elif op == 35: UI.venda_confirmar()

            elif op == 19 : print("\nSistema Encerrado!!! Até Mais🤙️"); break

            else: print("\n*** Opção inválida! ⚠️")

    #====== CRUD Cliente ======

    @staticmethod
    def cliente_inserir(op): #Create
        print()
        try:
            if op == 12:
                nome = input("Digite seu nome: ")
                email = input("Digite seu email: ").strip()
                fone = input("Digite seu telefone: ")
                senha = getpass("Digite sua senha: ")

            if op == 212:
                nome = input("Digite o nome do cliente: ")
                email = input("Digite o email do cliente: ")
                fone = input("Digite o telefone do cliente: ")
                senha = getpass("Digite a senha do cliente: ")

            View.cliente_inserir(nome,email,fone,senha)

        except ValueError as e:
            print(f"\n*** {e} ⚠️")
            return
        
        else:
            print("\n*** Conta de criada com sucesso! ✅️")

    @staticmethod
    def cliente_listar(): #Read
        print()
        for c in View.cliente_listar(): print(c)
   
    @staticmethod
    def cliente_atualizar(): #Update
        print()
        try:
            id = int(input("Digite o ID o cliente que deseja atualizar: "))
            nome = input("Informe o novo nome: ")
            email = input("Informe o novo e-mail: ")
            fone = input("Informe o novo fone: ")        
            senha = getpass("Digite a senha: ")
            View.cliente_atualizar(id,nome,email,fone,senha)

        except ValueError as e:
            print(f"\n*** {e}! ⚠️")
            return
        
        else:
            print("\n*** Conta de atualizada com sucesso! ✅️")
      
    @staticmethod
    def cliente_excluir(): #Delete
        print()
        try:
            id = int(input("Digite o ID o cliente que deseja excluir: "))
            View.cliente_excluir(id)

        except ValueError as e:
            print(f"\n*** {e}! ⚠️")
            return
        
        else:
            print("\n*** Conta de excluida com sucesso! ✅️")
    
    @classmethod
    def cliente_autenticar(cls): #Login
        print()
        try:
            email = input("Digite seu email: ")
            senha = getpass("Digite sua senha: ")
            usr = View.cliente_autenticar(email, senha)
            print (usr)

        except ValueError as e:
            print(f"\n*** {e}! ⚠️")
            return
        
        else:
            print("\n*** Login efetuado com sucesso! ✅️")
            cls.usr = usr
            cls.carrinho = View.carregar_carrinho(usr.id)

    @classmethod
    def cliente_logout(cls): #Logout
        cls.usr = None
        print("\n*** Logout efetuado com sucesso! ✅️")

    #====== CRUD Produto======

    @staticmethod
    def produto_inserir(): #Create
        try:
            desc = input("Digite a descrição do produto:")
            preco = float(input("Digite o preço do produto:"))
            estoq = int(input("Digite a quantidade em estoque:"))
            View.produto_inserir(desc, preco, estoq)
        
        except ValueError as e:
            print(f"\n*** {e}! ⚠️")
        else:
            print("\n*** Produto adicionado com sucesso! ✅️")
        
    @staticmethod
    def produto_listar(): #Read
        print()
        for c in View.produto_listar():
            print(c)
        
    @staticmethod
    def produto_atualizar(): #Update
        try:
            id = int(input("Digite o ID do produto que deseja atualizar: "))
            desc = input("Digite a nova descrição:")
            preco = float(input("Digite o novo preço: "))
            estoq = int(input("Digite a quantidade em estoque atualizada:"))
            View.produto_atualizar(id, desc, preco, estoq)
        except ValueError as e:
            print(f"\n*** {e} ⚠️")
            return
        else:
            print("\n*** Produto atualizado com sucesso! ✅️")

    @staticmethod
    def produto_excluir(): #Delete
        try:
            id = int(input("Digite o ID do produto que deseja excluir: "))
            View.produto_excluir(id)

        except ValueError as e:
            print(f"\n*** {e} ⚠️")
            return
        
        else:
            print("\n*** Exclusão do produto efetuado com sucesso! ✅️")

    @staticmethod
    def produto_reajuste():
        try:
            percentual = float(input("Digite o percentual de reajuste: "))
            View.produto_reajuste(percentual)

        except ValueError as e:
            print(f"\n*** {e} ⚠️")
            return
        
        else:
            if percentual > 0:
                print(f"\n*** Aumento de {percentual}% em todos os produtos efetuado com sucesso! ✅️")
            elif percentual < 0:
                print(f"\n*** Desconto de {abs(percentual)}% em todos os produtos efetuado com sucesso! ✅️")
        

    #====== CRUD Categoria======

    @staticmethod
    def categoria_inserir(): #Create
        try:
            desc = input("Digite a descrição do produto:")
            View.categoria_inserir(desc)

        except ValueError as e:
            print(f"\n*** {e} ⚠️")
            return
        
        else:
            print("\n*** Categoria adicionada com sucesso! ✅️")

        
    @staticmethod
    def categoria_listar(): #Read
        print()
        for c in View.categoria_listar():
            print(c)

    @staticmethod
    def categoria_atualizar(): #Update
        try:
            id = int(input("Digite o ID da categoria que deseja atualizar: "))
            desc = input("Digite a nova descrição:")
            View.categoria_atualizar(id, desc)

        except ValueError as e:
            print(f"\n*** {e} ⚠️")
            return
        
        else:
            print("\n*** Categoria atualizado com sucesso! ✅️")

        

    @staticmethod
    def categoria_excluir(): #Delete
        try:
            id = int(input("Digite o ID da categoria que deseja excluir: "))
            View.categoria_excluir(id)

        except ValueError as e:
            print(f"\n*** {e} ⚠️")
            return
        
        else:
            print("\n*** Exclusão da categoria efetuado com sucesso! ✅️")

    #======= Venda==========
    @classmethod
    def venda_iniciar(cls):
        try:
            cls.carrinho = View.venda_iniciar(cls.usr.id)

        except ValueError as e:
            print(f"\n*** {e} ⚠️")
            return
        
        else:
            print("\n*** Carrinho de compras iniciado com sucesso! ✅️")
        
    @classmethod    
    def venda_inserir_item(cls):
        if cls.carrinho is None: #Verificando se tem carrinho
            print("\n*** Para inserir um produto é necessario iniciar um carrinho! ⚠️")
            return
        
        print()
        UI.produto_listar() #Listando Produtos
        print("\nDigite -1 para sair\n")

        try:
            #Coletando informaçao para adicionar produto
            item_id = int(input("Insira o codigo do produto: "))
            if item_id == -1: return #Condição de parada para o laço recursivo
            qtd = int(input("Digite a quantidade: "))
            View.venda_inserir_item(item_id, qtd, cls.carrinho.id) #Chamando função do view para adicionar ao carrinho

        except ValueError as e:
            print(f"\n*** {e} ⚠️")
            UI.venda_inserir_item() #Repetindo novamente a operação novamente
        
        else:
            print(f"\n*** Produto adicionado com sucesso! ✅️***")
            UI.venda_inserir_item() #Repetindo novamente a operação novamente
            
    @staticmethod
    def venda_excluir_item():
        UI.venda_listar_usr()
        try:
            itemid = input("Digite o id do produto que deseja remover do carrinho: ")
            qtd = input("Digite a quantidade que deseja remover: ")
            View.venda_excluir_item(itemid, qtd)
        except ValueError as e:
            print(f"\n*** {e} ⚠️")
        else:
            print("\n*** Remoção efetuado com sucesso! ✅️")
        #METODO NÃO CONCLUIDO


    @staticmethod
    def venda_listar():
        print()
        vendas = View.venda_listar()
        items = View.vendaitem_listar()
        for v in vendas:
            print(v)
            for i in items:
                if i.idVenda == v.id:
                    print("    ",i)
            print()

    @classmethod
    def venda_listar_usr(cls):
        print()
        vendas = View.venda_listar()
        items = View.vendaitem_listar()
        for v in vendas:
            if v.idCliente == cls.usr.id and not v.carrinho:
                print(v)
                for i in items:
                    if i.idVenda == v.id:
                        print("    ",i)
                print()

    @classmethod
    def venda_listar_carrinho(cls): 
        if cls.carrinho is None: #Verificando se tem carrinho
            print("\n*** Você ainda não tem carrinho ⚠️")
            return
        print()

        items = View.vendaitem_listar()
        print(cls.carrinho)
        for i in items:
            if i.idVenda == cls.carrinho.id:
                print("    ",i)

    @classmethod
    def venda_confirmar(cls): 
        if cls.carrinho is None: #Verificando se tem carrinho
            print("\n*** Você ainda não tem carrinho! ⚠️")
            return
        
        print()
    
        cls.carrinho = View.venda_confirmar(cls.carrinho.id)
        print("\n*** Compra efetuado com sucesso! ✅️")

UI.main()




