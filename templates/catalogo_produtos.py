import streamlit as st
from views import View,Produtos
import base64

class CatalogoProdutos:

	@staticmethod
	def main ():
		st.header(":material/package_2: Catálogo de Produtos")
		st.divider()

		col1,col2,col3 = st.columns(3)
		produtos = View.produto_listar()
		for produto in produtos[::3]:
			with col1:
				with st.container(border=True):
					imagem64 = produto.imagem
					imagem = base64.b64decode(imagem64)
					if imagem is not None:
						st.image(imagem)
					
					st.markdown(f"<b>{produto.descricao}</b></br>R$ {produto.preco:.2f}".replace('.',','), unsafe_allow_html=True)
					st.button(":material/add_shopping_cart: Adicionar ao carrinho ", type='primary', use_container_width=True, key=f'item_{produto.id}')

		for produto in produtos[1::3]:
			with col2:
				with st.container(border=True):
					imagem64 = produto.imagem
					imagem = base64.b64decode(imagem64)
					if imagem is not None:
						st.image(imagem)
					
					st.markdown(f"<b>{produto.descricao}</b></br>R$ {produto.preco:.2f}".replace('.',','), unsafe_allow_html=True)
					st.button(":material/add_shopping_cart: Adicionar ao carrinho ", type='primary', use_container_width=True, key=f'item_{produto.id}')

		for produto in produtos[2::3]:
			with col3:
				with st.container(border=True):
					imagem64 = produto.imagem
					imagem = base64.b64decode(imagem64)
					if imagem is not None:
						st.image(imagem)
					
					st.markdown(f"<b>{produto.descricao}</b></br>R$ {produto.preco:.2f}".replace('.',','), unsafe_allow_html=True)
					st.button(":material/add_shopping_cart: Adicionar ao carrinho ", type='primary', use_container_width=True, key=f'item_{produto.id}')
				
				
		   