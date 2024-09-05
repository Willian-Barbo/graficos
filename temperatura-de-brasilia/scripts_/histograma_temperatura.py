import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_excel('data/temperatura_brasilia.xlsx')

# Gráfico de Histograma das Temperaturas
plt.figure(figsize=(10,6))
plt.hist(df['temperatura_media'], bins=20, color='orange', edgecolor='black')
plt.title('Distribuição da Temperatura Média - Brasília')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Frequêcia')
plt.grid(True)

plt.show()