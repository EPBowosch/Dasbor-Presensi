import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MECHATRONICS INFORMATION SYSTEM",
    page_icon="https://trmk.atmi.ac.id/wp-content/uploads/2023/06/atmi-logo-300x300.png",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------- CSS ----------
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebarNav"] {display: none;}
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

    /* ---- Kartu menu dengan ikon (untuk link eksternal) ---- */
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
        cursor: pointer;
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

    /* ---- st.page_link umum (menu utama) ---- */
    div[data-testid="stPageLink"] {
        background-color: white !important;
        border: 1px solid #e2e6ed;
        border-radius: 14px;
        padding: 12px 16px;
        margin-bottom: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    div[data-testid="stPageLink"] * {
        color: #1a3c6e !important;
        fill: #1a3c6e !important;
    }
    div[data-testid="stPageLink"] p {
        font-size: 15px;
        font-weight: 600;
        margin: 0;
    }
    div[data-testid="stPageLink"]:hover {
        border-color: #1a3c6e;
        box-shadow: 0 2px 10px rgba(26,60,110,0.15);
    }

    /* ---- Tombol "Sebagai Mahasiswa" & "Sebagai Instruktur" (st.button), gaya seragam ---- */
    /* Nilai pixel di bawah ini bisa kamu tuning manual sampai pas */
    div[data-testid="column"]:nth-of-type(1) button {
        background-color: #e8f0fe !important;
        border: 1px solid transparent !important;
        border-radius: 12px !important;
        height: 58px !important;
        width: 100% !important;
        padding: 4px 8px !important;
        color: #1a3c6e !important;
        font-size: 13px !important;
        font-weight: 700 !important;
        line-height: 1.3 !important;
        white-space: pre-line !important;
    }
    div[data-testid="column"]:nth-of-type(1) button:hover {
        border-color: #1a3c6e !important;
        box-shadow: 0 2px 8px rgba(26,60,110,0.15);
        color: #1a3c6e !important;
    }
    div[data-testid="column"]:nth-of-type(1) button p {
        color: #1a3c6e !important;
        font-size: 13px !important;
        font-weight: 700 !important;
        line-height: 1.3 !important;
        margin: 0 !important;
    }

    div[data-testid="column"]:nth-of-type(2) button {
        background-color: #eafaf0 !important;
        border: 1px solid transparent !important;
        border-radius: 12px !important;
        height: 58px !important;
        width: 100% !important;
        padding: 4px 8px !important;
        color: #1a7a4c !important;
        font-size: 13px !important;
        font-weight: 700 !important;
        line-height: 1.3 !important;
        white-space: pre-line !important;
    }
    div[data-testid="column"]:nth-of-type(2) button:hover {
        border-color: #1a7a4c !important;
        box-shadow: 0 2px 8px rgba(26,122,76,0.15);
        color: #1a7a4c !important;
    }
    div[data-testid="column"]:nth-of-type(2) button p {
        color: #1a7a4c !important;
        font-size: 13px !important;
        font-weight: 700 !important;
        line-height: 1.3 !important;
        margin: 0 !important;
    }

    /* ---- Container MKL ---- */
    .mkl-container {
        background-color: white;
        border: 1px solid #e2e6ed;
        border-radius: 14px;
        padding: 18px 16px 8px 16px;
        margin-bottom: 8px;
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
</style>
""", unsafe_allow_html=True)

# ---------- INJEKSI JAVASCRIPT GLOBAL UNTUK FALLBACK (khusus link EKSTERNAL) ----------
components.html("""
<script>
    window.parent.document.addEventListener('click', function(e) {
        var card = e.target.closest('.mkl-btn, .menu-card');
        if (!card) return;
        if (!card.hasAttribute('data-url')) return;

        var targetUrl = card.getAttribute('data-url');
        var fallbackUrl = card.getAttribute('data-fallback');
        if (!targetUrl) return;

        e.preventDefault();
        e.stopPropagation();

        if (!targetUrl.includes('script.google.com')) {
            window.parent.window.location.href = targetUrl;
            return;
        }

        var targetWindow = window.parent.window.open('about:blank', '_blank');
        if(!targetWindow) {
            alert('Mohon izinkan pop-up pada peramban Anda untuk membuka menu.');
            return;
        }

        var isResolved = false;
        var timeout = setTimeout(function() {
            if (!isResolved) {
                isResolved = true;
                targetWindow.close();
                window.parent.window.location.href = fallbackUrl;
            }
        }, 4500);

        fetch(targetUrl, { mode: 'no-cors', cache: 'no-store' })
            .then(function() {
                if (!isResolved) {
                    isResolved = true;
                    clearTimeout(timeout);
                    targetWindow.location.href = targetUrl;
                }
            })
            .catch(function() {
                if (!isResolved) {
                    isResolved = true;
                    clearTimeout(timeout);
                    targetWindow.close();
                    window.parent.window.location.href = fallbackUrl;
                }
            });
    }, true);
</script>
""", height=0, width=0)

# ---------- HEADER ----------
st.markdown("""
<div class="header-card">
    <img src="https://trmk.atmi.ac.id/wp-content/uploads/2023/06/logoatmiWARNA.png" />
    <h1>Rumpun Prodi Mekatronika</h1>
    <p>&middot; Politeknik ATMI Surakarta</p>
</div>
""", unsafe_allow_html=True)

FALLBACK_PAGE = "/Petunjuk"

# ---------- CONTAINER MKL (Mahasiswa -> internal MKL.py, Instruktur -> Apps Script) ----------
url_mkl_instruktur = "https://accounts.google.com/AccountChooser?continue=https://script.google.com/a/macros/atmi.ac.id/s/AKfycbyjhCOW6svsWOtVkjtL3a1kqC2lPzQ7b8D9TMnR-LHNrAgirbwTtJEI7QzbKguuS7NJ/exec"

st.markdown("""
<div class="mkl-container">
    <p class="mkl-title">Pencatatan Minus, Kompen, dan Lembur (MKL)</p>
    <p class="mkl-sub">Pilih peran Anda untuk melanjutkan</p>
</div>
""", unsafe_allow_html=True)

col_mhs, col_instruktur = st.columns(2)
with col_mhs:
    if st.button("🧑‍🎓\n\nSebagai Mahasiswa", key="btn_mhs", use_container_width=True):
        st.switch_page("pages/MKL.py")
with col_instruktur:
    if st.button("🧑‍🏫\n\nSebagai Instruktur", key="btn_instruktur", use_container_width=True):
        components.html(f"""
        <script>
            (function() {{
                var targetUrl = "{url_mkl_instruktur}";
                var fallbackUrl = "{FALLBACK_PAGE}";
                var targetWindow = window.parent.window.open('about:blank', '_blank');
                if (!targetWindow) {{
                    alert('Mohon izinkan pop-up pada peramban Anda untuk membuka menu.');
                }} else {{
                    var isResolved = false;
                    var timeout = setTimeout(function() {{
                        if (!isResolved) {{
                            isResolved = true;
                            targetWindow.close();
                            window.parent.window.location.href = fallbackUrl;
                        }}
                    }}, 4500);
                    fetch(targetUrl, {{ mode: 'no-cors', cache: 'no-store' }})
                        .then(function() {{
                            if (!isResolved) {{
                                isResolved = true;
                                clearTimeout(timeout);
                                targetWindow.location.href = targetUrl;
                            }}
                        }})
                        .catch(function() {{
                            if (!isResolved) {{
                                isResolved = true;
                                clearTimeout(timeout);
                                targetWindow.close();
                                window.parent.window.location.href = fallbackUrl;
                            }}
                        }});
                }}
            }})();
        </script>
        """, height=0, width=0)

st.markdown("<div style='margin-bottom: 18px;'></div>", unsafe_allow_html=True)

# ---------- MENU ----------
st.markdown('<div class="menu-label">MENU UTAMA</div>', unsafe_allow_html=True)

menu_items = [
    {
        "title": "Perijinan Mahasiswa",
        "sub": "Ajukan izin terencana, sakit, dan tugas luar",
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
        "url": "https://accounts.google.com/AccountChooser?continue=https://script.google.com/macros/s/AKfycbxtEoTgpp_yB4sYydJyekv52E_EcDXS1ekaU8EyVFDbLQG7LXNPgNMYm0yhjgdJADdw/exec",
        "bg": "#eafaf1",
        "color": "#1a7a4c",
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
        "icon": '''<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 16">
            <path d="M13 2.5a1.5 1.5 0 0 1 3 0v11a1.5 1.5 0 0 1-3 0v-.214c-2.162-1.241-4.49-1.843-6.912-2.083l.405 2.712A1 1 0 0 1 5.51 15.1h-.548a1 1 0 0 1-.916-.599l-1.85-3.446a.32.32 0 0 0-.32-.192l.014.008a13.5 13.5 0 0 0-.15-.028 2.5 2.5 0 0 1 .217-4.978A61.94 61.94 0 0 0 8.078 5.83c1.986-.399 3.987-.977 5.922-1.727V2.5zm1 0v11a.5.5 0 0 0 1 0v-11a.5.5 0 0 0-1 0zM3.088 6.905a1.5 1.5 0 0 0-.132 2.995z"/>
        </svg>''',
    },
    {
        "title": "Petunjuk",
        "sub": "Halaman tidak bisa dibuka? Coba langkah ini",
        "url": "/Petunjuk",
        "bg": "#f1f2f6",
        "color": "#57606f",
        "icon": '''<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 16">
            <path d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 1 8 0a8 8 0 0 1 0 16z"/>
            <path d="M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z"/>
        </svg>''',
    },
    {
        "title": "Presensi",
        "sub": "Rekam kehadiran Anda hari ini",
        "url": "/Presensi",
        "bg": "#eef2ff",
        "color": "#4338ca",
        "icon": '''<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 16">
            <path d="M11 6.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1z"/>
            <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V4H1z"/>
        </svg>''',
    },
    {
        "title": "Aktivitas",
        "sub": "Riwayat aktivitas per pertemuan",
        "url": "/Aktivitas",
        "bg": "#fef2f2",
        "color": "#b91c1c",
        "icon": '''<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 16">
            <path d="M8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71V3.5z"/>
            <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm7-8A7 7 0 1 1 1 8a7 7 0 0 1 14 0z"/>
        </svg>''',
    },
]

# Pemetaan url internal -> path file asli di folder pages/
PAGE_MAP = {
    "/Input_MKL": "pages/1_Input_MKL.py",
    "/Petunjuk": "pages/1_Petunjuk.py",
    "/Presensi": "pages/2_Presensi.py",
    "/Aktivitas": "pages/3_Aktivitas.py",
}

for item in menu_items:
    if item["url"].startswith("/"):
        # Halaman internal -> st.page_link (aman dari batasan sandbox iframe)
        page_path = PAGE_MAP.get(item["url"])
        if page_path:
            st.page_link(page_path, label=f"{item['title']} — {item['sub']}", icon="📋")
        else:
            st.warning(f"Path untuk {item['url']} belum dipetakan di PAGE_MAP.")
    else:
        # Halaman eksternal (Apps Script, dll) -> tetap pakai card HTML + JS
        st.markdown(f"""
        <div data-url="{item['url']}" data-fallback="{FALLBACK_PAGE}" class="menu-card">
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
        </div>
        """, unsafe_allow_html=True)
