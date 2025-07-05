import streamlit as st
from views import View
from templates.manter_usuario_ui import ManterUsuarioUI as MUsuarioUI
from templates.manter_produtos_ui import ManterProdutoUI as MProdutoUI
from templates.manter_categoria_ui import ManterCategoriaUI as MCategoriaUI
from templates.gerenciar_vendas_ui import GerenciarVendas
from templates.minhas_compras_ui import MinhasCompras
from templates.minhas_entregas_ui import MinhasEntregas
from templates.catalogo_produtos_ui import CatalogoProdutos
from templates.checkout_ui import CheckOut
from templates.login_ui import LoginUI

class IndexUI:

    @staticmethod
    def menu_visitante():
        if 'op' not in st.session_state:
            st.session_state.op = 0
       
        with st.sidebar:
            st.title(':red[Bem-Vindo, Visitante!] :smile:',)
            st.write('---')

            if st.button('**:material/login: Entrar**',use_container_width=True): st.session_state.op = 1
            if st.button('**:material/person_add: Cadastrar-se**',use_container_width=True): st.session_state.op = 2


        if st.session_state.op == 1:
            LoginUI.main()
        elif st.session_state.op == 2:
            MUsuarioUI.inserir()
        
           

    @staticmethod
    def menu_cliente():
        if 'op' not in st.session_state:
            st.session_state.op = 0
        with st.sidebar:
            st.title(':red[Área do Cliente]')
            st.subheader(f"E aí, :red[{st.session_state.usr.nome.split()[0]}]! Bem-vindo(a) de volta! ")
            st.write('---')
            
            if st.button('**:material/package_2: Catálogo de Produtos**',use_container_width=True): st.session_state.op = 1
            if st.button('**:material/shopping_cart: Carrinho de Compras**',use_container_width=True): st.session_state.op = 2
            if st.button('**:material/receipt: Minhas Compras**',use_container_width=True): st.session_state.op = 3
            st.divider()
            if st.button('**:material/logout: Sair da Conta**',use_container_width=True): st.session_state.op = 4

        if st.session_state.op == 1:
            CatalogoProdutos.main()
        elif st.session_state.op == 2:
            CheckOut.main()
        elif st.session_state.op == 3:
            MinhasCompras.main()
        elif st.session_state.op == 4:
            IndexUI.logout()

    @staticmethod
    def menu_entregador():
        if 'op' not in st.session_state:
            st.session_state.op = 0
        with st.sidebar:
            st.title(':red[Área do Entregador]')
            st.subheader(f"E aí, :red[{st.session_state.usr.nome.split()[0]}]! Bem-vindo(a) de volta! ")
            st.write('---')
            
            if st.button('**:material/local_shipping: Minhas Entregas**',use_container_width=True): st.session_state.op = 1
            st.divider()
            if st.button('**:material/logout: Sair da Conta**',use_container_width=True): st.session_state.op = 2

        if st.session_state.op == 1:
            MinhasEntregas.main()
        elif st.session_state.op == 2:
            IndexUI.logout()

    @staticmethod
    def menu_admin():
        if 'op' not in st.session_state:
            st.session_state.op = 0
        with st.sidebar:
            st.title(':red[Painel Administrativo]')
            st.subheader(f"E aí, :red[{st.session_state.usr.nome.split()[0]}]! Bem-vindo(a) de volta! ")
            st.write('---')

            if st.button('**:material/person: Gerenciar Usuarios**',use_container_width=True): st.session_state.op = 1
            if st.button('**:material/package_2: Gerenciar Produtos**',use_container_width=True): st.session_state.op = 2
            if st.button('**:material/category: Gerenciar Categorias**',use_container_width=True): st.session_state.op = 3
            if st.button('**:material/receipt: Gerenciar de Vendas**',use_container_width=True): st.session_state.op = 4
            st.divider()
            if st.button('**:material/logout: Sair da Conta**',use_container_width=True): st.session_state.op = 5

        if st.session_state.op == 1:
            MUsuarioUI.main()
        elif st.session_state.op == 2:
            MProdutoUI.main()
        elif st.session_state.op == 3:
            MCategoriaUI.main()
        elif st.session_state.op == 4:
            GerenciarVendas.main()
        elif st.session_state.op == 5:
            IndexUI.logout()

    @staticmethod
    def sidebar():
        if "usr" not in st.session_state:
            IndexUI.menu_visitante()
        elif st.session_state.usr.funcao == "admin":
            IndexUI.menu_admin()
        elif st.session_state.usr.funcao == "entregador":
            IndexUI.menu_entregador()
        elif st.session_state.usr.funcao == "cliente":
            IndexUI.menu_cliente()

    @staticmethod
    def logout():
        del st.session_state.usr
        st.rerun()
        
    @staticmethod
    def main():
        View.sem_categoria_criar()
        View.admin_criar()
        IndexUI.sidebar()
       
       
          
        
        

IndexUI.main()
        
    