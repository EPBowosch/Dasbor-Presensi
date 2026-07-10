import streamlit as st
from utils import require_login, get_sheet_values, filter_by_email

st.set_page_config(page_title="Input MKL", layout="centered")
require_login()

st.page_link("app.py", label="← Kembali ke menu")
st.subheader("Minus Kompen Lembur (MKL)")

values = get_sheet_values("Sheet3")
data = filter_by_email(values, 9)  # kolom J = email

if not data:
    st.info("Belum ada data MKL untuk akun kamu.")
else:
    row = data[0]

    st.markdown("**Total keseluruhan**")
    c1, c2, c3 = st.columns(3)
    c1.metric("Minus", row[0])
    c2.metric("Kompen", row[1])
    c3.metric("Plus", row[2])

    st.markdown("**Bulan ini**")
    c4, c5, c6 = st.columns(3)
    c4.metric("Minus", row[3])
    c5.metric("Kompen", row[4])
    c6.metric("Plus", row[5])
