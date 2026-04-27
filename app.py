import streamlit as st

st.set_page_config(page_title='ClusMath', page_icon='🌿', layout='centered')

# Session state
for k,v in {'page':'home','started':False,'section':1,'answers':{}}.items():
    if k not in st.session_state:
        st.session_state[k]=v

questions = {
1:[
'Saat mencoba alat atau aplikasi baru, saya biasanya:',
'Jika pergi ke tempat yang belum pernah dikunjungi:',
'Saat belajar resep masakan baru:',
'Ketika menjelaskan sesuatu ke orang lain:',
'Jika diberi instruksi:',
'Di waktu senggang, saya lebih suka:',
'Saat membeli pakaian:',
'Saat merencanakan perjalanan:',
'Saat ingin membeli barang mahal:',
'Saat belajar hal baru:'
],
2:[
'Saat memilih makanan di menu:', 'Saat menonton konser:', 'Saat berpikir serius:', 'Saat memilih barang:', 'Saya paling mudah belajar dengan:', 'Saat merasa tegang:', 'Saya mengingat seseorang dari:', 'Saat hasil belajar kurang baik:', 'Saat menjelaskan ide:', 'Aktivitas favorit:'
],
3:[
'Waktu luang saya biasanya:', 'Saat bertemu orang baru:', 'Saya menilai orang dari:', 'Saat marah:', 'Saya lebih mudah mengingat:', 'Saya tahu orang berbohong jika:', 'Saat bertemu teman lama:', 'Cara saya mengingat:', 'Jika komplain barang:', 'Saya sering mengatakan:'
]
}
opts={'A':'A (Visual)','B':'B (Auditori)','C':'C (Kinestetik)'}

if st.session_state.page=='home':
    st.title('ClusMath')
    st.subheader('🌿 Smart E-LKPD Aritmetika Sosial 🌿')
    nama=st.text_input('Nama', key='nama')
    kelas=st.text_input('Kelas', key='kelas')
    if st.button('MASUK'):
        if nama and kelas:
            st.session_state.page='vak'
            st.rerun()
        else:
            st.warning('Isi nama dan kelas terlebih dahulu.')

elif st.session_state.page=='vak':
    st.title('TES GAYA BELAJAR')
    st.write('Petunjuk: Pilih jawaban yang paling menggambarkan dirimu.')
    if not st.session_state.started:
        if st.button('START'):
            st.session_state.started=True
            st.rerun()
    else:
        sec=st.session_state.section
        st.header(f'Bagian {sec}')
        for i,q in enumerate(questions[sec], start=(sec-1)*10+1):
            resp = st.radio(q, ['A','B','C'], key=f'q{i}', horizontal=True, index=None, placeholder='Pilih jawaban')
            st.session_state.answers[i]=resp
        c1,c2=st.columns(2)
        if sec<3:
            with c2:
                if st.button('NEXT'):
                    st.session_state.section+=1
                    st.rerun()
        else:
            if st.button('FINISH'):
                st.session_state.page='result'
                st.rerun()

elif st.session_state.page=='result':
    st.success('Horeee, kamu telah menyelesaikan tes gaya belajar')
    if st.button('LIHAT HASIL'):
        vals=list(st.session_state.answers.values())
        a=vals.count('A'); b=vals.count('B'); c=vals.count('C')
        if a>=b and a>=c:
            gaya='Visual'; desc='belajar lebih mudah dengan melihat (gambar, tulisan, diagram, warna)'
        elif b>=a and b>=c:
            gaya='Auditori'; desc='belajar lebih mudah dengan mendengar (penjelasan guru, diskusi, rekaman suara)'
        else:
            gaya='Kinestetik'; desc='belajar lebih mudah dengan melakukan langsung (praktik, percobaan, aktivitas fisik)'
        st.subheader(f'Gaya belajarmu: {gaya}')
        st.write(desc)
        st.info('Setiap orang punya cara belajar yang berbeda, ada yang lebih paham kalau melihat, mendengar, atau langsung mencoba.')
        st.write('Sekarang saatnya kamu mengerjakan e-LKPD sesuai dengan gaya belajarmu.')
        if st.button('START LKPD'):
            st.write(f'Masuk ke LKPD untuk gaya belajar {gaya}. (Tambahkan link/halaman LKPD di sini)')
