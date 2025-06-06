from views import View

class UI:
    carrinho = None

    @staticmethod
    def menu() -> int:
        print("\n#================ LOGIN =================#")
        print("Selecione o tipo de login: \n")
        print("1. Admin | 2. Cliente | 9. Sair")
        usr = input("\n- Digite o número da opção desejada: ")
            
        if usr == "1":
            print("\n#================== MENU ADMIN ===================#")
            print("Selecione o item que quer editar\n")
            print("1. Cliente | 2. Produto | 3. Categoria | 9. Sair\n")
            op = usr+input("- Digite o número da opção desejada: ")

            if op == "11":
                print("\n#====================== CLIENTE ======================#")
                print("Selecione uma das opções:\n")
                print("1. Listar    | 2. Inserir | 3. Atualizar | 4. Excluir\n")
                op += input("- Digite o número da opção desejada: ")

            elif op == "12":
                print("\n#====================== PRODUTO ======================#")
                print("Selecione uma das opções:\n")
                print("1. Listar    | 2. Inserir | 3. Atualizar | 4. Excluir\n")
                op += input("- Digite o número da opção desejada: ")

            elif op == "13":
                print("\n#===================== CATEGORIA =====================#")
                print("Selecione uma das opções:\n")
                print("1. Listar    | 2. Inserir | 3. Atualizar | 4. Excluir\n")
                op += input("- Digite o número da opção desejada: ")

            

            elif op =="19":
                return 9

            return int(op)
        
        elif usr == "2":
            print("\n#======================== MENU CLIENTE ========================#")
            print("Selecione o item que quer editar\n")
            print("1. Iniciar carrinho de compras | 2. Listar as compras")
            print("3. Listar carrinho de compras  | 4. Inserir produto no carrinho")
            print("5. Confirmar compra            | 9. Sair\n")

            op = usr+input("- Digite o número da opção desejada: ")
            if op == "29":
                return 9

            return int(op)
        
        elif usr =="9":
            return 9
        
    @staticmethod
    def main():
        while True:
            op = UI.menu()

            if op == 111: UI.cliente_listar()
            elif op == 112: UI.cliente_inserir()
            elif op == 113: UI.cliente_atualizar()
            elif op == 114: UI.cliente_excluir()

            elif op == 121: UI.produto_listar()
            elif op == 122: UI.produto_inserir()
            elif op == 123: UI.produto_atualizar()
            elif op == 124: UI.produto_excluir()

            elif op == 131: UI.categoria_listar()
            elif op == 132: UI.categoria_inserir()
            elif op == 133: UI.categoria_atualizar()
            elif op == 134: UI.categoria_excluir()

            elif op == 21: UI.venda_iniciar()
            elif op == 22: UI.venda_listar()
            elif op == 23: UI.venda_listar_carrinho()
            elif op == 24: UI.venda_inserir_item()
            elif op == 25: UI.venda_confirmar()

            elif op == 9 : print("\nSistema Encerrado!!! Até Mais🤙️"); break

            else: print("Opção inválida!")

    #====== CRUD Cliente ======
    @staticmethod
    def cliente_listar():
        print()
        for c in View.cliente_listar(): print(c)
            
    @staticmethod
    def cliente_inserir():
        print()
        nome = input("Digite o nome do cliente:")
        email = input("Digite o email do cliente:")
        fone = input("Digite o telefone do cliente:")
        View.cliente_inserir(nome,email,fone)
       
    @staticmethod
    def cliente_atualizar():
        print()
        id = int(input("Digite o ID o cliente que deseja atualizar: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")        
        View.cliente_atualizar(id, nome, email, fone)
      
    @staticmethod
    def cliente_excluir():
        print()
        id = int(input("Digite o ID o cliente que deseja excluir: "))
        View.cliente_excluir(id)
       

    #====== CRUD Produto======

    @staticmethod
    def produto_listar():
        print()
        for c in View.produto_listar():
            print(c)
        
    @staticmethod
    def produto_inserir():
        desc = input("Digite a descrição do produto:")
        preco = float(input("Digite o preço do produto:"))
        estoq = int(input("Digite a quantidade em estoque:"))
        View.produto_inserir(desc, preco, estoq)
        
    @staticmethod
    def produto_atualizar():
        id = int(input("Digite o ID do produto que deseja atualizar: "))
        desc = input("Digite a nova descrição:")
        preco = float(input("Digite o novo preço: "))
        estoq = int(input("Digite a quantidade em estoque atualizada:"))
        View.produto_atualizar(id, desc, preco, estoq)
        

    @staticmethod
    def produto_excluir():
        id = int(input("Digite o ID do produto que deseja excluir: "))
        View.produto_excluir(id)
        

    #====== CRUD Categoria======

    @staticmethod
    def categoria_listar():
        print()
        for c in View.categoria_listar():
            print(c)
        

    @staticmethod
    def categoria_inserir():
        desc = input("Digite a descrição do produto:")
        View.categoria_inserir(desc)

    @staticmethod
    def categoria_atualizar():
        id = int(input("Digite o ID da categoria que deseja atualizar: "))
        desc = input("Digite a nova descrição:")
        View.categoria_atualizar(id, desc)
        

    @staticmethod
    def categoria_excluir():
        id = int(input("Digite o ID da categoria que deseja excluir: "))
        View.categoria_excluir(id)

    #======= Venda==========
    @classmethod
    def venda_iniciar(cls):
        cls.carrinho = View.venda_iniciar()
        print("\n*** Carrinho de compras iniciado com sucesso! ✅️")
        
    @classmethod    
    def venda_inserir_item(cls):
        if cls.carrinho is None: #Verificando se tem carrinho
            print("\n*** Para inserir um produto é necessario iniciar um carrinho! ⚠️")
            return
        
        print()
        UI.produto_listar() #Listando Produtos
        print("\nDigite -1 para sair\n")

        #Coletando informaçao para adicionar produto
        item_id = int(input("Insira o codigo do produto: "))
        if item_id == -1: return #Condição de parada para o laço recursivo
        qtd = int(input("Digite a quantidade: "))
        View.venda_inserir_item(item_id, qtd, cls.carrinho.id) #Chamando função do view para adicionar ao carrinho

        print(f"\n*** Produto adicionado com sucesso! ✅️***")
        UI.venda_inserir_item() #Repetindo novamente a operação novamente
        
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
            print("\n*** Você ainda não tem carrinho ⚠️")
            return
        print()
    
        cls.carrinho = View.venda_confirmar(cls.carrinho.id)
        
UI.main()




