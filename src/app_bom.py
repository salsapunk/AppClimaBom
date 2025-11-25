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

if 'dia_0' not in st.session_state:
  st.session_state.dia_0 = {
    'temp': None,
    'temp_min': None,
    'temp_max': None,
    'sensacao': None,
    'umidade': None,
    'vento_velo': None,
    'vento_dir': None
  }

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
    st.session_state.dia_0 = {
      'temp': p.clima_dia1['temperatura'],
      'temp_min': p.clima_dia1['temperatura mínima'],
      'temp_max': p.clima_dia1['temperatura máxima'],
      'sensacao': "N/A",
      'umidade': "N/A", # NÃO SE PREOCUPAR NO MOMENTO; Será obtida posteriormente
      'vento_velo': "{:.3f}".format(
        p.clima_dia1['velocidade do vento'] / 3.6
      ),
      'vento_dir': p.clima_dia1['direção do vento']
    }
    st.session_state.pesquisa_feita = True

# 2° Linha | Resultados:
if st.session_state.pesquisa_feita == True:
  with st.container(key="resultados_dia_0", border=True):
    row2 = st.columns(2)

    with row2[0]:
      st.header(f'{st.session_state['dia_0']['temp']} °C')
      st.markdown(f'''
        **Parcial, nublado** <br/>
        **MIN:** {st.session_state['dia_0']['temp_min']}° | 
        **MAX:** {st.session_state['dia_0']['temp_max']}° <br/>
        Sensação Térmica de {st.session_state['dia_0']['sensacao']}°
      ''', True)
    
    with row2[1]:
      st.subheader(f'{cidade}, {estado}') # Valores temporários; serão substituído por valores obtidos da API
      subrow = st.columns(2)

      with subrow[0]:
        st.markdown(f'''
          #### Vento:
          {st.session_state['dia_0']['vento_velo']} m/s <br/>
          Sentido {st.session_state['dia_0']['vento_dir']}
      ''', True)
        
      with subrow[1]:
        st.markdown(f'''
          #### Umidade:
          {st.session_state['dia_0']['umidade']}%
        ''')