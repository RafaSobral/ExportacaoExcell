# Análise de Dados de Turbina Eólica

Este projeto realiza a análise de dados de uma turbina eólica utilizando Python. O objetivo principal é processar os dados fornecidos em um arquivo CSV, categorizar as potências reais da turbina em relação aos limites calculados a partir da curva de potência teórica, e gerar gráficos para facilitar a visualização das informações.

## Requisitos

As dependências necessárias para rodar o projeto estão especificadas no arquivo `requirements.txt`. Certifique-se de instalar todas as dependências antes de executar o código.

Para instalar as dependências, execute:

```bash
pip install -r requirements.txt
```

## Dados

O arquivo CSV (`T1.csv`) deve conter as seguintes colunas:

- `Date/Time`: Data e hora do registro.
- `Wind Speed (m/s)`: Velocidade do vento em metros por segundo.
- `LV ActivePower (kW)`: Potência ativa medida em kW.
- `Theoretical_Power_Curve (KWh)`: Curva teórica de potência em KWh.
- `Wind Direction (°)`: Direção do vento em graus (opcional).

## Funcionalidades

1. **Carregamento e processamento de dados:**
   - Carrega os dados do arquivo CSV.
   - Converte a coluna `Date/Time` para o formato datetime.
   - Remove colunas desnecessárias, como `Wind Direction (°)`.

2. **Cálculo dos limites de potência:**
   - Calcula os limites máximo e mínimo baseados em 6% acima e 5% abaixo da potência teórica.
   - Classifica os dados em "Dentro", "Fora" ou "Zero", baseado nos limites calculados.

3. **Análise de dados:**
   - Gera gráficos de dispersão para a potência ativa e curva teórica.
   - Destaca visualmente os valores categorizados em relação à velocidade do vento.

4. **Cálculo de porcentagens:**
   - Exibe a porcentagem de valores dentro dos limites calculados.

## Uso

Execute o script principal em Python para processar os dados e gerar os gráficos:

```bash
python main.py
```

Certifique-se de que o arquivo `T1.csv` está no mesmo diretório do script ou especifique o caminho correto para o arquivo.

## Resultados

O script gera:

- Gráfico de dispersão da potência ativa em função da velocidade do vento.
- Gráfico com a classificação dos valores em "Dentro", "Fora" ou "Zero".
- Saída no terminal com a porcentagem de valores dentro do limite.

## Estrutura do Projeto

```plaintext
.
├── T1.csv               # Arquivo de dados
├── main.py              # Script principal
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação do projeto
```





