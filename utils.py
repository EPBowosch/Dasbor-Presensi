import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Menggunakan ID agar gspread langsung mengunci dokumen tanpa error URL
SPREADSHEET_ID = "1X4ViFRgzWB9ZdLfX_DccnAf1gA7E3sSdS_1pX5ucd2k"
SCOPES = ["https://googleapis.com"]

@st.cache_resource
def get_gspread_client():
    """Koneksi Google Sheets dengan pembersih tanda kunci otomatis."""
    try:
        creds_dict = dict(st.secrets["gcp_service_account"])
        if "private_key" in creds_dict:
            # Mengubah format teks \n sisa copy-paste agar dibaca baris baru utuh oleh Google
            creds_dict["private_key"] = creds_dict["private_key"].replace("\\n", "\n").strip()
        creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
        return gspread.authorize(creds)
    except Exception as e:
        st.error("Gagal menyusun Kunci Service Account Google.")
        st.stop()

@st.cache_data(ttl=300) 
def get_sheet_values(sheet_name: str):
    """Fungsi asli Anda untuk menarik data tab."""
    gc = get_gspread_client()
    sh = gc.open_by_key(SPREADSHEET_ID)
    ws = sh.worksheet(sheet_name)
    return ws.get_all_values()

def require_login():
    """KEMBALI KE ASLI: Sistem Login Otomatis Google SSO tanpa field tambahan dengan perbaikan struktur st.columns."""
    if not st.user.is_logged_in:
        st.markdown(
            "<div style='text-align:center; padding-top:60px;'>"
            "<h3>Sistem Informasi Akademik</h3>"
            "<p style='color:#6b7280;'>Silakan login dengan akun ATMI kamu untuk melanjutkan.</p>"
            "</div>",
            unsafe_allow_html=True,
        )
        
        # PERBAIKAN DI SINI: Memberikan angka 3 agar Streamlit tahu ingin membagi halaman menjadi 3 kolom
        col1, col2, col3 = st.columns(3)
        with col2:
            st.button("Login dengan Google", on_click=st.login, use_container_width=True)
        st.stop()

def filter_by_email(values: list, email_col_index: int):
    """Logika asli Anda untuk mencocokkan email login otomatis vs sheet."""
    email = st.user.email
    return [row for row in values if len(row) > email_col_index and row[email_col_index] == email]
