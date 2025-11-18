import streamlit as st

st.title('Ini akan live di streamlit.app')
st.text('Ini adalah aplikasi yang digunakan untuk demo deployment ke streamlit.app')

col1, col2 = st.columns(2)
with col1:
    st.image('tiukdw.jpg')
with col2:
    st.image('logo-ukdw.png')