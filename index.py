import streamlit as st
from templates.manter_cliente_ui import ManterClienteUI as MClienteUI

class IndexUI:

    @staticmethod
    def menu_admin():
        op = 0
        with st.sidebar:
            st.title(':red[Painel Administrativo]')
            st.write('---')
            if st.button('Gerenciar Clientes',use_container_width=True,): op = 1
            st.button('Gerenciar Produto',use_container_width=True)
            st.button('Gerenciar Categorias',use_container_width=True)
            st.button('Histórico de Vendas',use_container_width=True)

        if op == 1:
            MClienteUI.main()

    @staticmethod
    def sidebar():
        IndexUI.menu_admin()
    
    @staticmethod
    def main():
        IndexUI.sidebar()
        

IndexUI.main()
        
    