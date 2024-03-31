import streamlit as st
from contact import contact


st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")

    message = f"""\
Subject: {user_email} has contacted you from Harmony

From: {user_email}
{raw_message}
    """

    submit_button = st.form_submit_button("Submit")

    if submit_button:
        contact(message)
        st.info("""
        Thank you for contacting me!
        Your request has been submitted successfully.
        """)