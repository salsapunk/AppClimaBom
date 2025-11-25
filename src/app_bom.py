import streamlit as st
from weather import Resposta

# Funções:
def pesquisarCidade():
  r = Resposta(cidade, estado)
  r.requisicao()

  return r.d_clima

# Título da aplicação
st.title("AppClimaBom")

# Definindo variáveis de estado de sessão
if 'pesquisa_feita' not in st.session_state:
  st.session_state.pesquisa_feita = False

if 'clima_semana' not in st.session_state:
  st.session_state.clima_semana = []

# Definindo linhas da aplicação:
row1 = st.columns([3, 2.5, 1], vertical_alignment='bottom')

# 1° Linha | Barras de pesquisa:
with row1[0]:
  cidade = st.text_input("Cidade", placeholder="Ex.: Guarulhos")

with row1[1]:
  estado = st.text_input("Estado", placeholder="Ex.: São Paulo")

with row1[2]:
  p = None
  pesquisar = st.button('Buscar')

  if pesquisar:
    p = pesquisarCidade()
    arr_semana = list(vars(p).values())[1:] # A tag [1:] é para excluir a redundância da classe Clima_localidade ("clima_atual" & "clima_dia1")

    for dia in arr_semana:
      st.session_state.clima_semana.append({
        'temp': dia['temperatura'],
        'temp_min': dia['temperatura mínima'],
        'temp_max': dia['temperatura máxima'],
        'sensacao': "N/A",
        'umidade': "N/A", # NÃO SE PREOCUPAR NO MOMENTO; Será obtida posteriormente
        'vento_velo': "{:.3f}".format(
          dia['velocidade do vento'] / 3.6
        ),
        'vento_dir': dia['direção do vento']
      })
    st.session_state.pesquisa_feita = True

# 2° Linha | Resultados:
if st.session_state.pesquisa_feita == True:
  with st.container(key="resultados_dia_0", border=True):
    clima_dia0 = st.session_state['clima_semana'][0]
    row2 = st.columns(2)

    with row2[0]:
      st.header(f'{clima_dia0['temp']} °C')
      st.markdown(f'''
        **Parcial, nublado** <br/>
        **MIN:** {clima_dia0['temp_min']}° | 
        **MAX:** {clima_dia0['temp_max']}° <br/>
        Sensação Térmica de {clima_dia0['sensacao']}°
      ''', True)
    
    with row2[1]:
      st.subheader(f'{cidade}, {estado}') # Valores temporários; serão substituído por valores obtidos da API
      subrow = st.columns(2)

      with subrow[0]:
        st.markdown(f'''
          #### Vento:
          {clima_dia0['vento_velo']} m/s <br/>
          Sentido {clima_dia0['vento_dir']}
      ''', True)
        
      with subrow[1]:
        st.markdown(f'''
          #### Umidade:
          {clima_dia0['umidade']}%
        ''')