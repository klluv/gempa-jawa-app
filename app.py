import streamlit as st
import streamlit.components.v1 as components
import os

# ---------------------------------------------------------
# KONFIGURASI HALAMAN STREAMLIT
# ---------------------------------------------------------
st.set_page_config(
    page_title="Digital Storytelling: Gempa Bumi Pulau Jawa",
    page_icon="🌋",
    layout="centered"
)

# Kustomisasi Tampilan Sederhana
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1E3C72;
        font-weight: bold;
    }
    .sub-title {
        text-align: center;
        color: #555;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER & PENGANTAR (DIGITAL STORYTELLING)
# ---------------------------------------------------------
st.markdown("<h1 class='main-title'>Mengapa Pulau Jawa Sering Bergoyang?</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'><i>Digital Storytelling dalam Geologi: Mengubah Data Kebumian Menjadi Cerita yang Dipahami Masyarakat</i></p>", unsafe_allow_html=True)

st.write("""
Pulau Jawa terletak di atas batas lempeng aktif tempat **Lempeng Indo-Australia** menunjam ke bawah **Lempeng Eurasia**. 
Interaksi tektonik ini memicu aktivitas kegempaan yang berkelanjutan. Menggunakan data historis USGS dari periode **2021 hingga 2026**, 
mari kita jelajahi pola kejadian gempa di Pulau Jawa melalui 4 sudut pandang visualisasi data.
""")

st.divider()

# Fungsi Pembantu untuk Mengakses File HTML
def load_html_component(file_path, height=480):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        components.html(html_content, height=height, scrolling=True)
    else:
        st.error(f"File {file_path} tidak ditemukan. Pastikan file ada di folder 'visualisasi/'.")

# ---------------------------------------------------------
# BAB 1: GEMPA PER TAHUN
# ---------------------------------------------------------
st.header("1. Frekuensi Kejadian Gempa Bumi per Tahun")
st.write("""
Apakah jumlah kejadian gempa mengalami peningkatan dari tahun ke tahun? 
Grafik di bawah ini menggambarkan dinamika jumlah gempa bumi yang tercatat di wilayah Jawa selama rentang tahun 2021 hingga 2026.
""")

load_html_component("visualisasi/gempa_per_tahun.html", height=480)

st.divider()

# ---------------------------------------------------------
# BAB 2: HISTOGRAM MAGNITUDO
# ---------------------------------------------------------
st.header("2. Seberapa Kuat Gempa yang Terjadi?")
st.write("""
Sebagian besar gempa bumi yang terjadi berada pada rentang **magnitudo kecil hingga sedang** ($M < 5.0$). 
Gempa dengan skala sedang hingga besar ($M \\ge 5.0$) lebih jarang terjadi, namun memiliki potensi dampak kerusakan yang jauh lebih signifikan di pemukiman.
""")

load_html_component("visualisasi/histogram_magnitudo.html", height=480)

st.divider()

# ---------------------------------------------------------
# BAB 3: DISTRIBUSI KEDALAMAN
# ---------------------------------------------------------
st.header("3. Gempa Dangkal vs Gempa Dalam")
st.write("""
Kedalaman pusat gempa (hiposentrum) sangat menentukan tingkat getaran yang dirasakan di permukaan. 
Gempa bumi **dangkal** ($< 70\\text{ km}$) cenderung berdampak lebih merusak pada bangunan warga jika dibandingkan dengan gempa **menengah** maupun **dalam**.
""")

# Jika file kedalaman Anda berupa HTML:
load_html_component("visualisasi/distribusi_kedalaman.html", height=480)

# Catatan: Jika file kedalaman Anda dalam format PNG, gunakan perintah di bawah ini (hapus tanda # pada 2 baris di bawah):
# if os.path.exists("visualisasi/distribusi_kedalaman.png"):
#     st.image("visualisasi/distribusi_kedalaman.png", use_column_width=True)

st.divider()

# ---------------------------------------------------------
# BAB 4: DENSITY MAP (PETA KEPADATAN)
# ---------------------------------------------------------
st.header("4. Peta Kepadatan Titik Gempa (Density Map)")
st.write("""
Di mana saja wilayah dengan konsentrasi kegempaan paling padat? 
Peta interaktif di bawah ini memperlihatkan kluster kebencanaan di sepanjang wilayah selatan Jawa (zona subduksi) dan sesar-sesar aktif di daratan.
""")

load_html_component("visualisasi/density_map.html", height=580)

st.divider()

# ---------------------------------------------------------
# PENUTUP & MITIGASI
# ---------------------------------------------------------
st.subheader("💡 Kesiapsiagaan & Mitigasi Bencana")
st.info("""
**Pesan Utama:** Data menunjukkan bahwa gempa adalah fenomena alamiah yang rutin terjadi di Pulau Jawa. 
Memahami pola kegempaan membantu masyarakat dan pemerintah daerah untuk meningkatkan literasi kebencanaan, menerapkan standar bangunan tahan gempa, dan menyusun rencana jalur evakuasi mandiri.
""")

st.caption("Sumber Data: USGS Earthquakes Search API | Proyek Digital Storytelling Geologi")