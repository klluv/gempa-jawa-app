import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Digital Storytelling: Gempa Bumi Pulau Jawa",
    page_icon="🌋",
    layout="wide", # Menggunakan tampilan lebar
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    /* Mengatur background & font utama */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Styling Header Hero */
    .hero-container {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2.5rem 2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        color: #ffffff;
    }
    .hero-subtitle {
        font-size: 1.1rem;
        font-weight: 300;
        color: #e0e0e0;
    }
    
    /* Styling Card Narasi */
    .story-card {
        background-color: #ffffff;
        padding: 1.8rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
        border-left: 5px solid #1e3c72;
    }
    
    /* Custom divider line */
    hr {
        margin: 2rem 0;
        border: none;
        height: 1px;
        background-color: #e0e0e0;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://img.icons8.com/external-flaticons-lineal-color-flat-icons/64/external-earthquake-emergency-service-flaticons-lineal-color-flat-icons-2.png", width=80)
    st.title("Navigasi Cerita")
    st.markdown("Pilih bagian untuk langsung menuju topik:")
    
    st.markdown("""
    - [📌 Latar Belakang](#latar-belakang)
    - [📊 1. Frekuensi Per Tahun](#1-frekuensi-kejadian-gempa-bumi-per-tahun)
    - [📈 2. Skala Magnitudo](#2-seberapa-kuat-gempa-yang-terjadi)
    - [📉 3. Kedalaman Hiposentrum](#3-gempa-dangkal-vs-gempa-dalam)
    - [🗺️ 4. Peta Kepadatan](#4-peta-kepadatan-titik-gempa-density-map)
    - [💡 Kesimpulan & Mitigasi](#kesiapsiagaan-mitigasi-bencana)
    """)
    st.divider()
    st.info("**Metode Data:**\nData diambil dari API USGS Earthquakes dengan filter wilayah Pulau Jawa & sekitarnya ($M \\ge 2.5$).")

st.markdown("""
    <div class="hero-container">
        <div class="hero-title">Mengapa Pulau Jawa Sering Bergoyang?</div>
        <div class="hero-subtitle">Digital Storytelling Geologi: Mengubah Data Kebumian Menjadi Cerita yang Dipahami Masyarakat</div>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Rentang Waktu Data", value="2021 – 2026")
with col2:
    st.metric(label="Magnitudo Min.", value="2.5 M")
with col3:
    st.metric(label="Fokus Wilayah", value="Pulau Jawa")
with col4:
    st.metric(label="Sumber Data", value="USGS Global")

st.divider()

def load_html_component(file_path, height=500):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        components.html(html_content, height=height, scrolling=True)
    else:
        st.error(f"File `{file_path}` tidak ditemukan di folder `visualisasi/`.")

st.subheader("📌 Latar Belakang Tektonik")
st.write("""
Pulau Jawa berada di atas zona konvergensi lempeng aktif, tempat **Lempeng Indo-Australia** menunjam ke bawah **Lempeng Eurasia** dengan kecepatan sekitar 6–7 cm per tahun. 
Proses subduksi ini membentuk palung laut dangkal di selatan Jawa serta memicu pembentukan sesar-sesar aktif di daratan. Melalui data kegempaan 2021–2026, kita dapat mengenali karakteristik ancaman di sekitar kita.
""")

st.divider()

st.header("1. Frekuensi Kejadian Gempa Bumi per Tahun")
st.write("""
Apakah jumlah kejadian gempa mengalami peningkatan dari tahun ke tahun? 
Grafik di bawah menggambarkan dinamika frekuensi gempa bumi yang terekam di Jawa selama rentang 2021 hingga 2026.
""")

load_html_component("visualisasi/gempa_per_tahun.html", height=480)

st.divider()

st.header("2. Seberapa Kuat Gempa yang Terjadi?")
st.write("""
Sebagian besar gempa bumi yang terjadi berada pada rentang **magnitudo kecil hingga sedang** ($M < 5.0$). 
Gempa berskala sedang hingga besar ($M \\ge 5.0$) lebih jarang terjadi, namun memiliki potensi dampak kerusakan yang jauh lebih besar bagi infrastruktur pemukiman.
""")

load_html_component("visualisasi/histogram_magnitudo.html", height=480)

st.divider()

st.header("3. Gempa Dangkal vs Gempa Dalam")
st.write("""
Kedalaman pusat gempa (hiposentrum) sangat menentukan tingkat getaran yang dirasakan di permukaan. 
Gempa **dangkal** ($< 70\\text{ km}$) cenderung berdampak jauh lebih merusak di daratan jika dibandingkan dengan gempa **menengah** ($70-300\\text{ km}$) atau **dalam** ($> 300\\text{ km}$).
""")

load_html_component("visualisasi/distribusi_kedalaman.html", height=500)

st.divider()

st.header("4. Peta Kepadatan Titik Gempa (Density Map)")
st.write("""
Di mana saja titik konsentrasi kegempaan paling padat? 
Peta interaktif berbasis *heatmap* di bawah ini memperlihatkan kluster kebencanaan di sepanjang samudera selatan Jawa (zona subduksi) serta beberapa sesar aktif di daratan. *Gunakan mouse untuk zoom in/out.*
""")

load_html_component("visualisasi/density_map.html", height=580)

st.divider()

st.subheader("💡 Kesiapsiagaan & Mitigasi Bencana")
st.success("""
**Pesan Kunci untuk Masyarakat:** 
1. **Kenali Potensi:** Gempa adalah siklus alami Pulau Jawa yang tidak dapat dicegah, tetapi dampaknya bisa diminimalisir.
2. **Konstruksi Tahan Gempa:** Kerusakan terbesar saat gempa umumnya disebabkan oleh kegagalan struktur bangunan.
3. **Pahami Jalur Evakuasi:** Tentukan titik kumpul aman di sekitar rumah dan tempat kerja Anda.
""")

st.caption("Proyek Digital Storytelling Geologi | Data Source: USGS Earthquake Hazards Program")
