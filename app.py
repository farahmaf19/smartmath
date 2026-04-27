import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="ClusMath",
    page_icon="🌿",
    layout="centered"
)

# ---------------- CSS HIJAU ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#d9fdd3,#b8f2b2,#95e28f);
    background-attachment: fixed;
}

h1,h2,h3,h4,h5,h6,p,label,div {
    color:#103d10 !important;
}

.stButton>button {
    background-color:#2e8b57;
    color:white;
    border:none;
    border-radius:12px;
    padding:10px 18px;
    font-weight:bold;
}

.stButton>button:hover {
    background-color:#1f6b43;
    color:white;
}

.stTextInput input {
    border:2px solid #2e8b57;
    border-radius:10px;
}

[data-baseweb="radio"] {
    background-color: rgba(255,255,255,0.4);
    padding:8px;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
default_state = {
    "page": "home",
    "started": False,
    "section": 1,
    "answers": {}
}

for k,v in default_state.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ---------------- SOAL ----------------
questions = {
1:[
"Saat mencoba alat atau aplikasi baru, saya biasanya:",
"Jika pergi ke tempat yang belum pernah dikunjungi:",
"Saat belajar resep masakan baru:",
"Ketika menjelaskan sesuatu ke orang lain:",
"Jika diberi instruksi:",
"Di waktu senggang, saya lebih suka:",
"Saat membeli pakaian:",
"Saat merencanakan perjalanan:",
"Saat ingin membeli barang mahal:",
"Saat belajar hal baru:"
],

2:[
"Saat memilih makanan di menu:",
"Saat menonton konser:",
"Saat berpikir serius:",
"Saat memilih barang:",
"Saya paling mudah belajar dengan:",
"Saat merasa tegang:",
"Saya mengingat seseorang dari:",
"Saat hasil belajar kurang baik:",
"Saat menjelaskan ide:",
"Aktivitas favorit:"
],

3:[
"Waktu luang saya biasanya:",
"Saat bertemu orang baru:",
"Saya menilai orang dari:",
"Saat marah:",
"Saya lebih mudah mengingat:",
"Saya tahu orang berbohong jika:",
"Saat bertemu teman lama:",
"Cara saya mengingat:",
"Jika komplain barang:",
"Saya sering mengatakan:"
]
}

# ---------------- PILIHAN ----------------
choices = [
"A = Visual (lebih suka melihat gambar/tulisan)",
"B = Auditori (lebih suka mendengar penjelasan)",
"C = Kinestetik (lebih suka praktik langsung)"
]

# ---------------- HALAMAN HOME ----------------
if st.session_state.page == "home":

    st.title("ClusMath")
    st.subheader("🌿 Smart E-LKPD Aritmetika Sosial 🌿")

    st.write("Silakan isi identitas terlebih dahulu.")

    nama = st.text_input("Nama", key="nama")
    kelas = st.text_input("Kelas", key="kelas")

    if st.button("MASUK"):
        if nama and kelas:
            st.session_state.page = "vak"
            st.rerun()
        else:
            st.warning("Isi nama dan kelas terlebih dahulu.")

# ---------------- HALAMAN TES ----------------
elif st.session_state.page == "vak":

    st.title("TES GAYA BELAJAR")
    st.write("Petunjuk: Pilih jawaban yang paling menggambarkan dirimu. Tidak ada jawaban benar atau salah.")

    if not st.session_state.started:
        if st.button("START"):
            st.session_state.started = True
            st.rerun()

    else:
        sec = st.session_state.section
        st.header(f"Bagian {sec}")

        start_num = (sec-1)*10 + 1

        for i,q in enumerate(questions[sec], start=start_num):
            jawaban = st.radio(
                q,
                choices,
                key=f"q{i}"
            )

            if jawaban.startswith("A"):
                st.session_state.answers[i] = "A"
            elif jawaban.startswith("B"):
                st.session_state.answers[i] = "B"
            else:
                st.session_state.answers[i] = "C"

        col1,col2 = st.columns(2)

        if sec < 3:
            with col2:
                if st.button("NEXT"):
                    st.session_state.section += 1
                    st.rerun()

        else:
            if st.button("FINISH"):
                st.session_state.page = "result"
                st.rerun()

# ---------------- HASIL ----------------
elif st.session_state.page == "result":

    st.success("Horeee, kamu telah menyelesaikan tes gaya belajar 🎉")

    if st.button("LIHAT HASIL"):

        vals = list(st.session_state.answers.values())

        a = vals.count("A")
        b = vals.count("B")
        c = vals.count("C")

        if a >= b and a >= c:
            gaya = "VISUAL"
            ket = "Belajar lebih mudah dengan melihat gambar, tulisan, warna, diagram."
        elif b >= a and b >= c:
            gaya = "AUDITORI"
            ket = "Belajar lebih mudah dengan mendengar penjelasan guru, diskusi, rekaman suara."
        else:
            gaya = "KINESTETIK"
            ket = "Belajar lebih mudah dengan praktik langsung, percobaan, dan aktivitas fisik."

        st.subheader(f"Gaya belajarmu: {gaya}")
        st.write(ket)

        st.info("Setiap orang punya cara belajar yang berbeda, ada yang lebih paham kalau melihat, mendengar, atau langsung mencoba.")

        st.write("Sekarang saatnya kamu mengerjakan e-LKPD sesuai dengan gaya belajarmu 🌿")

        if st.button("START"):
            st.write(f"Masuk ke LKPD gaya belajar {gaya}")
