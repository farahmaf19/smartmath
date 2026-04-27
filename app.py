import streamlit as st

# ---------------------- CONFIG ----------------------
st.set_page_config(page_title="ClusMath", page_icon="🌿", layout="centered")

# ---------------------- CSS HIJAU ----------------------
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
    border-radius:10px;
    padding:10px 18px;
    font-weight:bold;
}

.stButton>button:hover {
    background-color:#1f6b43;
}

.stTextInput input {
    border-radius:10px;
    border:2px solid #2e8b57;
}
</style>
""", unsafe_allow_html=True)

# ---------------------- SESSION ----------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "section" not in st.session_state:
    st.session_state.section = 1

if "started" not in st.session_state:
    st.session_state.started = False

if "answers" not in st.session_state:
    st.session_state.answers = {}

# ---------------------- DATA SOAL ----------------------
questions = {
1: [
("Saat mencoba alat atau aplikasi baru, saya biasanya:",
"A. Membaca panduan atau melihat gambar petunjuknya",
"B. Mendengarkan penjelasan dari orang lain",
"C. Langsung mencoba dan belajar sambil praktik"),

("Jika pergi ke tempat yang belum pernah dikunjungi:",
"A. Saya melihat peta atau rute di aplikasi",
"B. Saya bertanya arah kepada orang lain",
"C. Saya mengikuti insting sambil mencoba jalan sendiri"),

("Saat belajar resep masakan baru:",
"A. Mengikuti langkah tertulis dengan detail",
"B. Mendengarkan arahan dari orang yang lebih ahli",
"C. Memasak sambil mencoba dan menyesuaikan sendiri"),

("Ketika menjelaskan sesuatu ke orang lain:",
"A. Saya menuliskan atau menggambarkannya",
"B. Saya menjelaskan dengan kata-kata",
"C. Saya memperagakan langsung"),

("Jika diberi instruksi:",
"A. Saya lebih paham jika melihat contoh",
"B. Saya lebih paham jika dijelaskan",
"C. Saya lebih paham jika langsung mencoba"),
],

2: [
("Di waktu senggang, saya lebih suka:",
"A. Melihat-lihat gambar, film, atau membaca",
"B. Mendengarkan musik atau ngobrol",
"C. Beraktivitas fisik atau membuat sesuatu"),

("Saat membeli pakaian:",
"A. Saya memperhatikan warna dan modelnya",
"B. Saya bertanya pendapat orang lain",
"C. Saya mencoba langsung"),

("Saat merencanakan perjalanan:",
"A. Mencari referensi visual (foto/tempat)",
"B. Mendengar cerita atau rekomendasi orang",
"C. Membayangkan aktivitas yang akan dilakukan"),

("Saat ingin membeli barang mahal:",
"A. Membaca review atau melihat gambar produk",
"B. Berdiskusi dengan orang lain",
"C. Mencoba langsung barang tersebut"),

("Saat belajar hal baru:",
"A. Melihat contoh terlebih dahulu",
"B. Mendengarkan penjelasan",
"C. Praktik langsung"),
],

3: [
("Saat memilih makanan di menu:",
"A. Membayangkan tampilannya",
"B. Meminta rekomendasi pelayan",
"C. Membayangkan rasa atau sensasinya"),

("Saat menonton konser:",
"A. Fokus pada tampilan panggung",
"B. Menikmati suara dan lirik",
"C. Ikut bergerak mengikuti musik"),

("Saat berpikir serius:",
"A. Membayangkan gambar atau tulisan",
"B. Mengulang kata-kata di pikiran",
"C. Banyak bergerak atau memainkan benda"),

("Saat memilih barang:",
"A. Melihat desainnya",
"B. Mendengar penjelasan penjual",
"C. Menyentuh dan merasakannya"),

("Saya paling mudah belajar dengan:",
"A. Melihat",
"B. Mendengar",
"C. Melakukan"),
]
}

# ---------------------- HOME ----------------------
if st.session_state.page == "home":

    st.title("ClusMath")
    st.subheader("🌿 Smart E-LKPD Aritmetika Sosial 🌿")

    nama = st.text_input("Nama")
    kelas = st.text_input("Kelas")

    if st.button("MASUK"):
        if nama and kelas:
            st.session_state.page = "tes"
            st.rerun()
        else:
            st.warning("Isi nama dan kelas terlebih dahulu.")

# ---------------------- TES ----------------------
elif st.session_state.page == "tes":

    st.title("TES GAYA BELAJAR")
    st.write("Pilih jawaban yang paling menggambarkan dirimu.")

    if not st.session_state.started:
        if st.button("START"):
            st.session_state.started = True
            st.rerun()

    else:
        sec = st.session_state.section
        st.header(f"Bagian {sec}")

        nomor = (sec - 1) * 5 + 1

        for i, soal in enumerate(questions[sec], start=nomor):
            q, a, b, c = soal

            jawab = st.radio(
                q,
                [a, b, c],
                key=f"q{i}"
            )

            if jawab == a:
                st.session_state.answers[i] = "A"
            elif jawab == b:
                st.session_state.answers[i] = "B"
            else:
                st.session_state.answers[i] = "C"

        if sec < 3:
            if st.button("NEXT"):
                st.session_state.section += 1
                st.rerun()
        else:
            if st.button("FINISH"):
                st.session_state.page = "hasil"
                st.rerun()

# ---------------------- HASIL ----------------------
elif st.session_state.page == "hasil":

    st.success("Horeee, kamu telah menyelesaikan tes gaya belajar 🎉")

    if st.button("LIHAT HASIL"):

        vals = list(st.session_state.answers.values())

        a = vals.count("A")
        b = vals.count("B")
        c = vals.count("C")

        if a >= b and a >= c:
            gaya = "VISUAL"
            desc = "Belajar lebih mudah dengan melihat gambar, tulisan, diagram, warna."
        elif b >= a and b >= c:
            gaya = "AUDITORI"
            desc = "Belajar lebih mudah dengan mendengar penjelasan guru, diskusi, rekaman suara."
        else:
            gaya = "KINESTETIK"
            desc = "Belajar lebih mudah dengan melakukan langsung, praktik, percobaan."

        st.subheader(f"Gaya belajarmu: {gaya}")
        st.write(desc)

        st.info("Setiap orang punya cara belajar yang berbeda, ada yang lebih paham kalau melihat, mendengar, atau langsung mencoba.")

        st.write("Sekarang saatnya kamu mengerjakan e-LKPD sesuai dengan gaya belajarmu 🌿")

        if st.button("START"):
            st.write(f"Masuk ke LKPD gaya belajar {gaya}")
