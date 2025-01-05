import streamlit as st

colum1, colum2 = st.columns([0.4, 0.6])

colum1.title("123 ")
nome = "Mario"
colum1.markdown(f"#### Olá, seja bem vindo(a), {nome} !")

botao_dash = colum1.button("Dashboards Combustiveis")
botao_ind = colum1.button("Analise de indicadores")

if botao_dash:
    st.switch_page("abas/dashboard.py")
if botao_ind:
    st.switch_page("abas/indicadores.py")

container = colum2.container(border=True)
container.image(
    r"imagens\20250105_0512_Engineering Project Collaboration_simple_compose_01jgtrbex5fersc48mc0syqjjs.gif")
