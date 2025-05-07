import streamlit as st

def show():
    # Títol amb animació via HTML
    st.markdown(
        '<h3 class="fade-in">📚 Tria el teu nivell de coneixement financer:</h3>',
        unsafe_allow_html=True
    )

    # Descripció animada amb lleu retard
    st.markdown(
        '<p class="fade-in fade-delay-1">'
        'Aquest primer pas ens ajuda a adaptar tot el qüestionari al teu grau d’experiència: '
        'des de la redacció de les preguntes fins al nivell de detall de les explicacions.'
        '</p>',
        unsafe_allow_html=True
    )

    # Botons de selecció de nivell dins de columnes
    cols = st.columns(3)
    levels = ["Baix", "Mitjà", "Expert"]
    for idx, lvl in enumerate(levels):
        sel = (st.session_state.get("level") == lvl)
        cls = "btn-opt-selected" if sel else ""
        with cols[idx]:
            # Obrim el div wrapper amb la classe corresponent
            st.markdown(f'<div class="btn-wrapper {cls}">', unsafe_allow_html=True)

            # El botó en si mateix
            if st.button(lvl, key=f"opt_{lvl}"):
                st.session_state.level = lvl

            # Tanquem el div
            st.markdown('</div>', unsafe_allow_html=True)

    # Descripcions detallades condicionals amb animació
    descr = {
        "Baix": """
<ul>
  🟢 Selecciona aquest nivell si compleixes alguna d'aquestes opcions:
  <li>Has sentit a parlar d’accions i bons, però només de manera bàsica.</li>
  <li>Has navegat alguna vegada per una plataforma d’inversió sense aprofundir.</li>
  <li>T’interessa invertir però no saps encara diferenciar productes (ETFs, fons índex, cripto…)</li>
</ul>
""",
        "Mitjà": """
<ul>
  🟡 Selecciona aquest nivell si compleixes alguna d'aquestes opcions:
  <li>Coneixes diferència entre els fons índexats i ETFs.</li>
  <li>Entens conceptes com la volatilitat, risc i rendibilitat.</li>
  <li>Has utilitzat plataformes d’inversió o el teu banc per invertir.</li>
</ul>
""",
        "Expert": """
<ul>
  🔴 Selecciona aquest nivell si compleixes alguna d'aquestes opcions:
  <li>Has creat carteres pròpies o tens formació en finances.</li>
  <li>Coneixes conceptes com diversificació, beta, sectors o volatilitat.</li>
  <li>T’agrada prendre decisions i entendre els detalls tècnics.</li>
</ul>
"""
    }
    level = st.session_state.get("level")
    if level:
        st.markdown(
            f'<div class="fade-in fade-delay-1 desc-box">{descr[level]}</div>',
            unsafe_allow_html=True
        )
