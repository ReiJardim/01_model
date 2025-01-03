import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth

# senhas_cripto = stauth.Hasher(["1234", "1234"]).generate()

credenciais = {"usernames": {
    "gato@gmal.com": {"name": "gato", "password": "123456"},
    "cachorro@gmal.com": {"name": "cachorro", "password": "123456"}
}}

authenticator = stauth.Authenticate(
    credenciais, "credenciais_navegagor", cookie_key="113158oeeokppdlpde", cookie_expiry_days=30)


def autenticar_usuario(authenticator):
    nome, status_autenticacao, username = authenticator.login()

    if status_autenticacao:
        return {"nome": nome, "username": username}
    elif status_autenticacao == False:
        st.error("Usuario ou senha invalido")
    else:
        st.error("Preencha o formulario para fazer login")


def logout():
    authenticator.logout()


@st.cache_data
def carregar_dados():
    local_data = r"dados\ca-2024-01\Preços semestrais - AUTOMOTIVOS_2024.01.csv"
    tabela = pd.read_csv(local_data, sep=';')
    return tabela


base = carregar_dados

'''
if dados_usuario:

    @st.cache_data
    def carregar_dados():
        local_data = r"dados\ca-2024-01\Preços semestrais - AUTOMOTIVOS_2024.01.csv"
        tabela = pd.read_csv(local_data, sep=';')
        return tabela

    base = carregar_dados

    pg = st.navigation(
        {
            "Home page": [st.Page("abas/homepage.py", title="🏠 - Home Page")],
            "DashBoard": [st.Page("abas/dashboard.py", title="📊 - Dash"), st.Page("abas/indicadores.py", title="🚩 - Indicadores")],
            "Conta": [st.Page(logout, title="Sair"), st.Page("abas/criar_conta.py", title="Criar Conta")]
        }
    )
    pg.run()

'''
st.write("olá")
