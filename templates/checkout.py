import streamlit as st
from views import View

class CheckOut:
    def main():

        class cabecalho:
            def __init__(self):
                pass
            def __str__(self):
                return f"{'ITEM':<27}     {'PREÇO':>15}   {'QTD':<6} {'SUBTOTAL':>26}"
                
        c = cabecalho()
        st.subheader(":material/shopping_cart: Carrinho de Compras")
        st.write('---')
        vendas= View.venda_listar()
        items = View.vendaitem_listar()
        for venda in vendas:
            if venda.idCliente == st.session_state.usr.id:
                if  venda.carrinho:
                    with st.expander(f'ID: {venda.id} ㅤ {venda.data}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ**TOTAL: R$ {venda.total:.2f}**', icon=':material/shopping_cart:'):
                        st.caption(f'CLIENTE: {venda.idCliente}')
                        st.write('---')
                        st.write(c)
                        for item in items:
                            if item.idVenda == venda.id:
                                st.write(item)

        if st.button("Confirmar Compra", type='primary'):
            View.venda_confirmar(st.session_state.carrinho.id)
            st.rerun()
                