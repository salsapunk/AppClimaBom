
# AppClimaBom 🌦️

## [ Levantamento de Requisitos ]

### 1. Introdução

Este documento descreve os requisitos funcionais e não funcionais do “Aplicativo de Clima”, o objetivo do sistema é fornecer informações meteorológicas atualizadas e precisas, permitindo que os usuários consultem o clima atual, previsões e alertas de forma simples e intuitiva.

### 2. Descrição Geral

### 2.1. Usuários

**Usuário comum:** consulta o clima e previsões.

### 2.2. Restrições

- Requer conexão com a internet para atualizações;
- O uso de dados de geolocalização depende de permissão do usuário;

### 3. Requisitos Funcionais (RF)

| Código | Descrição | Prioridade | Status |
| --- | --- | --- | --- |
| **RF01** | O sistema deve permitir buscar o clima por cidade. | Alta | Concluído |
| **RF02** | O sistema deve exibir dados como temperatura, umidade, vento e sensação térmica. | Alta | Concluído |
| **RF03** | O sistema deve emitir alertas meteorológicos. | Alta | A fazer |
| **RF04** | O sistema deve apresentar previsão para até 5 dias. | Média | Concluído |
| **RF05** | O sistema deve permitir alternar entre °C e °F. | Baixa | Concluído |

### 4. Requisitos Não Funcionais (RNF) ⭐

| Código | Descrição | Categoria | Prioridade | Status |
| --- | --- | --- | --- | --- |
| **RNF01** | Responder em até 3 segundos. | Desempenho | Alta | Concluído |
| **RNF02** | Alta disponibilidade (99%). | Confiabilidade | Alta | Concluído |
| **RNF03** | Interface responsiva e intuitiva. | Usabilidade | Alta | Concluído |
| **RNF04** | Utilizar API meteorológica confiável | Integração | Alta | Concluído |

### 5. Backlog de Prioridades

| Prioridade | Funcionalidade | Tipo | Status |
| --- | --- | --- | --- |
| 🟥 Alta | Clima atual, busca por cidade, alertas | RF | Em andamento |
| 🟨 Média | Previsão 5 dias | RF/RNF | Concluído |
| 🟩 Baixa | Escolha °C/°F, histórico | RF | Concluído |

### 6. Tecnologias

**IDE**: Visual Studio Code

**Controladores de versão**: Git e Github

**Bibliotecas Python**: requests, geopy e Streamlit, open-meteo

**Gerenciador de dependências**: pip

**Gerenciador de projetos**: Trello

**Ferramentas de design**: [Draw.io](http://draw.io/),Figma

### 7. Critérios de Aceitação

- O app exibe o clima atual em até 3 segundos;
- A busca retorna resultados válidos;
- O sistema exibe alerta quando há perigo climático.

# Estrutura de Dados

## Visão geral :

As variáveis mais importantes para garantir os RFs são armazenados em dicionários, como nos atributos da classe Clima_localidade e d_clima na classe Resposta. Há o uso rápido de strings e floats, mas apenas o suficiente para garantir o funcionamento da aplicação.

## Visão detalhada:

### [app.py](https://github.com/salsapunk/AppClimaBom/blob/main/src/app_bom.py)

Armazena, principalmente, strings dadas por inputs do usuário, como *cidade* e *estado*, além de armazenar a variável st.session_state, que permite atualizar os valores exibidos na página.

### [weather.py](https://github.com/salsapunk/AppClimaBom/blob/main/src/weather.py)

## **Clima_localidade**

Seus atributos armazenam dicionários com as informações selecionadas futuramente.

# **Resposta**

- *Localidade*: armazena o retorno de um método de classe
- *lat e lon*: armazenam inteiros da latitude e longitude respectivamente
- *API_KEY*: armazena uma string com a chave da API
- *resposta*: armazenará a response da API em json
- *d_clima*: armazenará um objeto da classe Clima_localidade
- *dados que são retornados pela API e o que o app oferece de informação:*
    - temperatura atual, máxima e mínima;
    - sensação térmica;
    - humidade relativa do ar;
    - velocidade do vento e a precipitação total;

[**Trello**](https://trello.com/invite/b/69035d59701d4b56c044175d/ATTI4570caebf70c43845a78070ffe26c48f07B73633/quadro-principal)

### PO: Lígia Andreza

### Scrum Master: Maria Eduarda

### Integrantes:

- Bernardo James (Implemenação)
- João Pedro da Silva Queiroz (Implementação)
- Lígia Andreza (PO e Analista de requisitos)
- Luiz Carlos (Implementação)
- Maria Eduarda (Scrum Master) 
