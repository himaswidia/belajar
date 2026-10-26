import streamlit as st
import random
import streamlit.components.v1 as components

# --- CONFIG HALAMAN ---
st.set_page_config(
    page_title="Belajar Hiragana Lengkap",
    layout="wide",
    page_icon="🇯🇵"
)

# --- DATABASE HIRAGANA LENGKAP ---
HIRAGANA_DATA = {
    "1. Gojūon (Huruf Dasar)": {
        "Vokal": [("あ", "a"), ("い", "i"), ("う", "u"), ("え", "e"), ("お", "o")],
        "K-Gyo": [("か", "ka"), ("き", "ki"), ("く", "ku"), ("け", "ke"), ("こ", "ko")],
        "S-Gyo": [("さ", "sa"), ("し", "shi"), ("す", "su"), ("せ", "se"), ("そ", "so")],
        "T-Gyo": [("た", "ta"), ("ち", "chi"), ("つ", "tsu"), ("て", "te"), ("と", "to")],
        "N-Gyo": [("な", "na"), ("に", "ni"), ("ぬ", "nu"), ("ね", "ne"), ("の", "no")],
        "H-Gyo": [("は", "ha"), ("ひ", "hi"), ("ふ", "fu"), ("へ", "he"), ("ほ", "ho")],
        "M-Gyo": [("ま", "ma"), ("み", "mi"), ("む", "mu"), ("め", "me"), ("も", "mo")],
        "Y-Gyo": [("や", "ya"), ("ゆ", "yu"), ("よ", "yo")],
        "R-Gyo": [("ら", "ra"), ("り", "ri"), ("る", "ru"), ("れ", "re"), ("ろ", "ro")],
        "W/N":   [("わ", "wa"), ("を", "wo"), ("ん", "n")]
    },
    "2. Dakuon & Handakuon (Tenten & Maru)": {
        "G-Gyo": [("が", "ga"), ("ぎ", "gi"), ("ぐ", "gu"), ("げ", "ge"), ("ご", "go")],
        "Z-Gyo": [("ざ", "za"), ("じ", "ji"), ("ず", "zu"), ("ぜ", "ze"), ("ぞ", "zo")],
        "D-Gyo": [("だ", "da"), ("ぢ", "ji/dji"), ("づ", "zu/dzu"), ("で", "de"), ("ど", "do")],
        "B-Gyo": [("ば", "ba"), ("び", "bi"), ("ぶ", "bu"), ("べ", "be"), ("ぼ", "bo")],
        "P-Gyo": [("ぱ", "pa"), ("ぴ", "pi"), ("ぷ", "pu"), ("ぺ", "pe"), ("ぽ", "po")]
    },
    "3. Yōon (Gabungan Ya, Yu, Yo Kecil)": {
        "KY-Gyo": [("きゃ", "kya"), ("きゅ", "kyu"), ("きょ", "kyo")],
        "SH-Gyo": [("しゃ", "sha"), ("しゅ", "shu"), ("しょ", "sho")],
        "CH-Gyo": [("ちゃ", "cha"), ("ちゅ", "chu"), ("ちょ", "cho")],
        "NY-Gyo": [("にゃ", "nya"), ("にゅ", "nyu"), ("にょ", "nyo")],
        "HY-Gyo": [("ひゃ", "hya"), ("ひゅ", "hyu"), ("ひょ", "hyo")],
        "MY-Gyo": [("みゃ", "mya"), ("みゅ", "myu"), ("みょ", "myo")],
        "RY-Gyo": [("りゃ", "rya"), ("りゅ", "ryu"), ("りょ", "ryo")],
        "GY-Gyo": [("ぎゃ", "gya"), ("ぎゅ", "gyu"), ("ぎょ", "gyo")],
        "J-Gyo":  [("じゃ", "ja"), ("じゅ", "ju"), ("じょ", "jo")],
        "BY-Gyo": [("びゃ", "bya"), ("びゅ", "byu"), ("びょ", "byo")],
        "PY-Gyo (Pya/Pyu/Pyo)": [("ぴゃ", "pya"), ("ぴゅ", "pyu"), ("ぴょ", "pyo")]
    }
}

# --- SIDEBAR NAVIGASI ---
st.sidebar.title("🌸 Belajar Hiragana")
menu = st.sidebar.radio(
    "Pilih Modul:",
    ["📖 Daftar & Kartu Hiragana", "🎯 Kuis Tebak Huruf", "ℹ️ Panduan Singkat"]
)

st.title("🇯🇵 Modul Belajar Hiragana Lengkap")

