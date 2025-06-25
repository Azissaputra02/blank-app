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
        ("Home", "HCSP", "Benefit", "Payroll"),
        index=("Home", "HCSP", "Benefit", "Payroll").index(st.session_state.page)
    )
    st.session_state.page = page

# Tampilan halaman Home
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
        if st.button("HCSP", key="hcsp_btn"):
            go_to("HCSP")
    with col2:
        if st.button("Benefit", key="benefit_btn"):
            go_to("Benefit")
    with col3:
        if st.button("Payroll", key="payroll_btn"):
            go_to("Payroll")

elif st.session_state.page == "HCSP":
    st.header("📘 HCSP Quick Reference")
    st.markdown("Panduan ringkas Human Capital Service Partner. Pilih topik di bawah ini untuk melihat detailnya:")

    # Dropdown untuk memilih sub-bab
    hcsp_options = [
        "1. Preboarding",
        "2. Onboarding",
        "3. Identity (ID Card)",
        "4. Absensi Kehadiran Work From Home",
        "5. Manajemen Waktu",
        "6. Perubahan status kepegawaian (1)",
        "7. Perubahan status kepegawaian (2)",
        "8. Surat Keterangan Kerja",
        "9. Program Retensi Pegawai",
        "10. Employee Service Center",
        "11. Pengakhiran Hubungan Kerja"
    ]
    selected_hcsp = st.selectbox("Pilih topik HCSP:", hcsp_options)

    # Tampilkan konten berdasarkan pilihan
    if selected_hcsp == "1. Preboarding":
        st.markdown("#### 1. Proses Preboarding")
        st.markdown("""
        | **Stakeholder**            | **Tugas**                                                                                  |
        |---------------------------|---------------------------------------------------------------------------------------------|
        | HCSP Support / HC Region  | - Buat **notifikasi penerimaan** via sistem HC kepada PUK  <br> - Kirim info preboarding ke calon pekerja via email |
        | PUK (Pimpinan Unit Kerja) | - Persiapkan **workstation, alat kerja, dan akses sistem** <br> - Koordinasi dengan unit terkait jika perlu penyesuaian |
        | Pekerja Baru              | - Terima email berisi **akses awal** (*user ID, link sistem HC, dll*) <br> - Mulai unggah dokumen prasyarat di sistem HC |
        | HCSP                      | - Kirim **reminder** jika pekerja belum melengkapi dokumen dalam waktu 3 hari kerja        |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen Wajib dari Pekerja Baru:**")
        st.markdown("""
        - KTP, KK, NPWP, Rekening Payroll, BPJS Kesehatan *(jika ada)*
        - Ijazah, Sertifikat Pendukung *(jika diminta)*
        """)

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("""
        - Gaji **bulan pertama tidak bisa diproses** jika dokumen belum lengkap maksimal **5 hari kerja** sebelum tanggal gajian.
        - Reminder otomatis dikirim oleh sistem HC **setiap 2 hari** jika belum lengkap.
        """)

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Pekerja harus melengkapi dokumen maksimal **5 hari kerja** sebelum tanggal mulai kerja.")

        # Sub-bab 2
        st.markdown("---")
        st.markdown("#### 2. Pelaksanaan Aktivitas untuk Pekerjaan Baru")
        st.markdown("""
        | **Stakeholder**           | **Tugas**                                                                                                        |
        |---------------------------|------------------------------------------------------------------------------------------------------------------|
        | PUK (Pimpinan Unit Kerja) | - Kirim email selamat datang ke pekerja baru *(opsional dengan CC ke tim terkait)* <br> - Koordinasikan penyediaan meja, kursi, laptop, dan akses lokal |
        | HCSP Support              | - Siapkan dan distribusikan: Seragam batik Danamon, ID Card & Akses Kantor, serta Starter Kit *(jika ada)*       |
        | Pekerja Baru              | - Ambil perlengkapan kerja di lokasi yang ditentukan <br> - Konfirmasi penerimaan item via sistem HC *(jika diminta)* |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen atau Item yang Diterima Pekerja Baru:**")
        st.markdown("""
        - ID Card
        - Seragam Batik (2 pcs)
        - Starter Kit (tergantung fungsi dan lokasi)
        - Akses Sistem (email, VPN, dil.)
        """)

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("""
        - Semua item idealnya sudah siap paling lambat hari pertama kerja.
        - Jika pekerja WFH/hybrid, ID card bisa dikirimkan ke alamat rumah setelah konfirmasi alamat.
        """)

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Distribusi perlengkapan: Maksimal H+1 dari tanggal mulai kerja")

        # Sub-bab 3
        st.markdown("---")
        st.markdown("#### 3. Langkah-Langkah Sebagai Pekerja Baru")
        st.markdown("""
        | **Stakeholder**           | **Tugas**                                                                                                        |
        |---------------------------|------------------------------------------------------------------------------------------------------------------|
        | Pekerja Baru              | - Akses sistem HC melalui link yang dikirim via email <br> - Unggah dokumen pribadi sesuai daftar <br> - Isi data onboarding (nomor rekening, ukuran seragam, dil.) <br> - Ajukan permintaan benefit opsional seperti kartu kredit (jika tersedia)       |
        | HCSP                      | - Verifikasi kelengkapan data dan dokumen <br> - Kirim reminder jika data belum lengkap dalam 3 hari kerja |
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("📌 **Daftar Dokumen & Data yang Harus Diisi oleh Pekerja Baru:**")
        st.markdown("""
        - Nomor Rekening Payroll
        - NPWP
        - Alamat Domisili
        - Nomor KTP, KK
        - Ukuran Baju (untuk batik)
        - Nomor BPJS (jika sudah punya sebelumnya)
        """)

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("""
        - Pastikan semua dokumen dan data dilengkapi maksimal 5 hari kerja sebelum tanggal gajian agar gaji pertama bisa diproses.
        - Permintaan kart kredit (opsional) bisa diajukan lewat sistem HC (fitur akan muncul setelah data lengkap).
        """)

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Pengisian dan unggah data oleh pekerja baru: Maksimal 3 hari sejak terima email preboarding")

        # Sub-bab 4
        st.markdown("---")
        st.markdown("#### 4. Proses Kelengkapan Dokumen")
        st.markdown("""
        | **Stakeholder**           | **Tugas**                                                                                                        |
        |---------------------------|------------------------------------------------------------------------------------------------------------------|
        | Pekerja Baru              | - Unggah seluruh dokumen wajib ke sistem HC <br> - Periksa kembali kelengkapan dokumen sebelum H-5 gajian |
        | Talent Acquisition (TA)   | - Verifikasi awal kelengkapan dokumen saat proses rekrutmen <br> - Input awal data kandidat ke sistem HC      |
        | HCSP Support              | - Final check dokumen onboarding <br> - Kirim reminder jika ada kekurangan <br> - Tandai status "SIAP GAJ!" jika dokumen sudah lengkap |
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("📌 **Dokumen Wajib (untuk status "SIAP GAJI"):**")
        st.markdown("""
        - KTP & KK
        - NPWP (wajib untuk perhitungan pajak)
        - Buku Tabungan / Bukti Rekening Payroll
        - BPJS Kesehatan (jika ada)
        - Ijazah Terakhir
        - Pas Foto
        """)

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("""
        - Dokumen harus diunggah maksimal H-5 sebelum payroll cut-off.
        - Jika belum lengkap, maka status gaji akan tertunda ke bulan berikutnya.
        - Sistem akan otomatis mengirim pengingat ke pekerja setiap 2 hari.
        """)

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Verifikasi kelengkapan oleh HCSP: maksimal 2 hari kerja setelah dokumen lengkap")

    elif selected_hcsp == "2. Onboarding":
        st.markdown("#### 2. Pelaksanaan Aktivitas untuk Pekerjaan Baru")
        st.markdown("""
        | **Stakeholder**           | **Tugas**                                                                                                        |
        |---------------------------|------------------------------------------------------------------------------------------------------------------|
        | PUK (Pimpinan Unit Kerja) | - Kirim email selamat datang ke pekerja baru *(opsional dengan CC ke tim terkait)* <br> - Koordinasikan penyediaan meja, kursi, laptop, dan akses lokal |
        | HCSP Support              | - Siapkan dan distribusikan: Seragam batik Danamon, ID Card & Akses Kantor, serta Starter Kit *(jika ada)*       |
        | Pekerja Baru              | - Ambil perlengkapan kerja di lokasi yang ditentukan <br> - Konfirmasi penerimaan item via sistem HC *(jika diminta)* |
        """, unsafe_allow_html=True)

    # Kamu bisa lanjutkan elif elif elif... untuk sub bab 3 - 11
# Halaman SOP HCSP
# elif st.session_state.page == "SOP HCSP":
#     st.header("📘 SOP HCSP")
#     st.markdown("Berikut adalah panduan ringkas dari seluruh proses dalam SOP Human Capital Service Partner, termasuk preboarding, onboarding, ID card, absensi, perubahan status, dan lain-lain.")

#     st.markdown("### 🔷 **HC QUICK REFERENCE — SOP HCSP**")

#     # Sub-bab 1
#     st.markdown("#### 1. Proses Preboarding")
#     st.markdown("""
#     | **Stakeholder**            | **Tugas**                                                                                  |
#     |---------------------------|---------------------------------------------------------------------------------------------|
#     | HCSP Support / HC Region  | - Buat **notifikasi penerimaan** via sistem HC kepada PUK  <br> - Kirim info preboarding ke calon pekerja via email |
#     | PUK (Pimpinan Unit Kerja) | - Persiapkan **workstation, alat kerja, dan akses sistem** <br> - Koordinasi dengan unit terkait jika perlu penyesuaian |
#     | Pekerja Baru              | - Terima email berisi **akses awal** (*user ID, link sistem HC, dll*) <br> - Mulai unggah dokumen prasyarat di sistem HC |
#     | HCSP                      | - Kirim **reminder** jika pekerja belum melengkapi dokumen dalam waktu 3 hari kerja        |
#     """, unsafe_allow_html=True)

#     st.markdown("---")
#     st.markdown("📌 **Dokumen Wajib dari Pekerja Baru:**")
#     st.markdown("""
#     - KTP, KK, NPWP, Rekening Payroll, BPJS Kesehatan *(jika ada)*
#     - Ijazah, Sertifikat Pendukung *(jika diminta)*
#     """)

#     st.markdown("---")
#     st.markdown("⚠️ **Catatan Penting:**")
#     st.markdown("""
#     - Gaji **bulan pertama tidak bisa diproses** jika dokumen belum lengkap maksimal **5 hari kerja** sebelum tanggal gajian.
#     - Reminder otomatis dikirim oleh sistem HC **setiap 2 hari** jika belum lengkap.
#     """)

#     st.markdown("---")
#     st.markdown("⏱ **SLA Waktu:**")
#     st.markdown("- Pekerja harus melengkapi dokumen maksimal **5 hari kerja** sebelum tanggal mulai kerja.")

#     # Sub-bab 2
#     st.markdown("---")
#     st.markdown("#### 2. Pelaksanaan Aktivitas untuk Pekerjaan Baru")
#     st.markdown("""
#     | **Stakeholder**           | **Tugas**                                                                                                        |
#     |---------------------------|------------------------------------------------------------------------------------------------------------------|
#     | PUK (Pimpinan Unit Kerja) | - Kirim email selamat datang ke pekerja baru *(opsional dengan CC ke tim terkait)* <br> - Koordinasikan penyediaan meja, kursi, laptop, dan akses lokal |
#     | HCSP Support              | - Siapkan dan distribusikan: Seragam batik Danamon, ID Card & Akses Kantor, serta Starter Kit *(jika ada)*       |
#     | Pekerja Baru              | - Ambil perlengkapan kerja di lokasi yang ditentukan <br> - Konfirmasi penerimaan item via sistem HC *(jika diminta)* |
#     """, unsafe_allow_html=True)

#     st.markdown("---")
#     st.markdown("📌 **Dokumen atau Item yang Diterima Pekerja Baru:**")
#     st.markdown("""
#     - ID Card
#     - Seragam Batik (2 pcs)
#     - Starter Kit (tergantung fungsi dan lokasi)
#     - Akses Sistem (email, VPN, dil.)
#     """)

#     st.markdown("---")
#     st.markdown("⚠️ **Catatan Penting:**")
#     st.markdown("""
#     - Semua item idealnya sudah siap paling lambat hari pertama kerja.
#     - Jika pekerja WFH/hybrid, ID card bisa dikirimkan ke alamat rumah setelah konfirmasi alamat.
#     """)

#     st.markdown("---")
#     st.markdown("⏱ **SLA Waktu:**")
#     st.markdown("- Distribusi perlengkapan: Maksimal H+1 dari tanggal mulai kerja")

#     # Sub-bab 3
#     st.markdown("---")
#     st.markdown("#### 3. Pembuatan ID Card")
#     st.markdown("""
#     | **Stakeholder**     | **Tugas**                                                                                   |
#     |----------------------|---------------------------------------------------------------------------------------------|
#     | HCSP Support         | - Ajukan permintaan ID Card ke vendor                                                      |
#     | Vendor              | - Produksi dan kirim ID Card dalam waktu maksimal **3 hari kerja**                          |
#     | PUK / Pekerja Baru  | - Mengambil ID Card di unit / HC / dikirim tergantung lokasi kerja                         |
#     """)

#     st.markdown("📎 *Jika pekerja pindah unit, ID Card dapat diminta ulang dengan approval dari atasan langsung.*")

#     # Sub-bab 4
#     st.markdown("#### 4. Absensi & Kehadiran WFH")
#     st.markdown("""
#     | **Stakeholder**     | **Tugas**                                                                                   |
#     |----------------------|---------------------------------------------------------------------------------------------|
#     | Pekerja              | - Wajib mengisi kehadiran harian melalui sistem HC sesuai jadwal                           |
#     | Atasan Langsung      | - Melakukan verifikasi & approval kehadiran                                                |
#     | HCSP Support         | - Memantau kepatuhan pengisian absensi dan memberikan notifikasi jika ada keterlambatan    |
#     """)

#     st.markdown("📌 *WFH harus sesuai jadwal resmi dan disetujui oleh atasan.*")

# Halaman SOP Benefit
elif st.session_state.page == "Benefit":
    st.header("🎁 SOP Benefit")
    st.markdown("Berikut adalah SOP terkait benefit untuk karyawan seperti tunjangan, reimburse, dan proses pengajuan klaim lainnya.")

# Halaman SOP Payroll
elif st.session_state.page == "Payroll":
    st.header("💸 SOP Payroll")
    st.markdown("Halaman ini menjelaskan alur proses payroll bulanan, komponen gaji, tanggal penting, dan prosedur terkait penggajian.")