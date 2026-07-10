import streamlit as st

# ==========================================
# 1. KONFIGURASI HALAMAN UTAMA
# ==========================================
st.set_page_config(
    page_title="Dasbor Presensi ATMI", 
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. DEFINISI DAFTAR HALAMAN (Eksplisit)
# ==========================================
halaman_home = st.Page("app.py", title="Menu Utama")
halaman_input = st.Page("pages/1_Input_MKL.py", title="Input MKL")
halaman_presensi = st.Page("pages/2_Presensi.py", title="Presensi")
halaman_aktivitas = st.Page("pages/3_Aktivitas.py", title="Aktivitas")

# Daftarkan semua rute halaman ke dalam router Streamlit
pg = st.navigation(
    [halaman_home, halaman_input, halaman_presensi, halaman_aktivitas], 
    position="sidebar"
)

# ==========================================
# 3. KONFIGURASI GAYA TAMPILAN (CSS KUSTOM)
# ==========================================
st.markdown("""
<style>
    /* Menyembunyikan total bilah samping bawaan Streamlit */
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    #MainMenu, footer, header { visibility: hidden !important; }
    
    .block-container { padding-top: 1.5rem; padding-bottom: 2rem; max-width: 480px; }

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

# ==========================================
# 4. KONTROL SISTEM LOGIN VIA UTILS
# ==========================================
try:
    from utils import require_login
    require_login()
except Exception as e:
    st.error("Gagal memuat modul login otomatis dari berkas utils.py.")
    st.exception(e)
    st.stop()

# ==========================================
# 5. TAMPILAN HALAMAN UTAMA (JIKA USER LOGGED IN)
# ==========================================
if st.session_state.get("is_logged_in", False):
    user_email = st.session_state.get("user_email", "Pengguna ATMI")

    st.markdown(f"""
    <div class="header-card">
        <img src="https://atmi.ac.id" />
        <h1>Sistem Informasi Praktikum Mekatronika ATMI Surakarta</h1>
        <p>Program Studi Mekatronika &middot; Politeknik ATMI Surakarta</p>
        <p style="margin-top:6px;">Login sebagai: <b>{user_email}</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="menu-label">MENU UTAMA</div>', unsafe_allow_html=True)
    
    # Memicu perpindahan rute URL internal menggunakan objek halaman yang valid
    st.page_link(halaman_input, label="📝  Input MKL", use_container_width=True)
    st.page_link(halaman_presensi, label="📊  Presensi", use_container_width=True)
    st.page_link(halaman_aktivitas, label="🗂️  Aktivitas", use_container_width=True)
    
    st.link_button("📢  Info Mekatro", "https://atmi.ac.id", use_container_width=True)

    def proses_logout_kustom():
        st.session_state.clear()
        st.rerun()

    st.write("")
    st.button("Logout", on_click=proses_logout_kustom)

# ==========================================
# 6. EKSEKUSI JALANNYA NAVIGASI (Wajib Berdiri Sendiri)
# ==========================================
# Memastikan modul inti router mengeksekusi perpindahan file saat st.page_link ditekan
pg.run()
