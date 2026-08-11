import streamlit as st
import random

# --- CONFIG HALAMAN ---
st.set_page_config(
    page_title="Belajar Katakana Lengkap",
    layout="wide",
    page_icon="🇯🇵"
)

# --- DATABASE KATAKANA LENGKAP ---
KATAKANA_DATA = {
    "1. Gojūon (Huruf Dasar)": {
        "Vokal": [("ア", "a"), ("イ", "i"), ("ウ", "u"), ("エ", "e"), ("オ", "o")],
        "K-Gyo": [("カ", "ka"), ("キ", "ki"), ("ク", "ku"), ("ケ", "ke"), ("コ", "ko")],
        "S-Gyo": [("サ", "sa"), ("シ", "shi"), ("ス", "su"), ("セ", "se"), ("ソ", "so")],
        "T-Gyo": [("タ", "ta"), ("チ", "chi"), ("ツ", "tsu"), ("テ", "te"), ("ト", "to")],
        "N-Gyo": [("ナ", "na"), ("ニ", "ni"), ("ヌ", "nu"), ("ネ", "ne"), ("ノ", "no")],
        "H-Gyo": [("ハ", "ha"), ("ヒ", "hi"), ("フ", "fu"), ("ヘ", "he"), ("ホ", "ho")],
        "M-Gyo": [("マ", "ma"), ("ミ", "mi"), ("ム", "mu"), ("メ", "me"), ("モ", "mo")],
        "Y-Gyo": [("ヤ", "ya"), ("ユ", "yu"), ("ヨ", "yo")],
        "R-Gyo": [("ラ", "ra"), ("リ", "ri"), ("ル", "ru"), ("レ", "re"), ("ロ", "ro")],
        "W/N":   [("ワ", "wa"), ("ヲ", "wo"), ("ン", "n")]
    },
    "2. Dakuon & Handakuon (Tenten & Maru)": {
        "G-Gyo": [("ガ", "ga"), ("ギ", "gi"), ("グ", "gu"), ("ゲ", "ge"), ("ゴ", "go")],
        "Z-Gyo": [("ザ", "za"), ("ジ", "ji"), ("ズ", "zu"), ("ゼ", "ze"), ("ゾ", "zo")],
        "D-Gyo": [("ダ", "da"), ("ヂ", "ji/dji"), ("ヅ", "zu/dzu"), ("デ", "de"), ("ド", "do")],
        "B-Gyo": [("バ", "ba"), ("ビ", "bi"), ("ブ", "bu"), ("ベ", "be"), ("ボ", "bo")],
        "P-Gyo": [("パ", "pa"), ("ピ", "pi"), ("プ", "pu"), ("ペ", "pe"), ("ポ", "po")]
    },
    "3. Yōon (Gabungan Ya, Yu, Yo Kecil)": {
        "KY-Gyo": [("キャ", "kya"), ("キュ", "kyu"), ("キョ", "kyo")],
        "SH-Gyo": [("シャ", "sha"), ("シュ", "shu"), ("ショ", "sho")],
        "CH-Gyo": [("チャ", "cha"), ("チュ", "chu"), ("チョ", "cho")],
        "NY-Gyo": [("ニャ", "nya"), ("ニュ", "nyu"), ("ニョ", "nyo")],
        "HY-Gyo": [("ヒャ", "hya"), ("ヒュ", "hyu"), ("ヒョ", "hyo")],
        "MY-Gyo": [("ミャ", "mya"), ("ミュ", "myu"), ("ミョ", "myo")],
        "RY-Gyo": [("リャ", "rya"), ("リュ", "ryu"), ("リョ", "ryo")],
        "GY-Gyo": [("ギャ", "gya"), ("ギュ", "gyu"), ("ギョ", "gyo")],
        "J-Gyo":  [("ジャ", "ja"), ("ジュ", "ju"), ("ジョ", "jo")],
        "BY-Gyo": [("ビャ", "bya"), ("ビュ", "byu"), ("ビョ", "byo")],
        "PY-Gyo (Pya/Pyu/Pyo)": [("ピャ", "pya"), ("ピュ", "pyu"), ("ピョ", "pyo")]
    }
}

# Kumpulkan seluruh daftar huruf
ALL_ITEMS = []
for kat in KATAKANA_DATA.values():
    for sub in kat.values():
        ALL_ITEMS.extend(sub)

# --- SIDEBAR NAVIGASI ---
st.sidebar.title("🌸 Belajar Katakana")
menu = st.sidebar.radio(
    "Pilih Modul:",
    ["📖 Daftar & Kartu Katakana", "🎯 Kuis Tebak Huruf", "ℹ️ Panduan Singkat"]
)

st.title("🇯🇵 Modul Belajar Katakana Lengkap")

# ==============================================================================
# MODUL 1: DAFTAR HURUF
# ==============================================================================
if menu == "📖 Daftar & Kartu Katakana":
    st.header("📖 Katalog Huruf Katakana")
    
    kategori = st.selectbox("Pilih Kelompok Huruf:", list(KATAKANA_DATA.keys()))
    sub_kategori = st.selectbox("Pilih Baris/Kelompok:", list(KATAKANA_DATA[kategori].keys()))
    
    list_huruf = KATAKANA_DATA[kategori][sub_kategori]
    
    st.write(f"### Kelompok: **{sub_kategori}**")
    
    cols = st.columns(len(list_huruf) if len(list_huruf) <= 5 else 3)
    for idx, (kana, romaji) in enumerate(list_huruf):
        with cols[idx % len(cols)]:
            with st.container(border=True):
                st.markdown(f"<h1 style='text-align: center; margin: 0;'>{kana}</h1>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='text-align: center; color: #1E88E5; margin: 0;'>[{romaji}]</h3>", unsafe_allow_html=True)

