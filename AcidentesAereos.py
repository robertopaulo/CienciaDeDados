from google.colab import files

# Fazer upload do arquivo do seu computador
uploaded = files.upload()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV
df = pd.read_csv('aviation-accident-data-2023-05-16.csv')

# Visualizar as primeiras linhas
df.head()

# -------------------------------------------
# 4. Exibir informações gerais do DataFrame
# -------------------------------------------
df.info()

# -------------------------------------------
# 5. Remover linhas com valores faltantes (NaN)
# -------------------------------------------
df_limpo = df.dropna()

# Verificar novamente após remoção
df_limpo.info()

# -------------------------------------------
# 6. Calcular estatísticas descritivas básicas
# -------------------------------------------

# Substitua por uma coluna numérica do seu dataset
# Aqui vamos tentar com a coluna "fatalities", se ela existir
coluna = 'fatalities'

# Verificar se a coluna existe e é numérica
if coluna in df_limpo.columns and pd.api.types.is_numeric_dtype(df_limpo[coluna]):
    media = df_limpo[coluna].mean()
    mediana = df_limpo[coluna].median()
    desvio_padrao = df_limpo[coluna].std()
    minimo = df_limpo[coluna].min()
    maximo = df_limpo[coluna].max()

    print(f"Média: {media}")
    print(f"Mediana: {mediana}")
    print(f"Desvio padrão: {desvio_padrao}")
    print(f"Mínimo: {minimo}")
    print(f"Máximo: {maximo}")
else:
    print(f"A coluna '{coluna}' não está disponível ou não é numérica.")

# -------------------------------------------
# 7. Obter resumo estatístico com describe()
# -------------------------------------------
df_limpo.describe()

# Estilo visual do seaborn
sns.set(style="whitegrid")
# Converte a coluna de texto para número
df['fatalities'] = pd.to_numeric(df['fatalities'], errors='coerce')

# Remove linhas com valores ausentes apenas dessa coluna
df_limpo = df.dropna(subset=['fatalities'])

# Filtrar dados até 50 fatalidades para visualização
df_fatal_filtrado = df_limpo[df_limpo['fatalities'] <= 50]

plt.figure(figsize=(10, 5))
sns.histplot(df_fatal_filtrado['fatalities'], bins=20, kde=True, color='darkblue')
plt.title('Distribuição de Fatalidades por Acidente (até 50 fatalidades)')
plt.xlabel('Total de Fatalidades')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Filtra os dados para até 50 fatalidades
df_fatal_filtrado = df_limpo[df_limpo['fatalities'] <= 50]

plt.figure(figsize=(8, 2))
sns.boxplot(x=df_fatal_filtrado['fatalities'], color='salmon')
plt.title('Boxplot de Fatalidades Totais (até 50)')
plt.xlabel('Total de Fatalidades')
plt.grid(True)
plt.show()

# Convert 'year' column to numeric, coercing errors
df_limpo['year'] = pd.to_numeric(df_limpo['year'], errors='coerce')

# Drop rows where 'year' conversion resulted in NaN
df_limpo.dropna(subset=['year'], inplace=True)

plt.figure(figsize=(16, 6))
sns.boxplot(data=df_limpo[df_limpo['year'] >= 2000], x='year', y='fatalities', palette='viridis')
plt.title('Distribuição de Fatalidades por Ano (a partir de 2000)')
plt.xlabel('Ano')
plt.ylabel('Total de Fatalidades')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Apenas se quiser ver número de acidentes por país (ou outro atributo)
plt.figure(figsize=(12, 5))
sns.countplot(data=df, y='country', order=df['country'].value_counts().head(10).index, palette='viridis')
plt.title('Top 10 Países com Mais Acidentes Registrados')
plt.xlabel('Número de Acidentes')
plt.ylabel('País')
plt.show()

# Selecionar os 10 países com mais registros
top_paises = df_limpo['country'].value_counts().head(10).index

plt.figure(figsize=(14, 6))
sns.boxplot(data=df_limpo[df_limpo['country'].isin(top_paises)],
            x='country', y='fatalities', palette='pastel')
plt.title('Distribuição de Fatalidades por País (Top 10)')
plt.xlabel('País')
plt.ylabel('Total de Fatalidades')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Tenta converter a coluna de data
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Cria uma nova coluna com o ano
df['year'] = df['date'].dt.year

# Remove linhas sem ano
df_ano = df.dropna(subset=['year'])

plt.figure(figsize=(12, 5))
df_ano['year'].value_counts().sort_index().plot(kind='line', marker='o', color='teal')
plt.title('Total de Acidentes por Ano')
plt.xlabel('Ano')
plt.ylabel('Número de Acidentes')
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 5))
fatal_por_ano.plot(kind='bar', color='tomato')

plt.title('Total de Fatalidades por Ano')
plt.xlabel('Ano')
plt.ylabel('Fatalidades Totais')
plt.grid(True)

# Exibir apenas de 10 em 10 anos
anos = fatal_por_ano.index
plt.xticks(ticks=range(0, len(anos), 10), labels=anos[::10], rotation=45)

plt.tight_layout()
plt.show()

# Filtrar apenas anos múltiplos de 10 (ex: 1960, 1970, 1980...)
fatal_por_ano_decada = fatal_por_ano[fatal_por_ano.index % 10 == 0]

plt.figure(figsize=(12, 5))
fatal_por_ano_decada.plot(kind='bar', color='tomato')

plt.title('Total de Fatalidades por Década')
plt.xlabel('Ano')
plt.ylabel('Fatalidades Totais')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
