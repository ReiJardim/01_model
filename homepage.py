import streamlit as st


sesao_usuario = st.session_state

nome = None
if "username" in sesao_usuario:
    nome = sesao_usuario.name

else:
    nome = ""


colum1, colum2 = st.columns([0.4, 0.6])

colum1.title(" ISC COMPANY ")

if nome:
    colum1.markdown(f"#### Olá, seja bem vindo(a)")
    colum1.markdown(f"#### {nome} !")

botao_dash = colum1.button("Dashboards Combustiveis")
botao_ind = colum1.button("Analise de indicadores")

if botao_dash:
    st.switch_page("dashboard.py")
if botao_ind:
    st.switch_page("indicadores.py")

container = colum2.container(border=True)
container.image(
    r"imagens\20250105_0512_Engineering Project Collaboration_simple_compose_01jgtrbex5fersc48mc0syqjjs.gif")
