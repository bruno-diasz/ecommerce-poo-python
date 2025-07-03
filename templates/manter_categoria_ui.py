import streamlit as st
import pandas as pd
import time
from views import View


class ManterCategoriaUI:

    @staticmethod
    def main():
        st.subheader(":material/category: Administração de Categorias")
        listar, inserir, editar, remover = st.tabs(['**:material/article: Lista de Categorias**','**:material/add_2: Cadastrar Categoria**','**:material/edit: Editar Categoria**','**:material/delete: Remover Categoria**'])
        with listar:
            ManterCategoriaUI.listar()
        with inserir:
            ManterCategoriaUI.inserir()
        with editar:
            ManterCategoriaUI.atualizar()
        with remover:
            ManterCategoriaUI.excluir()

    @staticmethod
    def listar():
        categorias  = View.categoria_listar()
        if len(categorias ) == 0:
            st.write("Nenhum categoria cadastrado")
        else:
            dic = []
            for obj in categorias :
                dic.append(obj.to_dict())
            df = pd.DataFrame(dic, columns=['id', 'descricao'])
            st.dataframe(df, hide_index=True,column_config={"id": "ID", "descricao": "Nome"})

    @staticmethod
    def inserir():
        try:
            with st.container(border=True):
                desc = st.text_input("Nome da Categoria: ", placeholder='Digite o nome da Categoria aqui')

                st.write('---')
                if st.button("Cadastrar", type='primary'):
                    View.categoria_inserir(desc)
                    st.success("Categoria criada com sucesso. :material/check:")
                    time.sleep(4)
                    st.rerun()
        except Exception as erro:
            st.error(f"{erro}",icon=":material/error:")
            time.sleep(4)
            st.rerun()

    @staticmethod
    def atualizar():
        categorias = View.categoria_listar()
        categoria = st.selectbox('Selecione um categoria para editar:',categorias[1::] , format_func=lambda categoria: f'{categoria.id}. {categoria.descricao}') 
         
        with st.container(border=True):
            try:
                nome = st.text_input("Novo Nome: ", placeholder='Digite seu novo Nome aqui',value=categoria.descricao )
           
                st.write('---')
                if st.button("Atualizar", type='primary'):
                    View.categoria_atualizar(categoria.id, nome)
                    st.success("Atualização realizado com sucesso. :material/check:")
                    time.sleep(4)
                    st.rerun()
            except Exception as erro:
                st.error(f"{erro}",icon=":material/error:")
                time.sleep(4)
                st.rerun()

    @staticmethod
    def excluir():
        try:
            categorias = View.categoria_listar()
            categoria = st.selectbox('Selecione um categoria para remover:',categorias[1::] , format_func=lambda categoria: f'{categoria.id}. {categoria.descricao}') 
        


            st.write('---')
            if st.button("Remover", type='primary'):
                View.categoria_excluir(categoria.id)
                st.success("Exclusão realizado com sucesso.", icon=":material/check:")
                time.sleep(4)
                st.rerun()
        except Exception as erro:
            st.error(f"{erro}",icon=":material/error:")
            time.sleep(4)
            st.rerun()
