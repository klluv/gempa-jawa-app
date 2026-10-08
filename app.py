import math
import os
import random
import textwrap

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Digital Storytelling: Gempa Bumi Pulau Jawa",
    page_icon="🌋",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def html(block: str):
    """Render blok HTML tanpa indentasi (agar tidak dibaca sebagai code block markdown)."""
    cleaned = "\n".join(line.strip() for line in textwrap.dedent(block).splitlines())
    st.markdown(cleaned, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# STYLE
# ---------------------------------------------------------------------------
html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Public+Sans:wght@400;500;600&display=swap');

:root {
  --bg: #EEF2F4;
  --surface: #FFFFFF;
  --ink: #0B2433;
  --ink-soft: #3E5666;
  --sea: #1F7A8C;
  --sea-deep: #123B4F;
  --magma: #E4572E;
  --line: #D3DDE3;
}

.stApp { background: var(--bg); }
.stApp, .stApp p, .stApp li, .stApp label {
  font-family: 'Public Sans', system-ui, sans-serif;
  color: var(--ink);
}
.stApp h1, .stApp h2, .stApp h3 {
  font-family: 'Bricolage Grotesque', 'Public Sans', sans-serif;
  letter-spacing: -0.02em;
  color: var(--ink);
}

/* Sembunyikan chrome bawaan Streamlit */
#MainMenu, footer { visibility: hidden; }
[data-testid="stHeader"] { background: transparent; }
[data-testid="stToolbar"] { display: none; }

.block-container {
  max-width: 1080px;
  padding-top: 1.5rem;
  padding-bottom: 4rem;
}

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] { background: var(--ink); }
[data-testid="stSidebar"] * { color: #D5E3EA; }
.side-title {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: 1.35rem; font-weight: 700; color: #fff !important;
  margin: 0.5rem 0 0.25rem;
}
.side-sub { font-size: 0.88rem; color: #8FA9B8 !important; margin-bottom: 1.25rem; }
.side-nav a {
  display: block; padding: 0.55rem 0.8rem; margin-bottom: 2px;
  border-radius: 8px; text-decoration: none !important;
  font-size: 0.95rem; color: #D5E3EA !important;
  transition: background 0.15s ease;
}
.side-nav a:hover { background: rgba(255,255,255,0.09); }
.side-note {
  margin-top: 1.5rem; padding: 0.9rem 1rem; border-radius: 10px;
  background: rgba(255,255,255,0.07); font-size: 0.85rem; line-height: 1.5;
}
.side-note strong { color: #fff !important; }

/* ---------- Hero ---------- */
.hero {
  position: relative; overflow: hidden;
  background: linear-gradient(160deg, var(--sea-deep) 0%, var(--ink) 100%);
  border-radius: 20px;
  padding: 3.2rem 3rem 10rem;
  min-height: 380px;
}
.hero-title {
  position: relative; z-index: 1;
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: clamp(2.2rem, 5.2vw, 4rem);
  font-weight: 800; line-height: 1.02; letter-spacing: -0.03em;
  color: #fff !important; max-width: 14ch; margin: 0 0 1.1rem;
}
.stApp .hero h1.hero-title { color: #fff !important; }
.hero-sub {
  position: relative; z-index: 1;
  font-size: 1.08rem; line-height: 1.55;
  color: #E6F0F5 !important; max-width: 52ch; margin: 0;
}
.stApp .hero p.hero-sub { color: #E6F0F5 !important; }
.hero svg {
  position: absolute; left: 0; bottom: 0;
  width: 100%; height: 42%;
}
.hero svg path {
  fill: none; stroke: #FF8A5B; stroke-width: 2;
  stroke-linejoin: round; stroke-linecap: round;
  stroke-dasharray: 1; stroke-dashoffset: 0;
  animation: draw 4s cubic-bezier(.4,0,.2,1) 0.3s both;
}
@keyframes draw { from { stroke-dashoffset: 1; } to { stroke-dashoffset: 0; } }
@media (prefers-reduced-motion: reduce) { .hero svg path { animation: none; } }

/* ---------- Stat strip ---------- */
.stats {
  display: grid; grid-template-columns: repeat(4, 1fr);
  background: var(--surface); border: 1px solid var(--line);
  border-radius: 14px; margin: 1.25rem 0 3rem;
}
.stat { padding: 1.1rem 1.3rem; border-left: 1px solid var(--line); }
.stat:first-child { border-left: none; }
.stat-label { font-size: 0.82rem; color: var(--ink-soft); margin-bottom: 0.25rem; }
.stat-value {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: 1.35rem; font-weight: 700; color: var(--ink);
}
@media (max-width: 760px) {
  .stats { grid-template-columns: repeat(2, 1fr); }
  .stat:nth-child(3) { border-left: none; }
  .stat:nth-child(n+3) { border-top: 1px solid var(--line); }
  .hero { padding: 2.2rem 1.5rem 8rem; }
}

/* ---------- Bab cerita ---------- */
.anchor { position: relative; top: -70px; visibility: hidden; }
.chapter { display: flex; gap: 1.2rem; align-items: flex-start; margin: 0 0 1.1rem; }
.chapter-num {
  flex: none; width: 3rem; height: 3rem; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  background: var(--sea); color: #fff;
  font-family: 'Bricolage Grotesque', sans-serif; font-size: 1.25rem; font-weight: 700;
}
.chapter-title {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: clamp(1.5rem, 3vw, 2.1rem); font-weight: 700;
  line-height: 1.1; letter-spacing: -0.02em; margin: 0 0 0.6rem;
  color: var(--ink);
}
.chapter-text { font-size: 1.05rem; line-height: 1.65; color: var(--ink-soft); max-width: 68ch; margin: 0; }
.chapter-text strong { color: var(--ink); }
.chips { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.9rem; }
.chip {
  display: inline-flex; align-items: center; gap: 0.45rem;
  padding: 0.3rem 0.75rem; border-radius: 999px;
  background: var(--surface); border: 1px solid var(--line);
  font-size: 0.85rem; color: var(--ink);
}
.dot { width: 9px; height: 9px; border-radius: 50%; display: inline-block; }
.section-gap { height: 3.2rem; }

/* Bingkai grafik */
.stApp iframe {
  border: 1px solid var(--line);
  border-radius: 14px;
  background: #fff;
}

/* ---------- Latar belakang ---------- */
.lead {
  background: var(--surface); border: 1px solid var(--line);
  border-left: 5px solid var(--sea);
  border-radius: 14px; padding: 1.6rem 1.8rem;
}
.lead h2 { font-size: 1.7rem; margin: 0 0 0.6rem; }
.lead p { font-size: 1.05rem; line-height: 1.7; margin: 0; color: var(--ink-soft); }
.lead strong { color: var(--ink); }

/* ---------- Mitigasi ---------- */
.mitigation {
  background: linear-gradient(160deg, var(--sea-deep) 0%, var(--ink) 100%);
  border-radius: 20px; padding: 2.4rem 2.2rem;
}
.mitigation h2 { color: #fff !important; font-size: 1.9rem; margin: 0 0 0.4rem; }
.mitigation .intro { color: #B9CDD8; margin: 0 0 1.6rem; font-size: 1.02rem; }
.mit-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
.mit-item {
  padding: 1.2rem 1.3rem; border-radius: 12px;
  background: rgba(255,255,255,0.07);
  border-top: 3px solid #FF8A5B;
}
.mit-item h3 { color: #fff !important; font-size: 1.1rem; margin: 0 0 0.45rem; }
.mit-item p { color: #C9D9E2 !important; font-size: 0.97rem; line-height: 1.55; margin: 0; }
@media (max-width: 760px) { .mit-grid { grid-template-columns: 1fr; } }

.footer-note { text-align: center; color: var(--ink-soft); font-size: 0.85rem; margin-top: 2.5rem; }
</style>
""")


# ---------------------------------------------------------------------------
# KOMPONEN
# ---------------------------------------------------------------------------
def seismograph_svg() -> str:
    """Garis seismograf: tenang, lalu getaran besar yang meluruh."""
    rng = random.Random(11)
    n, width, mid = 300, 1200, 70
    pts = []
    for i in range(n):
        t = i / (n - 1)
        amp = 3.0
        if 0.28 <= t < 0.33:
            amp += 12
        if t >= 0.33:
            amp += 58 * math.exp(-(t - 0.33) * 7.5)
        y = mid + amp * math.sin(i * 2.3) * rng.uniform(0.45, 1.0)
        pts.append(f"{t * width:.1f},{y:.1f}")
    d = "M" + " L".join(pts)
    return (
        '<svg viewBox="0 0 1200 140" preserveAspectRatio="none" aria-hidden="true">'
        f'<path d="{d}" pathLength="1"/></svg>'
    )


def chapter(anchor: str, num: int, title: str, text: str, chips: str = ""):
    html(f"""
    <div class="anchor" id="{anchor}"></div>
    <div class="chapter">
      <div class="chapter-num">{num}</div>
      <div>
        <h2 class="chapter-title">{title}</h2>
        <p class="chapter-text">{text}</p>
        {chips}
      </div>
    </div>
    """)


def load_html_component(file_path: str, height: int = 500):
    full_path = os.path.join(BASE_DIR, file_path)
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            components.html(f.read(), height=height, scrolling=True)
    else:
        st.error(
            f"Grafik belum tampil: file `{file_path}` tidak ditemukan. "
            "Pastikan file ada di folder `visualisasi/` dan namanya sama persis."
        )


def gap():
    html('<div class="section-gap"></div>')


# ---------------------------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------------------------
with st.sidebar:
    html("""
    <div class="side-title">🌋 Navigasi cerita</div>
    <div class="side-sub">Pilih bagian untuk langsung menuju topik.</div>
    <div class="side-nav">
      <a href="#latar-belakang" target="_self">Latar belakang</a>
      <a href="#frekuensi" target="_self">1. Frekuensi per tahun</a>
      <a href="#magnitudo" target="_self">2. Skala magnitudo</a>
      <a href="#kedalaman" target="_self">3. Kedalaman hiposentrum</a>
      <a href="#peta" target="_self">4. Peta kepadatan</a>
      <a href="#mitigasi" target="_self">Kesimpulan dan mitigasi</a>
    </div>
    <div class="side-note">
      <strong>Metode data</strong><br>
      Data dari API USGS Earthquakes, difilter untuk wilayah Pulau Jawa dan sekitarnya dengan magnitudo minimal 2,5.
    </div>
    """)

# ---------------------------------------------------------------------------
# HERO + STATISTIK
# ---------------------------------------------------------------------------
html(f"""
<div class="hero">
  <h1 class="hero-title">Mengapa Pulau Jawa sering bergoyang?</h1>
  <p class="hero-sub">Digital storytelling geologi: mengubah data kebumian menjadi cerita yang mudah dipahami masyarakat.</p>
  {seismograph_svg()}
</div>
<div class="stats">
  <div class="stat"><div class="stat-label">Rentang waktu data</div><div class="stat-value">2021 – 2026</div></div>
  <div class="stat"><div class="stat-label">Magnitudo minimum</div><div class="stat-value">M 2,5</div></div>
  <div class="stat"><div class="stat-label">Fokus wilayah</div><div class="stat-value">Pulau Jawa</div></div>
  <div class="stat"><div class="stat-label">Sumber data</div><div class="stat-value">USGS Global</div></div>
</div>
""")

# ---------------------------------------------------------------------------
# LATAR BELAKANG
# ---------------------------------------------------------------------------
html("""
<div class="anchor" id="latar-belakang"></div>
<div class="lead">
  <h2>Latar belakang tektonik</h2>
  <p>
    Pulau Jawa berada di atas zona konvergensi lempeng aktif, tempat <strong>Lempeng Indo-Australia</strong>
    menunjam ke bawah <strong>Lempeng Eurasia</strong> dengan kecepatan sekitar 6–7 cm per tahun.
    Proses subduksi ini membentuk palung laut dangkal di selatan Jawa dan memicu sesar-sesar aktif di daratan.
    Lewat data kegempaan 2021–2026, kita bisa mengenali karakter ancaman di sekitar kita.
  </p>
</div>
""")

gap()

# ---------------------------------------------------------------------------
# BAB 1
# ---------------------------------------------------------------------------
chapter(
    "frekuensi", 1, "Frekuensi kejadian gempa bumi per tahun",
    "Apakah jumlah gempa meningkat dari tahun ke tahun? Grafik di bawah menunjukkan "
    "dinamika frekuensi gempa yang terekam di Jawa selama 2021 hingga 2026.",
)
load_html_component("visualisasi/gempa_per_tahun.html", height=480)

gap()

# ---------------------------------------------------------------------------
# BAB 2
# ---------------------------------------------------------------------------
chapter(
    "magnitudo", 2, "Seberapa kuat gempa yang terjadi?",
    "Sebagian besar gempa berada pada rentang <strong>magnitudo kecil hingga sedang</strong>. "
    "Gempa berskala sedang hingga besar lebih jarang terjadi, tetapi berpotensi merusak "
    "infrastruktur pemukiman jauh lebih parah.",
    chips="""
    <div class="chips">
      <span class="chip"><span class="dot" style="background:#1F7A8C"></span>Kecil hingga sedang: M &lt; 5,0</span>
      <span class="chip"><span class="dot" style="background:#E4572E"></span>Sedang hingga besar: M ≥ 5,0</span>
    </div>
    """,
)
load_html_component("visualisasi/histogram_magnitudo.html", height=480)

gap()

# ---------------------------------------------------------------------------
# BAB 3
# ---------------------------------------------------------------------------
chapter(
    "kedalaman", 3, "Gempa dangkal vs gempa dalam",
    "Kedalaman pusat gempa (hiposentrum) menentukan seberapa kuat getaran terasa di permukaan. "
    "Gempa <strong>dangkal</strong> cenderung jauh lebih merusak di daratan dibandingkan gempa "
    "<strong>menengah</strong> atau <strong>dalam</strong>.",
    chips="""
    <div class="chips">
      <span class="chip"><span class="dot" style="background:#E4572E"></span>Dangkal: kurang dari 70 km</span>
      <span class="chip"><span class="dot" style="background:#1F7A8C"></span>Menengah: 70–300 km</span>
      <span class="chip"><span class="dot" style="background:#123B4F"></span>Dalam: lebih dari 300 km</span>
    </div>
    """,
)
load_html_component("visualisasi/distribusi_kedalaman.html", height=500)

gap()

# ---------------------------------------------------------------------------
# BAB 4
# ---------------------------------------------------------------------------
chapter(
    "peta", 4, "Peta kepadatan titik gempa",
    "Di mana gempa paling terkonsentrasi? Peta <em>heatmap</em> interaktif ini memperlihatkan kluster "
    "kegempaan di sepanjang samudra selatan Jawa (zona subduksi) dan beberapa sesar aktif di daratan. "
    "Gunakan mouse untuk memperbesar atau memperkecil peta.",
)
load_html_component("visualisasi/density_map.html", height=580)

gap()

# ---------------------------------------------------------------------------
# MITIGASI
# ---------------------------------------------------------------------------
html("""
<div class="anchor" id="mitigasi"></div>
<div class="mitigation">
  <h2>Kesiapsiagaan dan mitigasi bencana</h2>
  <p class="intro">Tiga pesan kunci untuk masyarakat.</p>
  <div class="mit-grid">
    <div class="mit-item">
      <h3>Kenali potensi</h3>
      <p>Gempa adalah siklus alami Pulau Jawa yang tidak bisa dicegah, tetapi dampaknya bisa diperkecil.</p>
    </div>
    <div class="mit-item">
      <h3>Bangun tahan gempa</h3>
      <p>Kerusakan terbesar saat gempa umumnya disebabkan oleh kegagalan struktur bangunan.</p>
    </div>
    <div class="mit-item">
      <h3>Pahami jalur evakuasi</h3>
      <p>Tentukan titik kumpul aman di sekitar rumah dan tempat kerja Anda.</p>
    </div>
  </div>
</div>
<div class="footer-note">Proyek Digital Storytelling Geologi · Sumber data: USGS Earthquake Hazards Program</div>
""")
