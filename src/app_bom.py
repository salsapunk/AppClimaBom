import datetime
import streamlit as st
from resposta import Resposta

# Funções:
def pesquisarCidade():
  try:
    r = Resposta(cidade, estado)
    r.requisicao()
    
    return {
      'success': True,
      'data': r.d_clima
    }
  except:
    return {
      'success': False,
      'data': None
    }

# Título da aplicação
st.title("AppClimaBom")

# Definindo variáveis de estado de sessão
if 'pesquisa_feita' not in st.session_state:
  st.session_state.pesquisa_feita = False

if 'clima_semana' not in st.session_state:
  st.session_state.clima_semana = []

if 'resposta_api' not in st.session_state:
  st.session_state.resposta_api = { 
    'success': None, 'data': None
  }

with st.form("pesquisa"):
  # Definindo linhas da aplicação:
  row1 = st.columns([3, 2.5, 1], vertical_alignment='bottom')

  # 1° Linha | Barras de pesquisa:
  with row1[0]:
    cidade = st.text_input("Cidade", placeholder="Ex.: Guarulhos")

  with row1[1]:
    estado = st.text_input("Estado", placeholder="Ex.: São Paulo")

  with row1[2]:
    pesquisar = st.form_submit_button('Buscar')

    if pesquisar:
      st.session_state.resposta_api = pesquisarCidade()
      st.session_state.pesquisa_feita = True

      if st.session_state.resposta_api['success']:
        semana = st.session_state.resposta_api['data'].clima_dia
        st.session_state.clima_semana = []

        for dia in semana:
          info_dia = {
            'temp': dia['Temperatura'],
            'temp_min': dia['Temperatura_min'],
            'temp_max': dia['Temperatura_max'],
            'sensacao': dia["Sensação térmica"],
            'umidade': dia["Humidade"],
            'vento_velo': dia["Velocidade do vento"],
            'precipitacao': dia["Precipitação"], # Não utilizada no momento
            'vento_dir': "N/A"
          }
          st.session_state.clima_semana.append(info_dia)

def alterarMedida():
  numMedidaAtual = st.session_state.select_unidade_medida 
  medidaAtual: int # 0 = Celsius, 1 = Fahrenheit, 2 = Kelvin
  match numMedidaAtual:
    case 0:
      medidaAtual = 'Celsius'
    case 1:
      medidaAtual = 'Fahrenheit'
    case 2:
      medidaAtual = 'Kelvin'
    case _:
      medidaAtual = 'Celsius'

  # Alteração:
  st.session_state.resposta_api['data'].converter_temp(medidaAtual)
  st.session_state.resposta_api['data'].medida = medidaAtual

# 2° Linha | Resultados:
if (
  st.session_state.pesquisa_feita == True 
  and st.session_state.resposta_api['success']
):
  mapa_abv_medidas = {
    0: '°C',
    1: '°F',
    2: '°K'
  }
  selection = st.segmented_control(
    "Unidade de medida",
    options=mapa_abv_medidas.keys(),
    format_func=lambda option: mapa_abv_medidas[option],
    key="select_unidade_medida",
    selection_mode="single",
    default=0,
    on_change=alterarMedida
  )
  abv_medida = '°C' if selection is None else mapa_abv_medidas[selection]
  
  with st.container(key="resultados_dia_atual", border=True):
    clima_dia0 = st.session_state['clima_semana'][0]
    row2 = st.columns(2)

    with row2[0]:
      st.header(f'{clima_dia0['temp']} {abv_medida}')
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

  for idx_dia, dia in enumerate(st.session_state.clima_semana):
    with st.container(key=f"resultados_dia_{idx_dia}", border=True):
      col1, col2 = st.columns(2, vertical_alignment='center')
      
      dias_semana = [
        'Segunda-feira', 'Terça-feira', 'Quarta-feira', 
        'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo',
      ] # Ordem baseada na semana de trabalho americana; Semana começa na Segunda-feira.
      idx_hoje = datetime.date.today().weekday()
      dias_ordenados = dias_semana[idx_hoje:] + dias_semana[:idx_hoje]

      with col1:
        dia_exibido = dias_ordenados[(idx_dia + 1) % 7 if idx_dia >= 7 else idx_dia]
        if idx_dia == 0: dia_exibido = "Hoje"
        
        st.markdown(f"""
          <h4>{dia_exibido}:</h4>
          <p>Dia {idx_dia + 1}</p> <!-- No futuro substituir por data (ex.: 1 de abril) -->
        """, True)
      
      with col2:
        st.markdown(f"""
          <p style='text-align: right;'>
            <strong style='font-size: 20px;'>{dia['temp']} °C</strong> <br/>
            {dia['temp_min']}° | {dia['temp_max']}°
          </p>
        """, True)

# 2° Linha | Tratamento de Erros:
if (
  st.session_state.pesquisa_feita == True 
  and not st.session_state.resposta_api['success']
):
  with st.container(key="erro", border=True):
    st.header('Localização Não Encontrada')
    st.markdown('''
      :man_shrugging: A localização que você inseriu não foi encontrada. <br />
      :mag: Por favor, certifique-se de ter digitado os dados corretamente.
    ''', True)