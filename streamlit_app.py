import streamlit as st
import pandas as pd
import altair as alt

# Set page configuration
st.set_page_config(page_title="Time Deposit Simulation", layout="wide")

# --- Title with gradient color ---
st.markdown("""
<h1 style="
    font-size: 3em;
    font-weight: 900;
    background: linear-gradient(to right, #27ae60, #2980b9);
    -webkit-background-clip: text;
    color: transparent;
    text-align: left;
    margin-top: -20px;
">
Deposito Simulation
</h1>
""", unsafe_allow_html=True)

# --- Subheader ---
st.markdown("<p style='color:white;'>This website will simulate how your money grows in a year if you invest in time deposits, compared to a savings account, which typically decreases your time value of money.</p>", unsafe_allow_html=True)

# --- Input money ---
principal = st.number_input("Input your money (Rp)", min_value=0, step=1_000_000, format="%d")

# --- Load deposit rate data ---
data = {
    'Bank': ['BCA', 'BCA', 'BCA', 'BCA', 'BNI', 'BNI', 'BNI', 'BNI', 'BRI', 'BRI', 'BRI', 'BRI', 'CIMB', 'CIMB', 'CIMB', 'CIMB', 
             'Danamon', 'Danamon', 'Danamon', 'Danamon', 'Danamon', 'Mandiri', 'Mandiri', 'Mandiri', 'Mandiri', 
             'Allo Bank', 'Allo Bank', 'Allo Bank', 'Allo Bank', 'Bank Jago', 'Bank Jago', 'Bank Jago', 'Bank Jago', 
             'Bank Neo', 'Bank Neo', 'Bank Neo', 'Bank Neo', 'Seabank', 'Seabank', 'Seabank', 'Seabank', 
             'Superbank', 'Superbank', 'Superbank', 'Superbank', 'Superbank'],
    'Tenor': [1, 3, 6, 12, 1, 3, 6, 12, 1, 3, 6, 12, 1, 3, 6, 12, 1, 3, 6, 9, 12, 1, 3, 6, 12, 1, 3, 6, 12, 1, 3, 6, 12, 1, 2, 6, 12, 1, 3, 6, 12, 1, 3, 6, 9, 12],
    'Interest': [3.00, 3.00, 2.25, 2.00, 2.25, 2.50, 2.75, 3.00, 3.35, 3.50, 3.00, 3.00, 2.75, 3.35, 3.35, 3.35, 3.25, 3.50, 4.00, 4.00, 4.25, 2.25, 2.25, 2.50, 2.50, 5.00, 6.50, 7.00, 7.50, 5.00, 5.50, 5.50, 5.50, 6.25, 6.75, 7.25, 8.00, 4.50, 5.25, 5.75, 6.00, 7.50, 7.50, 7.50, 7.50, 7.50]
}
df_deposit = pd.DataFrame(data)

# --- User select banks & tenors ---
col1, col2 = st.columns(2)
with col1:
    bank1 = st.selectbox("Choose Bank #1", sorted(df_deposit['Bank'].unique()), key='bank1')
    tenor1 = st.selectbox("Choose Tenor (months) #1", sorted(df_deposit[df_deposit['Bank'] == bank1]['Tenor'].unique()), key='tenor1')
with col2:
    bank2 = st.selectbox("Choose Bank #2", sorted(df_deposit['Bank'].unique()), key='bank2')
    tenor2 = st.selectbox("Choose Tenor (months) #2", sorted(df_deposit[df_deposit['Bank'] == bank2]['Tenor'].unique()), key='tenor2')

# --- Get deposit interest rates ---
def get_interest(bank, tenor):
    result = df_deposit[(df_deposit['Bank'] == bank) & (df_deposit['Tenor'] == tenor)]
    if not result.empty:
        return float(result['Interest'].values[0]) / 100
    return 0.0

# --- Bank color codes ---
bank_colors = {
    'BCA': '#00529B',
    'BNI': '#FF6A13',
    'BRI': '#0A3183',
    'CIMB': '#9D0A0E',
    'Danamon': '#FF9C00',
    'Mandiri': '#FDB913',
    'Allo Bank': '#FDB813',
    'Bank Jago': '#F7B731',
    'Bank Neo': '#FFCC00',
    'Seabank': '#0046FF',
    'Superbank': '#00B0B9'
}

# --- Simulation logic ---
def simulate_growth(principal, rate_annual, rollover_months):
    balance = principal
    balances = []
    for month in range(1, 13):
        if month % rollover_months == 1 or rollover_months == 1:
            interest = balance * rate_annual * rollover_months / 12
            net_interest = interest * (1 - 0.20)  # 20% tax
            balance += net_interest
        balances.append(round(balance))
    return balances

if principal > 0:
    months = [f"{i}-month" for i in range(1, 13)]
    month_num = list(range(1, 13))

    # --- Saving account basecase ---
    saving_rate_annual = 0.0025
    saving_balances = simulate_growth(principal, saving_rate_annual, 1)

    # --- Deposit 1 & 2 ---
    rate1 = get_interest(bank1, tenor1)
    rate2 = get_interest(bank2, tenor2)
    deposit1_balances = simulate_growth(principal, rate1, tenor1)
    deposit2_balances = simulate_growth(principal, rate2, tenor2)

    # --- Build chart data ---
    df_chart = pd.DataFrame({
        'Month': months * 3,
        'MonthNum': month_num * 3,
        'Balance': saving_balances + deposit1_balances + deposit2_balances,
        'Product': ['Saving Account'] * 12 + [f"{bank1} {tenor1}mo"] * 12 + [f"{bank2} {tenor2}mo"] * 12
    })

    color_scale = alt.Scale(domain=[
        'Saving Account', f"{bank1} {tenor1}mo", f"{bank2} {tenor2}mo"
    ], range=[
        '#AAAAAA',
        bank_colors.get(bank1, '#1f77b4'),
        bank_colors.get(bank2, '#ff7f0e')
    ])

    chart = alt.Chart(df_chart).mark_line(point=True).encode(
        x=alt.X('MonthNum:O', title='Month', axis=alt.Axis(labels=False), sort=month_num),
        y=alt.Y('Balance:Q', title='Balance (Rp)', scale=alt.Scale(domain=[
            min(saving_balances) * 0.998, max([*saving_balances, *deposit1_balances, *deposit2_balances]) * 1.002
        ])),
        color=alt.Color('Product:N', scale=color_scale),
        tooltip=['Month', 'Product', 'Balance']
    ).properties(
        width=800,
        height=450,
        title="Comparison: Savings vs Deposits (After Tax)"
    ).configure_axisX(
        labelExpr='datum.value + "-month"'
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.info("💡 Please input your money above to simulate.")