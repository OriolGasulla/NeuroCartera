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
    for i in range(1, 6):
        clau = f"risc_q{i}"
        resposta = st.session_state.get(clau, "No respost")
        st.write(f"**Pregunta {i}:**", resposta)

    # PAS 4
    st.subheader("📈 Pas 4 – Perfil de expectatives")
    for i in range(1, 6):
        clau = f"exp_q{i}"
        resposta = st.session_state.get(clau, "No respost")
        st.write(f"**Pregunta {i}:**", resposta)

    # DEBUG complet (opcional)
    st.markdown("---")
    st.markdown("🔧 **Debug complet de session_state:**")
    st.json(dict(st.session_state))
