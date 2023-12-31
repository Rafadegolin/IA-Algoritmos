# -*- coding: utf-8 -*-
"""entregaFinal_MB1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jpwm0bATKy56vdlnp5TUWRhGy_WrBz7X

"""

## Importando biblioteca do pandas 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Importando biblioteca que importa arquivos no Google Colab
from google.colab import files
uploaded = files.upload()

## Testando o arquivo
DSV = pd.read_csv("Immunotherapy.csv") # DSV = Dataset verruga
DSV.head()

"""**DESCRIÇÃO GERAL DO DATASET**

Este dataset se diz respeito a tratamento de verrugas.

**Atributos:** Sexo, idade, tempo de tratamento, número de verrudas, tipo de verrugas, tamanho da verruga em mm², tamanho do endurecimento da verruga no início do tratamento e o resultado do tratamento respectivamente como indicado na tabela acima.

**Número de instâncias:** existem 90 instâncias neste dataset.

**Valores esperados:** É esperado o resultado do tratamento de verruga de acordo com a variação do tipo, do tamanho e do tempo de tratamento de cada paciente.

**FASA DE PRÉ-PROCESSAMENTO**

Analisamos as características das pessoas contidas no dataset, a quantidade de cada sexo, o tempo que levou o tratamento de acordo com o tamanho da sua verruga.

**LIMPEZA E NORMALIZAÇÃO**

Não foi necessário nenhuma normalização, já que nosso dataset se encontra completamente normalizado com dados númericos para representadas cada atributo por exemplo: resultado do tratamento sendo 1 como bem sucedido e 0 como não sucedido. Algumas limpezas foram feitas com finalidades de realizar a execução dos algoritmos, facilitando a análise posterior.

**FASE DE ANÁLISE**

Algoritmo KNeighbors:
**PRIMEIRA CONFIGURAÇÃO**
"""

DSV.info()

DSV_clean = DSV.drop(['Number_of_Warts','Time'], axis = 1)
DSV_clean.info()

## Seleção dos atributos

DSV_sel = DSV_clean[['induration_diameter','age','Type','Area','sex']]
DSV_class = DSV_clean['Result_of_Treatment']
DSV_sel

DSV_class

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(DSV_sel, DSV_class, test_size=0.3)

## Treina o modelo

from sklearn.neighbors import KNeighborsClassifier

# 1- Criar uma instância do modelo
modelo = KNeighborsClassifier(n_neighbors = 5)

# 2- Treinar o modelo
modelo = modelo.fit(x_treino, y_treino)

# 3- Prever novos valores
y_prev = modelo.predict(x_treino)

y_prev

from sklearn.metrics import accuracy_score    # acurácia
from sklearn.metrics import precision_score   # precisão
from sklearn.metrics import recall_score      # revogação
from sklearn.metrics import f1_score          # medida-F
from sklearn.metrics import confusion_matrix  # matriz de confusão

y_prev = modelo.predict(x_teste)
y_prev

accuracy_score(y_teste, y_prev)

precision_score(y_teste, y_prev, average=None)

recall_score(y_teste, y_prev, average=None)

f1_score(y_teste, y_prev, average=None)

confusion_matrix(y_teste, y_prev)

plt.matshow(confusion_matrix(y_teste, y_prev), cmap=plt.cm.Blues)
plt.colorbar()
plt.ylabel('Valores verdadeiros')
plt.xlabel('Valores previstos')
plt.show()

"""Algoritmo KNeighbors: **SEGUNDA CONFIGURAÇÃO**"""

DSV_result = DSV_class == 1
DSV_result

DSV_removido = DSV_class.tail(52)

DSV_resultado = DSV_clean[~DSV_clean.isin(DSV_removido)]
DSV_resultado = DSV_resultado.dropna()

DSV_clean['Result_of_Treatment'].value_counts()

DSV_resultado

DSV_sel = DSV_resultado[['induration_diameter','age','Type','Area','sex']]
DSV_class = DSV_resultado['Result_of_Treatment']

x2_treino, x2_teste, y2_treino, y2_teste = train_test_split(DSV_sel, DSV_class, test_size=0.3)

## Treina o modelo


