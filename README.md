
# AppClimaBom 🌦️

## [ Levantamento de Requisitos ]

#### 1. Introdução

Este documento descreve os requisitos funcionais e não funcionais do “Aplicativo de Clima”, o objetivo do sistema é fornecer informações meteorológicas atualizadas e precisas, permitindo que os usuários consultem o clima atual, previsões e alertas de forma simples e intuitiva.

#### 2. Descrição Geral

##### 2.1. Usuários

**Usuário comum:** consulta o clima e previsões.

##### 2.2. Restrições

- Requer conexão com a internet para atualizações;
- O uso de dados de geolocalização depende de permissão do usuário;

##### 3. Requisitos Funcionais (RF)

| Código | Descrição | Prioridade |
|:---------------:|:---------------:|:---------------:|
| **RF01** | O sistema deve permitir buscar o clima por cidade. | Alta |
| **RF02** | O sistema deve apresentar previsão para até 5 dias | Média |
| **RF03** | O sistema deve exibir dados como temperatura, umidade, vento e sensação térmica. | Alta |
| **RF04** | O sistema deve emitir alertas meteorológicos. | Alta |
| **RF05**  | O sistema deve permitir alternar entre °C e °F. | Baixa |

##### 4. Requisitos Não Funcionais (RNF)

| Código | Descrição | Categoria | Prioridade |
|:---:|:---:|:---:|:---:|
| **RNF01** | Responder em até 3 segundos. | Desempenho | Alta |
| **RNF02** | Alta disponibilidade (99%). | Confiabilidade | Alta |
| **RNF03** | Interface responsiva e intuitiva. | Usabilidade | Alta |
| **RNF04** | Utilizar API meteorológica confiável  | Integração | Alta |

##### 5. Backlog de Prioridades

| Prioridade | Funcionalidade | Tipo |
| --- |:---:|:---:|
| 🟥 Alta | Clima atual, busca por cidade, alertas | RF |
| 🟨 Média | Previsão 5 dias | RF/RNF |
| 🟩 Baixa | Escolha °C/°F, histórico | RF |

##### 6. Tecnologias

**IDE**: Visual Studio Code
**Controladores de versão**: Git e Github
**Bibliotecas Python**: requests, OpenWeather API, geopy e Streamlit
**Gerenciador de dependências**: pip
**Gerenciador de projetos**: Trello
**Ferramentas de desing**: Figma

##### 7. Critérios de Aceitação

* O app exibe o clima atual em até 3 segundos;
* A busca retorna resultados válidos;
* O sistema exibe alerta quando há perigo climático.




***Versão 1.0*** 
