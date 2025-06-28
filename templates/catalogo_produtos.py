import streamlit as st
from views import View,Produtos
import base64
class CatalogoProdutos:

        @staticmethod
        def main ():

                imagem = st.file_uploader('Imagem do produto:', ['png','jpg'])
                if imagem is not None:
                        st.image(imagem)
                # produto= Produtos.listar_id(0)
                # imagem64 = produto.imagem
                # imagem = base64.b64decode(imagem64)
                # st.image(imagem)
                
                # col1,col2,col3 = st.columns(3)
                # with col1:
                #     with st.container(border=True):
                #         if imagem is not None:
                #             st.image(imagem,use_container_width=True)
                #         st.markdown("<b>Iphone</b></br>R$ 100,99", unsafe_allow_html=True)
                #         st.button(":material/add_shopping_cart: Adicionar ao carrinho ", type='primary', use_container_width=True)
                        
                # with col2:
                #     with st.container(border=True, ):
                #         if imagem is not None:
                #             st.image(imagem,use_container_width=True)
                #             st.text("desc")
                
                # with col3:
                #     with st.container(border=True, ):
                #         if imagem is not None:
                #             st.image(imagem,use_container_width=True)
                #             st.text("desc")