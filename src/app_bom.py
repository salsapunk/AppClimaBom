import datetime
import streamlit as st
from resposta import Resposta
from time import sleep

# Customizações visuais da interface:
with open("src/style.css") as f:
  st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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

def atualizarClimaSemana():
  # Atributos de dados da classe ClimaLocalidade:
  semana = st.session_state.clima_localidade['data'].clima_semana
  dia_atual = st.session_state.clima_localidade['data'].clima_horas
  alertas = st.session_state.clima_localidade['data'].alertas
  medida = st.session_state.clima_localidade['data'].medida
  
  # Redefinindo estado:
  st.session_state.clima_semana = []
  st.session_state.clima_dia = []
  
  # Formatações:
  fTempCompleto = "{:.0f} °{}"
  fTempSimples = "{:.0f}°"

  # Alterando estado:
  for dia in semana:
    info_dia = {
      'temp': fTempCompleto.format(dia['temperatura'], medida[:1]),
      'temp_min': fTempSimples.format(dia['temperatura_min']),
      'temp_max': fTempSimples.format(dia['temperatura_max']),
      'sensacao': fTempSimples.format(dia['sensacao_termica']),
      'umidade': dia['humidade'],
      'vento_velo': dia['velocidade_do_vento'],
      'precipitacao': dia['precipitacao'], # Não utilizada no momento
    }
    st.session_state.clima_semana.append(info_dia)

  for hora in dia_atual[0]:
    try: hora['hora'] = hora['hora'].split('T')[1]
    except: hora['hora'] = hora['hora']
    st.session_state.clima_dia.append(hora)

  st.session_state.alertas = alertas

def alterarMedida():
  numMedidaAtual = st.session_state.select_unidade_medida 
  st.session_state.num_unidade_medida = numMedidaAtual

  medidaAtual: str
  match numMedidaAtual:
    case 0:
      medidaAtual = 'Celsius'
    case 1:
      medidaAtual = 'Fahrenheit'
    case 2:
      medidaAtual = 'Kelvin'
    case _:
      medidaAtual = 'Celsius'

  st.session_state.clima_localidade['data'].converter_temp(medidaAtual)
  st.session_state.clima_localidade['data'].medida = medidaAtual
  atualizarClimaSemana()

# Definindo variáveis de estado de sessão
if 'pesquisa_feita' not in st.session_state:
  st.session_state.pesquisa_feita = False

if 'clima_semana' not in st.session_state:
  st.session_state.clima_semana = []

if 'clima_dia' not in st.session_state:
  st.session_state.clima_dia = []

if 'alertas' not in st.session_state:
  st.session_state.alertas = []

if 'clima_localidade' not in st.session_state:
  st.session_state.clima_localidade = { 
    'success': None, 'data': None
  }

if 'num_unidade_medida' not in st.session_state:
  # 0 = Celsius, 1 = Fahrenheit, 2 = Kelvin
  st.session_state.num_unidade_medida = 0

# Título da aplicação
st.title("AppClimaBom")

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
      st.session_state.clima_localidade = pesquisarCidade()
      st.session_state.pesquisa_feita = True

      if st.session_state.clima_localidade['success']:
        atualizarClimaSemana()

# 2° Linha | Resultados:
if (
  st.session_state.pesquisa_feita == True 
  and st.session_state.clima_localidade['success']
):
  mapa_abv_medidas = {
    0: '°C',
    1: '°F',
    2: '°K'
  }
  
  with st.container(key="resultados_dia_atual", border=True):
    clima_dia0 = st.session_state['clima_semana'][0]
    row2 = st.columns(2)

    with row2[0]:
      st.header(f'{clima_dia0['temp']}')
      st.markdown(f'''
        **MIN:** {clima_dia0['temp_min']} | 
        **MAX:** {clima_dia0['temp_max']} <br/>
        Sensação Térmica de {clima_dia0['sensacao']}
      ''', True)
    
    with row2[1]:
      st.subheader(f'{cidade}, {estado}') # Valores temporários; serão substituído por valores obtidos da API
      subrow = st.columns(2)

      with subrow[0]:
        st.markdown(f'''
          #### Vento:
          {clima_dia0['vento_velo']} m/s <br/>
      ''', True)
        
      with subrow[1]:
        st.markdown(f'''
          #### Umidade:
          {clima_dia0['umidade']}%
        ''')

  row1, row2 = st.columns(2, vertical_alignment='center')

  with row1:
    select_unidade_medida = st.segmented_control(
      "Unidade de medida",
      options=mapa_abv_medidas.keys(),
      format_func=lambda option: mapa_abv_medidas[option],
      key="select_unidade_medida",
      selection_mode="single",
      default=st.session_state.num_unidade_medida,
      on_change=alterarMedida
    )

  with row2:
    def exibindo_alertas(alertas):
      if alertas is not None:
        st.toast("Buscando alertas...")
        sleep(1)
        st.toast(f"Evento: {alertas["evento"]}")
        sleep(2)
        st.toast(f"Começo do alerta: {alertas["comeco"]}")
        sleep(1)
        st.toast(f"Fim do alerta: {alertas["fim"]}")
        sleep(2)
        st.toast(f"Orgão emissor: {alertas["emissor"]}")
        sleep(2)
        st.toast(f"Severidade: {alertas["severidade"]}")
        sleep(2)
        st.toast(f"Descrição: {alertas["descricao"]}")
        exibindo_alertas(alertas)
      else:
        st.toast("Não há alertas na sua região.")
    if st.button("Procurar alertas"):
      exibindo_alertas(st.session_state.alertas)

  tab1, tab2 = st.tabs(["Semana", "Dia Atual"])

  with tab1:
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
              <strong style='font-size: 20px;'>{dia['temp']}</strong> <br/>
              {dia['temp_min']} | {dia['temp_max']}
            </p>
          """, True)
  
  with tab2:
    st.line_chart(
      st.session_state.clima_dia, 
      x='hora', 
      y=['temperatura', 'sensacao_termica'], 
      x_label='Hora', 
      y_label=f'Temperaturas (°{st.session_state.clima_localidade['data'].medida[:1]})')

# 2° Linha | Tratamento de Erros:
if (
  st.session_state.pesquisa_feita == True 
  and not st.session_state.clima_localidade['success']
):
  with st.container(key="erro", border=True):
    st.header('Localização Não Encontrada')
    st.markdown('''
      :man_shrugging: A localização que você inseriu não foi encontrada. <br />
      :mag: Por favor, certifique-se de ter digitado os dados corretamente.
    ''', True)
