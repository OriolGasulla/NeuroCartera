import streamlit as st

def show():
    st.title("📋 Resum temporal de respostes")

    st.markdown("Aquesta pàgina mostra les dades recollides dels **passos 1 i 2** per comprovar que tot funciona correctament.")

    st.subheader("🔎 Pas 1 – Coneixements financers")
    st.write("**Nivell escollit:**", st.session_state.get("level", "No definit"))

    st.subheader("💼 Pas 2 – Informació general")

    st.write("**Edat:**", st.session_state.get("age", "No definida"))
    st.write("**Situació financera:**", st.session_state.get("financial_situation", "No definida"))
    st.write("**Horitzó d’inversió:**", st.session_state.get("investment_horizon", "No definit"))

    # Mostrem tot el session_state per a debugging
    st.markdown("---")
    st.markdown("🔧 **Debug complet de session_state:**")
    st.json(dict(st.session_state))

    st.markdown("---")
    if st.button("Tornar a la landing", use_container_width=True):
        st.session_state.page = "landing"
