import streamlit as st
from utils import require_login

# 1. Konfigurasi CSS Kustom (Tetap sama seperti milik Anda)
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 1.5rem; padding-bottom: 2rem; max-width: 480px;}

    .header-card {
        background: linear-gradient(135deg, #1a3c6e 0%, #0d1f3c 100%);
        border-radius: 16px;
        padding: 26px 20px 22px 20px;
        text-align: center;
        color: white;
        margin-bottom: 22px;
    }
    .header-card img { width: 64px; margin-bottom: 10px; }
    .header-card h1 { font-size: 17px; font-weight: 600; margin: 4px 0 2px 0; color: white; }
    .header-card p { font-size: 12.5px; color: #cfd8e8; margin: 0; }

    .menu-label {
        font-size: 13px; font-weight: 600; color: #6b7280;
        margin: 4px 2px 8px 2px; letter-spacing: 0.3px;
    }

    div.stButton > button,
    div[data-testid="stLinkButton"] > a,
    div[data-testid="stPageLink"] > a {
        width: 100%;
        text-align: left;
        background-color: white;
        border: 1px solid #e2e6ed;
        border-radius: 14px;
        padding: 16px 18px;
        font-size: 15.5px;
        font-weight: 500;
        color: #1a3c6e;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        margin-bottom: 10px;
        transition: all 0.15s ease;
        text-decoration: none;
        display: flex;
        justify-content: flex-start;
    }
    div.stButton > button:hover,
    div[data-testid="stLinkButton"] > a:hover,
    div[data-testid="stPageLink"] > a:hover {
        border-color: #1a3c6e;
        box-shadow: 0 2px 8px rgba(26,60,110,0.15);
        color: #1a3c6e;
    }
</style>
""", unsafe_allow_html=True)

# 2. Jalankan fungsi pengecekan login dari utils
require_login()

# 3. Ambil data email dari session state (Amankan dari crash)
# CATATAN: Ubah kata "email" di bawah sesuai dengan nama variabel session_state yang ada di utils.py Anda
user_email = st.session_state.get("email", "Pengguna Mekatronika")

# 4. Tampilkan Header Card dengan email yang aman
st.markdown(f"""
<div class="header-card">
    <img src="https://atmi.ac.id" />
    <h1>Sistem Informasi Praktikum Mekatronika ATMI Surakarta</h1>
    <p>Program Studi Mekatronika &middot; Politeknik ATMI Surakarta</p>
    <p style="margin-top:6px;">Login sebagai <b>{user_email}</b></p>
</div>
""", unsafe_allow_html=True)

# 5. Menu Utama Navigasi
st.markdown('<div class="menu-label">MENU UTAMA</div>', unsafe_allow_html=True)
st.page_link("pages/1_Input_MKL.py", label="📝  Input MKL", use_container_width=True)
st.page_link("pages/2_Presensi.py", label="📊  Presensi", use_container_width=True)
st.page_link("pages/3_Aktivitas.py", label="🗂️  Aktivitas", use_container_width=True)
st.link_button("📢  Info Mekatro", "https://atmi.ac.id", use_container_width=True)

# 6. Fungsi Logout Kustom untuk membersihkan session state
def proses_logout_kustom():
    st.session_state.clear()       # Menghapus semua data session login
    st.success("Berhasil logout!") # Menampilkan info sukses singkat
    st.rerun()                     # Memaksa aplikasi memuat ulang dan kembali ke menu login

st.write("")
st.button("Logout", on_click=proses_logout_kustom)
