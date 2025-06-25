import streamlit as st

# Inisialisasi page state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Fungsi untuk berpindah halaman
def go_to(page_name):
    st.session_state.page = page_name

# Sidebar radio dengan key berbeda
selected_page = st.sidebar.radio(
    "Pilih Halaman:",
    ("Home", "SOP HCSP", "SOP Benefit", "SOP Payroll"),
    index=("Home", "SOP HCSP", "SOP Benefit", "SOP Payroll").index(st.session_state.page),
    key="selected_page"
)

# Sinkronisasi pilihan sidebar dengan state utama
if selected_page != st.session_state.page:
    st.session_state.page = selected_page
    st.rerun()

# Halaman Home
if st.session_state.page == "Home":
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

    st.markdown("Panduan ringkas untuk memahami seluruh proses Human Capital Shared Service (HCSS) di Danamon. Dalam satu laman, Anda bisa mengakses 3 topik utama: **SOP HCSP**, **SOP Benefit**, dan **SOP Payroll** — semua dijelaskan secara singkat, jelas, dan praktis untuk memudahkan Anda dalam setiap kebutuhan kepegawaian.")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("SOP HCSP"):
            go_to("SOP HCSP")
            st.rerun()
    with col2:
        if st.button("SOP Benefit"):
            go_to("SOP Benefit")
            st.rerun()
    with col3:
        if st.button("SOP Payroll"):
            go_to("SOP Payroll")
            st.rerun()

# Halaman SOP HCSP
elif st.session_state.page == "SOP HCSP":
    st.header("📘 SOP HCSP")
    st.write("Berisi seluruh alur dan ketentuan dalam layanan Human Capital Service Partner (HCSP), seperti preboarding, onboarding, perubahan status, dan lainnya.")

# Halaman SOP Benefit
elif st.session_state.page == "SOP Benefit":
    st.header("🎁 SOP Benefit")
    st.write("Berisi panduan klaim dan pengelolaan benefit seperti asuransi kesehatan, tunjangan, dan fasilitas lainnya.")

# Halaman SOP Payroll
elif st.session_state.page == "SOP Payroll":
    st.header("💰 SOP Payroll")
    st.write("Berisi seluruh proses terkait penggajian karyawan, pemotongan pajak, komponen pendapatan, dan waktu pembayaran.")