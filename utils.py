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
    """Fungsi untuk menarik data tab Sheets."""
    gc = get_gspread_client()
    sh = gc.open_by_key(SPREADSHEET_ID)
    ws = sh.worksheet(sheet_name)
    return ws.get_all_values()

def require_login():
    """Sistem Proteksi: Hanya ada SATU kolom isian input teks untuk Email SSO ATMI."""
    # Inisialisasi status login di memori lokal jika belum ada
    if "is_logged_in" not in st.session_state:
        st.session_state.is_logged_in = False
        st.session_state.user_email = ""

    # Jika pengguna belum mengisi email dan menekan tombol login
    if not st.session_state.is_logged_in:
        st.markdown(
            "<div style='text-align:center; padding-top:40px;'>"
            "<h3>Sistem Informasi Akademik Mekatronika</h3>"
            "<p style='color:#6b7280;'>Silakan masukkan Email ATMI Anda untuk melanjutkan.</p>"
            "</div>",
            unsafe_allow_html=True,
        )
        
        # PERBAIKAN: Memberikan angka 3 agar tata letak kolom seimbang dan tidak memicu crash
        col1, col2, col3 = st.columns(3)
        with col2:
            # HANYA ADA SATU ISIAN EMAIL SEPERTI YANG ANDA MAKSUD
            input_email = st.text_input("Email Resmi ATMI", placeholder="nama@student.atmi.ac.id")
            tombol_login = st.button("Masuk ke Sistem", use_container_width=True)
            
            if tombol_login:
                if input_email and "@" in input_email:
                    # Simpan email ke memori session state lokal
                    st.session_state.user_email = input_email.strip()
                    st.session_state.is_logged_in = True
                    st.success("Login sukses!")
                    st.rerun()  # Muat ulang halaman untuk membuka menu utama di app.py
                else:
                    st.error("Mohon masukkan format email ATMI yang valid!")
                    
        st.stop() # Blokir menu utama sebelum input email diisi

def filter_by_email(values: list, email_col_index: int):
    """Mencocokkan email login dari kolom isian teks dengan data di sheet."""
    # Mengambil data email dari memori isian manual secara aman
    email = st.session_state.get("user_email", "")
    if not email:
        return []
    return [row for row in values if len(row) > email_col_index and row[email_col_index] == email]
