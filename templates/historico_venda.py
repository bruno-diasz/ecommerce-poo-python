import streamlit as st
import pandas as pd
from views import View

class HistoricoVenda:
    def main():

        class cabecalho:
            def __init__(self):
                pass
            def __str__(self):
                return f"{'ITEM':<27}     {'PREÇO':>15}   {'QTD':<6} {'SUBTOTAL':>25}"
                
        c = cabecalho()
        st.subheader(":material/receipt: Histórico de Vendas")
        st.write('---')
        vendas= View.venda_listar()
        items = View.vendaitem_listar()
        for venda in vendas:
            if venda.carrinho:
                with st.expander(f'ID: {venda.id} ㅤ {venda.data}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ**TOTAL: R$ {venda.total:.2f}**', icon=':material/shopping_cart:'):
                    st.caption(f'CLIENTE: {venda.idCliente}')
                    st.write('---')
                    st.write(c)
                    for item in items:
                        if item.idVenda == venda.id:
                            st.write(item)
            else:
                with st.expander(f'ID: {venda.id} ㅤ {venda.data}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ**TOTAL: R$ {venda.total:.2f}**', icon=':material/paid:'):
                    st.caption(f'CLIENTE: {venda.idCliente}')
                    st.write('---')
                    st.write(c)
                    for item in items:
                        if item.idVenda == venda.id:
                            st.write(item)
               