import pandas as pd
import seaborn as sns    
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure 

# Carregando o arquivo CSV
turbina = pd.read_csv('T1.csv')

# Verificando as colunas do DataFrame para garantir que o nome das colunas está correto
print(turbina.columns)

# Convertendo a coluna 'Date/Time' para formato datetime
turbina['Date/Time'] = pd.to_datetime(turbina['Date/Time'], format='%d %m %Y %H:%M')

# Deletando a coluna 'Wind Direction (°)' se não for necessária
del turbina['Wind Direction (°)']

# Verificando novamente as colunas para garantir que a remoção foi bem-sucedida
print(turbina.columns)

# Criando o gráfico de dispersão para a potência ativa versus velocidade do vento
sns.scatterplot(data=turbina, x='Wind Speed (m/s)', y='LV ActivePower (kW)')

# Criando o gráfico de dispersão para a curva teórica de potência
sns.scatterplot(data=turbina, x='Wind Speed (m/s)', y='Theoretical_Power_Curve (KWh)')

# Inicializando as listas para os limites de potência e a categorização
pot_real = turbina['LV ActivePower (kW)'].to_list()  # Assumindo que 'LV ActivePower (kW)' é a coluna correta
pot_teorica = turbina['Theoretical_Power_Curve (KWh)'].to_list()  # Assumindo que 'Theoretical_Power_Curve (KWh)' é a coluna correta
pot_max = []
pot_min = []
dentro_limite = []
cores = {'Dentro':'blue', 'Fora':'red', 'Zero':'orange'}

# Calculando os limites máximo e mínimo baseados na potência teórica
for potencia in pot_teorica:
    pot_max.append(potencia * 1.06)
    pot_min.append(potencia * 0.95)

# Categorizando se a potência real está dentro do limite ou não
for p, potencia in enumerate(pot_real):
    if potencia >= pot_min[p] and potencia <= pot_max[p]:
        dentro_limite.append('Dentro')
    elif potencia == 0:
        dentro_limite.append('Zero')
    else:
        dentro_limite.append('Fora')

# Exibindo a porcentagem de valores dentro do limite
print(dentro_limite.count('Dentro') / len(dentro_limite))

# Adicionando a coluna 'DentroLimite' ao DataFrame
turbina['DentroLimite'] = dentro_limite

# Exibindo o DataFrame atualizado
print(turbina)

# Criando o gráfico com a categorização das potências reais em função da velocidade do vento
sns.scatterplot(data=turbina, x='Wind Speed (m/s)', y='LV ActivePower (kW)', hue='DentroLimite', s=1, palette=cores)

# Exibindo o gráfico
plt.show()
