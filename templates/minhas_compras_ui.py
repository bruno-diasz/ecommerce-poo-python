import base64
import time
import streamlit as st
from views import View

class MinhasCompras:
	def main():

		class cabecalho:
			def __init__(self):
				pass
			def __str__(self):
				return f"{'ITEM':<27}     {'PREÇO':>15}   {'QTD':<6} {'SUBTOTAL':>26}"
			
		@st.dialog(' ')
		def modal(sucess:bool):
			if sucess : st.success("Produto adicionado ao carrinho com sucesso " ,icon=':material/check:') 
			else: st.error(f"{erro}")
			time.sleep(3)
			st.rerun()

		c = cabecalho()
		st.subheader(":material/receipt: Minhas de Compras")
		st.write('---')
		pedidos, novamente = st.tabs(["Pedidos", "Compre Novamente"])        
		vendas= View.venda_listar()
		items = View.vendaitem_listar()

		with pedidos:
			for venda in reversed(vendas):
				if venda.idCliente == st.session_state.usr.id:
					if  not venda.carrinho:
						with st.expander(f'ID: {venda.id} ㅤ {venda.data}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ**TOTAL: R$ {venda.total:.2f}**', icon=':material/paid:'):
							st.caption(f"STATUS: {venda.entrega.upper()}")
							st.write('---')
							st.write(c)
							for item in items:
								if item.idVenda == venda.id:
									st.write(item)
							if venda.entrega == "entregue":
								st.divider()
								st.feedback("stars")
		with novamente:
			try:
			

				#Ordenação de produtos mais comprados pelo usuario
				contador_produtos = {}
				for venda in vendas:
					if venda.idCliente == st.session_state.usr.id and not venda.carrinho:
						for item in items:
							if item.idVenda == venda.id:

								if item.idProduto in contador_produtos:
									contador_produtos[item.idProduto] += item.qtd
								else:
									contador_produtos[item.idProduto] = item.qtd
								


				produtos_ordem = sorted(contador_produtos,key=contador_produtos.get , reverse=True)[:6]
				st.write("**:streamlit: Compre novamente os prudutos que mais gostou:**")
			
				produtos_mais_comprados = [View.produto_listar_id(p) for p in produtos_ordem ]
			
				

				col1,col2,col3 = st.columns(3)
				for produto in produtos_mais_comprados[::3]:
					with col1:
						with st.container(border=True):
							imagem64 = produto.imagem
							imagem = base64.b64decode(imagem64)
							if imagem is not None:
								st.image(imagem)
							st.markdown(f"<b>{produto.descricao}</b></br>R$ {produto.preco:.2f}".replace('.',','), unsafe_allow_html=True)
							colun1,colun2 = st.columns([1,1])
							colun2.write("")
							colun2.write("")
							qtd = colun1.selectbox('Quantidade:',[i+1 for i in range(produto.estoque)],key=f'qtd_{produto.id}')
							btn_disable = produto.estoque == 0
							if colun2.button(":material/add_shopping_cart: :small[Add]", type='primary', use_container_width=True, key=f'add_{produto.id}', disabled=btn_disable):
								View.venda_inserir_item(produto.id, qtd,st.session_state.carrinho.id)
								modal(True)

				for produto in produtos_mais_comprados[1::3]:
					with col2:
						with st.container(border=True):
							imagem64 = produto.imagem
							imagem = base64.b64decode(imagem64)
							if imagem is not None:
								st.image(imagem)
							
							st.markdown(f"<b>{produto.descricao}</b></br>R$ {produto.preco:.2f}".replace('.',','), unsafe_allow_html=True)

							colun1,colun2 = st.columns([1,1])
							colun2.write("")
							colun2.write("")
							qtd = colun1.selectbox('Quantidade:',[i+1 for i in range(produto.estoque)],key=f'qtd_{produto.id}')
							btn_disable = produto.estoque == 0
							if colun2.button(":material/add_shopping_cart: :small[Add]", type='primary', use_container_width=True, key=f'add_{produto.id}', disabled=btn_disable):
								View.venda_inserir_item(produto.id, qtd,st.session_state.carrinho.id)
								modal(True)

				for produto in produtos_mais_comprados[2::3]:
					with col3:
						with st.container(border=True):
							imagem64 = produto.imagem
							imagem = base64.b64decode(imagem64)
							if imagem is not None:
								st.image(imagem)
							
							st.markdown(f"<b>{produto.descricao}</b></br>R$ {produto.preco:.2f}".replace('.',','), unsafe_allow_html=True)

							colun1,colun2 = st.columns([1,1])
							colun2.write("")
							colun2.write("")
							qtd = colun1.selectbox('Quantidade:',[i+1 for i in range(produto.estoque)],key=f'qtd_{produto.id}')
							btn_disable = produto.estoque == 0
							if colun2.button(":material/add_shopping_cart: :small[Add]", type='primary', use_container_width=True, key=f'add_{produto.id}',disabled=btn_disable):
								View.venda_inserir_item(produto.id, qtd,st.session_state.carrinho.id)
								modal(True)

			except Exception as erro:
				modal(False)
				