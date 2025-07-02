import streamlit as st
import pandas as pd
import time
import base64
from views import View


class ManterProdutoUI:

    @staticmethod
    def main():
        st.subheader(":material/package_2: Administração de Produtos")
        listar, inserir, editar, remover, reajustar = st.tabs(['**:material/article: Lista de Produtos**','**:material/add_2: Cadastrar Produto**','**:material/edit: Editar Produto**','**:material/delete: Remover Produto**', '**:material/shoppingmode: Reajustar Preços**'])
        with listar:
            ManterProdutoUI.listar()
        with inserir:
            ManterProdutoUI.inserir()
        with editar:
            ManterProdutoUI.atualizar()
        with remover:
            ManterProdutoUI.excluir()
        with reajustar:
           ManterProdutoUI.reajustar_precos()
        

    @staticmethod
    def listar():
        produtos = View.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            dic = []
            for obj in produtos:
                dic.append(obj.to_dict())
            df = pd.DataFrame(dic, columns= ['id', 'desc', 'preco', 'estoque', 'categoriaID'])
            st.dataframe(df, hide_index=True,column_config={"id": "ID", "desc": "Produto", "preco": "Preço", "estoque" : "Estoque","categoriaID": "CategoriaID"})

    @staticmethod
    def inserir():
        with st.container(border=True):
            col1,col2 = st.columns(2)
            desc = col1.text_input("Nome do Produto: ", placeholder='Digite o Nome do Produto aqui', key='produto_desc')
            categorias= View.categoria_listar()
            categoria = col2.selectbox('Selecione uma categoria:',categorias, format_func=lambda categoria: f'{categoria.id}. {categoria.descricao}', key="vincular_categoria",placeholder="Nenhuma") 
            preco = col1.number_input("Preço: ",min_value=0.0 ,key='produto_preco') 
            estoque = col2.number_input("Quantidade em estoque: ",min_value=0, key='produto_estoque')
            imagem = col1.file_uploader('Imagem do Produto:', ['png','jpg'],key="produto_imagem")
            with col2.container():
                colun1,colun2,colun3 = st.columns([1,3,1])
                if imagem is not None:
                    colun2.write(" ")
                    colun2.image(imagem, width=190,caption='Preview')

            st.write('---')
            if st.button("Cadastrar", type='primary'):
                View.produto_inserir(desc, preco, estoque,imagem,categoria.id)
                st.success("Cadastrado realizado com sucesso. :material/check:")

                time.sleep(4)
                st.rerun()
      
    @staticmethod
    def atualizar():
        produtos= View.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            produto = st.selectbox('Selecione um produto para editar:',produtos, format_func=lambda produto: f'{produto.id}. {produto.descricao}') 
            
            with st.container(border=True):
                col1,col2 = st.columns(2)
                desc = col1.text_input("Nome do Produto: ", placeholder='Digite o Nome do Produto aqui', value=produto.descricao)
                categorias= View.categoria_listar()
                categoria = col2.selectbox('Selecione uma categoria:',categorias, format_func=lambda categoria: f'{categoria.id}. {categoria.descricao}', key="editar_categoria",placeholder="Nenhuma") 
                preco = col1.number_input("Preço: ",min_value=0.0, value=produto.preco)
                estoque = col2.number_input("Quantidade em Estoque: ",min_value=0, value=produto.estoque)
                imagem = col1.file_uploader('Imagem do Produto:', ['png','jpg'],key="atualizar_img")
                with col2.container():
                    colun1,colun2,colun3 = st.columns([1,3,1])
                   
                    if imagem is not None:
                        colun2.write(" ")
                        colun2.image(imagem, width=190,caption='Preview')
                    else:
                        colun2.write(" ")
                        colun2.image(base64.b64decode(produto.imagem), width=190,caption='Preview')

             

                st.write('---')
                if st.button("Atualizar", type='primary'):
                    View.produto_atualizar(produto.id, desc, preco, estoque,imagem,categoria.id)
                    st.success("Atualização realizado com sucesso. :material/check:")
                    time.sleep(4)
                    st.rerun()

    @staticmethod
    def excluir():
        produtos= View.produto_listar()
        produto = st.selectbox('Selecione um produto para remover:',produtos, format_func=lambda produto: f'{produto.id}. {produto.descricao}') 

        st.write('---')
        if st.button("Remover", type='primary'):
            View.produto_excluir(produto.id)
            st.success("Exclusão realizado com sucesso. :material/check:")
            time.sleep(4)
            st.rerun()

    @staticmethod
    def reajustar_precos():
        porcentagem = st.number_input("Reajustar todos os preços em (%)", min_value=-100.0, step=0.1, format="%.2f", value=0.0)
        if st.button("Confirmar reajuste", type="primary"):
            View.produto_reajuste(porcentagem)
            st.success("Reajustes realizados com sucesso. :material/check:")
            time.sleep(4)
            st.rerun()
        


   
        
