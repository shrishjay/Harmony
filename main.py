import streamlit as st


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("title_image.png")

with col2:
    st.title("Harmony")
    st.info("""
    Introducing MindEase, the ultimate mobile app dedicated to promoting mental well-being and fostering mindfulness.
    With personalized tools ranging from mood tracking and guided meditations to stress reduction exercises, MindEase empowers individuals to proactively manage stress, anxiety, and depression. 
    Connect with a supportive community, access teletherapy services, and utilize evidence-based cognitive behavioral therapy tools to challenge negative thought patterns and build resilience. 
    Receive daily reminders and challenges, track your progress, and cultivate positive habits for a healthier, happier life. 
    Join MindEase today and embark on a journey towards greater peace, resilience, and well-being.
    """)

st.title(" ")
st.title(" ")
st.title(" ")
st.title(" ")
st.markdown("<h1 style='text-align: center;'>How are you feeling today?</h1>",
            unsafe_allow_html=True)
st.title(" ")

col3, col4, col5, col6, col7 = st.columns(5)

with col3:
    st.image("emote_images/crying.png")
    st.markdown("<h4><div style='text-align: center;'>Crying</div></h4>",
                unsafe_allow_html=True)

with col4:
    st.image("emote_images/unhappy.png")
    st.markdown("<h4><div style='text-align: center;'>Unhappy</div></h4>",
                unsafe_allow_html=True)

with col5:
    st.image("emote_images/neutral.png")
    st.markdown("<h4><div style='text-align: center;'>Neutral</div></h4>",
                unsafe_allow_html=True)

with col6:
    st.image("emote_images/happy.png")
    st.markdown("<h4><div style='text-align: center;'>Happy</div></h4>",
                unsafe_allow_html=True)

with col7:
    st.image("emote_images/laughing.png")
    st.markdown("<h4><div style='text-align: center;'>Laughing</div></h4>",
                unsafe_allow_html=True)

selected_emoji = st.selectbox("Pick the emoji best describing you",
                              ["Crying", "Unhappy", "Neutral", "Happy", "Laughing"],
                              key="selected_emoji")

