import streamlit as st
import pandas as pd
import altair as alt

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

    /* Input label in white */
    label {
        color: white !important;
        font-weight: bold;
        font-size: 18px;
    }

    /* Input box text white and border white */
    div[data-baseweb="input"] > input {
        background-color: #000000 !important;
        color: white !important;
        border: 1px solid white !important;
    }

    /* Input box focused state border white */
    div[data-baseweb="input"] > input:focus {
        border-color: white !important;
        outline: none !important;
        box-shadow: 0 0 0 1px white !important;
    }

    /* Set app background to black */
    .stApp {
        background-color: #000000;
        padding: 30px;
    }

    /* Saving interest text white */
    .saving-interest {
        color: white;
        font-size: 16px;
        margin-top: -10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Header and subheader
st.markdown('<h1 class="gradient-text">Deposito Simulation</h1>', unsafe_allow_html=True)

subheader_text = """
This website will simulate how your money grows in a year if you invest in time deposits, compared to a savings account, which typically decreases your time value of money.
"""
st.markdown(f'<p class="subheader-text">{subheader_text}</p>', unsafe_allow_html=True)
# Input
principal = st.number_input("Input your money (Rp)", min_value=0, step=1_000_000, format="%d")

# Run simulation only if amount > 0
if principal > 0:
    saving_rate_annual = 0.0025
    saving_rate_monthly = saving_rate_annual / 12

    months = [f"{i}-month" for i in range(1, 13)]
    balances = []

    amount = principal
    for _ in months:
        interest = amount * saving_rate_monthly
        amount += interest
        balances.append(round(amount))

    df = pd.DataFrame({
        'Month': months,
        'Savings Balance (Rp)': balances
    })

    # Display saving rate
    st.markdown(f"**Default Saving Account Interest Rate:** {saving_rate_annual * 100:.2f}% p.a.")

    # Calculate zoomed-in Y-axis range
    min_y = min(balances)
    max_y = max(balances)
    y_range = [min_y * 0.998, max_y * 1.002]  # 0.2% padding

    # Altair chart with zoomed Y-axis
    chart = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X('Month', title='Month'),
        y=alt.Y('Savings Balance (Rp)', title='Balance (Rp)', scale=alt.Scale(domain=y_range)),
        tooltip=['Month', 'Savings Balance (Rp)']
    ).properties(
        width=700,
        height=400,
        title="Savings Account Growth (0.25% p.a.)"
    )

    st.altair_chart(chart)

else:
    st.info("💡 Please input your money above to simulate.")