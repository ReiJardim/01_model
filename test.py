import pandas as pd


local_data = r"dados\ca-2024-01\Preços semestrais - AUTOMOTIVOS_2024.01.csv"
data = pd.read_csv(local_data, sep=';')
