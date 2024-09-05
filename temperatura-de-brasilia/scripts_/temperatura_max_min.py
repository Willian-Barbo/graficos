import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

# Carregando os Dados
df = pd.read_excel('data/temperatura_max_min.xlsx')


# Gerar dados fictícios
#np.random.seed(0)
#temperatura_maxima = np.random.uniform(low=25, high=35, size=len(datas))
#temperatura_minima = np.random.uniform(low=15, high=25, size=len(datas))

# Criando Gráfico Temperatura Max e Min
plt.figure(figsize=(10,6))
plt.plot(df['data'], df['temperatura_maxima'], marker='o', linestyle='-', color='r', label='Temperatura Máxima')
plt.plot(df['data'], df['temperatura_minima'], marker='o', linestyle='-', color='b', label='Temperatura Mínima')
#data = pd.date_range(start='01-08-2024', end='31-08-2024', freq='D')

plt.fill_between(df['data'], df['temperatura_maxima'], df['temperatura_minima'], color='lightgray', alpha=0.5)
plt.title('Temperatura Máxima e Mínima ao longo do Tempo - Brasília')
plt.xlabel('Data')
plt.ylabel('Temperatura °C')

plt.grid(True)
plt.xticks(rotation=0)
plt.legend()

plt.show()