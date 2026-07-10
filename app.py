import streamlit as st
import sys
import os

# --- SISTEM DEBUG ERROR (Akan menangkap semua crash) ---
st.error("🔧 SISTEM DEBUG STREAMLIT AKTIF")

# Cek 1: Deteksi Struktur Folder GitHub Anda
with st.expander("📁 Lihat Struktur Folder Server (Debug 1)", expanded=False):
    try:
        st.write("Lokasi saat ini:", os.getcwd())
        st.write("Daftar file di folder utama:", os.listdir("."))
        if os.path.exists("pages"):
            st.write("Daftar file di dalam folder /pages:", os.listdir("pages"))
        else:
            st.warning("Peringatan: Folder 'pages' tidak ditemukan! Tombol perpindahan halaman akan error.")
    except Exception as e:
        st.exception(e)

# Cek 2: Tes Proses Import utils.py & Fungsi require_login
with st.expander("🔑 Tes Import utils.py & Login (Debug 2)", expanded=True):
    try:
        from utils import require_login
        st.success("✅ File 'utils.py' berhasil di-import tanpa error.")
        
        # Jalankan fungsi login milik Anda
        require_login()
        st.success("✅ Fungsi 'require_login()' sukses dieksekusi.")
    except Exception as e:
        st.error("❌ GAGAL DI SINI: File 'utils.py' atau fungsi 'require_login()' rusak!")
        st.exception(e)

# Cek 3: Memeriksa isi data Session State Anda
with st.expander("💾 Cek Isi Data Session State (Debug 3)", expanded=True):
    st.write("Isi memory login saat ini:")
    st.json(dict(st.session_state))
    # Mengambil email dengan aman
    user_email = st.session_state.get("email", st.session_state.get("username", "Pengguna Tanpa Nama"))


# --- TAMPILAN INTERFACE UTAMA (DILINDUNGI AGAR TIDAK CRASH) ---
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 1.5rem; padding-bottom: 2rem; max-width: 480px;}
    .header-card {
        background: linear-gradient(135deg, #1a3c6e 0%, #0d1f3c 100%);
        border-radius: 16px; padding: 26px 20px 22px 20px;
        text-align: center; color: white; margin-bottom: 22px;
    }
    .header-card img { width: 64px; margin-bottom: 10px; }
    .header-card h1 { font-size: 17px; font-weight: 600; margin: 4px 0 2px 0; color: white; }
    .header-card p { font-size: 12.5px; color: #cfd8e8; margin: 0; }
    .menu-label { font-size: 13px; font-weight: 600; color: #6b7280; margin: 4px 2px 8px 2px; letter-spacing: 0.3px; }
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="header-card">
    <img src="https://atmi.ac.id" />
    <h1>Sistem Informasi Praktikum Mekatronika ATMI Surakarta</h1>
    <p>Program Studi Mekatronika &middot; Politeknik ATMI Surakarta</p>
    <p style="margin-top:6px;">Login sebagai <b>{user_email}</b></p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="menu-label">MENU UTAMA</div>', unsafe_allow_html=True)

# Membuka halaman dengan validasi file agar tidak melempar internal server error
def buat_halaman_aman(path, label):
    if os.path.exists(path):
        st.page_link(path, label=label, use_container_width=True)
    else:
        st.error(f"File halaman '{path}' tidak ditemukan di GitHub Anda!")

buat_halaman_aman("pages/1_Input_MKL.py", "📝  Input MKL")
buat_halaman_aman("pages/2_Presensi.py", "📊  Presensi")
buat_halaman_aman("pages/3_Aktivitas.py", "🗂️  Aktivitas")
st.link_button("📢  Info Mekatro", "https://atmi.ac.id", use_container_width=True)

def proses_logout_kustom():
    st.session_state.clear()
    st.rerun()

st.write("")
st.button("Logout", on_click=proses_logout_kustom)
