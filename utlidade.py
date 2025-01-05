import pandas as pd
import streamlit as st


@st.cache_data
def carregar_dados():
    local_data = "Preços semestrais - AUTOMOTIVOS_2024.01.csv"
    tabela = pd.read_csv(local_data, sep=';')
    return tabela


base = carregar_dados()
