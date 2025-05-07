# app.py

import streamlit as st
from streamlit_lottie import st_lottie
import requests

# -------------------------------------------------------------------
# 1. Configuració pàgina
# -------------------------------------------------------------------
st.set_page_config(
    page_title="NeuroCartera",
    page_icon="🧠",
    layout="centered"
)

# -------------------------------------------------------------------
# 2. Estil personalitzat (Demo fosc)
# -------------------------------------------------------------------
st.markdown("""
<style>
/* Fons negre, text blanc, font Inter */
html, body, [class*="css"] {
    background-color: #000000;
    color: #ffffff;
    font-family: 'Inter', sans-serif;
}
/* Contenidor central, fons transparent */
main > div {
    max-width: 700px;
    margin: auto;
    padding: 20px;
    background: transparent;
}

/* Botons centrats i animats (blau demo) */
.stButton > button {
    background-color: #2d61e3 !important;
    color: #ffffff !important;
    border-radius: 0.5rem !important;
    padding: 0.5rem 1rem !important;
    border: none !important;
    transition: transform 0.2s, background-color 0.2s !important;
    display: block;
    margin: 1rem auto;
}
.stButton > button:hover {
    background-color: #1a4fd4 !important;
    transform: scale(1.05) !important;
}
.stButton > button:active {
    transform: scale(0.95) !important;
}

/* Progress bar blau */
.stProgress > div > div > div > div {
    background-color: #2d61e3 !important;
}

/* Radio blanc */
div[data-baseweb="radio"] .baseweb-radio-control {
    border-color: #ffffff !important;
}
div[data-baseweb="radio"] .baseweb-radio-control:hover {
    background-color: rgba(255,255,255,0.1) !important;
}
div[data-baseweb="radio"] .baseweb-radio-check {
    background-color: #e63946 !important;  /* Accent vermell de Streamlit Dark */
}

/* Recuadre animat per a descripcions (blau demo) */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to   { opacity: 1; transform: translateY(0); }
}
.desc-box {
  background-color: #172D43;
  border-radius: 0.5rem;
  padding: 1rem;
  color: #94DEFF;
  margin: 1rem 0;
  animation: fadeIn 0.4s ease-out;
}
.desc-box ul {
  list-style-type: disc;
  padding-left: 1.5rem;
  margin: 0;
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
<div style='text-align: center; margin-top: -30px; margin-bottom: 2em;'>
  <img src='https://i.imgur.com/JSTDDGq.png' style='width:180px; margin-bottom: 10px; filter: brightness(0) invert(1);'/>
  <h1 style='margin-top: 0.2em; color: #ffffff;'>NeuroCartera</h1>
  <p style='font-size: 1.1em; color: #bbbbbb; margin-top: -10px;'>
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

def load_lottie_url(url: str):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else {}

# -------------------------------------------------------------------
# 5. Landing Page
# -------------------------------------------------------------------
def landing_page():
    st.subheader("El teu assessor d'inversió personalitzat i educatiu")
    st.write("""
        Benvingut/da a **NeuroCartera**, la plataforma gratuïta que et guia pas a pas
        en la teva inversió. Fes clic al botó per començar el test i descobrir
        la cartera ideal per al teu perfil.
    """)
    lottie = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")
    st_lottie(lottie, height=200)
    st.button("🚀 Començar el test", on_click=go_to_quiz_step_1)

# -------------------------------------------------------------------
# 6. Pas 1: Nivell de coneixements
# -------------------------------------------------------------------
def quiz_step_1():
    st.progress(0.25)
    st.subheader("Pas 1 de 5: Nivell de coneixements")
    st.write("Selecciona el teu nivell; adaptarà tot el qüestionari:")

    options = ["Baix", "Mitjà", "Alt"]
    st.radio(
        label="Quin és el teu nivell en finances?",
        options=options,
        key="level"
    )

    if st.session_state.level:
        html_lists = {
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
        st.markdown(
            f"<div class='desc-box'>{html_lists[st.session_state.level]}</div>",
            unsafe_allow_html=True
        )

    col1, col2 = st.columns(2)
    with col1:
        st.button("◀️ Enrere", on_click=go_to_landing)
    with col2:
        if st.session_state.level:
            st.button("Continuar ▶️", on_click=go_to_quiz_step_2)

# -------------------------------------------------------------------
# 7. Ruting de pàgines
# -------------------------------------------------------------------
init_session()
if st.session_state.page == "landing":
    landing_page()
elif st.session_state.page == "quiz_step_1":
    quiz_step_1()
# elif st.session_state.page == "quiz_step_2":
#     quiz_step_2()
