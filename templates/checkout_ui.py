import streamlit as st
import time
from views import View
import base64

class CheckOut:
	def main():
	
		
		try:
			vendas = View.venda_listar()
			items = View.vendaitem_listar()
			produtos = View.produto_listar()

			for venda in vendas:
				if venda.idCliente == st.session_state.usr.id and venda.carrinho:
					t_col1, t_col2 = st.columns([2, 1])
					t_col1.subheader(":material/shopping_cart: Carrinho de Compras")
					t_col2.subheader(f"Total: :small[R$] {venda.total:.2f}".replace('.', ','))
					st.caption(f"ID: {venda.id} - {venda.data}")
					st.divider()

					for item in items:
						if item.idVenda == venda.id:
							for produto in produtos:
								if produto.id == item.idProduto:
									with st.container(border=True):
									# Correção da quantidade
										safe_value = max(1, min(item.qtd, produto.estoque))
										if item.qtd > produto.estoque:
											st.warning(f"A quantidade do ({produto.descricao}) excede o estoque disponível, a quantidade sera ajustada para a disponivel.",icon="⚠️")
											time.sleep(4)

										imagem = base64.b64decode(produto.imagem)
										col1, col2, col3, col4 = st.columns([2, 1.5, 2, 2])

										with col1:
											col1.image(imagem)

										with col2:
											col2.write(f'**{produto.descricao}**')

											new_qtd = col2.number_input("Quantidade:",min_value=1,max_value=produto.estoque,value=safe_value,key=f"qtd_{item.id}")

											if new_qtd > item.qtd:
												View.venda_inserir_item(produto.id, new_qtd - item.qtd, st.session_state.carrinho.id)
												st.rerun()
											elif new_qtd < item.qtd:
												View.venda_excluir_item(produto.id, item.qtd - new_qtd, st.session_state.carrinho.id)
												st.rerun()

											if col2.button("Excluir", icon=':material/delete:', type='primary', use_container_width=True, key=f'delete_{item.id}'):
												View.venda_excluir_item(produto.id, item.qtd, st.session_state.carrinho.id)
												st.rerun()

										with col4:
											st.subheader(f":small[R$] {item.preco:.2f}".replace('.', ','))

					st.divider()
					if st.button("Confirmar Compra", type='primary', icon=':material/shopping_bag:'):
						View.venda_confirmar(st.session_state.carrinho.id)
						st.session_state.carrinho = View.carregar_carrinho(st.session_state.usr.id)
						st.success("Compra realizada com sucesso", icon=":material/check:")
						st.balloons()
						time.sleep(3)
						st.rerun()

		except Exception as erro:
			st.error(f"{erro}", icon=":material/error:")
			time.sleep(3)
			st.rerun()
