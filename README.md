# Modelo de _Machine Learning_ para a Predição de Câncer de Mama 

# 1. Introdução

Este projeto é o MVP - _Minimum Viable Product_ - da Sprint Arquitetura de Softwares do Curso de Engenharia de Software da PUC-Rio. O MVP é composto por um [_notebook_](Relatorio_ML.ipynb) Google Colab e uma aplicação _Full Stack_.

# 2. Modelo de _Machine Learning_

O _notebook_ contém o Relatório do Modelo de _Machine Learning_ (e o próprio modelo) treinado para a classificação e predição de tipos de tumores mamários (benignos ou malignos), utilizando como base o _dataset Diagnostic Wisconsin Breast Cancer_ disponível no [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic).

No presente MVP, obteve-se uma acurácia de 94,74%, com um modelo treinado a partir do algoritmo SVM (_Support Vector Machine_) com validação cruzada (_cross validation_).


# 3. Aplicação _Full Stack_

A aplicação desenvolvida objetiva, de forma simples, carregar o modelo de _machine learning_ de forma embarcada no _back-end_, com a possibilidade de entrada de novos dados no _front-end_, de modo que o modelo de classificação faça a predição da classe de saída (tumor maligno ou benigno) para estes dados.

## 3.1. Execução do _Back-end_

### 3.1.1. Pré-requisitos
- Recomenda-se o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

- Faz-se necessária a instalação de todas as dependências/bibliotecas listadas no arquivo requirements.txt do diretório do [Back-end](back_end):

```
        (env)$ pip install -r requirements.txt
```

### 3.1.2. Testes Automatizados

Para assegurar que o modelo embarcado atenda aos requisitos estabelecidos (Acurácia, Precisão e _Recall_ acima de 95%), executar:

```
        (env)$ pytest -v test_modelo.py  
```

### 3.1.3. Execução

1. Para processar a API e consultar sua documentação em Swagger, executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

2. Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.


## 3.2. Execução do _Front-End_

### 3.2.1. Pré-requisitos

- Recomenda-se o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

- Faz-se necessária a instalação de todas as dependências/bibliotecas listadas no arquivo requirements.txt do diretório [Front-End](front_end):

```
(env)$ pip install -r requirements.txt
```

- Faz-se necessário realizar o procesamento da API previamente. Para isto, executar os procedimentos do item 3.1. do presente documento.


### 3.2.2. Execução
1. Para processar o _Front-End_, executar:

```
(env)$ streamlit run interface.py
```

## 4. Considerações

Por se tratar de um MVP, algumas funcionalidades, não foram priorizadas para o desenvolvimento, tais como:
- um banco de dados integrado à aplicação; e
- a possibilidade de entrada dos dados de outras formas, como um arquivo json para entrada únicas, ou CSV, para múltiplas entradas.

Ressalta-se, ainda, que no Relatório do Modelo de _Machine Learning_, também foram apontadas sugestões de possíveis melhorias ao modelo de predição. 


