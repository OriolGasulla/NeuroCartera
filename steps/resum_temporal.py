import streamlit as st

def show():
    st.title("📋 Resum temporal de respostes")

    st.markdown("Aquesta pàgina mostra les dades recollides dels **passos 1, 2 i 3** per comprovar que tot funciona correctament.")

    # PAS 1
    st.subheader("🔎 Pas 1 – Coneixements financers")
    st.write("**Nivell escollit:**", st.session_state.get("level", "No definit"))

    # PAS 2
    st.subheader("💼 Pas 2 – Informació general")
    st.write("**Edat:**", st.session_state.get("age", "No definida"))
    st.write("**Situació financera:**", st.session_state.get("financial_situation", "No definida"))
    st.write("**Horitzó d’inversió:**", st.session_state.get("investment_horizon", "No definit"))

    # PAS 3
    st.subheader("🧠 Pas 3 – Perfil de risc emocional")
    res3 = st.session_state.get("respostes_pas3", {})
    if not res3:
        st.write("No hi ha respostes de pas 3 disponibles.")
    else:
        for i in range(1, 6):
            clave = f"risc_q{i}"
            st.write(f"**Pregunta {i}:**", res3.get(clave, "No respost"))

    # PAS 4
    st.subheader("📈 Pas 4 – Perfil d'expectatives")
    res4 = st.session_state.get("respostes_pas4", {})
    if not res4:
        st.write("No hi ha respostes de pas 4 disponibles.")
    else:
        for i in range(1, 6):
            clave = f"exp_q{i}"
            st.write(f"**Pregunta {i}:**", res4.get(clave, "No respost"))

    # DEBUG complet (opcional)
    st.markdown("---")
    st.markdown("🔧 **Debug complet de session_state:**")
    st.json(dict(st.session_state))
