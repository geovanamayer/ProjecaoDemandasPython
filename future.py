import pandas as pd
import matplotlib.pyplot as plt

dados_demandas = [
    {'Pessoa': 'João', 'Data': '2022-01-01'},
    {'Pessoa': 'Maria', 'Data': '2022-01-15'},
    {'Pessoa': 'João', 'Data': '2023-02-01'},
    {'Pessoa': 'Maria', 'Data': '2023-03-10'},
    {'Pessoa': 'Pedro', 'Data': '2023-05-20'}
]

df_demandas = pd.DataFrame(dados_demandas)

df_demandas['Data'] = pd.to_datetime(df_demandas['Data'])

demandas_2022 = df_demandas[df_demandas['Data'].dt.year == 2022]

demandas_2023 = df_demandas[df_demandas['Data'].dt.year == 2023]

quantidade_demandas_2022 = demandas_2022['Pessoa'].value_counts()

quantidade_demandas_2023_atual = demandas_2023['Pessoa'].value_counts()

hoje = pd.to_datetime('today').date()
demandas_restantes_2023 = demandas_2023[demandas_2023['Data'].dt.date > hoje]

# Calcular 
quantidade_demandas_restantes_2023 = demandas_restantes_2023['Pessoa'].value_counts()

#  dados para o gráfico
pessoas = quantidade_demandas_2022.index.tolist()
demandas_2022_valores = quantidade_demandas_2022.values.tolist()
demandas_2023_atual_valores = quantidade_demandas_2023_atual.values.tolist()
demandas_restantes_2023_valores = quantidade_demandas_restantes_2023.values.tolist()

# Configurar o gráfico
plt.figure(figsize=(10, 6))
plt.bar(pessoas, demandas_2022_valores, label='2022')
plt.bar(pessoas, demandas_2023_atual_valores, label='2023 Até o Momento')
plt.bar(pessoas, demandas_restantes_2023_valores, label='Restante de 2023')
plt.xlabel('Pessoa')
plt.ylabel('Quantidade de Demandas')
plt.title('Quantidade de Demandas por Pessoa')
plt.legend()

plt.show()
