import streamlit as st
import pandas as pd
from utils import require_login, get_sheet_values, filter_by_email

st.set_page_config(page_title="Presensi", layout="centered")
require_login()

st.page_link("app.py", label="← Kembali ke menu")
st.subheader("Rekap presensi")

values = get_sheet_values("Sheet2")
data = filter_by_email(values, 24)  # kolom Y = email

if not data:
    st.info("Belum ada data presensi untuk akun kamu.")
else:
    df = pd.DataFrame(
        [row[0:6] for row in data],
        columns=["Hari", "Tanggal", "Masuk", "Istirahat", "Msk ist", "Pulang"],
    )
    st.dataframe(df, use_container_width=True, hide_index=True)
