import pandas as pd
import pickle
import warnings

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

# To run: pytest -v test_modelo.py

# configuração para não exibir os warnings
warnings.filterwarnings("ignore")

# Carregamento do modelo de Machine Learning
with open('modelo.pkl', 'rb') as file:
    modelo = pickle.load(file)

# Carregamento do arquivo de teste
teste = 'dados_teste.csv'
dataset_teste = pd.read_csv(teste)
X_teste = dataset_teste.iloc[:, :-1].values
y_teste = dataset_teste.iloc[:, -1].values

# Realiza a predição
predicao = modelo.predict(X_teste)

# Cálculo das métricas
accuracy = accuracy_score(y_teste, predicao)
precision = precision_score(y_teste, predicao)
recall = recall_score(y_teste, predicao)

def test_accuracy():
    assert accuracy >= 0.90

def test_precision():
    assert precision >= 0.90

def test_recall():
    assert recall >= 0.90