# 1- Criar uma instância do modelo
modelo2 = KNeighborsClassifier(n_neighbors = 5)

# 2- Treinar o modelo
modelo2 = modelo2.fit(x2_treino, y2_treino)

# 3- Prever novos valores
y2_prev = modelo2.predict(x2_treino)

y2_prev

accuracy_score(y2_treino, y2_prev)

precision_score(y2_treino, y2_prev, average=None)

recall_score(y2_treino, y2_prev, average=None)

f1_score(y2_treino, y2_prev, average=None)

confusion_matrix(y2_teste, y2_prev)

y2_prev = modelo.predict(x2_teste)
y2_prev

plt.matshow(confusion_matrix(y2_teste, y2_prev), cmap=plt.cm.Reds)
plt.colorbar()
plt.ylabel('Valores verdadeiros')
plt.xlabel('Valores previstos')
plt.show()

"""Algoritmo KNeighbors: **TERCEIRA CONFIGURAÇÃO**"""

x3_treino, x3_teste, y3_treino, y3_teste = train_test_split(DSV_sel, DSV_class, test_size=0.3)

## Treina o modelo



# 1- Criar uma instância do modelo
modelo3 = KNeighborsClassifier(n_neighbors = 5)

# 2- Treinar o modelo
modelo3 = modelo3.fit(x3_treino, y3_treino)

# 3- Prever novos valores
y3_prev = modelo3.predict(x3_treino)

y3_prev

accuracy_score(y3_treino, y3_prev)

precision_score(y3_treino, y3_prev, average=None)

recall_score(y3_treino, y3_prev, average=None)

f1_score(y3_treino, y3_prev, average=None)

confusion_matrix(y3_teste, y3_prev)

y3_prev = modelo.predict(x3_teste)
y3_prev

plt.matshow(confusion_matrix(y3_teste, y3_prev), cmap=plt.cm.Greens)
plt.colorbar()
plt.ylabel('Valores verdadeiros')
plt.xlabel('Valores previstos')
plt.show()

"""Algoritmo DecisionTree: **PRIMEIRA CONFIGURAÇÃO**"""

# importando a biblioteca necessária pro algoritmo DecisionTree
from sklearn.tree import DecisionTreeClassifier, plot_tree
# Carregar novamente o arquivo aqui, para manipular o decimal
DSV2 = pd.read_csv("Immunotherapy.csv")
# Substituir vírgulas por pontos na coluna 'Time'
DSV2['Time'] = DSV2['Time'].str.replace(',', '.').astype(float)
# testando a leitura do dataset, com a troca da , pelo .
DSV2.head()

# Separar as variáveis independentes (X) e a variável dependente (y)
X = DSV2.iloc[:, :-1]
y = DSV2.iloc[:, -1]

# Primeira config: profundidade max da árvore = 3; amostras pra dividir nó da árvore = 5; max de recursos = nenhum
dt1 = DecisionTreeClassifier(max_depth=3, min_samples_split=5, max_features=None)
dt1.fit(X, y)

# Imprimir e plotar árvore resultante
fig, ax = plt.subplots(figsize=(10, 10))
plot_tree(dt1, ax=ax, feature_names=X.columns, class_names=['classe0', 'classe1'])
plt.show()
print("O score do modelo 1 é: ", dt1.score(X, y)) # Imprimir score do modelo

"""Algoritmo DecisionTree: **SEGUNDA CONFIGURAÇÃO**"""

# Segunda config: profundidade max da árvore = 10; amostras pra dividir nó da árvore = 10; max de recursos = 2
dt2 = DecisionTreeClassifier(max_depth=10, min_samples_split=10, max_features=2)
dt2.fit(X, y)

# Imprimir e plotar árvore resultante
fig, ax = plt.subplots(figsize=(10, 10))
plot_tree(dt2, ax=ax, feature_names=X.columns, class_names=['classe0', 'classe1'])
plt.show()
print("O score do modelo 2 é: ", dt2.score(X, y)) # Imprimir score do modelo

"""Algoritmo DecisionTree: **TERCEIRA CONFIGURAÇÃO**"""

