import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="RUPTL Comparison Dashboard", layout="wide")
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
RUPTL Comparison Dashboard
</h1>
""", unsafe_allow_html=True)
st.markdown("""
Welcome to the **Time Deposit Simulation**. This website will simulate how your money grows in a year if you invest in time deposits, compared to a savings account, which typically decreases your time value of money
""", unsafe_allow_html=True)
    
# --- Input: Amount of Money ---
principal = st.number_input("Input your money (Rp)", min_value=0, step=1_000_000, format="%d")

if principal > 0:
    # --- Default savings interest rate ---
    saving_rate_annual = 0.0025  # 0.25% per year
    saving_rate_monthly = saving_rate_annual / 12

    # --- Simulate 12 months ---
    months = [f"{i}-month" for i in range(1, 13)]
    balances = []
    amount = principal

    for _ in months:
        interest = amount * saving_rate_monthly
        amount += interest
        balances.append(round(amount))

    # --- DataFrame ---
    df = pd.DataFrame({
        'Month': months,
        'Savings Balance (Rp)': balances,
        'MonthNum': list(range(1, 13))
    })

    # --- Display rate ---
    st.markdown(f"**Default Saving Account Interest Rate:** {saving_rate_annual * 100:.2f}% p.a.")

    # --- Y-axis zoom (small change visualization) ---
    min_y = min(balances)
    max_y = max(balances)
    y_range = [min_y * 0.998, max_y * 1.002]

    # --- Altair chart with zoomed-in Y-axis and ordered X-axis ---
    chart = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X('MonthNum:O', title='Month', axis=alt.Axis(labels=False), sort=list(range(1, 13))),
        tooltip=['Month', 'Savings Balance (Rp)'],
        y=alt.Y('Savings Balance (Rp)', title='Balance (Rp)', scale=alt.Scale(domain=y_range))
    ).properties(
        width=700,
        height=400,
        title="Savings Account Growth (0.25% p.a.)"
    ).configure_axisX(
        labelExpr='datum.value + "-month"'
    )

    st.altair_chart(chart)

else:
    st.info("Please input your money above to simulate.")