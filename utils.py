import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# 1. Gunakan ID Spreadsheet langsung agar 100% bebas dari NoValidUrlKeyFound
SPREADSHEET_ID = "1X4ViFRgzWB9ZdLfX_DccnAf1gA7E3sSdS_1pX5ucd2k"
SCOPES = ["https://googleapis.com"]

@st.cache_resource
def get_gspread_client():
    """Koneksi Google Sheets dengan pembersih kunci otomatis agar bebas dari RefreshError."""
    try:
        creds_dict = dict(st.secrets["gcp_service_account"])
        
        # Memperbaiki karakter baris baru (\n) pada private_key secara otomatis
        if "private_key" in creds_dict:
            raw_key = creds_dict["private_key"]
            clean_key = raw_key.replace("\\n", "\n")
            if clean_key.startswith('"""') and clean_key.endswith('"""'):
                clean_key = clean_key[3:-3].strip()
            creds_dict["private_key"] = clean_key.strip()

        creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
        return gspread.authorize(creds)
    except Exception as e:
        st.error("Gagal menyusun Kunci Service Account Google Sheets.")
        st.exception(e)
        st.stop()

@st.cache_data(ttl=300)
def get_sheet_values(sheet_name: str):
    """Ambil data dari Google Sheets secara stabil menggunakan ID."""
    gc = get_gspread_client()
    sh = gc.open_by_key(SPREADSHEET_ID)
    ws = sh.worksheet(sheet_name)
    return ws.get_all_values()

def require_login():
    """Sistem Proteksi: Login Otomatis Google bawaan dengan Field Tambahan."""
    # Menghubungkan st.session_state dengan st.user bawaan secara otomatis
    if st.user.is_logged_in:
        st.session_state.is_logged_in = True
        st.session_state.user_email = st.user.email
    else:
        st.session_state.is_logged_in = False
        st.session_state.user_email = ""

    # Jika user belum terdeteksi login otomatis oleh Google, kunci halaman
    if not st.user.is_logged_in:
        st.markdown(
            "<div style='text-align:center; padding-top:40px;'>"
            "<h3>Sistem Informasi Akademik Mekatronika</h3>"
            "<p style='color:#6b7280;'>Silakan isi data dan login untuk melanjutkan.</p>"
            "</div>",
            unsafe_allow_html=True,
        )
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            # --- FIELD ISIAN MANDIRI YANG ANDA MAKSUD ---
            # Data ini akan tersimpan di memory session_state meskipun menggunakan st.login
            st.session_state.nama_lengkap = st.text_input("Nama Lengkap / NIM", placeholder="Masukkan nama atau NIM kamu")
            st.session_state.kelas = st.selectbox("Pilih Kelas", ["", "MK-1A", "MK-1B", "MK-2A", "MK-2B", "MK-3A", "MK-3B"])
            
            st.write("") # Jeda jarak
            
            # Tombol Login Otomatis Google bawaan Streamlit Cloud
            tombol_klik = st.button("Login dengan Google / ATMI", on_click=st.login, use_container_width=True)
            
            # Validasi jika tombol diklik tapi field masih kosong
            if tombol_klik and (not st.session_state.nama_lengkap or st.session_state.kelas == ""):
                st.error("⚠️ Mohon isi Nama Lengkap dan Pilih Kelas terlebih dahulu!")
                st.stop()
                
        st.stop()

def filter_by_email(values: list, email_col_index: int):
    """Menyaring baris data Sheets berdasarkan email login otomatis Google."""
    email = st.user.email if st.user.is_logged_in else st.session_state.get("user_email", "")
    if not email:
        return []
    return [row for row in values if len(row) > email_col_index and row[email_col_index] == email]
