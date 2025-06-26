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
    # Tombol kembali ke Home
    if st.button("Back to Home"):
        go_to("Home")

    st.header("📘 HCSP Quick Reference")
    st.markdown("Panduan ringkas Human Capital Service Partner. Pilih topik di bawah ini untuk melihat detailnya.")

    # Dropdown untuk memilih sub-bab
    hcsp_options = [
        "1. Preboarding",
        "2. Onboarding",
        "3. Identity (ID Card)",
        "4. Absensi Kehadiran Work From Home",
        "5. Manajemen Waktu",
        "6. Perubahan status kepegawaian",
        "7. Surat Keterangan Kerja",
        "8. Program Retensi Pegawai",
        "9. Employee Service Center",
        "10. Pengakhiran Hubungan Kerja"
    ]
    selected_hcsp = st.selectbox("Pilih topik:", hcsp_options)

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
        st.markdown("📌 **Dokumen Wajib (untuk status SIAP GAJI):**")
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
        st.markdown("---")

    elif selected_hcsp == "2. Onboarding":
        st.markdown("#### 1. Proses Onboarding Hari Pertama")
        st.markdown("""
        | **Stakeholder**           | **Tugas**                                                                 |
        |---------------------------|---------------------------------------------------------------------------|
        | PUK                       | - Menyambut pekerja baru, perkenalan tim, serta penjelasan peran kerja   |
        | Pekerja Baru              | - Mengikuti perkenalan dan mulai beradaptasi dengan lingkungan kerja     |
        | HCSP                      | - Memastikan pekerja aktif dalam sistem dan sudah mengakses email kantor |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Tidak ada dokumen wajib.")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Hari pertama berfokus pada pengenalan unit kerja dan lingkungan.")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Dilaksanakan pada **H1 masuk kerja**.")

        st.markdown("---")
        st.markdown("#### 2. Proses Onboarding Minggu Pertama")
        st.markdown("""
        | **Stakeholder**           | **Tugas**                                                                                       |
        |---------------------------|-------------------------------------------------------------------------------------------------|
        | PUK                       | - Menjelaskan peran detail, struktur organisasi unit, dan ekspektasi kerja                      |
        | HCSP                      | - Memfasilitasi akses ke platform internal jika belum tersedia                                  |
        | Pekerja Baru              | - Menyelesaikan pembelajaran awal dan bertanya jika ada kendala                                 |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Panduan internal unit kerja *(jika ada)*")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- PUK dapat menunjuk **buddy** untuk membantu adaptasi.")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Diselesaikan maksimal **minggu pertama kerja**.")

        st.markdown("---")
        st.markdown("#### 3. Proses Onboarding Bulan Pertama")
        st.markdown("""
        | **Stakeholder**           | **Tugas**                                                                                       |
        |---------------------------|-------------------------------------------------------------------------------------------------|
        | PUK                       | - Memberikan arahan awal tugas dan project aktual                                               |
        | HC Learning & Development | - Memastikan pekerja mengikuti pelatihan onboarding lanjutan                                   |
        | Pekerja Baru              | - Menyelesaikan pelatihan dan mulai menjalankan pekerjaan fungsional                            |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("""
        - Jadwal pelatihan  
        - Form evaluasi pelatihan
        """)

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Pekerja mulai **dievaluasi secara informal** terkait kesiapan kerja.")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Seluruh pelatihan dasar diselesaikan dalam **30 hari kerja**.")

        st.markdown("---")
        st.markdown("#### 4. Proses Onboarding Bulan Kedua dan Ketiga")
        st.markdown("""
        | **Stakeholder**           | **Tugas**                                                                                       |
        |---------------------------|-------------------------------------------------------------------------------------------------|
        | PUK                       | - Memberikan tanggung jawab lebih kompleks dan melakukan **coaching mingguan**                 |
        | Pekerja Baru              | - Menunjukkan hasil kerja dan keterlibatan dalam tim                                            |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Form evaluasi berkala *(jika disediakan)*")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- **Keterlibatan aktif PUK** sangat memengaruhi keberhasilan onboarding.")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Coaching dilakukan secara mingguan selama **bulan ke-2 dan ke-3**.")

        st.markdown("---")
        st.markdown("#### 5. Proses Evaluasi Masa Percobaan")
        st.markdown("""
        | **Stakeholder**           | **Tugas**                                                                                       |
        |---------------------------|-------------------------------------------------------------------------------------------------|
        | PUK                       | - Menyusun hasil evaluasi selama masa percobaan dan diskusi dengan HC Region                   |
        | HCSP                      | - Menyiapkan dokumen administrasi hasil evaluasi (lulus/tidak)                                 |
        | Pekerja Baru              | - Menerima hasil evaluasi secara formal                                                        |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("""
        - Form evaluasi masa percobaan  
        - Surat hasil evaluasi
        """)

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Masa percobaan umumnya **3 bulan**, tapi bisa diperpanjang jika perlu.")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Evaluasi final dilakukan maksimal **H-7 dari akhir masa percobaan**.")

        st.markdown("---")
        st.markdown("#### 6. Proses Perubahan PKWT menjadi PKWTT")
        st.markdown("""
        | **Stakeholder**           | **Tugas**                                                                                       |
        |---------------------------|-------------------------------------------------------------------------------------------------|
        | PUK                       | - Mengajukan rekomendasi perubahan status                                                      |
        | HCSP                      | - Memproses perubahan dari kontrak ke tetap                                                    |
        | Pekerja Baru              | - Menandatangani surat perjanjian kerja tetap                                                  |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("""
        - Surat perubahan status  
        - Kontrak PKWTT
        """)

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Perubahan ini berlaku bagi **pekerja kontrak** yang **lulus masa percobaan**.")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Proses administrasi maksimal **7 hari kerja** setelah masa percobaan selesai.")
        st.markdown("---")

    elif selected_hcsp == "3. Identity (ID Card)":
        st.markdown("#### 1. Proses Penerbitan ID Card untuk Pekerja Baru")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                                                     |
        |-----------------|-----------------------------------------------------------------------------------------------|
        | HCSP            | - Input data pekerja baru ke sistem pembuatan ID Card                                        |
        | Vendor          | - Mencetak ID Card berdasarkan data dari HCSP                                                 |
        | HCSP            | - Menerima ID Card jadi dan kirim ke PUK atau rumah pekerja (jika remote)                    |
        | PUK             | - Menyerahkan ID Card ke pekerja baru                                                         |
        | Pekerja Baru    | - Menyimpan dan menggunakan ID Card saat bekerja di kantor                                    |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Data pekerja dari sistem HC")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("""
        - Untuk pekerja di luar kantor pusat, pengiriman dilakukan via ekspedisi  
        - ID Card **wajib dimiliki** oleh seluruh pekerja (tetap, kontrak, outsourcing)
        """)

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Maksimal **7 hari kerja** setelah data diterima lengkap oleh HCSP")

        st.markdown("---")
        st.markdown("#### 2. Proses Penggantian ID Card karena Hilang atau Rusak")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                                                     |
        |-----------------|-----------------------------------------------------------------------------------------------|
        | Pekerja         | - Melaporkan kehilangan/kerusakan ID Card ke HCSP via email atau portal internal             |
        | HCSP            | - Verifikasi laporan dan proses pencetakan ulang ke vendor                                   |
        | HCSP            | - Menerima ID Card baru dan mendistribusikannya ke pekerja                                   |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Laporan kehilangan atau ID lama yang rusak *(jika tersedia)*")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("""
        - Pekerja bertanggung jawab atas keamanan ID Card  
        - Kehilangan > 2x dalam 1 tahun dapat dikenakan **catatan peringatan**
        """)

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Maksimal **5 hari kerja** setelah laporan diterima")

        st.markdown("---")
        st.markdown("#### 3. Proses Perubahan ID Card karena Perubahan Unit/Jabatan")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                                                     |
        |-----------------|-----------------------------------------------------------------------------------------------|
        | PUK             | - Ajukan permintaan update ID Card ke HCSP saat ada perubahan jabatan/unit kerja             |
        | HCSP            | - Ajukan pencetakan ulang ID Card ke vendor dengan data baru                                 |
        | HCSP            | - Menerima ID Card baru dan menyerahkannya ke pekerja                                         |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Surat perubahan jabatan/unit dari sistem HC")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- ID Card lama **dikembalikan ke HCSP** sebelum ID baru diberikan")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Maksimal **5 hari kerja** sejak permintaan diterima")
        st.markdown("---")

    elif selected_hcsp == "4. Absensi Kehadiran Work From Home":
        st.markdown("#### 1. Proses Registrasi Akses Aplikasi Absensi")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                                 |
        |-----------------|---------------------------------------------------------------------------|
        | HCSP            | - Memastikan pekerja memiliki akses ke sistem absensi                    |
        | Pekerja         | - Melakukan login pertama & menyetujui kebijakan penggunaan aplikasi     |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Data pekerja dari sistem HC")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Akses diberikan saat preboarding atau onboarding")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Maksimal **H-1 sebelum tanggal mulai kerja**")

        st.markdown("---")
        st.markdown("#### 2. Proses Pencatatan Kehadiran Pagi")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                                 |
        |-----------------|---------------------------------------------------------------------------|
        | Pekerja         | - Melakukan absensi hadir via aplikasi maksimal pukul 09.00 WIB          |
        | Sistem          | - Mencatat jam kehadiran dan lokasi otomatis                             |
        | Atasan          | - Monitoring harian kehadiran tim                                        |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Tidak ada")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Keterlambatan tanpa keterangan dapat memengaruhi penilaian kinerja")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Maksimal **pukul 09.00 WIB** setiap hari kerja")

        st.markdown("---")
        st.markdown("#### 3. Proses Pencatatan Pulang")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                                 |
        |-----------------|---------------------------------------------------------------------------|
        | Pekerja         | - Melakukan absensi pulang saat selesai bekerja                          |
        | Sistem          | - Mencatat jam dan lokasi absensi pulang                                 |
        | Atasan          | - Verifikasi jika jam kerja tidak lengkap atau abnormal                  |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Tidak ada")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Jika lupa absen pulang, wajib lapor ke atasan untuk koreksi")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Absensi pulang dilakukan **sebelum pukul 18.00 WIB**")

        st.markdown("---")
        st.markdown("#### 4. Proses Pengajuan dan Perubahan Lokasi WFH")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                                 |
        |-----------------|---------------------------------------------------------------------------|
        | Pekerja         | - Ajukan WFH via sistem/email                                             |
        | Atasan          | - Menyetujui permintaan WFH                                               |
        | HCSP            | - Mencatat lokasi kerja baru untuk keperluan audit                       |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Form/email pengajuan WFH *(jika manual)*")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Lokasi WFH wajib bisa dipantau & memiliki koneksi kerja memadai")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Permintaan minimal **H-1 sebelum pelaksanaan**")

        st.markdown("---")
        st.markdown("#### 5. Proses Monitoring dan Evaluasi Kehadiran")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                                 |
        |-----------------|---------------------------------------------------------------------------|
        | HCSP            | - Rekap data absensi mingguan & bulanan                                   |
        | Atasan          | - Evaluasi pola kehadiran tim                                             |
        | Pekerja         | - Memberikan klarifikasi jika ada penyimpangan absensi                   |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Laporan absensi dari sistem")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Pola keterlambatan & ketidakhadiran masuk dalam catatan kinerja")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Evaluasi dilakukan **per bulan**")
        st.markdown("---")

    elif selected_hcsp == "5. Manajemen Waktu":
        st.markdown("#### 1. Proses Pengajuan Cuti Tahunan")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                              |
        |-----------------|------------------------------------------------------------------------|
        | Pekerja         | - Mengajukan cuti melalui sistem HC/aplikasi cuti                     |
        | Atasan          | - Menyetujui atau menolak pengajuan cuti                              |
        | HCSP            | - Memperbarui dan merekap saldo cuti secara otomatis                  |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Tidak ada, dilakukan melalui sistem")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Cuti diambil jika saldo tersedia & sesuai kebutuhan operasional")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Pengajuan minimal **H-3 sebelum tanggal cuti**")

        st.markdown("---")
        st.markdown("#### 2. Proses Cuti Khusus (Menikah, Melahirkan, Duka, dll.)")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                              |
        |-----------------|------------------------------------------------------------------------|
        | Pekerja         | - Ajukan cuti khusus + lampirkan dokumen pendukung                    |
        | Atasan          | - Memberi persetujuan                                                  |
        | HCSP            | - Verifikasi & catat cuti ke dalam sistem                             |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Surat undangan, akta kelahiran, surat kematian *(sesuai jenis cuti)*")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Mengacu pada kebijakan perusahaan & UU Ketenagakerjaan")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Maksimal **3 hari kerja** setelah dokumen lengkap")

        st.markdown("---")
        st.markdown("#### 3. Proses Izin Tidak Masuk Kerja")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                              |
        |-----------------|------------------------------------------------------------------------|
        | Pekerja         | - Menginformasikan ke atasan secara langsung atau via sistem          |
        | Atasan          | - Mencatat dan menyetujui alasan izin                                 |
        | HCSP            | - Mencatat izin ke sistem                                              |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Informal (WA / Email / Verbal)")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Izin tanpa laporan dapat dianggap **alfa**")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Disampaikan **minimal di hari yang sama sebelum jam masuk kerja**")

        st.markdown("---")
        st.markdown("#### 4. Proses Perhitungan Cuti Pro-Rata")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                              |
        |-----------------|------------------------------------------------------------------------|
        | HCSP            | - Hitung hak cuti berdasarkan masa kerja berjalan                     |
        | Pekerja         | - Dapat melihat cuti prorata di sistem                                |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Tidak ada")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Berlaku untuk pekerja baru, masuk, atau resign di tengah tahun")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Maksimal **1 minggu setelah tanggal kerja efektif**")

        st.markdown("---")
        st.markdown("#### 5. Proses Cuti di Luar Tanggungan (CDT)")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                              |
        |-----------------|------------------------------------------------------------------------|
        | Pekerja         | - Ajukan CDT melalui surat resmi ke PUK dan HC                        |
        | PUK & HC Region | - Evaluasi & berikan keputusan disetujui/ditolak                      |
        | HCSP            | - Catat CDT di sistem dan hentikan gaji jika disetujui                |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Surat permohonan resmi + dokumen pendukung *(surat dokter, belajar, dsb)*")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Hanya diberikan untuk alasan tertentu dengan persetujuan manajemen")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Maksimal **7 hari kerja** sejak dokumen permohonan lengkap")
        st.markdown("---")

    elif selected_hcsp == "6. Perubahan status kepegawaian":
        st.markdown("#### 1. Proses Perubahan Data Pribadi")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                        |
        |-----------------|------------------------------------------------------------------|
        | Pekerja         | - Melakukan pembaruan data (alamat, telp, status pernikahan, dll) |
        | HCSP            | - Verifikasi & update data dalam sistem HC                      |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- KTP baru, KK baru, Akta Nikah, atau dokumen pendukung lainnya")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Perubahan data penting untuk proses payroll, pajak, dan benefit")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Maksimal **3 hari kerja** sejak dokumen diterima")

        st.markdown("---")
        st.markdown("#### 2. Proses Perubahan Jabatan (Promosi/Demosi)")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                        |
        |-----------------|------------------------------------------------------------------|
        | PUK             | - Ajukan perubahan jabatan berdasarkan evaluasi kinerja          |
        | HC Region       | - Review dan beri persetujuan                                    |
        | HCSP            | - Update sistem & siapkan surat perubahan                        |
        | Pekerja         | - Tanda tangan dokumen perubahan                                 |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Formulir perubahan jabatan & SK promosi/demosi")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Harus disertai bukti kinerja atau kebutuhan organisasi")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Maksimal **5 hari kerja** setelah disetujui")

        st.markdown("---")
        st.markdown("#### 3. Proses Mutasi/Rotasi Unit Kerja")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                        |
        |-----------------|------------------------------------------------------------------|
        | PUK             | - Ajukan mutasi antar unit/cabang ke HC Region                   |
        | HCSP            | - Verifikasi & proses perpindahan di sistem                      |
        | Pekerja         | - Menerima surat tugas dan lokasi kerja baru                     |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Surat mutasi atau rotasi resmi")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Mutasi dapat diminta oleh organisasi atau pekerja")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Maksimal **5 hari kerja** sejak surat disetujui")

        st.markdown("---")
        st.markdown("#### 4. Proses Perubahan Status Kontrak (PKWT ↔ PKWTT)")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                        |
        |-----------------|------------------------------------------------------------------|
        | HC Region       | - Ajukan perubahan status setelah evaluasi                       |
        | HCSP            | - Siapkan & cetak kontrak baru                                   |
        | Pekerja         | - Tanda tangan kontrak baru                                      |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Kontrak kerja baru & form evaluasi masa percobaan")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Harus sesuai ketentuan durasi kontrak & hasil evaluasi")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Tanda tangan kontrak maksimal **7 hari kerja sebelum efektif**")

        st.markdown("---")
        st.markdown("#### 5. Proses Perubahan Gaji")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                        |
        |-----------------|------------------------------------------------------------------|
        | PUK             | - Ajukan penyesuaian gaji berdasarkan review/promosi             |
        | HC Region       | - Setujui dan kirim ke HCSP                                      |
        | HCSP            | - Update nominal gaji di sistem dan payroll                      |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Surat keputusan penyesuaian gaji")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Berlaku sejak tanggal efektif yang telah ditentukan")

        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Update sistem & payroll maksimal **H-5 sebelum cut-off**")
        st.markdown("---")

    elif selected_hcsp == "7. Surat Keterangan Kerja":
        st.markdown("#### 1. Proses Permintaan Surat Keterangan Kerja Aktif")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                        |
        |-----------------|------------------------------------------------------------------|
        | Pekerja         | - Ajukan permintaan melalui sistem HC/email ke HCSP              |
        | HCSP            | - Verifikasi status kepegawaian & susun surat                    |
        | HCSP            | - Kirim surat bertandatangan digital/fisik ke pekerja            |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Data diri pekerja (ditarik otomatis dari sistem)")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Umumnya digunakan untuk pengajuan **KPR, pinjaman, visa**, dll\n- Maksimal pengajuan **1x per bulan**, kecuali kebutuhan mendesak")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Surat terbit maksimal **3 hari kerja** sejak permintaan diterima")

        st.markdown("---")
        st.markdown("#### 2. Proses Permintaan Surat Rekomendasi/Referensi Kerja")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                        |
        |-----------------|------------------------------------------------------------------|
        | Pekerja         | - Ajukan permintaan melalui PUK atau langsung ke HCSP            |
        | PUK             | - Beri persetujuan & input isi rekomendasi                       |
        | HCSP            | - Susun dan kirim surat berdasarkan input dari PUK               |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Surat permintaan atau email formal dari pekerja")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Surat rekomendasi **tidak wajib** dan sesuai kebijakan unit kerja\n- Bisa diberikan untuk pekerja aktif atau yang **sudah resign** dalam waktu tertentu")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Surat terbit maksimal **5 hari kerja** setelah semua data lengkap")
        st.markdown("---")

    elif selected_hcsp == "8. Program Retensi Pegawai":
        st.markdown("#### 1. Proses Identifikasi dan Pengajuan Program Retensi")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                                 |
        |-----------------|---------------------------------------------------------------------------|
        | PUK/HC Region   | - Identifikasi pekerja high potential atau high risk turnover             |
        | PUK             | - Ajukan usulan retensi ke HC Region dan/atau HC Learning                 |
        | HCSP            | - Terima rekomendasi dan proses benefit retensi sesuai persetujuan        |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Formulir rekomendasi retensi\n- Data kinerja & kontribusi pekerja")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Retensi bisa berupa **promosi, insentif, penyesuaian job grade**, atau **pelatihan khusus**\n- Tidak semua pengajuan disetujui, harus melalui **justifikasi dan review HRBP**")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Review dan approval maksimal **10 hari kerja**")

        st.markdown("---")
        st.markdown("#### 2. Proses Implementasi Program Retensi")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                                     |
        |-----------------|--------------------------------------------------------------------------------|
        | HCSP            | - Lakukan proses administratif (perubahan gaji, job grade, akses pelatihan)   |
        | HC Region       | - Monitor dampak retensi terhadap keberlanjutan pekerja                       |
        | Pekerja         | - Tanda tangan dokumen implementasi (jika ada)                                |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Surat penetapan benefit retensi\n- Perubahan kontrak kerja (jika ada)")

        st.markdown("---")
        st.markdown("⚠️ **Catatan Penting:**")
        st.markdown("- Seluruh proses **bersifat rahasia** dan hanya diketahui pihak terkait\n- Dampak retensi dimonitor selama **3–6 bulan**")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Implementasi maksimal **7 hari kerja** sejak persetujuan")
        st.markdown("---")

    elif selected_hcsp == "9. Employee Service Center":
        st.markdown("#### 1. Proses Penanganan Pertanyaan dan Permintaan Informasi HC")
        st.markdown("""
        | **Stakeholder**  | **Tugas**                                                                 |
        |------------------|---------------------------------------------------------------------------|
        | Pekerja          | - Menghubungi ESC untuk pertanyaan HC (benefit, payroll, cuti, dll.)     |
        | ESC Agent (HCSP) | - Menerima & mencatat tiket layanan melalui kanal resmi                   |
        | ESC Agent        | - Menjawab langsung / eskalasi ke unit terkait jika perlu                 |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Tidak ada, kecuali jika permintaan terkait dokumen personal")

        st.markdown("---")
        st.markdown("📬 **Saluran Resmi:**")
        st.markdown("- Email ESC\n- WhatsApp ESC\n- MS Teams HC Channel\n- Hotline internal")

        st.markdown("---")
        st.markdown("⚠️ **Catatan:**")
        st.markdown("- Semua pertanyaan & permintaan dicatat dalam sistem ticketing untuk monitoring SLA")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Respon awal: maksimal **2 hari kerja**\n- Penyelesaian: maksimal **5 hari kerja** atau sesuai SLA layanan")

        st.markdown("---")
        st.markdown("#### 2. Proses Permintaan Dokumen oleh Pekerja")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                                 |
        |-----------------|----------------------------------------------------------------------------|
        | Pekerja         | - Kirim permintaan dokumen ke ESC (e.g., slip gaji, surat keterangan)     |
        | ESC             | - Verifikasi & terbitkan dokumen via sistem/email                         |
        | ESC             | - Catat pengiriman ke dalam log layanan                                   |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Permintaan via email atau sistem ticketing")

        st.markdown("---")
        st.markdown("⚠️ **Catatan:**")
        st.markdown("- Dokumen diberikan dalam format **PDF** atau **fisik** bila disetujui\n- Permintaan mendadak/massal akan disesuaikan dengan antrean")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Dokumen diterbitkan maksimal **3 hari kerja** sejak permintaan lengkap")
        st.markdown("---")

    elif selected_hcsp == "10. Pengakhiran Hubungan Kerja":
        st.markdown("#### 1. Proses Pengajuan Pengakhiran Hubungan Kerja (PHK, Resign, Pensiun)")
        st.markdown("""
        | **Stakeholder**  | **Tugas**                                                                          |
        |------------------|-------------------------------------------------------------------------------------|
        | PUK              | - Sampaikan rencana PHK/resign/pensiun ke HC Region & HCSP                         |
        | HCSP             | - Verifikasi data & susun dokumen formal (SK PHK, surat resign, dll.)              |
        | HC Region        | - Beri persetujuan atas dasar justifikasi dan kelengkapan dokumen                  |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Surat pengunduran diri\n- SK PHK / SK Pensiun\n- Checklist clearance")

        st.markdown("---")
        st.markdown("⚠️ **Catatan:**")
        st.markdown("- Resign diajukan tertulis minimal **30 hari sebelumnya**\n- Proses mengikuti regulasi perusahaan & UU Ketenagakerjaan")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- SK terbit maksimal **7 hari kerja** setelah semua dokumen lengkap")

        st.markdown("---")
        st.markdown("#### 2. Proses Exit Clearance")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                                      |
        |-----------------|---------------------------------------------------------------------------------|
        | Pekerja         | - Kembalikan aset & dokumen (ID Card, laptop, akses sistem)                    |
        | PUK             | - Cek dan verifikasi pengembalian aset                                          |
        | HCSP            | - Catat status clearance & arsipkan dokumentasi                                 |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Form Exit Clearance\n- Bukti pengembalian aset")

        st.markdown("---")
        st.markdown("⚠️ **Catatan:**")
        st.markdown("- Clearance wajib **sebelum tanggal akhir kerja**\n- Pembayaran final dapat ditahan jika aset belum kembali")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Clearance selesai maksimal **H-1** sebelum tanggal terakhir bekerja")

        st.markdown("---")
        st.markdown("#### 3. Proses Pembayaran Hak Pekerja (Final Payment)")
        st.markdown("""
        | **Stakeholder** | **Tugas**                                                                 |
        |-----------------|----------------------------------------------------------------------------|
        | HCSP            | - Hitung hak akhir: gaji, cuti, THR, kompensasi (jika ada)                |
        | Finance         | - Proses pembayaran sesuai hasil perhitungan                              |
        | Pekerja         | - Terima slip pembayaran & bukti transfer                                 |
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("📌 **Dokumen:**")
        st.markdown("- Rekap hak akhir\n- Slip gaji terakhir")

        st.markdown("---")
        st.markdown("⚠️ **Catatan:**")
        st.markdown("- Pembayaran dilakukan **setelah seluruh proses clearance selesai**")

        st.markdown("---")
        st.markdown("⏱ **SLA Waktu:**")
        st.markdown("- Pembayaran final maksimal **14 hari kerja** setelah tanggal efektif akhir kerja")
        st.markdown("---")

# Halaman SOP Benefit
elif st.session_state.page == "Benefit":
    # Tombol kembali ke Home
    if st.button("Back to Home"):
        go_to("Home")
    st.header("🎁 HC Benefit Quick Reference")
    st.markdown("Panduan ringkas Human Capital Benefit. Pilih topik di bawah ini untuk melihat detailnya.")

    # Dropdown untuk memilih sub-bab
    hcsp_options = [
        "1. Administrasi Dana Kerohanian",
        "2. Administrasi Dana Rekreasi",
        "3. Asuransi Jiwa Kesehatan Komersial",
        "4. Bantuan Kematian Duka",
        "5. Dana Pensiun",
        "6. E-Registrasi Welcoming Pack & Logam Mulia",
        "7. Pengajuan dan Penghentian Club Membership",
        "8. Penghargaan Masa Kerja Plakat dan Logam Mulia",
        "9. Pinjaman Pekerja"
    ]
    selected_hcsp = st.selectbox("Pilih topik:", hcsp_options)

    # Tampilkan konten berdasarkan pilihan
    if selected_hcsp == "1. Preboarding":
        st.markdown("#### 1. Proses Preboarding")

# Halaman SOP Payroll
elif st.session_state.page == "Payroll":
    # Tombol kembali ke Home
    if st.button("Back to Home"):
        go_to("Home")
    st.header("💸 HC Payroll Quick Reference")
    st.markdown("Panduan ringkas Human Capital Payroll. Pilih topik di bawah ini untuk melihat detailnya.")

    # Dropdown untuk memilih sub-bab
    hcsp_options = [
        "1. Administrasi Shift Pekerja",
        "2. Administrasi Pembayaran Insentif Pekerja",
        "3. Administrasi Pembayaran Pelaporan SPT",
        "4. Payroll Outsourcing",
        "5. Pengaturan Rekening Payroll",
        "6. Proses Pengajuan Klaim dan Permintaan Barang/Jasa",
        "7. BPJS Kesehatan",
        "8. BPJS Ketenagakerjaan",
        "9. Fasilitas Penugasan Pekerja"
    ]
    selected_hcsp = st.selectbox("Pilih topik:", hcsp_options)

    # Tampilkan konten berdasarkan pilihan
    if selected_hcsp == "1. Preboarding":
        st.markdown("#### 1. Proses Preboarding")