if menu == "📖 Daftar & Kartu Hiragana":
    st.header("📖 Katalog Huruf Hiragana")
    
    mode_tampil = st.radio("Pilih Tampilan Katalog:", ["Semua Kategori Sekaligus", "Pilih Per Kelompok / Terpisah"], horizontal=True)
    
    if mode_tampil == "Semua Kategori Sekaligus":
        for kat_name, kat_dict in HIRAGANA_DATA.items():
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
        kategori = st.selectbox("Pilih Kelompok Utama:", list(HIRAGANA_DATA.keys()))
        sub_kategori = st.selectbox("Pilih Baris/Kelompok:", list(HIRAGANA_DATA[kategori].keys()))
        
        list_huruf = HIRAGANA_DATA[kategori][sub_kategori]
        st.write(f"### Kelompok: **{sub_kategori}**")
        
        cols = st.columns(len(list_huruf) if len(list_huruf) <= 5 else 3)
        for idx, (kana, romaji) in enumerate(list_huruf):
            with cols[idx % len(cols)]:
                with st.container(border=True):
                    st.markdown(f"<h1 style='text-align: center; margin: 0;'>{kana}</h1>", unsafe_allow_html=True)
                    st.markdown(f"<h3 style='text-align: center; color: #1E88E5; margin: 0;'>[{romaji}]</h3>", unsafe_allow_html=True)

elif menu == "🎯 Kuis Tebak Huruf":
    st.header("🎯 Kuis Latihan Tebak Huruf Hiragana")
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

    if not st.session_state.kuis_berjalan:
        st.subheader("⚙️ Pengaturan Kuis")
        
        pilihan_kategori_kuis = st.selectbox(
            "Pilih Kategori Huruf untuk Kuis:",
            ["Semua Kategori (Campur)", "1. Gojūon (Huruf Dasar)", "2. Dakuon & Handakuon (Tenten & Maru)", "3. Yōon (Gabungan Ya, Yu, Yo Kecil)"]
        )
        
        target_soal = st.selectbox("Pilih Jumlah Soal:", [5, 10, 15, 20], index=0)

        if st.button("🚀 Mulai Kuis Sekarang", type="primary"):
            pool_soal = []
            if pilihan_kategori_kuis == "Semua Kategori (Campur)":
                for kat in HIRAGANA_DATA.values():
                    for sub in kat.values():
                        pool_soal.extend(sub)
            else:
                kat_terpilih = HIRAGANA_DATA[pilihan_kategori_kuis]
                for sub in kat_terpilih.values():
                    pool_soal.extend(sub)
            
            jumlah_ambil = min(target_soal, len(pool_soal))
            
            st.session_state.soal_list = random.sample(pool_soal, jumlah_ambil)
            st.session_state.index_soal = 0
            st.session_state.skor = 0
            st.session_state.riwayat_jawaban = []
            st.session_state.kuis_berjalan = True
            st.rerun()

    elif st.session_state.index_soal < len(st.session_state.soal_list):
        total_soal = len(st.session_state.soal_list)
        idx_sekarang = st.session_state.index_soal
        soal_kana, soal_romaji = st.session_state.soal_list[idx_sekarang]
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
                jawaban_user = st.text_input("Ketik Romaji (contoh: pya, ka, shi, dsb):", key=f"input_box_{idx_sekarang}").strip().lower()
                btn_jawab = st.form_submit_button("Submit Jawaban ➡️", type="primary")
                if btn_jawab:
                    is_correct = (jawaban_user == soal_romaji)
                    if is_correct:
                        st.session_state.skor += 1
                    st.session_state.riwayat_jawaban.append({
                        "No": idx_sekarang + 1,
                        "Huruf": soal_kana,
                        "Jawaban Kamu": jawaban_user if jawaban_user else "(Kosong)",
                        "Kunci Jawaban": soal_romaji,
                        "Status": "✅ BENAR" if is_correct else "❌ SALAH"
                    })
                    st.session_state.index_soal += 1
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
        st.success("🎉 Selamat! Kamu telah menyelesaikan seluruh soal kuis.")
        total_soal = len(st.session_state.soal_list)
        skor_akhir = st.session_state.skor
        persentase = int((skor_akhir / total_soal) * 100)

        st.metric("Hasil Akhir Kamu:", f"{skor_akhir} / {total_soal} Soal Benar", delta=f"{persentase}% Nilai")

        st.markdown("---")
        st.subheader("📊 Pembahasan & Evaluasi Jawaban Kamu")
        st.dataframe(st.session_state.riwayat_jawaban, use_container_width=True)

        st.markdown("---")
        if st.button("🔄 Ulangi Kuis Baru", type="primary"):
            st.session_state.kuis_berjalan = False
            st.rerun()

elif menu == "ℹ️ Panduan Singkat":
    st.header("ℹ️ Ringkasan Pembagian Huruf")
    st.markdown("""
    * **Gojūon (Huruf Dasar):** Huruf vokal baku (A, I, U, E, O) dan turunan dasarnya.
    * **Dakuon (`"`) & Handakuon (`°`):** Huruf dengan tanda *tenten* (misal: か `ka` → が `ga`) dan *maru* (misal: は `ha` → ぱ `pa`).
    * **Yōon (Huruf Gabungan Kecil):** Huruf gabungan dengan `ya`, `yu`, `yo` kecil.
      * *Contoh kelompok **Pya/Pyu/Pyo***:
        * ぴ + ゃ = **ぴゃ (pya)**
        * ぴ + ゅ = **ぴゅ (pyu)**
        * ぴ + ょ = **ぴょ (pyo)**
    """)
