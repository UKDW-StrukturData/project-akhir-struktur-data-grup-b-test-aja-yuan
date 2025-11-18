import streamlit as st

st.title('Ini akan live di streamlit.app')

col1, col2 = st.columns()
with col1:
    st.image('tiukdw.jpg', width=100)
with col2:
    st.image('logo-ukdw.png', width=100)