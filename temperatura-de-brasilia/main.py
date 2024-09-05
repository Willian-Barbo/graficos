# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt


# Carregando um conjunto de dados fictício (Temperatura ao longo do tempo)
# Carregar um aquivo excel
df = pd.read_excel('data/temperatura_brasilia.xlsx')

# Mas para fins de exemplo, vamos criar um DataFrane diretamente:
data = {
    'Data': pd.date_range(start='01/01/2024', periods=10, freq='D'),
    'Temperatura':[22, 21, 23, 22, 24, 25, 20, 21, 22, 23]
}
df=pd.DataFrame(data)

# Exibindo as primeiras linhas do DataFrame para verificação, você pode adicionar quantas linhas quer visualizar
print(df.head())
