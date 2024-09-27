from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from pydantic import BaseModel, Field
import pickle
import numpy as np


# Configuração da aplicação
info = Info(title="API de Predição de Câncer de Mama", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definição das Tags
tag_home = Tag(name='Home', description='Documentação em Swagger')
tag_predicao = Tag(
    name='Predição',
    description='Operações de predição de câncer de mama'
)


# Criação da Rota de Redirecionamento à raiz da documentação
@app.get('/', tags=[tag_home])
def home():
    """ Redireciona para a tela inicial da documentação em Swagger.
    """
    return redirect('/openapi/swagger')


# Definição da classe de entrada
class EntradaPredicao(BaseModel):
    dados: list[float] = Field(
        ...,
        description='Lista de características do tumor',
        example=[
            14.13, 19.29, 91.97, 654.89, 0.10, 0.10, 0.09, 0.05, 0.18, 0.06,
            0.41, 1.22, 2.87, 40.34, 0.01, 0.03, 0.03, 0.01, 0.02, 0.00,
            16.27, 25.68, 107.26, 880.58, 0.13, 0.25, 0.27, 0.11, 0.29, 0.08
        ]
    )


# Carregamento do modelo de Machine Learning
with open('modelo.pkl', 'rb') as file:
    modelo = pickle.load(file)


# Definição da rota de predição
@app.post('/predicao', tags=[tag_predicao])
def predicao(body: EntradaPredicao):
    '''Realiza a predição de câncer de mama'''
    dados = np.array(body.dados).reshape(1, -1)
    predicao = modelo.predict(dados)
    resultado = 'Maligno' if predicao[0] == 1 else 'Benigno'
    return {'predicao': resultado}


if __name__ == '__main__':
    app.run(debug=True)
