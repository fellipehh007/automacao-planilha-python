import pandas as pd
import os

pasta = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(pasta, "dados.xlsx")

df = pd.read_excel(arquivo, engine="openpyxl")

df = df.drop_duplicates()
df = df.sort_values(by="Nome")

saida = os.path.join(pasta, "relatorio_organizado.xlsx")
df.to_excel(saida, index=False)

print("Relatório gerado com sucesso!")
