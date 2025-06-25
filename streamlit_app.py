import streamlit as st
import pandas as pd

st.markdown("""
<h1 style="
    font-size: 3em;
    font-weight: 900;
    background: linear-gradient(to right, #8e44ad, #2980b9, #e84393);
    -webkit-background-clip: text;
    color: transparent;
    text-align: left;
    margin-top: -20px;
">
HC Quick Reference
</h1>
""", unsafe_allow_html=True)

st.markdown("Compare time deposit returns from two banks and find which gives you a better deal—all in one place.")