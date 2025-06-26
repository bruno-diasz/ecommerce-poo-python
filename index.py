import streamlit as st
from templates.manter_cliente_ui import ManterClienteUI as MClienteUI
from templates.manter_produtos_ui import ManterProdutoUI as MProdutoUI
from templates.manter_categoria_ui import ManterCategoriaUI as MCategoriaUI
from templates.historico_venda import HistoricoVenda 
from templates.login_ui import LoginUI

class IndexUI:

    @staticmethod
    def menu_visitante():
        if 'op' not in st.session_state:
            st.session_state.op = 0
        with st.sidebar:
            st.title(':red[Bem-Vindo Visitante] :smile:')
            st.write('---')

            if st.button('**:material/login: Entrar**',use_container_width=True): st.session_state.op = 1
            if st.button('**:material/person_add: Cadastrar-se**',use_container_width=True): st.session_state.op = 2


        if st.session_state.op == 1:
            LoginUI.main()
        elif st.session_state.op == 2:
            MClienteUI.inserir()
        
           

    @staticmethod
    def menu_usuario():
        st.text("logado legal")

    @staticmethod
    def menu_admin():
        if 'op' not in st.session_state:
            st.session_state.op = 0
        with st.sidebar:
            st.title(':red[Painel Administrativo]')
            st.write('---')

            if st.button('**:material/person: Gerenciar Clientes**',use_container_width=True): st.session_state.op = 1
            if st.button('**:material/package_2: Gerenciar Produtos**',use_container_width=True): st.session_state.op = 2
            if st.button('**:material/category: Gerenciar Categorias**',use_container_width=True): st.session_state.op = 3
            if st.button('**:material/receipt: Histórico de Vendas**',use_container_width=True): st.session_state.op = 4
            st.divider()
            if st.button('**:material/logout: Sair da Conta**',use_container_width=True): st.session_state.op = 5

        if st.session_state.op == 1:
            MClienteUI.main()
        elif st.session_state.op == 2:
            MProdutoUI.main()
        elif st.session_state.op == 3:
            MCategoriaUI.main()
        elif st.session_state.op == 4:
            HistoricoVenda.main()
        elif st.session_state.op == 5:
            IndexUI.logout()

    @staticmethod
    def sidebar():
        if "usr" not in st.session_state:
            IndexUI.menu_visitante()
        elif st.session_state.usr.email == "admin":
            IndexUI.menu_admin()
        else:
            IndexUI.menu_usuario()

    @staticmethod
    def logout():
        del st.session_state.usr
        st.rerun()
        
    @staticmethod
    def main():
      
        IndexUI.sidebar()
        # imagem = st.file_uploader('texte', type='png,jpg')
        # if imagem is not None:
        #     st.image(imagem, width=110)

IndexUI.main()
        
    