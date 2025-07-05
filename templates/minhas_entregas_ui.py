import streamlit as st
import time
from views import View


class MinhasEntregas:

    @staticmethod
    def main():
        class cabecalho:
            def __init__(self):
                pass
            def __str__(self):
                return f"{'ITEM':<27}     {'PREÇO':>15}   {'QTD':<6} {'SUBTOTAL':>26}"
                    
        c = cabecalho()
        st.subheader(":material/local_shipping: Minhas Entregas")
        st.write('---')
        vendas= View.venda_listar()
        items = View.vendaitem_listar()
        pendente, entregue = st.tabs(["**:material/schedule:** **Pendente**",  "**:material/task_alt:** **Entregue**"])

        for venda in vendas:     
            if not venda.carrinho: 
                if venda.idEntregador == st.session_state.usr.id:

                    if venda.entrega == "enviado":    
                        with pendente.expander(f'ID: {venda.id} ㅤ {venda.data}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon=':material/paid:'):
                            st.caption(f"CLIENTE: {venda.idCliente}")
                       
                            if st.button(":green[:small[**CONFIRMAR ENTREGA**]]", key=f"confirmar_entrega_{venda.id}", type='secondary', icon=":material/task_alt:"):
                                View.finalizar_entrega(venda.id)
                                st.success("Entrega concluida com sucesso", icon=":material/check:")
                                time.sleep(3)
                                st.rerun()
                            st.write('---')
                           

                    if venda.entrega == "entregue":    
                        with entregue.expander(f'ID: {venda.id} ㅤ {venda.data}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ', icon=':material/paid:'):
                            st.caption(f"CLIENTE: {venda.idCliente}")
                            st.write('---')
                            