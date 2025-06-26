import streamlit as st
from views import View

class LoginUI:
    
    @staticmethod 
    def main():
        st.subheader("Login:")
        with st.form("login"):
            email = st.text_input("Email:", placeholder="Digite seu email")
            senha = st.text_input("Senha:", type='password', placeholder="Digite sua senha")
            if st.form_submit_button("Entrar"): 
                st.session_state
                st.session_state.usr = View.cliente_autenticar(email,senha)
                st.rerun()