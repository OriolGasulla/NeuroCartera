import streamlit as st
import streamlit.components.v1 as components


def show():
    # FORÇA el navegador a fer scroll a (0,0) quan es carrega la pàgina
    st.markdown(
        '<div id="scroll-target" tabindex="-1" '
        'style="position:absolute;top:-80px;left:0;height:1px;width:1px;"></div>',
        unsafe_allow_html=True
    )
    components.html(
        """
        <script>
          setTimeout(() => {
            try {
              // Recolzem sobre window.top perquè estigui fora de l'iframe
              const root = window.top.document;
              const target = root.getElementById('scroll-target');
              if (target) {
                target.scrollIntoView({ behavior: 'auto', block: 'start' });
                window.top.scrollBy(0, -80);
                target.focus();  // algunes vegades focus() reforça el scroll
              }
            } catch (e) {
              // silenciem errors
            }
          }, 50);  // pots ajustar el 300 ms si la pàgina triga més a renderitzar
        </script>
        """,
        height=0,
    )


    st.subheader("🎯 Expectatives i motivacions")
    st.markdown("Aquestes preguntes t’ajudaran a connectar amb els teus objectius reals i a establir una visió clara del que esperes de la teva experiència inversora.")

    def pregunta_bloc(titol, descripcio, clave, opcions):
        with st.container():
            col1, col2, col3 = st.columns([1, 6, 1])
            with col2:
                st.markdown(
                    f"""
                    <div style='border: 1px solid #807dfb; border-radius: 10px; padding: 20px; background-color: transparent;'>
                        <h4>{titol}</h4>
                        <p style='margin-bottom: 12px;'>{descripcio}</p>
                    """,
                    unsafe_allow_html=True
                )
                st.radio("", opcions, key=clave)
                st.markdown("</div>", unsafe_allow_html=True)

    pregunta_bloc(
        "1️⃣ Què t’ha portat fins aquí?",
        "Què t’ha motivat a començar a invertir?",
        "exp_q1",
        [
            "M’he adonat que els diners al banc no em generen res.",
            "Vull començar a construir el meu futur financer des de ja.",
            "M’inquieta la meva situació econòmica a llarg termini.",
            "Tinc interès a entendre com funciona el món de les inversions."
        ]
    )

    pregunta_bloc(
        "2️⃣ Objectiu de la inversió",
        "Imagina’t que d’aquí 5 anys tot ha anat bé amb la teva suposada inversió. Què hauria de passar perquè et sentis satisfet/da?",
        "exp_q2",
        [
            "Hauré assolit un objectiu concret (ex. comprar un pis, pagar uns estudis).",
            "Tindré un sistema estable que em dona ingressos extra mensuals.",
            "M’hauré sentit més tranquil/a sabent que faig créixer el meu futur.",
            "Hauré après a gestionar millor els meus diners i em sentiré empoderat/da."
        ]
    )

    pregunta_bloc(
        "3️⃣ Horitzó i paciència",
        "Quan esperes començar a veure resultats significatius de la teva inversió?",
        "exp_q3",
        [
            "A curt termini: m’agradaria veure moviment en pocs mesos.",
            "A mitjà termini: en 1-2 anys ja voldria notar millores.",
            "A llarg termini: em centro en resultats a 5-10 anys vista.",
            "No tinc pressa: la meva prioritat és fer-ho bé, ni ràpid ni lent."
        ]
    )

    pregunta_bloc(
        "4️⃣ Tipus de creixement esperat",
        "Com t’agradaria que creixés la teva inversió?",
        "exp_q4",
        [
            "Lent però segur, com un arbre que fa fruit amb el temps.",
            "Amb petites aportacions mensuals que vagin sumant a llarg termini.",
            "Amb pujades accentuades, sabent que també pot baixar greument.",
            "Flexible: si en algun moment vull ajustar-ho, ho podré fer."
        ]
    )

    pregunta_bloc(
        "5️⃣ Relació emocional amb la inversió",
        "Si poguessis descriure la teva inversió ideal amb una metàfora, quina seria?",
        "exp_q5",
        [
            "Una caixa forta on tot està segur.",
            "Una màquina que treballa per mi mentre jo faig la meva vida.",
            "Una planta que rego cada mes i em dona fruits al cap d’un temps.",
            "Una aventura amb possibilitats reals de fer créixer el meu patrimoni."
        ]
    )
    respostes = {}
    for i in range(1, 6):
        clau = f"exp_q{i}"
        respostes[clau] = st.session_state.get(clau, None)
    st.session_state["respostes_pas4"] = respostes
