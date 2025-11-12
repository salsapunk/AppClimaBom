
# AppClimaBom 🌦️

## [ Levantamento de Requisitos ]

### 1. Introdução

Este documento descreve os requisitos funcionais e não funcionais do “Aplicativo de Clima”, o objetivo do sistema é fornecer informações meteorológicas atualizadas e precisas, permitindo que os usuários consultem o clima atual, previsões e alertas de forma simples e intuitiva.

### 2. Descrição Geral

#### 2.1. Usuários

**Usuário comum:** consulta o clima e previsões.

#### 2.2. Restrições

- Requer conexão com a internet para atualizações;
- O uso de dados de geolocalização depende de permissão do usuário;

### 3. Requisitos Funcionais (RF)

| Código | Descrição | Prioridade |
|:---------------:|:---------------:|:---------------:|
| **RF01** | O sistema deve permitir buscar o clima por cidade. | Alta |
| **RF02** | O sistema deve apresentar previsão para até 5 dias | Média |
| **RF03** | O sistema deve exibir dados como temperatura, umidade, vento e sensação térmica. | Alta |
| **RF04** | O sistema deve emitir alertas meteorológicos. | Alta |
| **RF05**  | O sistema deve permitir alternar entre °C e °F. | Baixa |

### 4. Requisitos Não Funcionais (RNF)

| Código | Descrição | Categoria | Prioridade |
|:---:|:---:|:---:|:---:|
| **RNF01** | Responder em até 3 segundos. | Desempenho | Alta |
| **RNF02** | Alta disponibilidade (99%). | Confiabilidade | Alta |
| **RNF03** | Interface responsiva e intuitiva. | Usabilidade | Alta |
| **RNF04** | Utilizar API meteorológica confiável  | Integração | Alta |

### 5. Backlog de Prioridades

| Prioridade | Funcionalidade | Tipo |
| --- |:---:|:---:|
| 🟥 Alta | Clima atual, busca por cidade, alertas | RF |
| 🟨 Média | Previsão 5 dias | RF/RNF |
| 🟩 Baixa | Escolha °C/°F, histórico | RF |

### 6. Tecnologias

**IDE**: Visual Studio Code
**Controladores de versão**: Git e Github
**Bibliotecas Python**: requests, OpenWeather API, geopy e Streamlit
**Gerenciador de dependências**: pip
**Gerenciador de projetos**: Trello
**Ferramentas de desing**: Draw.io

### 7. Critérios de Aceitação

* O app exibe o clima atual em até 3 segundos;
* A busca retorna resultados válidos;
* O sistema exibe alerta quando há perigo climático.



## Estrutura de Dados


### menu.py 

#### Variáveis

| Nome das variáveis |  Para que servem     |
| ---------- | --------------------------------------------------------------------------------- |
| estado | armazena o estado inserido como string pelo usuário |
| municipio | armazena o município inserido como string pelo usuário |
| juntos | armazena uma string que junta o estado e o município separando-os por um espaço |

### geo.py (biblioteca geopy)

Geopy é uma biblioteca que facilita a localização das coordenadas de os desenvolvedores do Python endereços, cidades, países e pontos de referência em todo o mundo usando terceiros geocódigos e outras fontes de dados.

Importaremos a classe Nominatim, que possui o método geocode(), que nos retornará a localização pelo endereço passado como parâmetro.

#### Funções

|  Funções  |                                     Para que servem                                       |
| --------- | ----------------------------------------------------------------------------------------- |
| geocode() | Retorna a localização e informações sobre ela com base no endereço passado como parâmetro |

#### Variáveis

| Nome das variáveis |                              Para que servem                                      |
| ------------------ | --------------------------------------------------------------------------------- |
| geolocator         | objeto da classe Nominatim, que guarda métodos necessários para o programa        |
| location           | armazena o retorno do método geocode(x), onde x é o endereço passado pelo usuário |
| location.latitude  | consegue a latitude do endereço armazenado em location                            |
| location.longitude | consegue a longitude do endereço armazenado em location                           |


### wheater.py (OpenWheater API e biblioteca requests)

OpenWheater é uma API que tem diversos retornos em se tratando de clima baseado em uma latitude e longitude dada.

Usaremos a biblioteca requests para fazer uma requisição para a API OpenWheater com a latitude e a longitude coletada pelo geopy através do município, estado ou país fornecido pelo usuário.

#### Variáveis

| Nomes das variáveis |              Para que servem              |
|-------------------- | ----------------------------------------- |
| lat                 | armanena a latidude                       |
| long                | armazena a longitude                      |
| api_key             | armazena a API_Key do usuário OpenWheater |
| request | faz a requisição para a API OpenWeather |
| clima | dicionário que armazena as informações recebidas pela request |


[**Trello**](https://trello.com/invite/b/69035d59701d4b56c044175d/ATTI4570caebf70c43845a78070ffe26c48f07B73633/quadro-principal)

##### PO: Lígia Andreza
##### Scrum Master: Maria Eduarda

##### Integrantes:
- Bernardo James (Implemenação)
- João Pedro da Silva Queiroz (Implementação)
- Lígia Andreza (PO e Analista de requisitos)
- Luiz Carlos (Implementação)
- Maria Eduarda (Scrum Master)

***Versão 1.0*** 
