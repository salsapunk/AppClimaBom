# Estrutura de Dados

## Visão geral :
As variáveis mais importantes para garantir os RFs são armazenados em dicionários, como nos atributos da classe Clima_localidade e d_clima na classe Resposta. Há o uso rápido de strings e floats, mas apenas o suficiente para garantir o funcionamento da aplicação.

## Visão detalhada:
### [app.py](https://github.com/salsapunk/AppClimaBom/blob/main/src/app_bom.py)

Armazena, principalmente, strings dadas por inputs do usuário, como *cidade* e *estado*, além de armazenar a variável st.session_state, que permite atualizar os valores exibidos na página.

### [weather.py](https://github.com/salsapunk/AppClimaBom/blob/main/src/weather.py)

## Clima_localidade

Seus atributos armazenam dicionários com as informações selecionadas futuramente.

# Resposta

- **Localidade**: armazena o retorno de um método de classe
- **lat e lon**: armazenam inteiros da latitude e longitude respectivamente
- **API_KEY**: armazena uma string com a chave da API
- **resposta**: armazenará a response da API em json
- **d_clima**: armazenará um objeto da classe Clima_localidade
