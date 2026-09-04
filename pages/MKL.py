import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from datetime import date

st.set_page_config(
    page_title="Presensi Aktivitas",
    page_icon="https://trmk.atmi.ac.id/wp-content/uploads/2023/06/atmi-logo-300x300.png",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Sembunyikan sidebar navigasi bawaan biar konsisten dengan halaman utama
st.markdown(
    '<style>[data-testid="stSidebarNav"] {display: none;} #MainMenu, footer, header {visibility: hidden;}</style>',
    unsafe_allow_html=True,
)

# ---------- Deteksi login Google ----------
if not st.user.is_logged_in:
    st.title("Presensi Aktivitas")
    st.write("Silakan login dengan akun Google ATMI Anda untuk melanjutkan.")
    st.button("Login dengan Google", on_click=st.login)
    st.stop()

email = st.user.email
nama = email.split("@")[0]

# Opsional tapi disarankan: batasi hanya domain kampus
if not email.endswith("@atmi.ac.id"):
    st.error("Akun ini tidak terdaftar sebagai bagian dari domain atmi.ac.id.")
    st.button("Logout", on_click=st.logout)
    st.stop()

st.title("Presensi Aktivitas")
st.markdown(f"**Alamat Email Anda:** {email}")

# ---------- Form ----------
with st.form("form_presensi"):
    aktivitas = st.text_input("Aktivitas")
    section = st.text_input("Section")
    tanggal = st.date_input("Tanggal", value=date.today())
    submitted = st.form_submit_button("Submit")

if submitted:
    if not aktivitas.strip() or not section.strip():
        st.error("Aktivitas dan Section wajib diisi.")
    else:
        qr_data = f"{nama}|{email}|{aktivitas}|{section}|{tanggal.strftime('%Y-%m-%d')}"
        encoded = urllib.parse.quote(qr_data)

        qr_url_1 = f"https://quickchart.io/chart?cht=qr&chs=500x500&chl={encoded}"
        qr_url_2 = f"https://api.qrserver.com/v1/create-qr-code/?data={encoded}&size=500x500"

        st.success("Data berhasil dicatat. Silakan tunjukkan salah satu QR Code berikut.")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**QR Code 1**")
            st.image(qr_url_1)
        with col2:
            st.markdown("**QR Code 2**")
            st.image(qr_url_2)

st.markdown("---")
col_a, col_b = st.columns(2)
with col_a:
    if st.button("Home"):
        components.html(
            "<script>window.parent.window.location.href='/';</script>",
            height=0, width=0,
        )
with col_b:
    st.button("Logout", on_click=st.logout)
