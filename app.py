import streamlit as st

st.set_page_config(
    page_title="MECHATRONICS INFORMATION SYSTEM",
    page_icon="https://trmk.atmi.ac.id/wp-content/uploads/2023/06/atmi-logo-300x300.png",
    layout="centered",
    initial_sidebar_state="collapsed",
)

#st.title("Sistem Informasi Praktikum Mekatronika ATMI")
#st.write("dasbor sementara")

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

    /* ---- Container MKL dengan 2 tombol proporsional ---- */
    .mkl-container {
        background-color: white;
        border: 1px solid #e2e6ed;
        border-radius: 14px;
        padding: 18px 16px;
        margin-bottom: 18px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        text-align: center;
    }
    .mkl-title {
        font-size: 15px;
        font-weight: 700;
        color: #1a3c6e;
        margin: 0 0 4px 0;
    }
    .mkl-sub {
        font-size: 12px;
        color: #8792a2;
        margin: 0 0 14px 0;
    }
    .mkl-buttons {
        display: flex;
        gap: 10px;
    }
    .mkl-btn {
        flex: 1 1 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 4px;
        padding: 14px 8px;
        border-radius: 12px;
        text-decoration: none;
        font-size: 13.5px;
        font-weight: 700;
        transition: all 0.15s ease;
        border: 1px solid transparent;
    }
    .mkl-btn:hover {
        transform: translateY(-1px);
    }
    .mkl-btn svg {
        width: 22px;
        height: 22px;
    }
    .mkl-btn.mahasiswa {
        background-color: #e8f0fe;
        color: #1a3c6e;
    }
    .mkl-btn.mahasiswa:hover {
        border-color: #1a3c6e;
        box-shadow: 0 2px 8px rgba(26,60,110,0.15);
    }
    .mkl-btn.instruktur {
        background-color: #eafaf0;
        color: #1a7a4c;
    }
    .mkl-btn.instruktur:hover {
        border-color: #1a7a4c;
        box-shadow: 0 2px 8px rgba(26,122,76,0.15);
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

# ---------- CONTAINER MKL (2 TOMBOL) ----------
st.markdown("""
<div class="mkl-container">
    <p class="mkl-title">Pencatatan Minus, Kompen, dan Lembur (MKL)</p>
    <p class="mkl-sub">Pilih peran Anda untuk melanjutkan</p>
    <div class="mkl-buttons">
        <a href="https://accounts.google.com/AccountChooser?continue=https://script.google.com/a/macros/atmi.ac.id/s/AKfycbyJGN50wnNe8k0b1u9xj8XZoNXScqxrYVeJ1U4bg-z_JQbo_t-XRzHZyqe5b09YP-Co/exec" target="_blank" class="mkl-btn mahasiswa">
            <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 16">
                <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664z"/>
            </svg>
            Sebagai Mahasiswa
        </a>
        <a href="https://accounts.google.com/AccountChooser?continue=https://script.google.com/a/macros/atmi.ac.id/s/AKfycbyjhCOW6svsWOtVkjtL3a1kqC2lPzQ7b8D9TMnR-LHNrAgirbwTtJEI7QzbKguuS7NJ/exec" target="_blank" class="mkl-btn instruktur">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
                <circle cx="12" cy="8" r="3.4" fill="currentColor" stroke="none" opacity="0.15"/>
                <circle cx="12" cy="8" r="3.4"/>
                <circle cx="9.7" cy="9.4" r="1.4"/>
                <circle cx="14.3" cy="9.4" r="1.4"/>
                <path d="M11.1 9.4h1.8"/>
                <path d="M8.3 9.1c-.7-.2-1.2-.2-1.7.1"/>
                <path d="M15.7 9.1c.7-.2 1.2-.2 1.7.1"/>
                <path d="M6 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/>
            </svg>
            Sebagai Instruktur
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- MENU ----------
st.markdown('<div class="menu-label">MENU UTAMA</div>', unsafe_allow_html=True)

menu_items = [
    {
        "title": "Perijinan Mahasiswa",
        "sub": "Ajukan izin terencana, sakit, dan tugas dinas",
        "url": "https://accounts.google.com/AccountChooser?continue=https://script.google.com/a/macros/atmi.ac.id/s/AKfycby-x1aUypHkd5xt2gfVoiRhBY7cyOWJBj-qW2EAZm3pIQl_zLXlSld02iX9IhmORY-l7Q/exec",
        "bg": "#fff4e6",
        "color": "#d97706",
        "icon": '''<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 16">
            <path d="M10 1.5v1a.5.5 0 0 0 .5.5H11A1.5 1.5 0 0 1 12.5 4.5v9A1.5 1.5 0 0 1 11 15H5A1.5 1.5 0 0 1 3.5 13.5v-9A1.5 1.5 0 0 1 5 3h.5a.5.5 0 0 0 .5-.5v-1A1.5 1.5 0 0 1 7.5 0h1A1.5 1.5 0 0 1 10 1.5zM7.5 1a.5.5 0 0 0-.5.5V2h2v-.5a.5.5 0 0 0-.5-.5h-1z"/>
            <path d="M10.854 7.146a.5.5 0 0 1 0 .708L8.207 10.5a.5.5 0 0 1-.707 0L6.146 9.146a.5.5 0 1 1 .708-.708l1 1 2.293-2.292a.5.5 0 0 1 .707 0z"/>
        </svg>''',
    },
    {
        "title": "Rekap Aktivitas Saya",
        "sub": "Lihat ringkasan dan riwayat aktivitas",
        "url": "https://accounts.google.com/AccountChooser?continue=https://script.google.com/a/macros/atmi.ac.id/s/AKfycbwdIJxFrLHp5pLP0wmYe7yqvlCJB6zEERexu7j02qWYmxUYY9vk6xxO2J-VLaQDZzpG/exec",
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
    {
        "title": "Petunjuk",
        "sub": "Halaman tidak bisa dibuka? Coba langkah ini",
        "url": "/Petunjuk",
        "target": "_self",
        "bg": "#f1f2f6",
        "color": "#57606f",
        # ikon tanda tanya (Bootstrap Icons: question-circle)
        "icon": '''<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z"/>
            <path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"/>
        </svg>''',
    },
]

for item in menu_items:
    target = item.get("target", "_blank")
    st.markdown(f"""
    <a href="{item['url']}" target="{target}" class="menu-card">
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
