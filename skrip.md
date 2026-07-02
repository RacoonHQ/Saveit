# 🎬 Naskah Video YouTube: Kupas Tuntas Hugging Face & RAG (15 Menit)

Naskah ini disusun untuk memandu pembuatan video YouTube dengan durasi **15 menit**. Gaya bahasa yang digunakan santai, komunikatif, mudah dipahami masyarakat umum (tidak terlalu akademis), serta langsung pada intinya.

Setiap bagian dilengkapi dengan **Petunjuk Visual (Visual Cues)** dan **Estimasi Waktu** agar mempermudah proses rekaman dan editing.

---

## 📝 Referensi File Praktikum
* Notebook 1: [Sayyid Abdullah Azzam 2023230021 - Praktikum HuggingFace.ipynb](file:///g:/Users/Documents/SEMESTER%206%20UNSADA/BIGDATA%20DAN%20ANALITIK/Review%20HF%20dan%20RAG/Sayyid%20Abdullah%20Azzam%202023230021%20-%20Praktikum%20HuggingFace.ipynb)
* Notebook 2: [Modul_Praktikum_RAG_Fondasi_v4.ipynb](file:///g:/Users/Documents/SEMESTER%206%20UNSADA/BIGDATA%20DAN%20ANALITIK/Review%20HF%20dan%20RAG/Modul_Praktikum_RAG_Fondasi_v4.ipynb)

---

## ⏱️ Rencana Pembagian Waktu (Timeline)
| Segmen | Topik Bahasan | Durasi |
| :--- | :--- | :--- |
| **01** | **Pembukaan & Pengenalan Masalah RAM / LLM** | 00:00 - 02:00 (2 Menit) |
| **02** | **Kupas Praktikum 1: Ekosistem Hugging Face & Streaming Mode** | 02:00 - 06:00 (4 Menit) |
| **03** | **Kupas Praktikum 2: Fondasi RAG (Ujian Buka Buku untuk AI)** | 06:00 - 10:30 (4.5 Menit) |
| **04** | **Studi Kasus & Jawaban Tugas: Mengapa AI Bisa "Halu"?** | 10:30 - 13:30 (3 Menit) |
| **05** | **Rangkuman & Penutup** | 13:30 - 15:00 (1.5 Menit) |

---

## 🎙️ Detail Naskah & Panduan Visual

### 🎬 Segmen 1: Pembukaan & Pengenalan Masalah (00:00 - 02:00)
**[VISUAL]**: *Kamera menyorot wajah Anda (A-Roll) dengan ekspresi antusias. Di latar belakang terdapat tampilan samar kode Python. Muncul judul teks di layar: "Big Data & AI Tanpa Bikin RAM Jebol!"*

**[DIALOG]**:
"Halo teman-teman! Selamat datang kembali di channel kita. Hari ini kita bakal bahas dua topik yang lagi panas banget di dunia teknologi: **Hugging Face** dan **RAG (Retrieval-Augmented Generation)**.

Pernah gak sih kalian kepikiran, gimana caranya perusahaan teknologi memproses data teks yang ukurannya bergiga-giga, bahkan terabyte? Padahal laptop kita RAM-nya cuma 8 atau 16 GB? Kalau kita paksain buka semua datanya sekaligus, dijamin laptop bakal langsung nge-freeze atau 'jebol'!

Nah, masalah kedua: Gimana caranya bikin AI atau Large Language Model (LLM) seperti ChatGPT atau Llama bisa menjawab pertanyaan tentang dokumen internal kita dengan super akurat dan gak ngasal?

Hari ini, kita akan bedah solusinya lewat dua file praktikum keren milik mahasiswa Universitas Darma Persada bernama **Sayyid Abdullah Azzam**. Kita akan bahas rahasia memproses data besar dengan teknik *Streaming*, cara kerja *Semantic Search*, dan bagaimana RAG menyelamatkan AI dari penyakit 'halusinasi' alias mengada-ada. 

Tonton video ini sampai habis, karena penjelasannya bakal kita buat sesimpel mungkin tanpa rumus matematika yang rumit. Yuk, kita mulai!"

---

### 🎬 Segmen 2: Ekosistem Hugging Face & Streaming Mode (02:00 - 06:00)
**[VISUAL]**: *Beralih ke rekaman layar (B-Roll). Tampilkan notebook pertama:* [Sayyid Abdullah Azzam 2023230021 - Praktikum HuggingFace.ipynb](file:///g:/Users/Documents/SEMESTER%206%20UNSADA/BIGDATA%20DAN%20ANALITIK/Review%20HF%20dan%20RAG/Sayyid%20Abdullah%20Azzam%202023230021%20-%20Praktikum%20HuggingFace.ipynb). *Perlihatkan bagian kode `load_dataset` dengan parameter `streaming=True`.*

**[DIALOG]**:
"Oke, sekarang kita masuk ke file pertama tentang **Hugging Face**. Hugging Face itu ibaratnya 'Play Store' buat model AI dan dataset. Kita bisa ambil model yang sudah pintar secara gratis.

Tapi, ada satu trik penting di sini yang namanya **Streaming Mode**. Coba lihat potongan kode ini:"

**[VISUAL]**: *Sorot baris kode [load_dataset di baris 85-101](file:///g:/Users/Documents/SEMESTER%206%20UNSADA/BIGDATA%20DAN%20ANALITIK/Review%20HF%20dan%20RAG/Sayyid%20Abdullah%20Azzam%202023230021%20-%20Praktikum%20HuggingFace.ipynb#L85-L101).*

**[DIALOG]**:
"Di sini ada parameter `streaming=True`. Nah, apa fungsinya? 

Biar gampang, bayangkan kalian mau nonton film berdurasi 3 jam. Kalau kalian **download** dulu seluruh filmnya sampai 100% baru ditonton, memori HP kalian pasti penuh dan nunggunya lama banget. Itu namanya metode *klasik*.

Sedangkan **Streaming Mode** itu seperti kalian nonton **Netflix atau YouTube**. Videonya diputar sedikit demi sedikit sambil berjalan. Hugging Face melakukan hal yang sama pada data! Data teks ulasan film dari IMDb ditarik baris demi baris dari cloud. Hasilnya? RAM laptop kita tetap aman dan sangat hemat!

Setelah datanya ditarik, langkah berikutnya adalah menganalisis sentimen dari ulasan tersebut. Apakah ulasan filmnya bernada positif atau negatif?"

**[VISUAL]**: *Tunjuk/sorot bagian pemanggilan [pipeline sentiment-analysis di baris 117-126](file:///g:/Users/Documents/SEMESTER%206%20UNSADA/BIGDATA%20DAN%20ANALITIK/Review%20HF%20dan%20RAG/Sayyid%20Abdullah%20Azzam%202023230021%20-%20Praktikum%20HuggingFace.ipynb#L117-L126).*

**[DIALOG]**:
"Untuk klasifikasi ini, praktikum ini menggunakan model bernama **DistilBERT**. Model ini versi ringkas dan cepat dari model BERT buatan Google.

Di tugas mandirinya, Sayyid juga memodifikasi model ini untuk menganalisis emosi yang lebih spesifik menggunakan dataset `dair-ai/emotion`. Hasilnya keren banget! AI bisa membedakan 6 emosi manusia: sedih, senang, cinta, marah, takut, dan terkejut.

Dan dari pengujian performa yang ia lakukan:"

**[VISUAL]**: *Tampilkan tabel hasil evaluasi di notebook:*
* *5 Data: 0.13 detik (Akurasi 100%)*
* *50 Data: 1.11 detik (Akurasi 100%)*
* *100 Data: 2.13 detik (Akurasi 98%)*

**[DIALOG]**:
"Kalian bisa lihat, semakin banyak data yang diuji secara bersamaan (menggunakan metode *Batch Processing*), waktu pemrosesannya relatif sangat cepat dan efisien dengan akurasi yang tetap terjaga di atas 98%. Ini membuktikan bahwa kombinasi *Streaming Mode* dan *Batch Processing* di Hugging Face sangat ampuh untuk Big Data!"

---

### 🎬 Segmen 3: Fondasi RAG (Retrieval-Augmented Generation) (06:00 - 10:30)
**[VISUAL]**: *Kamera kembali ke wajah Anda (A-Roll). Gunakan animasi sederhana di layar atau gestur tangan.*

**[DIALOG]**:
"Sekarang kita masuk ke topik kedua yang gak kalah seru: **RAG** atau *Retrieval-Augmented Generation*.

Teman-teman, LLM atau model AI itu pintar, tapi mereka punya batas ingatan. Kalau kita tanya aturan internal kampus kita yang fiktif atau dokumen rahasia kantor, LLM bawaan internet gak bakal tahu. Nah, solusinya adalah **RAG**.

Supaya gampang dipahami, bayangkan kalian sedang ikut ujian. 
* Kalau tanpa RAG, itu seperti **Ujian Tutup Buku**. AI cuma menjawab berdasarkan apa yang pernah dia pelajari dulu saat training. Kalau dia lupa, dia bakal ngarang jawaban atau halusinasi.
* Kalau pakai RAG, itu seperti **Ujian Buka Buku**. AI diberikan dokumen referensi yang relevan tepat sebelum menjawab pertanyaan kita. Jadi jawabannya dijamin berdasarkan fakta di buku itu!

Gimana tahapannya di Python? Mari kita buka notebook kedua."

**[VISUAL]**: *Tampilkan layar notebook:* [Modul_Praktikum_RAG_Fondasi_v4.ipynb](file:///g:/Users/Documents/SEMESTER%206%20UNSADA/BIGDATA%20DAN%20ANALITIK/Review%20HF%20dan%20RAG/Modul_Praktikum_RAG_Fondasi_v4.ipynb). *Scroll perlahan melintasi Langkah 1 sampai Langkah 6.*

**[DIALOG]**:
"Di dalam praktikum RAG ini, ada 4 langkah utama yang dilakukan langkah demi langkah:

**Langkah 1: Chunking (Pemotongan Teks)**
Dokumen akademik kampus dipotong menjadi bagian-bagian kecil. Kenapa? Karena LLM punya batas maksimal teks yang bisa dibaca sekali jalan (*Context Window*). Di sini digunakan alat bernama [RecursiveCharacterTextSplitter](file:///g:/Users/Documents/SEMESTER%206%20UNSADA/BIGDATA%20DAN%20ANALITIK/Review%20HF%20dan%20RAG/Modul_Praktikum_RAG_Fondasi_v4.ipynb#L196-L209) dengan ukuran potongan 150 karakter dan *overlap* (tumpang tindih) 30 karakter. *Overlap* ini penting supaya tidak ada kalimat yang terpotong di tengah jalan sehingga maknanya hilang.

**Langkah 2: Embedding (Mengubah Teks Jadi Angka)**
Komputer tidak mengerti kata-kata, komputer mengerti angka. Potongan teks tadi diubah menjadi koordinat matematika berupa 512 deretan angka menggunakan model [HuggingFaceEmbeddings](file:///g:/Users/Documents/SEMESTER%206%20UNSADA/BIGDATA%20DAN%20ANALITIK/Review%20HF%20dan%20RAG/Modul_Praktikum_RAG_Fondasi_v4.ipynb#L250-L261). Di sini kita memakai model multilingual yang ramah bahasa Indonesia.

**Langkah 3: Vector Database (Penyimpanan Pintar)**
Deretan angka (vektor) tersebut kemudian disimpan ke basis data khusus bernama [FAISS](file:///g:/Users/Documents/SEMESTER%206%20UNSADA/BIGDATA%20DAN%20ANALITIK/Review%20HF%20dan%20RAG/Modul_Praktikum_RAG_Fondasi_v4.ipynb#L287-L292) buatan Meta/Facebook. FAISS ini bekerja langsung di memori komputer sehingga pencariannya super cepat.

**Langkah 4: Retrieval & Generation (Pencarian & Penyusunan Jawaban)**
Ketika pengguna bertanya: *'Berapa SKS syarat untuk ambil skripsi?'*, FAISS akan mencari potongan dokumen yang maknanya paling mirip dengan pertanyaan itu. Setelah ketemu, potongan dokumen itu ditempelkan ke instruksi prompt LLM, lalu dikirim ke model LLM (dalam kasus ini menggunakan Llama 3.1 lewat Groq API) untuk dirangkai menjadi jawaban yang rapi."

---

### 🎬 Segmen 4: Studi Kasus & Jawaban Tugas (10:30 - 13:30)
**[VISUAL]**: *A-Roll diselingi cuplikan hasil eksekusi tugas evaluasi dari Notebook RAG.*

**[DIALOG]**:
"Nah, di bagian akhir praktikum RAG ini, ada beberapa soal evaluasi menarik yang membongkar batasan terdalam dari sistem AI saat ini. Mari kita bahas 3 temuan penting dari tugas mandiri Sayyid:

**Temuan 1: Apa jadinya kalau pemotongan teks terlalu pendek?**
Ketika `chunk_size` diatur sangat kecil, yaitu cuma 50 karakter tanpa tumpang tindih, potongan kalimat menjadi hancur. Kalimat seperti *'Ujian Akhir Semester'* terpisah di potongan yang berbeda. Akibatnya, AI kehilangan konteks makna utuh dan tidak bisa memberikan jawaban komprehensif saat kita bertanya.

**Temuan 2: Efek bertanya di luar topik dokumen (Out of Domain Query)**
Ini unik banget! Di praktikum ini, Sayyid mencoba mengajukan pertanyaan: *'Bagaimana cara memasak rendang?'* ke dokumen akademik kampus. 
Anehnya, database FAISS tetap saja mengembalikan potongan dokumen akademik tentang panduan kampus! Kenapa bisa begitu? 

Karena database vektor bekerja dengan prinsip *K-Nearest Neighbors* atau mencari tetangga terdekat secara relatif. Dia tidak tahu makna absolut dari memasak rendang. Dia hanya mencari dokumen apa saja di dalam database yang jarak vektornya paling dekat secara matematika dengan kueri tersebut. 

Risikonya besar banget kalau data ini langsung dikirim ke LLM biasa tanpa instruksi khusus: AI akan berhalusinasi dan memaksakan diri menjawab cara memasak rendang menggunakan aturan kelulusan SKS kampus! Hahaha, kebayang kan kacaunya?

**Temuan 3: Pentingnya Prompt Grounding (Konteks vs Tanpa Konteks)**
Saat LLM ditanya syarat skripsi *tanpa diberikan dokumen hasil pencarian*, LLM menjawab secara umum (menebak sekitar 110 hingga 140 SKS kebijakan umum kampus lain). Tapi saat *diberikan konteks dokumen RAG*, LLM menjawab dengan sangat akurat dan presisi: *'Minimal 120 SKS sesuai aturan Universitas Darma Persada'*. Ini membuktikan RAG sangat efektif mencegah AI mengarang bebas."

---

### 🎬 Segmen 5: Rangkuman & Penutup (13:30 - 15:00)
**[VISUAL]**: *Kembali ke A-Roll (Kamera utama). Tampilkan poin-poin kesimpulan grafis yang muncul di samping Anda.*

**[DIALOG]**:
"Jadi kesimpulannya apa dari review dua modul praktikum ini?

Pertama, kalau kalian mau membuat aplikasi AI yang menangani dokumen raksasa tanpa membuat server atau komputer hang, gunakan ekosistem **Hugging Face dengan fitur Streaming Mode** dan **Batch Processing**.

Kedua, kalau kalian ingin LLM menjawab pertanyaan spesifik tentang data lokal kalian secara akurat dan jujur tanpa halusinasi, buatlah pipeline **RAG** yang andal dengan memperhatikan ukuran pemotongan dokumen (*chunking*) secara bijak.

Terima kasih banyak untuk Sayyid Abdullah Azzam atas dokumentasi praktikumnya yang sangat rapi dan mendalam di Universitas Darma Persada.

Gimana menurut kalian? Apakah kalian tertarik buat mencoba bikin chatbot pintar sendiri pakai RAG? Tulis pendapat kalian di kolom komentar di bawah ya!

Jangan lupa untuk **Like**, **Subscribe**, dan bagikan video ini ke teman-teman kalian yang juga tertarik belajar AI dan Big Data. Sampai jumpa di video berikutnya. *Keep learning and stay curious! Bye bye!*"

**[VISUAL]**: *Layar meredup perlahan (Fade to black). Menampilkan tombol subscribe dan rekomendasi video berikutnya.*
