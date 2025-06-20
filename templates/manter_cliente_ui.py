import streamlit as st
import pandas as pd
import time
from views import View


class ManterClienteUI:

    @staticmethod
    def main():
        st.subheader(":material/person: Administração de Usuários")
        listar, inserir, editar, remover = st.tabs(['**:material/article_person: Lista de Clientes**','**:material/person_add: Cadastrar Cliente**','**:material/person_edit: Editar Cliente**','**:material/person_remove: Remover Cliente**'])
        with listar:
            ManterClienteUI.listar()
        with inserir:
            ManterClienteUI.inserir()
        with editar:
            ManterClienteUI.atualizar()
        with remover:
            ManterClienteUI.excluir()

    @staticmethod
    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            dic = []
            for obj in clientes:
                dic.append(obj.to_dict())
            df = pd.DataFrame(dic, columns=['id', 'nome', 'email', 'fone'])
            st.dataframe(df, hide_index=True,column_config={"id": "ID", "nome": "Nome", "email": "E-mail", "fone": "Telefone"})

    @staticmethod
    def inserir():
        with st.form(key='cadastro_cliente', clear_on_submit=True):
            nome = st.text_input("Nome: ", placeholder='Digite seu Nome aqui')
            email = st.text_input("E-mail: ", placeholder='Digite seu E-mail aqui')
            senha = st.text_input("Senha: ", type='password', placeholder='Digite sua Senha aqui')
            senha2 = st.text_input("Repita a Senha: ", type='password', placeholder='Digite novamente sua Senha aqui')
            fone = st.text_input("Telefone: ", placeholder='Digite seu Telefone aqui')

            st.write('---')
            if st.form_submit_button("Cadastrar", type='primary'):
                View.cliente_inserir(nome, email, fone, senha)
                st.success("Cadastrado realizado com sucesso. :material/check:")
                time.sleep(4)
                st.rerun()

    @staticmethod
    def atualizar():
        clientes= View.cliente_listar()
        cliente = st.selectbox('Selecione um Cliente para editar:',clientes, format_func=lambda cliente: f'{cliente.id}. {cliente.nome:} - {cliente.email} - {cliente.fone}') 
         
        with st.form(key='atualizar_cliente', clear_on_submit=True):
            nome = st.text_input("Novo Nome: ", placeholder='Digite seu novo Nome aqui',value=cliente.nome )
            email = st.text_input("Novo E-mail: ", placeholder='Digite seu novo E-mail aqui', value=cliente.email)
            senha = st.text_input("Nova Senha: ", type='password', placeholder='Digite sua nova Senha aqui', value=cliente.senha)
            senha2 = st.text_input("Nova Repita a Senha: ", type='password', placeholder='Digite novamente sua nova Senha aqui', value=cliente.senha)
            fone = st.text_input("Novo Telefone: ", placeholder='Digite seu novo Telefone aqui', value=cliente.fone)

            st.write('---')
            if st.form_submit_button("Atualizar", type='primary'):
                View.cliente_atualizar(cliente.id, nome, email, fone, senha)
                st.success("Atualização realizado com sucesso. :material/check:")
                time.sleep(4)
                st.rerun()

    @staticmethod
    def excluir():
        clientes= View.cliente_listar()
        cliente = st.selectbox('Selecione um Cliente para remover:',clientes, format_func=lambda cliente: f'{cliente.id}. {cliente.nome} - {cliente.email} - {cliente.fone}') 

        st.write('---')
        if st.button("Remover", type='primary'):
            View.cliente_excluir(cliente.id)
            st.success("Exclusão realizado com sucesso. :material/check:")
            time.sleep(4)
            st.rerun()