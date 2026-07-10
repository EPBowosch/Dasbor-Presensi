import streamlit as st

st.title("Hello world")
st.write("Dasbor presensi mahasiswa - masih tahap uji coba")
st.set_page_config(
    page_title="SI Akademik - Mekatronika ATMI",
    page_icon="https://trmk.atmi.ac.id/wp-content/uploads/2023/06/atmi-logo-300x300.png",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------- CSS ----------
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 1.5rem; padding-bottom: 2rem; max-width: 480px;}

    .header-card {
        background: linear-gradient(135deg, #1a3c6e 0%, #0d1f3c 100%);
        border-radius: 16px;
        padding: 26px 20px 22px 20px;
        text-align: center;
        color: white;
        margin-bottom: 22px;
    }
    .header-card img {
        width: 64px;
        margin-bottom: 10px;
    }
    .header-card h1 {
        font-size: 17px;
        font-weight: 600;
        margin: 4px 0 2px 0;
        color: white;
    }
    .header-card p {
        font-size: 12.5px;
        color: #cfd8e8;
        margin: 0;
    }

    .menu-label {
        font-size: 13px;
        font-weight: 600;
        color: #6b7280;
        margin: 4px 2px 8px 2px;
        letter-spacing: 0.3px;
    }

    div.stButton > button,
    div[data-testid="stLinkButton"] > a {
        width: 100%;
        text-align: left;
        background-color: white;
        border: 1px solid #e2e6ed;
        border-radius: 14px;
        padding: 16px 18px;
        font-size: 15.5px;
        font-weight: 500;
        color: #1a3c6e;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        margin-bottom: 10px;
        transition: all 0.15s ease;
        text-decoration: none;
        display: flex;
        justify-content: flex-start;
    }
    div.stButton > button:hover,
    div[data-testid="stLinkButton"] > a:hover {
        border-color: #1a3c6e;
        box-shadow: 0 2px 8px rgba(26,60,110,0.15);
        color: #1a3c6e;
    }
    div.stButton > button:active {
        background-color: #f0f4fa;
    }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="header-card">
    <img src="https://trmk.atmi.ac.id/wp-content/uploads/2023/06/logoatmiWARNA.png" />
    <h1>Sistem Informasi Akademik</h1>
    <p>Program Studi Mekatronika &middot; Politeknik ATMI Surakarta</p>
</div>
""", unsafe_allow_html=True)

# ---------- MENU ----------
st.markdown('<div class="menu-label">MENU UTAMA</div>', unsafe_allow_html=True)
st.link_button(
    "📝  Input MKL",
    "https://script.google.com/a/macros/atmi.ac.id/s/AKfycbyJGN50wnNe8k0b1u9xj8XZoNXScqxrYVeJ1U4bg-z_JQbo_t-XRzHZyqe5b09YP-Co/exec",
    use_container_width=True,
)
st.link_button(
    "📊  Rekap Aktivitas Saya",
    "https://script.google.com/macros/s/AKfycbw4HixjQIhR94SOWa6iBztLFFB1fX3AF0IgAwVQyPscH_uqnYSWrxYyKklHnw-7LbKt/exec",
    use_container_width=True,
)
st.link_button(
    "📢  Info Mekatro",
    "https://trmk.atmi.ac.id",
    use_container_width=True,
)
