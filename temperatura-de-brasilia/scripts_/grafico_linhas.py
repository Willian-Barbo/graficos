import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_excel('data/temperatura_brasilia.xlsx')

# Converter o campo 'Data' para o formato de data
df['data'] = df['data'].dt.strftime('%d/%m/%Y')


# Criar o Gráfico
plt.figure(figsize=(10, 6))
plt.fill_between(df['data'], df['temperatura_media'], color='lightgray', alpha=0.5)
plt.plot(df['data'], df['temperatura_media'], marker='o', linestyle='-', color='b')
plt.title('Temperatura ao longo do Tempo - Brasília')
plt.xlabel('data')
plt.ylabel('temperatura (°C)')
plt.grid(True)
plt.xticks(rotation=45)

# Resumo estatístico dos dados
#print(df.describe())

# Verificar se há valores nulos
#print(df.isnull().sum())

# Ver as primeiras linhas do DataFrame
#print(df.head())

plt.show()