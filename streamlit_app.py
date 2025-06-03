import streamlit as st
import pandas as pd

# Title and description
st.title("Deposito Simulation")
st.subheader("This website will simulate how your money grows in a year if you invest in time deposits, compared to a savings account, which typically decreases your time value of money.")

# User input
principal = st.number_input("Input your money (Rp)", min_value=0, step=100000, format="%d")

# Run simulation only if user entered a positive amount
if principal > 0:
    # Default savings account rate
    saving_rate_annual = 0.0025  # 0.25% p.a.
    saving_rate_monthly = saving_rate_annual / 12

    # Simulate monthly growth (Jun to Dec)
    months = ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    balances = []

    amount = principal
    for _ in months:
        interest = amount * saving_rate_monthly
        amount += interest
        balances.append(round(amount))

    # Create DataFrame
    df = pd.DataFrame({
        'Month': months,
        'Savings Balance (Rp)': balances
    })

    # Show interest rate info
    st.markdown(f"**Default Saving Account Interest Rate:** {saving_rate_annual * 100:.2f}% p.a.")

    # Show chart
    st.line_chart(df.set_index('Month'))

else:
    st.info("💡 Please input your money above to simulate.")