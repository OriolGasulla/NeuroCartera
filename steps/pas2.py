import streamlit as st

# Pas 2: Preguntes generals per a tots els nivells
def show():
    st.subheader("Dades Generals")

    # 1) Edat de l'usuari
    st.number_input(
        label="Quina és la teva edat?",
        min_value=18,
        max_value=100,
        step=1,
        key="age"
    )

    # 2) Situació financera personal
    fs = st.selectbox(
        label="Com descriuries la teva situació financera actual?",
        options=["Estable", "Moderada", "Inestable"],
        key="financial_situation"
    )
    # Explicació contextual automàtica segons la selecció
    if fs == "Inestable":
        st.info(
            "**Inestable**: Tens ingressos o despeses variables que dificulten planificar pressupostos. "
            "Per exemple, si els teus ingressos depenen de comissions o projectes puntuals, pot ser complicat mantenir una estratègia d’inversió estable."
        )
    elif fs == "Moderada":
        st.info(
            "**Moderada**: La teva situació és relativament estable, però pot haver-hi algunes fluctuacions. "
            "Potser tens un salari fixe amb algun variable, així que pots planificar inversions però amb cert marge de seguretat."
        )
    elif fs == "Estable":
        st.info(
            "**Estable**: Tens ingressos regulars i baix risc de variacions brusques. "
            "Per exemple, un salari mensual o una pensió estable et permeten destinar capital a inversions de manera planificada."
        )


    # 3) Capital disponible a invertir
    capital_option = st.selectbox(
        label="Capital disponible per a inversió (aproximat):",
        options=[
            "Menys de 5.000 €",
            "De 5.000 € a 15.000 €",
            "Més de 15.000 €",
            "No ho sé encara"
        ],
        key="capital_option"
    )
    # 4) Horitzó d'inversió
    st.selectbox(
        label="Horitzó d’inversió:",
        options=[
            "Menys de 3 anys", 
            "De 3 a 5 anys", 
            "De 5 a 10 anys", 
            "Més de 10 anys"
        ],
        key="investment_horizon"
    )
