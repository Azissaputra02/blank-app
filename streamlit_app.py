import streamlit as st

# Inisialisasi session_state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Fungsi untuk berpindah halaman
def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# Sidebar navigasi
with st.sidebar:
    st.markdown("## Navigasi SOP")
    page = st.radio(
        "Pilih Halaman:",
        ("Home", "SOP HCSP", "SOP Benefit", "SOP Payroll"),
        index=("Home", "SOP HCSP", "SOP Benefit", "SOP Payroll").index(st.session_state.page)
    )
    st.session_state.page = page

# Tampilan halaman
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

    # Styling tombol
    st.markdown("""
        <style>
        .sop-button button {
            padding: 0.5em 1.5em;
            font-weight: bold;
            border-radius: 8px;
            border: 1px solid #888;
            background-color: #0E1117;
            color: #EEE;
            transition: 0.3s;
            width: 100%;
        }
        .sop-button button:hover {
            background-color: #333;
            border-color: #8e44ad;
            color: #fff;
        }
        </style>
    """, unsafe_allow_html=True)

    # Tampilan 3 tombol sejajar
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("SOP HCSP", key="hcsp_btn"):
            go_to("SOP HCSP")
    with col2:
        if st.button("SOP Benefit", key="benefit_btn"):
            go_to("SOP Benefit")
    with col3:
        if st.button("SOP Payroll", key="payroll_btn"):
            go_to("SOP Payroll")

# Halaman SOP HCSP
elif st.session_state.page == "SOP HCSP":
    st.header("📘 SOP HCSP")
    st.markdown("Berikut adalah panduan ringkas dari seluruh proses dalam SOP Human Capital Service Partner, termasuk preboarding, onboarding, ID card, absensi, perubahan status, dan lain-lain.")

# Halaman SOP Benefit
elif st.session_state.page == "SOP Benefit":
    st.header("🎁 SOP Benefit")
    st.markdown("Berikut adalah SOP terkait benefit untuk karyawan seperti tunjangan, reimburse, dan proses pengajuan klaim lainnya.")

# Halaman SOP Payroll
elif st.session_state.page == "SOP Payroll":
    st.header("💸 SOP Payroll")
    st.markdown("Halaman ini menjelaskan alur proses payroll bulanan, komponen gaji, tanggal penting, dan prosedur terkait penggajian.")