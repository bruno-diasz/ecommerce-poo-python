import streamlit as st
from views import View
import base64
import time

class CatalogoProdutos:

	@staticmethod
	def main ():
		try:
			
			@st.dialog(' ')
			def modal(sucess:bool):
				if sucess : st.success("Produto adicionado ao carrinho com sucesso " ,icon=':material/check:') 
				else: st.error(f"{erro}")
				time.sleep(3)
				st.rerun()
				

			st.header(":material/package_2: Catálogo de Produtos")
			st.divider()

			categorias = View.categoria_listar()
			categoria = st.segmented_control('Categorias:',categorias)
			if categoria is not None:
				produtos = View.produto_listar_categoria(categoria.id)
			else:
				produtos = View.produto_listar()

			col1,col2,col3 = st.columns(3)
			for produto in produtos[::3]:
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

			for produto in produtos[1::3]:
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

			for produto in produtos[2::3]:
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
			
			
							

				
				
		   