import streamlit as st
import os

# 1. Konfigurasi Gaya Tampilan (CSS Kustom)
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

# 2. Validasi & Proteksi Login
try:
    from utils import require_login
    require_login()
except Exception as e:
    st.error("Gagal memuat modul login otomatis dari berkas utils.py.")
    st.exception(e)
    st.stop()

# 3. Ambil data Email dari memori Session State lokal
user_email = st.session_state.get("user_email", "Pengguna ATMI")

# 4. Tampilkan Kartu Informasi Header
st.markdown(f"""
<div class="header-card">
    <img src="https://atmi.ac.id" />
    <h1>Sistem Informasi Praktikum Mekatronika ATMI Surakarta</h1>
    <p>Program Studi Mekatronika &middot; Politeknik ATMI Surakarta</p>
    <p style="margin-top:6px;">Login sebagai: <b>{user_email}</b></p>
</div>
""", unsafe_allow_html=True)

# 5. Navigasi Menu Utama Multipage
st.markdown('<div class="menu-label">MENU UTAMA</div>', unsafe_allow_html=True)

if os.path.exists("pages/1_Input_MKL.py"):
    st.page_link("pages/1_Input_MKL.py", label="📝  Input MKL", use_container_width=True)
else:
    st.error("⚠️ Berkas '1_Input_MKL.py' tidak ditemukan di dalam folder 'pages'.")

if os.path.exists("pages/2_Presensi.py"):
    st.page_link("pages/2_Presensi.py", label="📊  Presensi", use_container_width=True)
else:
    st.error("⚠️ Berkas '2_Presensi.py' tidak ditemukan di dalam folder 'pages'.")

if os.path.exists("pages/3_Aktivitas.py"):
    st.page_link("pages/3_Aktivitas.py", label="🗂️  Aktivitas", use_container_width=True)
else:
    st.error("⚠️ Berkas '3_Aktivitas.py' tidak ditemukan di dalam folder 'pages'.")

# Tombol Tautan Eksternal Website ATMI
st.link_button("📢  Info Mekatro", "https://atmi.ac.id", use_container_width=True)

# 6. Fungsi dan Tombol Logout Mandiri
def proses_logout_kustom():
    st.session_state.clear()
    st.rerun()

st.write("")
st.button("Logout", on_click=proses_logout_kustom)
