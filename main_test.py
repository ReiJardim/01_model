import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from models import session, Usuario


lista_usuarios = session.query(Usuario).all()

credenciais = {"usernames": {
    usuario.email: {"name": usuario.nome, "password": usuario.senha} for usuario in lista_usuarios
}}

authenticator = stauth.Authenticate(
    credenciais, "credenciais_hashco", "fsyfus%$67fs76AH7", cookie_expiry_days=30)


def autenticar_usuario(authenticator):
    nome, status_autenticacao, username = authenticator.login()

    if status_autenticacao:
        return {"nome": nome, "username": username}
    elif status_autenticacao == False:
        st.error("Combinação de usuário e senha inválidas")
    else:
        st.error("Preencha o formulário para fazer login")


def logout():
    authenticator.logout()


# st.write("olá")
# autenticar o usuario
dados_usuario = autenticar_usuario(authenticator)

if dados_usuario:
    @st.cache_data
    def carregar_dados():
        local_data = r"dados\ca-2024-01\Preços semestrais - AUTOMOTIVOS_2024.01.csv"
        tabela = pd.read_csv(local_data, sep=';')
        return tabela

    base = carregar_dados()

    email_usuario = dados_usuario["username"]
    usuario = session.query(Usuario).filter_by(email=email_usuario).first()

    if usuario.admin:

        pg = st.navigation(
            {
                "Home page": [st.Page("abas/homepage.py", title="🏠 - Home Page")],
                "DashBoard": [
                    st.Page("abas/dashboard.py", title="📊 - Dash"),
                    st.Page("abas/indicadores.py", title="🚩 - Indicadores"),
                ],
                "Conta": [
                    st.Page(logout, title="Sair"),
                    st.Page("abas/criar_conta.py", title="Criar Conta"),
                ],
            }
        )

    else:
        pg = st.navigation(
            {
                "Home page": [st.Page("abas/homepage.py", title="🏠 - Home Page")],
                "DashBoard": [
                    st.Page("abas/dashboard.py", title="📊 - Dash"),
                    st.Page("abas/indicadores.py", title="🚩 - Indicadores"),
                ],
                "Conta": [
                    st.Page(logout, title="Sair")
                ],
            }
        )
    pg.run()


elif dados_usuario == False:
    @st.cache_data
    def carregar_dados():
        local_data = r"dados\ca-2024-01\Preços semestrais - AUTOMOTIVOS_2024.01.csv"
        tabela = pd.read_csv(local_data, sep=';')
        return tabela

    base = carregar_dados()

    pg = st.navigation(
        {
            "Home page": [st.Page("abas/homepage.py", title="🏠 - Home Page")]
        }
    )
    pg.run()
