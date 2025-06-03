import streamlit as st

st.markdown("""
    <style>
    /* Gradient text for header */
    .gradient-text {
        font-size: 48px;
        font-weight: bold;
        background: linear-gradient(90deg, green, blue);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* White colored subheader text */
    .subheader-text {
        color: white;
        font-size: 20px;
        margin-bottom: 30px;
    }

    /* Set background color to black */
    .stApp {
        background-color: #000000;
        padding: 30px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="gradient-text">Deposito Simulation</h1>', unsafe_allow_html=True)

subheader_text = """
This website will simulate how your money grows in a year if you invest in time deposits, compared to a savings account, which typically decreases your time value of money.
"""
st.markdown(f'<p class="subheader-text">{subheader_text}</p>', unsafe_allow_html=True)