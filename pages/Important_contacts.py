import streamlit as st


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/telephone.png")
with col2:
    st.title("Some important telephone numbers")
    st.info(f"""
    National Suicide helpline (India) - +91 9152987821 
    
    National suicide prevention lifeline (US) - 988
    
    Suicide Crisis helpline (Canada) - 988
    
    Prevention of young suicide HOPELINE247(UK) - 0800 068 41 41
    """)

st.header("Apart from these contacts, more resources related to suicide prevention can be found [here](https://www.cdc.gov/suicide/resources/prevention.html)")