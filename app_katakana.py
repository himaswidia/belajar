import streamlit as st
import random
import streamlit.components.v1 as components

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

# --- SIDEBAR NAVIGASI ---
st.sidebar.title("🌸 Belajar Katakana")
menu = st.sidebar.radio(
    "Pilih Modul:",
    ["📖 Daftar & Kartu Katakana", "🎯 Kuis Tebak Huruf", "ℹ️ Panduan Singkat"]
)

st.title("🇯🇵 Modul Belajar Katakana Lengkap")

if menu == "📖 Daftar & Kartu Katakana":
    st.header("📖 Katalog Huruf Katakana")
    
    mode_tampil = st.radio("Pilih Tampilan Katalog:", ["Semua Kategori Sekaligus", "Pilih Per Kelompok / Terpisah"], horizontal=True)
    
    if mode_tampil == "Semua Kategori Sekaligus":
        for kat_name, kat_dict in KATAKANA_DATA.items():
            st.markdown(f"### 📌 {kat_name}")
            for sub_name, list_huruf in kat_dict.items():
                st.write(f"**{sub_name}**")
                cols = st.columns(len(list_huruf) if len(list_huruf) <= 5 else 3)
                for idx, (kana, romaji) in enumerate(list_huruf):
                    with cols[idx % len(cols)]:
                        with st.container(border=True):
                            st.markdown(f"<h1 style='text-align: center; margin: 0;'>{kana}</h1>", unsafe_allow_html=True)
                            st.markdown(f"<h3 style='text-align: center; color: #1E88E5; margin: 0;'>[{romaji}]</h3>", unsafe_allow_html=True)
            st.markdown("---")
    else:
        kategori = st.selectbox("Pilih Kelompok Utama:", list(KATAKANA_DATA.keys()))
        sub_kategori = st.selectbox("Pilih Baris/Kelompok:", list(KATAKANA_DATA[kategori].keys()))
        
        list_huruf = KATAKANA_DATA[kategori][sub_kategori]
        st.write(f"### Kelompok: **{sub_kategori}**")
        
        cols = st.columns(len(list_huruf) if len(list_huruf) <= 5 else 3)
        for idx, (kana, romaji) in enumerate(list_huruf):
            with cols[idx % len(cols)]:
                with st.container(border=True):
                    st.markdown(f"<h1 style='text-align: center; margin: 0;'>{kana}</h1>", unsafe_allow_html=True)
                    st.markdown(f"<h3 style='text-align: center; color: #1E88E5; margin: 0;'>[{romaji}]</h3>", unsafe_allow_html=True)

