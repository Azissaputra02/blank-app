import streamlit as st
import pandas as pd
import altair as alt

# --- Page Configuration ---
st.set_page_config(page_title="Time Deposit Simulation", layout="wide")

# --- Header ---
st.markdown("""
<h1 style="
    font-size: 3em;
    font-weight: 900;
    background: linear-gradient(to right, #00b894, #0984e3, #ffffff);
    -webkit-background-clip: text;
    color: transparent;
    text-align: left;
    margin-top: -20px;
">
Time Deposit Simulation
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style="color:white; font-size:1.1em;">
Simulate how your money grows in a year through time deposit options. Select two banks and tenors, and compare the performance of their products after 12 months.
</p>
""", unsafe_allow_html=True)

# --- Load Interest Rate Database ---
data = {
    'Bank': [...],  # Use your full bank/tenor/interest table here
    'Tenor': [...],
    'Interest': [...]
}
df_rate = pd.DataFrame(data)

# --- Money Input ---
principal_str = st.text_input("💵 Input your money (Rp)", value="1,000,000")
principal = int(principal_str.replace(",", "").strip())

# --- Bank & Tenor Selection ---
bank1 = st.selectbox("🏦 Choose Bank 1", sorted(df_rate['Bank'].unique()), key="bank1")
tenor1 = st.selectbox("📅 Tenor for Bank 1 (months)", sorted(df_rate[df_rate['Bank'] == bank1]['Tenor'].unique()), key="tenor1")

bank2 = st.selectbox("🏦 Choose Bank 2", sorted(df_rate['Bank'].unique()), key="bank2")
tenor2 = st.selectbox("📅 Tenor for Bank 2 (months)", sorted(df_rate[df_rate['Bank'] == bank2]['Tenor'].unique()), key="tenor2")

# --- Deposit Simulation Function ---
def simulate(principal, rate, tenor_months, tax=0.20):
    amount = principal
    monthly_balances = []
    for month in range(1, 13):
        if month % tenor_months == 0:
            gross = amount * (rate / 100) * (tenor_months / 12)
            net = gross * (1 - tax)
            amount += net
        monthly_balances.append(round(amount))
    return monthly_balances

# --- Get Interest Rates ---
r1 = df_rate[(df_rate['Bank'] == bank1) & (df_rate['Tenor'] == tenor1)]['Interest'].values[0]
r2 = df_rate[(df_rate['Bank'] == bank2) & (df_rate['Tenor'] == tenor2)]['Interest'].values[0]

# --- Run Simulations ---
balances1 = simulate(principal, r1, tenor1)
balances2 = simulate(principal, r2, tenor2)
months = [f"{i}-month" for i in range(1, 13)]
month_nums = list(range(1, 13))

# --- Create Chart Data ---
df_chart = pd.DataFrame({
    "Month": months * 2,
    "MonthNum": month_nums * 2,
    "Balance": balances1 + balances2,
    "Product": [f"{bank1} {tenor1}mo"] * 12 + [f"{bank2} {tenor2}mo"] * 12
})

# --- Color Assignment ---
color_range = ["#6c5ce7", "#00cec9"] if bank1 != bank2 else ["#6c5ce7", "#81ecec"]
color_scale = alt.Scale(
    domain=[f"{bank1} {tenor1}mo", f"{bank2} {tenor2}mo"],
    range=color_range
)

# --- Draw Line Chart ---
chart = alt.Chart(df_chart).mark_line(point=True).encode(
    x=alt.X('MonthNum:O', title='Month'),
    y=alt.Y('Balance:Q', title='Balance (Rp)', scale=alt.Scale(zero=False)),
    color=alt.Color('Product:N', scale=color_scale),
    tooltip=['Product', 'Month', 'Balance']
).properties(
    width=800,
    height=400,
    title="📈 Time Deposit Growth Over 12 Months"
)

st.altair_chart(chart, use_container_width=True)

# --- Summary Table ---
summary_df = pd.DataFrame({
    "Product": [f"{bank1} {tenor1}mo", f"{bank2} {tenor2}mo"],
    "Total Return (Rp)": [balances1[-1] - principal, balances2[-1] - principal],
    "Total Balance (Rp)": [balances1[-1], balances2[-1]]
})

summary_df["Total Return (Rp)"] = summary_df["Total Return (Rp)"].map("{:,.0f}".format)
summary_df["Total Balance (Rp)"] = summary_df["Total Balance (Rp)"].map("{:,.0f}".format)

st.markdown("### 📊 Summary Table")
st.dataframe(summary_df, use_container_width=True)