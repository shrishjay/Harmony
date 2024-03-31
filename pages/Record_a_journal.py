import streamlit as st
from send_email import send_email
import time


st.set_page_config(layout="wide")

col9, col10 = st.columns(2)

with col9:
    st.image("images/journal.png")

with col10:
    with st.form(key="email_form"):

        st.markdown("<h1 style='text-align: center;'>Make a journal of how you are feeling</h1>",
                    unsafe_allow_html=True)
        receiver = st.text_input("Enter your email Id: ")
        raw_message = st.text_area("Briefly describe how you feel")

        message =f"""\
Subject:{time.strftime("DATE - %d %b, %Y; TIME - %H:%M")}

From: Harmony app
Recorded Journal: {raw_message}
        """

        submit_button = st.form_submit_button("Submit and send to your email")

        if submit_button:
            send_email(message, receiver)
            st.info("""
            Thank you for recording a journal with Harmony!
            """)