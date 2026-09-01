import streamlit as st

st.set_page_config(
    page_title="Petunjuk - MECHATRONICS INFORMATION SYSTEM",
    page_icon="https://trmk.atmi.ac.id/wp-content/uploads/2023/06/atmi-logo-300x300.png",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------- CSS (konsisten dengan halaman utama) ----------
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 1.5rem; padding-bottom: 2rem; max-width: 560px;}

    .header-card {
        background: linear-gradient(135deg, #1a3c6e 0%, #0d1f3c 100%);
        border-radius: 16px;
        padding: 26px 20px 22px 20px;
        text-align: center;
        color: white;
        margin-bottom: 22px;
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

    .back-link {
        display: inline-block;
        margin-bottom: 16px;
        font-size: 13px;
        color: #6b7280;
        text-decoration: none;
    }

    .section-label {
        font-size: 13px;
        font-weight: 600;
        color: #6b7280;
        margin: 22px 2px 10px 2px;
        letter-spacing: 0.3px;
        text-transform: uppercase;
    }

    .problem-card {
        background: #fdecea;
        border: 1px solid #f5c6c2;
        border-radius: 14px;
        padding: 16px 18px;
        margin-bottom: 16px;
    }
    .problem-card b { color: #c0392b; }

    .step-card {
        background: white;
        border: 1px solid #e2e6ed;
        border-radius: 14px;
        padding: 16px 18px;
        margin-bottom: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .step-num {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 26px;
        height: 26px;
        border-radius: 50%;
        background: #1a3c6e;
        color: white;
        font-size: 13px;
        font-weight: 700;
        margin-right: 8px;
        flex-shrink: 0;
    }
    .step-title {
        font-size: 15px;
        font-weight: 600;
        color: #1a3c6e;
        display: flex;
        align-items: center;
        margin-bottom: 6px;
    }
    .step-desc {
        font-size: 13.5px;
        color: #4b5563;
        line-height: 1.5;
        margin-left: 34px;
    }

    .note-card {
        background: #fff8e6;
        border: 1px solid #f2dca0;
        border-radius: 12px;
        padding: 14px 16px;
        font-size: 13px;
        color: #7a5b00;
        margin-top: 6px;
        margin-bottom: 20px;
        line-height: 1.5;
    }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="header-card">
    <h1>Petunjuk Mengatasi Halaman Tidak Bisa Dibuka</h1>
    <p>Rumpun Prodi Mekatronika &middot; Politeknik ATMI Surakarta</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<a class="back-link" href="/" target="_self">&larr; Kembali ke menu utama</a>', unsafe_allow_html=True)

# ---------- MASALAH ----------
st.markdown("""
<div class="problem-card">
    <b>Gejala:</b> Setelah klik menu (misalnya "MKL Instruktur" atau "Rekap Aktivitas"),
    muncul pesan <i>"Tidak dapat mendeteksi akun Google Anda"</i> atau halaman gagal
    terbuka &mdash; padahal HP sudah login dengan akun email atmi (<b>@atmi.ac.id</b>).
    Ini paling sering terjadi di HP (Chrome Android), jarang di laptop/desktop.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="note-card">
    Penyebabnya bukan akun email atmi kamu salah &mdash; ini soal setelan cookie
    di browser HP. Google membuka halaman ini lewat sebuah "jendela tersembunyi"
    di dalam halaman (disebut iframe), dan sebagian HP memblokir Google membaca
    sesi login di jendela tersembunyi itu. Ikuti langkah di bawah sesuai urutan.
</div>
""", unsafe_allow_html=True)

# ---------- LANGKAH 1 ----------
st.markdown('<div class="section-label">Coba dulu &mdash; paling cepat</div>', unsafe_allow_html=True)

st.markdown("""
<div class="step-card">
    <div class="step-title"><span class="step-num">1</span>Pastikan akun email atmi jadi akun utama Chrome</div>
    <div class="step-desc">
        Buka Chrome &rarr; ketuk titik tiga (pojok kanan atas) &rarr; lihat foto/nama
        akun yang tertera di bagian atas menu. Kalau bukan akun email atmi
        (<b>...@atmi.ac.id</b>) yang aktif di situ, ketuk foto akun tersebut lalu
        pilih atau tambahkan akun email atmi, dan jadikan itu akun utama Chrome
        di HP tersebut. Setelah itu buka lagi menunya &mdash; biasanya langsung berhasil.
    </div>
</div>

<div class="step-card">
    <div class="step-title"><span class="step-num">2</span>Tutup dan buka ulang Chrome</div>
    <div class="step-desc">
        Kadang sesi login lama masih "menyangkut". Tutup Chrome sepenuhnya
        (bukan cuma pindah aplikasi), buka lagi, lalu coba menu yang sama.
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- LANGKAH 2 ----------
st.markdown('<div class="section-label">Kalau langkah 1 belum berhasil</div>', unsafe_allow_html=True)

st.markdown("""
<div class="step-card">
    <div class="step-title"><span class="step-num">3</span>Pastikan tidak sedang di mode Incognito</div>
    <div class="step-desc">
        Tab Penyamaran/Incognito di Chrome selalu memblokir sesi seperti ini.
        Pastikan dibuka di tab biasa.
    </div>
</div>

<div class="step-card">
    <div class="step-title"><span class="step-num">4</span>Buka lewat Chrome, bukan aplikasi lain</div>
    <div class="step-desc">
        Kalau link diklik dari dalam WhatsApp, Gmail, atau aplikasi lain, ketuk
        titik tiga di kanan atas layar tersebut lalu pilih "Buka di Chrome" /
        "Open in browser" dulu sebelum mengakses menu.
    </div>
</div>

<div class="step-card">
    <div class="step-title"><span class="step-num">5</span>Izinkan cookie pihak ketiga untuk domain Google</div>
    <div class="step-desc">
        Buka <code>chrome://settings/privacy</code> di Chrome HP &rarr; cari
        "Third-party cookies" / "Cookie pihak ketiga" &rarr; pastikan tidak
        di-set "Blokir semua cookie pihak ketiga". Kalau memungkinkan, izinkan
        khusus untuk *.google.com dan *.googleusercontent.com.
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- MASIH GAGAL ----------
st.markdown('<div class="section-label">Masih belum bisa juga?</div>', unsafe_allow_html=True)

st.markdown("""
<div class="step-card">
    <div class="step-title"><span class="step-num">6</span>Hubungi admin sistem</div>
    <div class="step-desc">
        Kirim screenshot pesan errornya, sebutkan tipe HP dan versi Chrome
        (Chrome &rarr; titik tiga &rarr; Settings &rarr; About Chrome), serta menu
        mana yang gagal dibuka. Ini membantu admin melacak penyebabnya lebih cepat.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<a class="back-link" href="/" target="_self">&larr; Kembali ke menu utama</a>', unsafe_allow_html=True)
