import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1X4ViFRgzWB9ZdLfX_DccnAf1gA7E3sSdS_1pX5ucd2k/edit?usp=sharing"
SCOPES = ["https://googleapis.com"]


@st.cache_resource
def get_gspread_client():
    """Buat koneksi ke Google Sheets pakai service account."""
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"], scopes=SCOPES
    )
    return gspread.authorize(creds)


@st.cache_data(ttl=300)  # cache 5 menit
def get_sheet_values(sheet_name: str):
    gc = get_gspread_client()
    sh = gc.open_by_url(SPREADSHEET_URL)
    ws = sh.worksheet(sheet_name)
    return ws.get_all_values()


def require_login():
    """Panggil di awal tiap halaman. Menggunakan session state agar aman dari crash 500."""
    # Inisialisasi status login lokal jika belum ada
    if "is_logged_in" not in st.session_state:
        st.session_state.is_logged_in = False
        st.session_state.user_email = ""

    # Jika pengguna belum berhasil login
    if not st.session_state.is_logged_in:
        st.markdown(
            "<div style='text-align:center; padding-top:40px;'>"
            "<h3>Sistem Informasi Akademik Mekatronika</h3>"
            "<p style='color:#6b7280;'>Silakan masukkan Email ATMI Anda untuk melanjutkan.</p>"
            "</div>",
            unsafe_allow_html=True,
        )
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            # Form input email sebagai pengganti OAuth sementara yang crash
            input_email = st.text_input("Email Resmi ATMI", placeholder="nama@student.atmi.ac.id")
            tombol_login = st.button("Masuk ke Sistem", use_container_width=True)
            
            if tombol_login:
                if input_email and "@" in input_email:
                    # Simpan data ke session state lokal
                    st.session_state.is_logged_in = True
                    st.session_state.user_email = input_email.strip()
                    st.success("Login sukses!")
                    st.rerun() # Refresh halaman untuk memuat menu utama
                else:
                    st.error("Mohon masukkan format email ATMI yang valid!")
                    
        st.stop() # Hentikan eksekusi kode halaman selanjutnya sebelum login


def filter_by_email(values: list, email_col_index: int):
    """Mencocokkan email login dari session state lokal dengan kolom email di sheet."""
    # Ambil email dari session state lokal, bukan dari st.user yang rawan error
    email = st.session_state.get("user_email", "")
    if not email:
        return []
    return [row for row in values if len(row) > email_col_index and row[email_col_index] == email]
