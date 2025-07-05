import streamlit as st
from views import View
import time

class GerenciarVendas:
    def main():

        class cabecalho:
            def __init__(self):
                pass
            def __str__(self):
                return f"{'ITEM':<27}     {'PREÇO':>15}   {'QTD':<6} {'SUBTOTAL':>26}"
                
        c = cabecalho()
        st.subheader(":material/receipt: Gerenciar de Vendas")
        st.write('---')
        vendas= View.venda_listar()
        items = View.vendaitem_listar()
        pendente, enviado, entregue = st.tabs(["**:material/schedule:** **Pendente**", "**:material/local_shipping:** **Enviado**", "**:material/task_alt:** **Entregue**"])

        for venda in vendas:     
            if not venda.carrinho: 
                if venda.entrega == "pendente":    
                    with pendente.expander(f'ID: {venda.id} ㅤ {venda.data}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ**TOTAL: R$ {venda.total:.2f}**', icon=':material/paid:'):
                        st.caption(f"CLIENTE: {venda.idCliente}")
                        col1,col2,col3 = st.columns([1.2,1.2,1.6])
                        entregador = col1.selectbox("entregador",[entregador for entregador in View.usuario_listar() if entregador.funcao =="entregador"], key=f"entregador_{venda.id}", label_visibility='collapsed',  format_func=lambda entregador: f'{entregador.id}. {entregador.email}')
                        if col2.button(":green[:small[**INICIAR ENTREGA**]]", key=f"iniciar_entrega_{venda.id}", type='secondary', icon=":material/local_shipping:"):
                            View.iniciar_entrega(entregador.id,venda.id)
                            st.success("Entrega iniciada com sucesso", icon=":material/check:")
                            time.sleep(3)
                            st.rerun()
                        st.write('---')
                        st.write(c)
                        for item in items:
                            if item.idVenda == venda.id:
                                st.write(item)

                if venda.entrega == "enviado":    
                    with enviado.expander(f'ID: {venda.id} ㅤ {venda.data}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ**TOTAL: R$ {venda.total:.2f}**', icon=':material/paid:'):
                        st.caption(f"CLIENTE: {venda.idCliente} - ENTREGADOR: {venda.idEntregador}")
                       
                        st.write('---')
                        st.write(c)
                        for item in items:
                            if item.idVenda == venda.id:
                                st.write(item)

                if venda.entrega == "entregue":    
                    with entregue.expander(f'ID: {venda.id} ㅤ {venda.data}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ**TOTAL: R$ {venda.total:.2f}**', icon=':material/paid:'):
                        st.caption(f"CLIENTE: {venda.idCliente} - ENTREGADOR: {venda.idEntregador}")
                        st.write('---')
                        st.write(c)
                        for item in items:
                            if item.idVenda == venda.id:
                                st.write(item)
               