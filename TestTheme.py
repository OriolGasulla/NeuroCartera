import streamlit as st

# Ha de ser la primera crida a Streamlit!
st.set_page_config(page_title="Test Theme")

st.write("Primary color from theme:", st.get_option("theme.primaryColor"))

# Un slider de prova
val = st.slider("Slider test", 0, 100, 50)
st.write("Valor:", val)
