
# Estrutura de Dados


## Geo.py (biblioteca geopy)

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


## Wheater.py (OpenWheater API e biblioteca requests)

OpenWheater é uma API que tem diversos retornos em se tratando de clima baseado em uma latitude e longitude dada.

Usaremos a biblioteca requests para fazer uma requisição para a API OpenWheater com a latitude e a longitude coletada pelo geopy através do município, estado ou país fornecido pelo usuário.

### Variáveis

| Nomes das variáveis |              Para que servem              |
|-------------------- | ----------------------------------------- |
| lat                 | armanena a latidude                       |
| long                | armazena a longitude                      |
| api_key             | armazena a API_Key do usuário OpenWheater |
