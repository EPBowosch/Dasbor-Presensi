import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1X4ViFRgzWB9ZdLfX_DccnAf1gA7E3sSdS_1pX5ucd2k/edit"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]


@st.cache_resource
def get_gspread_client():
    """Buat koneksi ke Google Sheets pakai service account (bukan akun pribadi)."""
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"], scopes=SCOPES
    )
    return gspread.authorize(creds)


@st.cache_data(ttl=300)  # cache 5 menit biar gak nembak Sheets tiap reload
def get_sheet_values(sheet_name: str):
    gc = get_gspread_client()
    sh = gc.open_by_url(SPREADSHEET_URL)
    ws = sh.worksheet(sheet_name)
    return ws.get_all_values()


def require_login():
    """Panggil di awal tiap halaman. Kalau belum login, tampilkan tombol login dan stop."""
    if not st.user.is_logged_in:
        st.markdown(
            "<div style='text-align:center; padding-top:60px;'>"
            "<h3>Sistem Informasi Akademik</h3>"
            "<p style='color:#6b7280;'>Silakan login dengan akun ATMI kamu untuk melanjutkan.</p>"
            "</div>",
            unsafe_allow_html=True,
        )
        col = st.columns([1, 2, 1])[1]
        with col:
            st.button("Login dengan Google", on_click=st.login, use_container_width=True)
        st.stop()


def filter_by_email(values: list, email_col_index: int):
    """Samakan logika dengan getDataForCurrentUser() di Apps Script: cocokkan email login vs kolom email di sheet."""
    email = st.user.email
    return [row for row in values if len(row) > email_col_index and row[email_col_index] == email]
