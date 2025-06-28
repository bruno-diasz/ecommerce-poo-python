import streamlit as st
import pandas as pd
import time
from views import View


class ManterProdutoUI:

    @staticmethod
    def main():
        st.subheader(":material/package_2: Administração de Produtos")
        listar, inserir, editar, remover,categoria = st.tabs(['**:material/article: Lista de Produtos**','**:material/add_2: Cadastrar Produto**','**:material/edit: Editar Produto**','**:material/delete: Remover Produto**','**:material/category: Vincular Categoria**'])
        with listar:
            ManterProdutoUI.listar()
        with inserir:
            ManterProdutoUI.inserir()
        with editar:
            ManterProdutoUI.atualizar()
        with remover:
            ManterProdutoUI.excluir()
        with categoria:
            ManterProdutoUI.vincular_categoria()

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
            desc = st.text_input("Nome do Produto: ", placeholder='Digite o Nome do Produto aqui')
            col1,col2 = st.columns(2)
            preco = col1.number_input("Preço: ",min_value=0.0 ) 
            estoque = col2.number_input("Quantidade em estoque: ",min_value=0)
            imagem = col1.file_uploader('Imagem do produto:', ['png','jpg'],key="adicionar_img")
            with col2.container():
                colun1,colun2,colun3 = st.columns([1,3,1])
                if imagem is not None:
                    colun2.write(" ")
                    colun2.image(imagem, width=190,caption='Preview')

            st.write('---')
            if st.button("Cadastrar", type='primary'):
                View.produto_inserir(desc, preco, estoque,imagem)
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
                desc = st.text_input("Nome do Produto: ", placeholder='Digite o Nome do Produto aqui', value=produto.descricao)
                col1,col2 = st.columns(2)
                preco = col1.number_input("Preço: ",min_value=0.0, value=produto.preco)
                estoque = col2.number_input("Quantidade em Estoque: ",min_value=0, value=produto.estoque)
                imagem = col1.file_uploader('Imagem do Produto:', ['png','jpg'],key="atualizar_img")
                with col2.container():
                    colun1,colun2,colun3 = st.columns([1,3,1])
                    if imagem is not None:
                        colun2.write(" ")
                        colun2.image(imagem, width=190,caption='Preview')

             

                st.write('---')
                if st.button("Atualizar", type='primary'):
                    View.produto_atualizar(produto.id, desc, preco, estoque,imagem)
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
    def vincular_categoria():
        col1,col2 = st.columns(2)
        produtos= View.produto_listar()
        produto = col1.selectbox('Selecione um produto para vincular a categoria :',produtos, format_func=lambda produto: f'{produto.id}. {produto.descricao}') 

        categorias= View.categoria_listar()
        categoria = col2.selectbox('Selecione uma categoria:',categorias, format_func=lambda categoria: f'{categoria.id}. {categoria.descricao}') 

        st.write('---')
        if st.button("Vincular produto", type='primary'):
            View.produto_vincular_categoria(produto.id,categoria.id)
            st.success("Vínculo realizado com sucesso. :material/check:")
            time.sleep(4)
            st.rerun()