# ==============================================================================
# MODUL 2: KUIS DENGAN EVALUASI DETAILED
# ==============================================================================
elif menu == "🎯 Kuis Tebak Huruf":
    st.header("🎯 Kuis Latihan Tebak Huruf Katakana")

    # Inisialisasi variabel state kuis
    if "kuis_berjalan" not in st.session_state:
        st.session_state.kuis_berjalan = False
    if "soal_list" not in st.session_state:
        st.session_state.soal_list = []
    if "index_soal" not in st.session_state:
        st.session_state.index_soal = 0
    if "skor" not in st.session_state:
        st.session_state.skor = 0
    if "riwayat_jawaban" not in st.session_state:
        st.session_state.riwayat_jawaban = []

    # TAMPILAN 1: Pengaturan Awal Kuis
    if not st.session_state.kuis_berjalan:
        st.subheader("⚙️ Pengaturan Kuis")
        target_soal = st.selectbox("Pilih Jumlah Soal:", [5, 10, 15, 20], index=0)

        if st.button("🚀 Mulai Kuis Sekarang", type="primary"):
            st.session_state.soal_list = random.sample(ALL_ITEMS, target_soal)
            st.session_state.index_soal = 0
            st.session_state.skor = 0
            st.session_state.riwayat_jawaban = []
            st.session_state.kuis_berjalan = True
            st.rerun()

    # TAMPILAN 2: Proses Pengerjaan Soal
    elif st.session_state.index_soal < len(st.session_state.soal_list):
        total_soal = len(st.session_state.soal_list)
        idx_sekarang = st.session_state.index_soal
        soal_kana, soal_romaji = st.session_state.soal_list[idx_sekarang]

        # Indicator Progress Bar
        st.progress((idx_sekarang) / total_soal)
        st.write(f"**Soal Ke-{idx_sekarang + 1} dari {total_soal}**")

        col_q1, col_q2 = st.columns([1, 2])
        with col_q1:
            with st.container(border=True):
                st.markdown(f"<h1 style='text-align: center; font-size: 100px; margin:0;'>{soal_kana}</h1>", unsafe_allow_html=True)
                st.caption("<p style='text-align: center;'>Tebak cara baca huruf di atas!</p>", unsafe_allow_html=True)

        with col_q2:
            st.subheader("Bagaimana cara membaca huruf tersebut?")
            
            with st.form(key=f"form_kuis_{idx_sekarang}"):
                jawaban_user = st.text_input("Ketik Romaji (contoh: pya, ka, shi, dsb):").strip().lower()
                btn_jawab = st.form_submit_button("Submit Jawaban ➡️", type="primary")

                if btn_jawab:
                    is_correct = (jawaban_user == soal_romaji)
                    if is_correct:
                        st.session_state.skor += 1
                    
                    # Catat ke riwayat
                    st.session_state.riwayat_jawaban.append({
                        "No": idx_sekarang + 1,
                        "Huruf": soal_kana,
                        "Jawaban Kamu": jawaban_user if jawaban_user else "(Kosong)",
                        "Kunci Jawaban": soal_romaji,
                        "Status": "✅ BENAR" if is_correct else "❌ SALAH"
                    })

                    st.session_state.index_soal += 1
                    st.rerun()

    # TAMPILAN 3: Halaman Hasil Akhir & Evaluasi
    else:
        st.progress(1.0)
        st.balloons()
        st.success("🎉 Selamat! Kamu telah menyelesaikan seluruh soal kuis Katakana.")
        
        total_soal = len(st.session_state.soal_list)
        skor_akhir = st.session_state.skor
        persentase = int((skor_akhir / total_soal) * 100)

        st.metric("Hasil Akhir Kamu:", f"{skor_akhir} / {total_soal} Soal Benar", delta=f"{persentase}% Nilai")

        st.markdown("---")
        st.subheader("📊 Pembahasan & Evaluasi Jawaban Kamu")
        st.write("Cek daftar di bawah ini untuk melihat nomor mana yang salah dan benar:")

        # Tampilkan tabel evaluasi
        st.dataframe(st.session_state.riwayat_jawaban, use_container_width=True)

        st.markdown("---")
        if st.button("🔄 Ulangi Kuis Baru", type="primary"):
            st.session_state.kuis_berjalan = False
            st.rerun()

# ==============================================================================
# MODUL 3: PANDUAN
# ==============================================================================
elif menu == "ℹ️ Panduan Singkat":
    st.header("ℹ️ Ringkasan Katakana")
    st.markdown("""
    * **Fungsi Katakana:** Digunakan untuk menulis kata-kata serapan bahasa asing (contoh: *Amerika* = アメリカ, *Kopi* = コーヒー), nama orang asing, atau penekanan kata.
    * **Gojūon (Huruf Dasar):** Huruf vokal baku (ア, イ, ウ, エ, オ) dan turunan dasarnya.
    * **Dakuon (`"`) & Handakuon (`°`):** Menggunakan tanda *tenten* (misal: カ `ka` → ガ `ga`) dan *maru* (misal: ハ `ha` → パ `pa`).
    * **Yōon (Huruf Gabungan Kecil):** Penggabungan dengan ャ `ya`, ュ `yu`, ョ `yo` kecil.
      * *Contoh kelompok **Pya/Pyu/Pyo***:
        * ピ + ャ = **ピャ (pya)**
        * ピ + ュ = **ピュ (pyu)**
        * ピ + ョ = **ピョ (pyo)**
    """)