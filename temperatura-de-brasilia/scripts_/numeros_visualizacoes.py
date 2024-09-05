import matplotlib.pyplot as plt

# Dados fornecidos
visualizacoes_iniciais = 1_906_660 # Visualizações em 10 horas
tempo_inicial = 10 #horas
tempo_total = 168 # 7 dias em horas

# Calcular a taxa de crescimento de visualizações por hora
taxa_visualizacoes_por_hora = visualizacoes_iniciais / tempo_inicial

# Projetar o número de visualizações em 7 dias (168 horas)
visualizacoes_7_dias = taxa_visualizacoes_por_hora * tempo_total

# Exibir os resultados
print(f'Taxa de visualizações por hora: {taxa_visualizacoes_por_hora:.2f}')
print(f'Visualizações estimadas em 7 dias: {visualizacoes_7_dias:.0f}')


# Opcional: Visualizar o crescimento ao longo do tempo em um gráfico
horas = list(range(0, tempo_total + 1))
visualizacoes = [taxa_visualizacoes_por_hora * h for h in horas]

plt.figure(figsize=(10,6))
plt.plot(horas, visualizacoes, marker='o', linestyle='-', color='b')
plt.title('Projeção de Visualizações ao Longo do Tempo')
plt.xlabel('Horas')
plt.ylabel('Número de Visualizações')
plt.grid(True)
plt.show()