import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Carregar os dados do arquivo Excel
df = pd.read_excel('data/suavizacao_tendencia.xlsx')

# Converter o campo "Mes/Ano" para o formato de data
df['Mes/Ano'] = pd.to_datetime(df['Mes/Ano'], format='%m/%Y')

# Definir a coluna 'Mes/Ano' como índice
df.set_index('Mes/Ano', inplace=True)

# Criar variáveis para análise
X = np.arange(len(df)).reshape(-1, 1)
y = df['Vendas'].values

# Modelagem de Regressão Linear
model = LinearRegression()
model.fit(X, y)
futuro_meses = np.arange(len(df), len(df) + 6).reshape(-1, 1)
previsoes_regressao = model.predict(futuro_meses)

# Modelagem de Suavização Exponencial
model_exp = ExponentialSmoothing(df['Vendas'], trend='add', seasonal=None)
fit_exp = model_exp.fit()
previsoes_exp = fit_exp.forecast(steps=6)

# Plotar os dados e previsões
plt.figure(figsize=(14, 7))

# Gráfico de Regressão Linear
plt.subplot(1, 2, 1)
plt.plot(df.index, df['Vendas'], marker='o', linestyle='-', color='b', label='Vendas Reais')
plt.plot(pd.date_range(start=df.index[-1] + pd.DateOffset(months=1), periods=6, freq='ME'), previsoes_regressao, marker='x', linestyle='--', color='r', label='Previsões Regressão Linear')
plt.title('Previsão de Vendas - Regressão Linear')
plt.xlabel('Data')
plt.ylabel('Vendas (unidades)')
plt.legend()
plt.grid(True)

# Gráfico de Suavização Exponencial
plt.subplot(1, 2, 2)
plt.plot(df.index, df['Vendas'], marker='o', linestyle='-', color='b', label='Vendas Reais')
plt.plot(pd.date_range(start=df.index[-1] + pd.DateOffset(months=1), periods=6, freq='ME'), previsoes_exp, marker='x', linestyle='--', color='g', label='Previsões Suavização Exponencial')
plt.title('Previsão de Vendas - Suavização Exponencial')
plt.xlabel('Data')
plt.ylabel('Vendas (unidades)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
