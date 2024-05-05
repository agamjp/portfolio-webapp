import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/apw_2024.jpg")

with col2:
    st.title("Agnieszka Przybyła-Wilkin")
    with open("about.txt", 'r', encoding="utf8") as file:
        content = file.read()
    st.info(content)

description = """
Below you can find some of my Python projects. 
There are some apps I created for training and scripts I used for my academic work.
Feel free to contact me!
"""
st.write(description)
