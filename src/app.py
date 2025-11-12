import streamlit as st

## Dados para exibição
# (números são figurativos e serão alterados após a modificação destes dados)
if 'dia_0' not in st.session_state:
  st.session_state['dia_0'] = {
    'temp': 28,
    'temp_min': 24,
    'temp_max': 29,
    'sensacao': 31,
    'umidade': 50, # NÃO SE PREOCUPAR NO MOMENTO; Será obtida posteriormente
    'vento_velo_kmph': 19
  }

# Funções:
def pesquisarCidade():
  print(cidade, estado) # <- Substituir por interação com weather.py

# Título da aplicação
st.title("ClimaBom")

# Definindo linhas da aplicação:
row1 = st.columns([3, 2.5, 1], vertical_alignment='bottom')

# 1° Linha | Barras de pesquisa:
with row1[0]:
  cidade = st.text_input("Cidade", placeholder="Ex.: Guarulhos")

with row1[1]:
  estado = st.text_input("Estado", placeholder="Ex.: São Paulo")

with row1[2]:
  pesquisar = st.button('Buscar', on_click=pesquisarCidade)

# 2° Linha | Resultados:
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
    st.subheader('Maceió, AL')
    subrow = st.columns(2)
    
    with subrow[0]:
      st.markdown(f'''
        #### Umidade:
        {st.session_state['dia_0']['umidade']}%
      ''')

    with subrow[1]:
      st.markdown(f'''
        #### Vento:
        {st.session_state['dia_0']['vento_velo_kmph']} km/h
    ''')
