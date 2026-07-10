import streamlit as st

st.set_page_config(
    page_title="SIPMAS",
    page_icon="https://trmk.atmi.ac.id/wp-content/uploads/2023/06/atmi-logo-300x300.png",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("Sistem Informasi Praktikum Mekatronika ATMI")
st.write("dasbor sementara")

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
        margin: 4px 2px 10px 2px;
        letter-spacing: 0.3px;
    }

    /* ---- Kartu menu dengan ikon ---- */
    .menu-card {
        display: flex;
        align-items: center;
        gap: 14px;
        width: 100%;
        background-color: white;
        border: 1px solid #e2e6ed;
        border-radius: 14px;
        padding: 14px 16px;
        margin-bottom: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        text-decoration: none;
        transition: all 0.15s ease;
    }
    .menu-card:hover {
        border-color: #1a3c6e;
        box-shadow: 0 2px 10px rgba(26,60,110,0.15);
        transform: translateY(-1px);
    }
    .menu-icon {
        flex-shrink: 0;
        width: 42px;
        height: 42px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .menu-icon svg {
        width: 22px;
        height: 22px;
    }
    .menu-text {
        flex-grow: 1;
    }
    .menu-text .menu-title {
        font-size: 15px;
        font-weight: 600;
        color: #1a3c6e;
        margin: 0;
    }
    .menu-text .menu-sub {
        font-size: 12px;
        color: #8792a2;
        margin: 1px 0 0 0;
    }
    .menu-arrow {
        flex-shrink: 0;
        color: #c2c9d6;
    }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="header-card">
    <img src="https://trmk.atmi.ac.id/wp-content/uploads/2023/06/logoatmiWARNA.png" />
    <h1>Rumpun Prodi Mekatronika</h1>
    <p>&middot; Politeknik ATMI Surakarta</p>
</div>
""", unsafe_allow_html=True)

# ---------- MENU ----------
st.markdown('<div class="menu-label">MENU UTAMA</div>', unsafe_allow_html=True)

menu_items = [
    {
        "title": "Input MKL",
        "sub": "Catat kegiatan praktikum harian",
        "url": "https://accounts.google.com/Logout?continue=https://script.google.com/a/macros/atmi.ac.id/s/AKfycbyJGN50wnNe8k0b1u9xj8XZoNXScqxrYVeJ1U4bg-z_JQbo_t-XRzHZyqe5b09YP-Co/exec",
        "bg": "#e8f0fe",
        "color": "#1a3c6e",
        # ikon pensil/dokumen (Bootstrap Icons: pencil-square)
        "icon": '''<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 16">
            <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
            <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
        </svg>''',
    },
    {
        "title": "Rekap Aktivitas Saya",
        "sub": "Lihat ringkasan dan riwayat aktivitas",
        "url": "https://accounts.google.com/Logout?continue=https://script.google.com/a/macros/atmi.ac.id/s/AKfycbxKybxN1nlYBAGgb1btLXxJm_oqjmpabag__gDJLaBgknphvldsSmRWOg6zfaCVgJLu/exec",
        "bg": "#eafaf1",
        "color": "#1a7a4c",
        # ikon grafik batang (Bootstrap Icons: bar-chart-line)
        "icon": '''<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 16">
            <path d="M11 2a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v13h1.5a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1H2v-3a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3h1V9a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v6h1V2z"/>
        </svg>''',
    },
    {
        "title": "Info Mekatro",
        "sub": "Berita dan pengumuman terbaru",
        "url": "https://trmk.atmi.ac.id",
        "bg": "#fdf1e7",
        "color": "#b5651d",
        # ikon megaphone (Bootstrap Icons: megaphone)
        "icon": '''<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 16">
            <path d="M13 2.5a1.5 1.5 0 0 1 3 0v11a1.5 1.5 0 0 1-3 0v-.214c-2.162-1.241-4.49-1.843-6.912-2.083l.405 2.712A1 1 0 0 1 5.51 15.1h-.548a1 1 0 0 1-.916-.599l-1.85-3.446a.32.32 0 0 0-.32-.192l.014.008a13.5 13.5 0 0 0-.15-.028 2.5 2.5 0 0 1 .217-4.978A61.94 61.94 0 0 0 8.078 5.83c1.986-.399 3.987-.977 5.922-1.727V2.5zm1 0v11a.5.5 0 0 0 1 0v-11a.5.5 0 0 0-1 0zM3.088 6.905a1.5 1.5 0 0 0-.132 2.995z"/>
        </svg>''',
    },
]

for item in menu_items:
    st.markdown(f"""
    <a href="{item['url']}" target="_blank" class="menu-card">
        <div class="menu-icon" style="background-color:{item['bg']}; color:{item['color']};">
            {item['icon']}
        </div>
        <div class="menu-text">
            <p class="menu-title">{item['title']}</p>
            <p class="menu-sub">{item['sub']}</p>
        </div>
        <div class="menu-arrow">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"/>
            </svg>
        </div>
    </a>
    """, unsafe_allow_html=True)
