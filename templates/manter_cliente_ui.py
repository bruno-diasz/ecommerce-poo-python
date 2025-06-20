import streamlit as st
import pandas as pd
from views import View


class ManterClienteUI:


    @staticmethod
    def main():
        st.subheader("Administração de Usuários")
        listar,inserir,editar,remover = st.tabs(['**:material/article_person: Lista de Clientes**','**:material/person_add: Cadastrar Cliente**', '**:material/person_edit: Editar Cliente**','**:material/person_remove: Remover Cliente**'] )
        with listar: ManterClienteUI.listar()
        with inserir: ManterClienteUI.inserir()
        with editar: pass #ManterClienteUI.atualizar()
        with remover: pass #ManterClienteUI.excluir()
       
    @staticmethod
    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:    
            dic = []
            for obj in clientes: dic.append(obj.to_dict())
            df = pd.DataFrame(dic, columns=['id','nome','email','fone'])
            st.dataframe(df, hide_index=True, column_config={"id":"ID", "nome":"Nome", "email":"E-mail", "fone":"Telefone"})


    @staticmethod
    def inserir():
        with st.form("Criar Usuario"):
            st.text_input("Nome:")
            st.text_input("E-mail:")
            st.text_input("Telefone:")
            st.text_input("Senha:")
            st.text_input("Repita a Senha:")
            st.form_submit_button("Cadastrar")




