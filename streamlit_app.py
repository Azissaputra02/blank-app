import streamlit as st
import pandas as pd

# UI: Title and explanation
st.title("Deposito Simulation")
st.subheader("This website will simulate how your money grows in a year if you invest in time deposits, compared to a savings account, which typically decreases your time value of money.")

# Input: initial money
principal = st.number_input("Input your money (Rp)", min_value=100000, step=100000, format="%d")

# Default savings interest
saving_rate_annual = 0.0025  # 0.25%
saving_rate_monthly = saving_rate_annual / 12

# Simulate from June to December
months = ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
balances = []

amount = principal
for i in range(len(months)):
    interest = amount * saving_rate_monthly
    amount += interest
    balances.append(round(amount))

# Build dataframe for chart
df = pd.DataFrame({
    'Month': months,
    'Savings Balance (Rp)': balances
})

# Display savings rate info
st.markdown(f"**Default Saving Account Interest Rate:** {saving_rate_annual * 100:.2f}% p.a.")

# Plot chart
st.line_chart(df.set_index('Month'))