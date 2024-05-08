import streamlit as st
from send_email import send_email
import re

st.header("Contact me")

with st.form("contact"):
    user_email = st.text_input(label="Enter your email address:", key="user_email", )
    label = st.markdown("")
    raw_message = st.text_area(label="Enter your message:", key="message")
    button = st.form_submit_button("Submit")
    if button:
        message = f"""\
Subject: Portfolio: New message from {user_email}

User {user_email} sent the following message:

{raw_message}
"""
        message = message.encode()
        pattern = re.compile(r"[A-Za-z0-9-.%+_]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
        match = re.fullmatch(pattern, user_email)
        print(match)
        if match is not None:
            send_email(message)
            label = st.markdown(":green[Message sent!]")
        else:
            label = st.markdown(":red[Invalid email address!]")
