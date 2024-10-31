import streamlit as st
import pandas
from send_email import send_email

df = pandas.read_csv("topics.csv")

with st.form(key = 'my_form'):
    user_email=st.text_input("Your email address")
    topic = st.selectbox(label="What topic do you wanna discuss?", options=df['topic'])
    raw_message=st.text_area("Text")
    message = f"""\
Subject: New Email from: {user_email}

From: {user_email}
Topic: {topic}
{raw_message}
"""  
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Correo enviado")