elif menu == "🎯 Kuis Tebak Huruf":
    st.header("🎯 Kuis Latihan Tebak Huruf Katakana")
    if "kuis_berjalan_katakana" not in st.session_state:
        st.session_state.kuis_berjalan_katakana = False
    if "soal_list_katakana" not in st.session_state:
        st.session_state.soal_list_katakana = []
    if "index_soal_katakana" not in st.session_state:
        st.session_state.index_soal_katakana = 0
    if "skor_katakana" not in st.session_state:
        st.session_state.skor_katakana = 0
    if "riwayat_jawaban_katakana" not in st.session_state:
        st.session_state.riwayat_jawaban_katakana = []

    if not st.session_state.kuis_berjalan_katakana:
        st.subheader("⚙️ Pengaturan Kuis")
        
        pilihan_kategori_kuis = st.selectbox(
            "Pilih Kategori Huruf untuk Kuis:",
            ["Semua Kategori (Campur)", "1. Gojūon (Huruf Dasar)", "2. Dakuon & Handakuon (Tenten & Maru)", "3. Yōon (Gabungan Ya, Yu, Yo Kecil)"]
        )
        
        target_soal = st.selectbox("Pilih Jumlah Soal:", [5, 10, 15, 20], index=0)

        if st.button("🚀 Mulai Kuis Sekarang", type="primary"):
            pool_soal = []
            if pilihan_kategori_kuis == "Semua Kategori (Campur)":
                for kat in KATAKANA_DATA.values():
                    for sub in kat.values():
                        pool_soal.extend(sub)
            else:
                kat_terpilih = KATAKANA_DATA[pilihan_kategori_kuis]
                for sub in kat_terpilih.values():
                    pool_soal.extend(sub)
            
            jumlah_ambil = min(target_soal, len(pool_soal))
            
            st.session_state.soal_list_katakana = random.sample(pool_soal, jumlah_ambil)
            st.session_state.index_soal_katakana = 0
            st.session_state.skor_katakana = 0
            st.session_state.riwayat_jawaban_katakana = []
            st.session_state.kuis_berjalan_katakana = True
            st.rerun()

    elif st.session_state.index_soal_katakana < len(st.session_state.soal_list_katakana):
        total_soal = len(st.session_state.soal_list_katakana)
        idx_sekarang = st.session_state.index_soal_katakana
        soal_kana, soal_romaji = st.session_state.soal_list_katakana[idx_sekarang]
        st.progress((idx_sekarang) / total_soal)
        st.write(f"**Soal Ke-{idx_sekarang + 1} dari {total_soal}**")
        col_q1, col_q2 = st.columns([1, 2])
        with col_q1:
            with st.container(border=True):
                st.markdown(f"<h1 style='text-align: center; font-size: 100px; margin:0;'>{soal_kana}</h1>", unsafe_allow_html=True)
                st.caption("<p style='text-align: center;'>Tebak cara baca huruf di atas!</p>", unsafe_allow_html=True)
        with col_q2:
            st.subheader("Bagaimana cara membaca huruf tersebut?")
            with st.form(key=f"form_kuis_katakana_{idx_sekarang}"):
                jawaban_user = st.text_input("Ketik Romaji (contoh: pya, ka, shi, dsb):", key=f"input_box_katakana_{idx_sekarang}").strip().lower()
                btn_jawab = st.form_submit_button("Submit Jawaban ➡️", type="primary")
                if btn_jawab:
                    is_correct = (jawaban_user == soal_romaji)
                    if is_correct:
                        st.session_state.skor_katakana += 1
                    st.session_state.riwayat_jawaban_katakana.append({
                        "No": idx_sekarang + 1,
                        "Huruf": soal_kana,
                        "Jawaban Kamu": jawaban_user if jawaban_user else "(Kosong)",
                        "Kunci Jawaban": soal_romaji,
                        "Status": "✅ BENAR" if is_correct else "❌ SALAH"
                    })
                    st.session_state.index_soal_katakana += 1
                    st.rerun()
        
        components.html(
            """
            <script>
                function focusInput() {
                    const doc = window.parent.document;
                    const inputs = doc.querySelectorAll('input[type="text"]');
                    if (inputs.length > 0) {
                        const targetInput = inputs[inputs.length - 1];
                        targetInput.focus();
                        return true;
                    }
                    return false;
                }
                
                let attempts = 0;
                const interval = setInterval(function() {
                    attempts++;
                    if (focusInput() || attempts > 30) {
                        clearInterval(interval);
                    }
                }, 30);
            </script>
            """,
            height=0
        )
    else:
        st.progress(1.0)
        st.balloons()
        st.success("🎉 Selamat! Kamu telah menyelesaikan seluruh soal kuis Katakana.")
        total_soal = len(st.session_state.soal_list_katakana)
        skor_akhir = st.session_state.skor_katakana
        persentase = int((skor_akhir / total_soal) * 100)

        st.metric("Hasil Akhir Kamu:", f"{skor_akhir} / {total_soal} Soal Benar", delta=f"{persentase}% Nilai")

        st.markdown("---")
        st.subheader("📊 Pembahasan & Evaluasi Jawaban Kamu")
        st.dataframe(st.session_state.riwayat_jawaban_katakana, use_container_width=True)

        st.markdown("---")
        if st.button("🔄 Ulangi Kuis Baru", type="primary"):
            st.session_state.kuis_berjalan_katakana = False
            st.rerun()

elif menu == "ℹ️ Panduan Singkat":
    st.header("ℹ️ Ringkasan Katakana")
    st.markdown("""
    * **Fungsi Katakana:** Digunakan untuk menulis kata-kata serapan bahasa asing, nama orang asing, atau penekanan kata.
    * **Gojūon (Huruf Dasar):** Huruf vokal baku (ア, イ, ウ, エ, オ) dan turunan dasarnya.
    * **Dakuon (`"`) & Handakuon (`°`):** Menggunakan tanda *tenten* (misal: カ `ka` → ガ `ga`) dan *maru* (misal: ハ `ha` → パ `pa`).
    * **Yōon (Huruf Gabungan Kecil):** Penggabungan dengan ャ `ya`, ュ `yu`, ョ `yo` kecil.
      * *Contoh kelompok **Pya/Pyu/Pyo***:
        * ピ + ャ = **ピャ (pya)**
        * ピ + ュ = **ピュ (pyu)**
        * ピ + ョ = **ピョ (pyo)**
    """)