# Terceira config: profundidade max da árvore = 5; amostras pra dividir nó da árvore = 20; max de recursos = 3
# Configuração 3: max_depth=5, min_samples_split=20, max_features=3
dt3 = DecisionTreeClassifier(max_depth=5, min_samples_split=20, max_features=3)
dt3.fit(X, y)

# Imprimir e plotar árvore resultante
fig, ax = plt.subplots(figsize=(10, 10))
plot_tree(dt3, ax=ax, feature_names=X.columns, class_names=['classe0', 'classe1'])
plt.show()
print("O score do modelo 3 é: ", dt3.score(X, y)) # Imprimir score do modelo

"""Algoritmo a ser escolhido -> ***RANDOM FOREST***: **PRIMEIRA CONFIGURAÇÃO**

Como algoritmo a ser escolhido escolhemos o Random Forest, por ainda utilizar árvore de classificação, não fugindo muito do último algoritmo, porém ele utiliza várias árvores de decisões durante o método, assim obtendo uma classificação final mais precisa, ele funciona criando várias árvores de decisão em cima de diferentes subconjuntos dos dados e combinando seus resultados.
"""

# importando as bibliotecas necessárias pro algoritmo RANDOM FOREST
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

DSV3 = pd.read_csv("Immunotherapy.csv")
DSV3['Time'] = DSV3['Time'].str.replace(',', '.').astype(float)
# testando a leitura do dataset
DSV3.head(90)

# Separar as colunas de features e a coluna de target (classe)
X = DSV3.drop('Result_of_Treatment', axis=1)
y = DSV3['Result_of_Treatment']

# Separar as colunas de features e a coluna de target (classe)
X = DSV3.drop('Result_of_Treatment', axis=1)  # colunas de features
y = DSV3['Result_of_Treatment']  # coluna de target

# Divisão dos dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Primeira configuração: estimators (complexidade do modelo) = 100; profundidade max = nenhuma
# Criando o modelo para treinar
rfc1 = RandomForestClassifier(n_estimators=100, max_depth=None, max_features='sqrt', random_state=42)
rfc1.fit(X_train, y_train)

# previsao do modelo
y_pred = rfc1.predict(X_test)

# Plotando a árvore da primeira configuração 
plt.figure(figsize=(15, 10))
tree.plot_tree(rfc1.estimators_[0], feature_names=X.columns, class_names=[str(i) for i in rfc1.classes_], filled=True)
plt.show()

# Avaliando o desempenho do modelo na configuração 1
print("Acurácia do modelo é: ", accuracy_score(y_test, y_pred))

# Segunda configuração: estimators (complexidade do modelo) = 50; profundidade max = 10; aleatoridade = 42
# Criando o modelo para treinar
rfc2 = RandomForestClassifier(n_estimators=500, max_depth=5, max_features='sqrt', random_state=42)
rfc2.fit(X_train, y_train)

# previsao do modelo
y_pred = rfc2.predict(X_test)

# Plotando a árvore da segunda configuração 
plt.figure(figsize=(15, 10))
tree.plot_tree(rfc2.estimators_[0], feature_names=X.columns, class_names=[str(i) for i in rfc1.classes_], filled=True)
plt.show()

# Avaliando o desempenho do modelo na configuração 2
print("Acurácia: ", accuracy_score(y_test, y_pred))

# Terceira configuração: estimators (complexidade do modelo) = 50; profundidade max = 10; aleatoridade = 42
# Criando o modelo para treinar
rfc3 = RandomForestClassifier(n_estimators=250, max_depth=8, max_features='log2', random_state=42)
rfc3.fit(X_train, y_train)

# previsao do modelo
y_pred = rfc3.predict(X_test)

# Plotando a árvore da terceira configuração 
plt.figure(figsize=(15, 10))
tree.plot_tree(rfc2.estimators_[0], feature_names=X.columns, class_names=[str(i) for i in rfc1.classes_], filled=True)
plt.show()

# Avaliando o desempenho do modelo na configuração 3
print("Acurácia:", accuracy_score(y_test, y_pred))

"""**FASE DE CONCLUSÃO**

Nosso dataset continha dados de tratamento de verrugas por imunoterapia, onde a margem de recuperação era na média de 83% num total de 90 pessoas, onde 41 eram homens e 49 mulheres, de 15 a 56 anos de idade.
"""
