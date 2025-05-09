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

    st.subheader("🧠 Perfil de risc i emocions en la inversió")
    st.markdown("Aquestes preguntes et situaran en escenaris reals per entendre com viuries emocionalment les inversions, i fins a quin punt pots tolerar incertesa, pèrdues o automatització.")

    def pregunta_bloc(titol, descripcio, clave, opcions):
        with st.container():
            col1, col2, col3 = st.columns([1, 6, 1])
            with col2:
                st.markdown(
                    f"""
                    <div style='border: 1px solid #807dfb; border-radius: 10px; padding: 20px; background-color: transparent;'>
                        <h5>{titol}</h5>
                        <p style='margin-bottom: 12px;'>{descripcio}</p>
                    """,
                    unsafe_allow_html=True
                )
                st.radio("", opcions, key=clave)
                st.markdown("</div>", unsafe_allow_html=True)

    pregunta_bloc(
        "Pèrdues a curt termini",
        "Fa 3 mesos que tens 2.000 € invertits. Durant aquest temps, la teva inversió ha pujat un 5%, però avui, després d’una notícia negativa al mercat, obres l’app i veus que tens només 1.700 €. Els mitjans parlen de crisi i molta gent està venen les seves inversions.",
        "risc_q1",
        [
            "Em posaria nerviós/sa i voldria vendre per evitar més pèrdues.",
            "Em preocuparia, però esperaria abans de fer res.",
            "Ho veuria com part del joc i no em generaria angoixa.",
            "Potser afegiria diners per aprofitar la baixada."
        ]
    )

    pregunta_bloc(
        "Incertesa i falta de control",
        "Dues setmanes seguides el valor de la teva inversió oscil·la molt: un dia guanyes 100 €, l’endemà en perds 120 €. Saps que podia passar, però et sorprenen la volatilitat. Com et sentiries?",
        "risc_q2",
        [
            "Molt insegur/a, voldria intervenir-hi d’alguna manera.",
            "Em costaria confiar, però m’esperaria si l’assistent m’ho explica bé.",
            "Em sentiria tranquil, ja sé que les oscil·lacions són normals."
        ]
    )

    pregunta_bloc(
        "Necessitat d’entendre-ho tot",
        "Reps una notificació: la teva cartera ha canviat lleugerament. No tens clar què ha passat, però el sistema t’assegura que és per optimitzar el rendiment.",
        "risc_q3",
        [
            "Necessito saber exactament què ha passat i per què.",
            "M’agradaria una explicació clara, però si em donen confiança, m’ho crec.",
            "Em sembla bé que l’app prengui decisions si millora el resultat."
        ]
    )

    pregunta_bloc(
        "Què esperes sentir mentre inverteixes?",
        "Com t’agradaria sentir-te respecte a la teva inversió en el dia a dia?",
        "risc_q4",
        [
            "Tranquil i amb confiança, sense pensar-hi gaire si puja o baixa.",
            "Implicat i amb control, revisant i entenent cada pas de la inversió.",
            "Amb precaució, evitant a tota costa la pèrdua de diners."
        ]
    )

    pregunta_bloc(
        "Relació emocional amb la inversió",
        "Si poguessis descriure la teva inversió ideal amb una metàfora, quina seria?",
        "risc_q5",
        [
            "Una caixa forta on tot està segur.",
            "Una màquina que treballa per mi mentre jo faig la meva vida.",
            "Una planta que rego cada mes i em dona fruits al cap d’un temps.",
            "Una aventura amb possibilitats reals de fer créixer el meu patrimoni."
        ]
    )

    respostes = {}
    for i in range(1, 6):
        clau = f"risc_q{i}"
        respostes[clau] = st.session_state.get(clau, None)
    st.session_state["respostes_pas3"] = respostes