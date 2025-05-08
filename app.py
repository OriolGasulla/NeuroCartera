import streamlit as st
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import requests
import streamlit.components.v1 as components

from steps.pas1 import show as show_pas1
from steps.pas2 import show as show_pas2
from steps.pas3 import show as show_pas3
from steps.pas4 import show as show_pas4
from steps.resum_temporal import show as show_resum_temporal

# Després dels imports:
if "page" not in st.session_state:
    st.session_state.page = "landing"
if "level" not in st.session_state:
    st.session_state.level = None

# -------------------------------------------------------------------
# 0. Configuració de la pàgina
# -------------------------------------------------------------------
st.set_page_config(
    page_title="NeuroCartera",
    page_icon="🧠",
    layout="centered"
)

@st.cache_data(ttl=3600)
def load_lottie_from_url(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# -------------------------------------------------------------------
# 1. Sessió i navegació
# -------------------------------------------------------------------
def init_session():
    if "page" not in st.session_state:
        st.session_state.page = "landing"
    if "level" not in st.session_state:
        st.session_state.level = None

init_session()

lottie_placeholder = st.empty()


# -------------------------------------------------------------------
# 2. Estil personalitzat (igual que el teu primer app.py)
# -------------------------------------------------------------------
st.markdown("""
<style>
  /* GLOBAL */
  html, body, [class*="css"] {
    background-color: #000;
    color: #fff;
    font-family: 'Inter', sans-serif;
    text-align: center;
  }
  main > div {
    max-width: 700px;
    margin: auto;
    padding: 20px;
  }

  /* Botons d'opció: style adaptat a NeuroCartera */
  .stButton > button {
    width: 10rem !important;
    height: 4rem !important;
    border-radius: 4rem !important;
    border-color: #423eaf !important;
    background-color: none !important;   /* blau principal */
    color: #fff !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
    transition: background-color 0.2s ease !important;
    margin: -1rem 0 !important;
  }
  .stButton > button:hover {
    background-color: #807dfb !important;   /* blau hover */
  }
  
  .stButton > button:focus,
  .stButton > button:active {
    background-color: #807dfb !important;
    color: #fff !important;
  }
            
  /* ESTAT “SELECCIONAT” PERSISTENT */
  .btn-wrapper.btn-opt-selected .stButton > button {
      background-color: #807dfb !important;  /* fons blau */
      color: #ffffff !important;             /* text blanc */
      border-color: #6f5fe7 !important;      /* opcional: remarca el contorn */
  }


  /* Navegació: Enrere/Continuar */
  .btn-nav .stButton > button {
    width: 260px !important;
    padding: 1.75rem 3rem !important;
    font-size: 1.1rem !important;
    border-radius: 0.5rem !important;
    background-color: #807dfb !important;
    color: #fff !important;
    border: none !important;
    box-shadow: none !important;
    transform: none !important;
    margin: 0 !important;
  }
  .btn-nav .stButton > button:hover {
    background-color: #1a4fd4 !important;
  }

  /* Progress bar color */
  .stProgress > div > div > div > div {
    background-color: #423eaf !important;
  }

  /* Descripció amb animació */
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  .desc-box {
    background-color: #172D43;
    border-radius: 0.5rem;
    padding: 1rem;
    color: #94DEFF;
    margin: 1rem auto;
    max-width: 600px;
    animation: fadeIn 0.4s ease-out;
  }
  .desc-box ul {
    list-style-type: disc;
    padding-left: 1.5rem;
    margin: 0;
    text-align: left;
  }
  .desc-box ul li {
    margin-bottom: 0.5rem;
  }
/* A partir de 375px d'ample (iPhone) fem que els nav-botons ocupin ~45% cada un */
  @media (max-width: 375px) {
    .btn-nav {
      display: flex !important;
      justify-content: space-between !important;
      gap: 0.5rem !important;
    }
    .btn-nav .stButton > button[data-baseweb="button"] {
      width: 45% !important;    /* dos botons de 45% caben junts */
      padding: 1rem 0.5rem !important;
      font-size: 0.9rem !important;
    }
  }

  @keyframes fadeIn { from{opacity:0;} to{opacity:1;} }
  .fade-in { animation:fadeIn 0.8s ease-out forwards; opacity:0; }
  .fade-delay-1 { animation-delay:0.3s; }
  .fade-delay-2 { animation-delay:0.6s; }

)

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# 3. Header / Landing
# -------------------------------------------------------------------
if st.session_state.page == "landing":
  st.markdown("""
  <div style='text-align: center; margin: -50px 0 2em; margin-bottom: 0px;'>
    <a href="?page=landing" target="_self" style="text-decoration: none;">
      <img src='https://i.imgur.com/JSTDDGq.png' style='width:180px; filter: brightness(0) invert(1);'/>
        <h1 style='color:#fff; margin:0.2em 0;'>NeuroCartera</h1>
    </a>          
    <p style='color:#bbb; margin-top:-10px;'>
      La teva guia personal d'inversió basada en qui ets, no només en què tens.
    </p>
  </div>
  """, unsafe_allow_html=True)
else:
  st.markdown(
      """
      <div style='text-align: center; margin: -50px 0; margin-bottom: 15px;'>
        <a href="?page=landing" target="_self" style="text-decoration: none;">
          <img src="https://i.imgur.com/JSTDDGq.png"
              style="width:180px; filter: brightness(0) invert(1);"/>
        </a>
      </div>
      """,
      unsafe_allow_html=True
  )


# -------------------------------------------------------------------
# 5. Rotació de pàgines
# -------------------------------------------------------------------
# Total de passos
TOTAL_STEPS = 6

# Assigna un número segons la pàgina actual
step_mapping = {
    "quiz_step_1": 1,
    "quiz_step_2": 2,
    "quiz_step_3": 3,
    "quiz_step_4": 4,
    "quiz_step_5": 5,
    "quiz_step_6": 6
}

current_step = step_mapping.get(st.session_state.get("page", "landing"), 0)

# Barra de progrés (només si estem a partir del pas 1)
TOTAL_STEPS = 6

if current_step > 0:
  percentatge = int(((current_step - 1) / (TOTAL_STEPS - 1)) * 100)
  percentatge = max(0, percentatge)  # per evitar valors negatius

  st.progress((current_step - 1) / (TOTAL_STEPS - 1), text=f"{percentatge}% completat")


if st.session_state.page == "landing":
    st.subheader("El teu assessor d'inversió personalitzat i educatiu")
    st.write("Benvingut/da a **NeuroCartera**, la plataforma gratuïta que et guia pas a pas.")
    lottie = requests.get("https://lottie.host/87fe68b4-bdf6-4aad-b65c-fe579eb218d5/QrVwYWgyev.json").json()
    lottie_url = "https://lottie.host/87fe68b4-bdf6-4aad-b65c-fe579eb218d5/QrVwYWgyev.json"
    lottie_data = load_lottie_from_url(lottie_url)
    st_lottie(lottie_data, height=200, key="landing_lottie")
    st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
    st.button("🚀 Començar", on_click=lambda: st.session_state.__setitem__('page','quiz_step_1'))
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "quiz_step_1":
    lottie_placeholder.empty()
    show_pas1()
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        st.button("← Enrere", on_click=lambda: st.session_state.__setitem__('page','landing'))
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        if st.session_state.level:
            st.button("Continuar →", on_click=lambda: st.session_state.__setitem__('page','quiz_step_2'))
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "quiz_step_2":
    show_pas2()
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        st.button("← Enrere", on_click=lambda: st.session_state.__setitem__('page','quiz_step_1'))
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        st.button("Continuar →", on_click=lambda: st.session_state.__setitem__('page','quiz_step_3'))
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "quiz_step_3":
    show_pas3()
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        st.button("← Enrere", on_click=lambda: st.session_state.__setitem__('page','quiz_step_2'))
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        st.button("Continuar →", on_click=lambda: st.session_state.__setitem__('page','quiz_step_4'))
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "quiz_step_4":
    show_pas4()
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        st.button("← Enrere", on_click=lambda: st.session_state.__setitem__('page','quiz_step_3'))
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        st.button("Continuar →", on_click=lambda: st.session_state.__setitem__('page','resum_temporal'))
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "resum_temporal":
    show_resum_temporal()
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        st.button("← Enrere", on_click=lambda: st.session_state.__setitem__('page','quiz_step_4'))
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        st.button("Finalitzar", on_click=lambda: st.session_state.__setitem__('page','landing'))
        st.markdown('</div>', unsafe_allow_html=True)

