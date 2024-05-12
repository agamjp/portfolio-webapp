import streamlit as st
import pandas as pd
import math

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

df = pd.read_csv("data.csv", sep=';')

col3, empty_space, col4 = st.columns([1.5, 0.5, 1.5])

df_display = df[df["url"] != "https://pythonhow.com"]
print(type(df), type(df_display))

half = int(math.ceil(len(df_display)/2))


with col3:
    for index, row in df_display[:half].iterrows():
            st.header(row["title"])
            st.write(f"[Source code]({row['url']})")
            st.image(row["image"])
            st.write(row["description"])

with col4:
    for index, row in df_display[half:].iterrows():
        if row["url"] != "https://pythonhow.com":
            st.header(row["title"])
            st.write(f"[Source code]({row['url']})")
            st.image(row["image"])
            st.write(row["description"])
