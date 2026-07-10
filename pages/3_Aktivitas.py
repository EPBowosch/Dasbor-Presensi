import streamlit as st
import pandas as pd
from utils import require_login, get_sheet_values, filter_by_email

st.set_page_config(page_title="Aktivitas", layout="centered")
require_login()

st.page_link("app.py", label="← Kembali ke menu")
st.subheader("Rekap aktivitas")

values = get_sheet_values("Sheet4")
data = filter_by_email(values, 24)  # kolom Y = email

if not data:
    st.info("Belum ada data aktivitas untuk akun kamu.")
else:
    rows = []
    for row in data:
        rows.append([
            row[1] if len(row) > 1 else "",
            row[17] if len(row) > 17 else "",
            row[18] if len(row) > 18 else "",
            row[19] if len(row) > 19 else "",
            row[20] if len(row) > 20 else "",
            row[21] if len(row) > 21 else "",
            row[22] if len(row) > 22 else "",
        ])
    df = pd.DataFrame(
        rows,
        columns=["Tanggal", "Minus", "Kompen", "Lembur", "Keterangan", "Ket. 2", "Ket. 3"],
    )
    st.dataframe(df, use_container_width=True, hide_index=True)
