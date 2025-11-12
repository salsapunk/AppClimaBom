import streamlit as st

st.title("ClimaBom")

# Funções:
def pesquisarCidade():
  print(cidade, estado) # <- Substituir por interação com weather.py

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
    st.header('30 °C')
    st.markdown('**Parcial, nublado** <br> **MAX:** 29° | **MIN:** 24° <br/> Sensação Térmica de 31°', True)
  
  with row2[1]:
    st.subheader('Maceió, AL')
    subrow = st.columns(2)
    
    with subrow[0]:
      st.markdown('''
        #### Umidade:
        70%
      ''')

    with subrow[1]:
      st.markdown('''
        #### Vento:
        19 km/h
      ''')
