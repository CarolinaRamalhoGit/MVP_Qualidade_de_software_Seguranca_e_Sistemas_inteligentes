# Modelo de _Machine Learning_ para a Predição de Câncer de Mama 

## 1. Introdução

Este projeto é o MVP - Minimum Viable Product - da Sprint Arquitetura de Softwares do Curso de Engenharia de Software da PUC-Rio. O MVP é composto por um _notebook_ Google Colab e uma aplicação _Full Stack_.

## 2. Modelo de _Machine Learning_

O _notebook_ contém o Relatório do Modelo de _Machine Learning_ (e o próprio modelo) treinado para a classificação e predição de tipos de tumores mamários (benignos ou malignos), utilizando como base o _dataset Diagnostic Wisconsin Breast Cancer_ disponível no [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic).

Este _dataset_ foi criado a partir de imagens de biópsias de tumores de mama, coletadas e analisadas pela Universidade de Wisconsin. De acordo com o [artigo original](https://minds.wisconsin.edu/bitstream/handle/1793/59692/TR1131.pdf?sequence=1), foram utilizadas técnicas de processamento de imagem, que permitiram extrair 10 características que descrevem propriedades de cada núcleo de um conjunto das células do tumor de 569 indivíduos, como tamanho, forma, textura, dentre outros. Para cada um desses conjuntos foram calculados a média, o desvio-padrão e o "pior" (ou maior) valor, resultando, assim, em 30 características para cada indivíduo, além da característica-alvo: a benignidade ou malignidade do tumor.

:warning: :warning: :warning: Atualizar :warning: :warning: :warning: No presente MVP, obteve-se uma acurácia de XXXX%, com um modelo treinado a partir do algoritmo xxxx com validação cruzada (_cross validation_).


## 3. Aplicação _Full Stack_

A aplicação desenvolvida objetiva, de forma simples, carregar o modelo de _machine learning_ de forma embarcada no _back-end_, com a possibilidade de entrada de novos dados no _front-end_, de modo que o modelo de classificação faça a predição da classe de saída (tumor maligno ou benigno).

### 3.1 Execução do Back-end

### 3.1.1. Pré-requisitos
- Recomenda-se o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

- Faz-se necessária a instalação de todas as dependências/bibliotecas listadas no arquivo requirements.txt:

        (env)$ pip install -r requirements.txt

### 3.1.2. Execução
1. Para processar a API e consultar sua documentação em Swagger, executar:

        (env)$ flask run --host 0.0.0.0 --port 5000

2. Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.


## 4. Considerações
:warning: :warning: :warning: Atualizar :warning: :warning: :warning: Por se tratar de um MVP, 
