# Estrutura de Dados 🎲

## Visão geral:

- As variáveis mais importantes para garantir os RFs são armazenados em dicionários, como nos atributos da classe Clima_localidade e d_clima na classe Resposta.
- Há o uso rápido de strings e floats, mas apenas o suficiente para garantir o funcionamento da aplicação.
- Utilizamos listas (para guardar as informações) em variáveis como '''clima_semana''' e '''dia''' em '''[resposta.py](src/resposta.py)''' e dicionários (para organizar a resposta da API) como '''diario''' e '''horario'''
- Usamos a busca binária --- complexidade O(n) --- para todas as buscar realizadas nos dicionários da API.

## Visão detalhada:

## [app.py](https://github.com/salsapunk/AppClimaBom/blob/main/src/app_bom.py)

Armazena, principalmente, strings dadas por inputs do usuário, como cidade e estado.Armazena, também, a variável st.session_state, que permite atualizar os valores exibidos na página

## [weather.py](https://github.com/salsapunk/AppClimaBom/blob/main/src/weather.py)

Clima_localidade -
Seus atributos recebem e armazenam listas ordenadas, como o clima_horas, que armazena pelo dia ('''clima_horas[0]''', retorna todos as as horas do dia atual) e pelas horas ('''clima_horas[0][0]''' retorna a hora 00:00 dia dia atual).

## [Resposta.py](src/resposta.py)

- Localidade: armazena o retorno de um método de classe;
- lat e lon: armazenam inteiros da latitude e longitude respectivamente;
- API_KEY: armazena uma string com a chave da API;
- response: armazenará a response da API em json;
- d_clima: armazenará um objeto da classe Clima_localidade;
