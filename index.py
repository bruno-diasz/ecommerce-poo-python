import streamlit as st
from templates.manter_cliente_ui import ManterClienteUI as MClienteUI
from templates.manter_categoria_ui import ManterCategoriaUI as MCategoriaUI

class IndexUI:

    @staticmethod
    def menu_admin():
        if 'op' not in st.session_state:
            st.session_state.op = 0
        with st.sidebar:
            st.title(':red[Painel Administrativo]')
            st.write('---')

            #===MENU ALTERNATIVO ===
            # if st.button('**:material/person: Gerenciar Clientes**',use_container_width=True): st.session_state.op = 1
            # st.button('**:material/package_2: Gerenciar Produto**',use_container_width=True)
            # st.button('**:material/category: Gerenciar Categorias**',use_container_width=True)
            # st.button('**:material/receipt: Histórico de Vendas**',use_container_width=True)

            if st.button('**:material/person: Gerenciar Clientes**', type='tertiary'): st.session_state.op = 1
            st.button('**:material/package_2: Gerenciar Produto**', type='tertiary')
            if st.button('**:material/category: Gerenciar Categorias**', type='tertiary'): st.session_state.op = 2
            st.button('**:material/receipt: Histórico de Vendas**', type='tertiary')


        if st.session_state.op == 1:
            MClienteUI.main()
        elif st.session_state.op == 2:
            MCategoriaUI.main()

    @staticmethod
    def sidebar():
        IndexUI.menu_admin()
    
    @staticmethod
    def main():
        IndexUI.sidebar()
        

IndexUI.main()
        
    