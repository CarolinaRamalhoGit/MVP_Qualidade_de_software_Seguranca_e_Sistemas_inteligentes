from sklearn.datasets import load_breast_cancer
import pandas as pd
import streamlit as st
import requests

# Carregamento e preparação do dataset
dados = load_breast_cancer()
X = dados.data
nomes_caracteristicas = list(dados.feature_names)
dataset = pd.DataFrame(X, columns=nomes_caracteristicas)

# Calcular estatísticas descritivas
estatisticas = dataset.describe().T

# Criar um dicionário com as estatísticas
estatisticas_caracteristicas = {}
for nome in nomes_caracteristicas:
    estatisticas_caracteristicas[nome] = {
        'min': estatisticas.loc[nome, 'min'],
        'max': estatisticas.loc[nome, 'max'],
        'média': estatisticas.loc[nome, 'mean'],
        'desvio padrão': estatisticas.loc[nome, 'std']
    }

# Criação de um dicionário com a descrição das características
descricao_caracteristicas = {
    'mean radius': 'Média dos valores do raio do tumor',
    'mean texture': 'Média dos valores da textura do tumor',
    'mean perimeter': 'Média dos valores do perímetro do tumor',
    'mean area': 'Média dos valores da área do tumor',
    'mean smoothness': 'Média dos valores da suavidade do tumor',
    'mean compactness': 'Média dos valores da compacidade do tumor',
    'mean concavity': 'Média dos valores da concavidade do tumor',
    'mean concave points': 'Média dos valores dos pontos côncavos do tumor',
    'mean symmetry': 'Média dos valores da simetria do tumor',
    'mean fractal dimension': 'Média dos valores da dimensão fractal do tumor',
    'radius error': 'Desvio-padrão dos raios do tumor',
    'texture error': 'Desvio-padrão das texturas do tumor',
    'perimeter error': 'Desvio-padrão dos perímetros do tumor',
    'area error': 'Desvio-padrão das áreas do tumor',
    'smoothness error': 'Desvio-padrão das suavidades do tumor',
    'compactness error': 'Desvio-padrão das compacidades do tumor',
    'concavity error': 'Desvio-padrão das concavidades do tumor',
    'concave points error': 'Desvio-padrão dos pontos côncavos do tumor',
    'symmetry error': 'Desvio-padrão das simetrias do tumor',
    'fractal dimension error': 'Desvio-padrão das dimensões fractais do tumor',
    'worst radius': 'Pior valor de raio do tumor',
    'worst texture': 'Pior valor de textura do tumor',
    'worst perimeter': 'Pior valor de perímetro do tumor',
    'worst area': 'Pior valor de área do tumor',
    'worst smoothness': 'Pior valor de suavidade do tumor',
    'worst compactness': 'Pior valor de compacidade do tumor',
    'worst concavity': 'Pior valor de concavidade do tumor',
    'worst concave points': 'Pior valor de pontos côncavos do tumor',
    'worst symmetry': 'Pior valor de simetria do tumor',
    'worst fractal dimension': 'Pior valor de dimensão fractal do tumor'
}

# Inicializar o estado das entradas
if 'inputs' not in st.session_state:
    st.session_state['inputs'] = {}

# Funções para limpar e pré-preencher o formulário


def reset_inputs():
    '''Limpa o formulário'''
    for nome in nomes_caracteristicas:
        st.session_state['inputs'][nome] = None
        st.session_state[nome] = None


def prefill_inputs():
    '''Pré-preenche o formulário com os valores médios'''
    for nome in nomes_caracteristicas:
        stats = estatisticas_caracteristicas[nome]
        media = float(stats['média'])
        st.session_state['inputs'][nome] = media
        st.session_state[nome] = media


# Título da aplicação
st.title('Predição de Câncer de Mama')

# Botões de Ação
st.header('Escolha uma ação:')
col1, col2 = st.columns(2)
with col1:
    if st.button('Limpar Formulário'):
        reset_inputs()
with col2:
    if st.button('Pré-preencher Formulário'):
        prefill_inputs()

# Botão para realizar a predição
st.header("Realizar Predição")
if st.button('Fazer Predição', key='predict_button'):
    # Preparar dados a partir do estado das entradas
    caracteristicas = [st.session_state['inputs'].get(
        nome) for nome in nomes_caracteristicas]
    
    # Verificar se todas as entradas foram preenchidas
    if None in caracteristicas:
        st.error(
            'Por favor, preencha todas as características antes de fazer a predição')
    else:
        # Converter "," para "." em cada característica
        caracteristicas = [f"{float(str(c).replace(',', '.')):.2f}" for c in caracteristicas]
        
        entrada = {'dados': caracteristicas}
        resposta = requests.post(
            'http://localhost:5000/predicao', json=entrada)
        # Verificar a resposta da API
        if resposta.status_code == 200:
            predicao = resposta.json()['predicao']
            st.success(
                f'A predição realizada para as características inseridas é: **{predicao}**')
        else:
            st.error('Erro ao realizar a predição. Por favor, tente novamente.')


# Dividir as características em grupos
grupos = {'Média': [], 'Desvio-Padrão': [], 'Pior Valor': []}
for nome in nomes_caracteristicas:
    if 'mean' in nome:
        grupos['Média'].append(nome)
    elif 'error' in nome:
        grupos['Desvio-Padrão'].append(nome)
    else:
        grupos['Pior Valor'].append(nome)

# Adicionar abas para cada um dos grupos
tab1, tab2, tab3 = st.tabs(['Média', 'Desvio-Padrão', 'Pior Valor'])

for grupo_nome, tab in zip(['Média', 'Desvio-Padrão', 'Pior Valor'], [tab1, tab2, tab3]):
    with tab:
        st.header(f'Características das Medidas de {grupo_nome}')
        for nome in grupos[grupo_nome]:
            stats = estatisticas_caracteristicas[nome]
            media = float(stats['média'])
            desvio = float(stats['desvio padrão'])
            step = desvio / 10 if desvio != 0 else 0.1

            help_text = (
                f"Valores típicos entre {media - 2 *
                                         desvio:.4f} e {media + 2*desvio:.4f}."
            )
            label = descricao_caracteristicas.get(nome, nome)
            valor = st.number_input(
                label=label,
                value=st.session_state.get(nome, media),
                step=step,
                help=help_text
            )
            st.session_state['inputs'][nome] = valor
