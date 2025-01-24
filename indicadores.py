import streamlit as st
from utlidade import carregar_dados

# st.title(r"1o Sem 2024 - Combustíveis Automotivos")

total_dados = carregar_dados()

base = total_dados[total_dados["Produto"] == "GASOLINA"]
base_gasolina = total_dados[total_dados["Produto"] == "GASOLINA"]
base_disels10 = total_dados[total_dados["Produto"] == "DIESEL S10"]
base_etanol = total_dados[total_dados["Produto"] == "ETANOL"]
base_disel = total_dados[total_dados["Produto"] == "DIESEL"]
base_gasolina_ad = total_dados[total_dados["Produto"] == "GASOLINA ADITIVADA"]


def criar_card(icone, numero, texto, coluna_card):
    conteiner = coluna_card.container(border=True)
    # Aplica CSS para estilizar o container

    colum_1, colum_2 = conteiner.columns([1, 2.5])
    colum_1.image(icone)
    colum_2.write((numero))
    colum_2.write((texto))


def indi(base_combustivel, titulo):

    st.title(titulo)
    quant_dados = base_combustivel["Regiao - Sigla"].count()
    base_ne = base_combustivel[base_combustivel["Regiao - Sigla"] == "NE"]
    quant_ne = base_ne["Regiao - Sigla"].count()

    cnpj_pi = base_ne[base_ne["Estado - Sigla"] == "PI"]
    cnpj_ba = base_ne[base_ne["Estado - Sigla"] == "BA"]
    cnpj_ma = base_ne[base_ne["Estado - Sigla"] == "MA"]

    unico_ba = cnpj_ba["CNPJ da Revenda"].unique()
    unico_pi = cnpj_pi["CNPJ da Revenda"].unique()
    unico_ma = cnpj_ma["CNPJ da Revenda"].unique()

    # Converta a 'coluna1' para numérica, substituindo vírgulas por pontos
    base_ne['Valor de Venda'] = base_ne['Valor de Venda'].astype(
        str).str.replace(',', '.').astype(float)
    media_ne = base_ne['Valor de Venda'].mean()
    media_arredondada_ne = f"R$ {round(media_ne, 2)}"

    colum_1, colum_2, colum_3 = st.columns([1, 1, 1])

    criar_card(icone=r"https://cdn-icons-png.flaticon.com/512/5110/5110785.png",
               numero=str(quant_dados), texto="Quant. dados", coluna_card=colum_1)
    criar_card(icone=r"https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Regi%C3%A3o_Nordeste.svg/817px-Regi%C3%A3o_Nordeste.svg.png",
               numero=str(quant_ne), texto="Quant. NE", coluna_card=colum_2)
    criar_card(icone=r"imagens/icones/2091806.png",
               numero=media_arredondada_ne, texto="V. médio NE", coluna_card=colum_3)

    criar_card(icone=r"imagens\icones\BERIM.png",
               numero=str(len(unico_ba)), texto="CNPJ Bahia", coluna_card=colum_1)
    criar_card(icone=r"imagens\icones\Brasão_do_Maranhão.svg.png",
               numero=str(len(unico_ma)), texto="CNPJ Maranhão", coluna_card=colum_2)
    criar_card(icone=r"imagens\icones\caju.png",
               numero=str(len(unico_pi)), texto="CNPJ Piaui", coluna_card=colum_3)

    # st.table(base_combustivel)


titulo_gasolina = "Indicadores de gasolina"
indi(base_combustivel=base_gasolina, titulo=titulo_gasolina)

titulo_disels10 = "Indicadores de disel S10"
indi(base_combustivel=base_disels10, titulo=titulo_disels10)


titulo_disel = "Indicadores de disel"
indi(base_combustivel=base_disel, titulo=titulo_disel)

titulo_etanol = "Indicadores de etanol"
indi(base_combustivel=base_etanol, titulo=titulo_etanol)

titulo_gasolinaad = "Indicadores de gasolina aditivada"
indi(base_combustivel=base_gasolina_ad, titulo=titulo_gasolinaad)
