import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# GANTI DENGAN ID GOOGLE SHEETS ANDA (Ambil dari antara /d/ dan /edit pada URL Sheets Anda)
SPREADSHEET_ID = "1X4ViFRgzWB9ZdLfX_DccnAf1gA7E3sSdS_1pX5ucd2k"
SCOPES = ["https://googleapis.com"]

@st.cache_resource
def get_gspread_client():
    """Koneksi Google Sheets dengan pembersih kunci otomatis."""
    try:
        creds_dict = dict(st.secrets["gcp_service_account"])
        
        # Memperbaiki baris baru pada private_key secara aman
        if "private_key" in creds_dict:
            raw_key = creds_dict["private_key"]
            clean_key = raw_key.replace("\\n", "\n")
            if clean_key.startswith('"""') and clean_key.endswith('"""'):
                clean_key = clean_key[3:-3].strip()
            creds_dict["private_key"] = clean_key.strip()

        creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
        return gspread.authorize(creds)
    except Exception as e:
        st.error("Gagal menyusun Kunci Service Account Google.")
        st.exception(e)
        st.stop()

@st.cache_data(ttl=300)
def get_sheet_values(sheet_name: str):
    """Ambil data menggunakan open_by_key agar bebas dari NoValidUrlKeyFound."""
    gc = get_gspread_client()
    # Menggunakan open_by_key jauh lebih stabil daripada open_by_url
    sh = gc.open_by_key(SPREADSHEET_ID)
    ws = sh.worksheet(sheet_name)
    return ws.get_all_values()

def require_login():
    """Sistem proteksi halaman login otomatis."""
    if "is_logged_in" not in st.session_state:
        st.session_state.is_logged_in = False
        st.session_state.user_email = ""

    if not st.session_state.is_logged_in:
        st.markdown("<h3 style='text-align:center; padding-top:40px;'>Sistem Informasi Akademik Mekatronika</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#6b7280;'>Silakan masukkan Email ATMI Anda.</p>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns()
        with col2:
            input_email = st.text_input("Email Resmi ATMI", placeholder="nama@student.atmi.ac.id")
            tombol_login = st.button("Masuk ke Sistem", use_container_width=True)
            
            if tombol_login:
                if input_email and "@" in input_email:
                    st.session_state.user_email = input_email.strip()
                    st.session_state.is_logged_in = True
                    st.success("Login sukses!")
                    st.rerun()
                else:
                    st.error("Mohon masukkan format email ATMI yang valid!")
        st.stop()

def filter_by_email(values: list, email_col_index: int):
    """Filter data sheets berdasarkan email pengguna."""
    email = st.session_state.get("user_email", "")
    if not email:
        return []
    return [row for row in values if len(row) > email_col_index and row[email_col_index] == email]
