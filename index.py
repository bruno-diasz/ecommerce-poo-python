import streamlit as st
from templates.manter_cliente_ui import ManterClienteUI as MClienteUI
from templates.manter_categoria_ui import ManterCategoriaUI as MCategoriaUI
from templates.historico_venda import HistoricoVenda 

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
            if st.button('**:material/package_2: Gerenciar Produto**', type='tertiary'): st.session_state.op = 2
            if st.button('**:material/category: Gerenciar Categorias**', type='tertiary'): st.session_state.op = 3
            if st.button('**:material/receipt: Histórico de Vendas**', type='tertiary'): st.session_state.op = 4


        if st.session_state.op == 1:
            MClienteUI.main()
        elif st.session_state.op == 2:
            pass
        elif st.session_state.op == 3:
            MCategoriaUI.main()
        elif st.session_state.op == 4:
            HistoricoVenda.main()

    @staticmethod
    def sidebar():
        IndexUI.menu_admin()
    
    @staticmethod
    def main():
        IndexUI.sidebar()
        

IndexUI.main()
        
    