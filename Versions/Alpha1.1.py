import streamlit as st
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import requests

# -------------------------------------------------------------------
# 1. Configuració de la pàgina
# -------------------------------------------------------------------
st.set_page_config(
    page_title="NeuroCartera",
    page_icon="🧠",
    layout="centered"
)

# -------------------------------------------------------------------
# 2. Estil personalitzat (overrides CSS per als botons)
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

  /* Opcions: botons escalats i transparents */
  button[data-baseweb="button"] {
    transform: scale(1.5) !important;
    transform-origin: center center !important;
    background: transparent !important;
    color: #2d61e3 !important;
    border: 2px solid #2d61e3 !important;
    border-radius: 1rem !important;
    transition: background-color 0.2s, color 0.2s !important;
  }
  button[data-baseweb="button"]:hover {
    background-color: rgba(45,97,227,0.1) !important;
  }

  /* Estat seleccionat (resalta l'opció activa) */
  .btn-opt-selected button[data-baseweb="button"] {
    background-color: #2d61e3 !important;
    color: #fff !important;
  }

  /* Navegació: Enrere/Continuar */
  .btn-nav .stButton > button[data-baseweb="button"] {
    transform: none !important;
    background-color: #2d61e3 !important;
    color: #fff !important;
    border-radius: 0.5rem !important;
    padding: 1.75rem 3rem !important;
    font-size: 1.1rem !important;
    border: none !important;
    width: 260px !important;
    margin: 0 !important;
  }
  .btn-nav .stButton > button[data-baseweb="button"]:hover {
    background-color: #1a4fd4 !important;
    transform: none !important;
  }

  /* Progress bar color */
  .stProgress > div > div > div > div {
    background-color: #2d61e3 !important;
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
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# 3. Header / Landing
# -------------------------------------------------------------------
st.markdown("""
<div style='text-align: center; margin: -30px 0 2em;'>
  <img src='https://i.imgur.com/JSTDDGq.png' style='width:180px; filter: brightness(0) invert(1);'/>
  <h1 style='color:#fff; margin:0.2em 0;'>NeuroCartera</h1>
  <p style='color:#bbb; margin-top:-10px;'>
    La teva guia personal d'inversió basada en qui ets, no només en què tens.
  </p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# 4. Sessió i navegació
# -------------------------------------------------------------------
def init_session():
    if "page" not in st.session_state:
        st.session_state.page = "landing"
    if "level" not in st.session_state:
        st.session_state.level = None


def go_to_landing():
    st.session_state.page = "landing"
    st.session_state.level = None


def go_to_quiz_step_1():
    st.session_state.page = "quiz_step_1"


def go_to_quiz_step_2():
    st.session_state.page = "quiz_step_2"


def go_to_quiz_step_3():
    st.session_state.page = "quiz_step_3"


def load_lottie_url(url: str):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else {}

# -------------------------------------------------------------------
# 5. Landing Page
# -------------------------------------------------------------------
def landing_page():
    st.subheader("El teu assessor d'inversió personalitzat i educatiu")
    st.write("Benvingut/da a **NeuroCartera**, la plataforma gratuïta que et guia pas a pas en la teva inversió.")
    lottie = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")
    st_lottie(lottie, height=200)
    st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
    st.button("🚀 Començar el test", on_click=go_to_quiz_step_1)
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------------
# 6. Pas 1: Nivell de coneixements
# -------------------------------------------------------------------
def quiz_step_1():
    st.progress(0.25)
    st.subheader("Pas 1 de 5: Nivell de coneixements")
    st.write("Selecciona el teu nivell; adaptarà tot el qüestionari:")

    # Estil de l'opció seleccionada
    if st.session_state.level:
        st.markdown(f"""
            <style>
              .btn-opt-selected button[data-baseweb="button"] {{
                background-color: #2d61e3 !important;
                color: #fff !important;
              }}
            </style>
        """, unsafe_allow_html=True)

    # Botons d'opcions
    for lvl in ["Baix", "Mitjà", "Alt"]:
        cls = "btn-opt-selected" if st.session_state.level == lvl else ""
        st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
        st.button(lvl, key=f"opt_{lvl}", on_click=lambda l=lvl: st.session_state.__setitem__('level', l))
        st.markdown('</div>', unsafe_allow_html=True)

    # Descripció contextual
    if st.session_state.level:
        descr = {
            "Baix": """
<ul>
    🟢 Escolleix aquest nivell si compleixes alguna d'aquestes opcions:
  <li>Mai has invertit o només ho has fet a través d'un banc.</li>
  <li>No saps què és un ETF, un dividend o la volatilitat.</li>
  <li>Et fa respecte la inversió i prefereixes seguretat.</li>
</ul>
""",
            "Mitjà": """
<ul>
    🟡 Escolleix aquest nivell si compleixes alguna d'aquestes opcions:
  <li>Coneixes què són les accions i els bons.</li>
  <li>Has utilitzat alguna plataforma com MyInvestor, Indexa o Degiro.</li>
  <li>Coneixes ETFs, cripto o fons de dividends, però sense aprofundir tècnicament.</li>
</ul>
""",
            "Alt": """
<ul>
    🔴 Escolleix aquest nivell si compleixes alguna d'aquestes opcions:
  <li>Has creat carteres pròpies o tens formació en finances.</li>
  <li>Coneixes conceptes com diversificació, beta, sectors o volatilitat.</li>
  <li>T’agrada prendre decisions i entendre els detalls tècnics.</li>
</ul>
"""
        }
        st.markdown(f"<div class='desc-box'>{descr[st.session_state.level]}</div>", unsafe_allow_html=True)

    # Navegació Pas 1
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        st.button("◀️ Enrere", on_click=go_to_landing)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        if st.session_state.level:
            st.button("Continuar ▶️", on_click=go_to_quiz_step_2)
        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------------
# 7. Pas 2: Estructura en construcció
# -------------------------------------------------------------------
def quiz_step_2():
    st.progress(0.50)
    st.caption("Pas 2 de 5: A definir")
    st.subheader("🛠️ Aquesta secció està en construcció.")
    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        st.button("◀️ Enrere", on_click=go_to_quiz_step_1)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        st.button("Continuar ▶️", on_click=go_to_quiz_step_3)
        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------------
# 8. Pas 3: Estructura en construcció
# -------------------------------------------------------------------
def quiz_step_3():
    st.progress(0.75)
    st.caption("Pas 3 de 5: A definir")
    st.subheader("🔧 Aquesta secció encara està en construcció.")

    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        st.button("◀️ Enrere", on_click=go_to_quiz_step_2)
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="btn-nav">', unsafe_allow_html=True)
        st.button("Continuar ▶️", on_click=lambda: None)
        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------------
# 9. Rutació de pàgines
# -------------------------------------------------------------------
init_session()
if st.session_state.page == "landing":
    landing_page()
elif st.session_state.page == "quiz_step_1":
    quiz_step_1()
elif st.session_state.page == "quiz_step_2":
    quiz_step_2()
elif st.session_state.page == "quiz_step_3":
    quiz_step_3()