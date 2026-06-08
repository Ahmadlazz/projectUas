# projectUas
Nama_NIM_Github:

I Gusti Ari Regina Dharmagita_
2501010379_
gunggita49-oss

Dania syifa rezkia_
2501010012_
daniasif

Ahmad Paesoel_
2501010143_
Ahmadlazz

# **BAB 1 – PENDAHULUAN**

## 1.1 Latar Belakang

Dalam proses pengiriman barang, seorang kurir sering dihadapkan pada banyak pilihan rute untuk mencapai tujuan. Jika pemilihan rute tidak tepat, maka waktu pengiriman bisa menjadi lebih lama dan biaya operasional juga meningkat. Hal ini menjadi tantangan terutama ketika jumlah lokasi pengiriman cukup banyak dan saling terhubung.

Dengan adanya perkembangan teknologi, permasalahan tersebut dapat dibantu dengan sistem berbasis komputer. Salah satu pendekatan yang dapat digunakan adalah struktur data graph, di mana setiap lokasi direpresentasikan sebagai node dan jalur antar lokasi sebagai edge.

Berdasarkan hal tersebut, pada penelitian ini dibuat sebuah Decision Support System (DSS) yang dapat membantu menentukan rute terbaik bagi kurir. Sistem ini memanfaatkan algoritma Dijkstra untuk mencari jalur dengan jarak terpendek sehingga proses pengiriman menjadi lebih efisien.

---

## 1.2 Rumusan Masalah

Berdasarkan latar belakang di atas, maka rumusan masalah dalam penelitian ini adalah:

1. Bagaimana merepresentasikan rute pengiriman kurir menggunakan graph?
2. Bagaimana menentukan jalur terpendek antar lokasi?
3. Bagaimana mengimplementasikan sistem DSS berbasis graph?

---

## 1.3 Tujuan

Tujuan dari pembuatan sistem ini adalah:

1. Membuat model graph untuk merepresentasikan lokasi pengiriman
2. Mengimplementasikan algoritma Dijkstra dalam sistem
3. Menentukan rute terbaik berdasarkan jarak terpendek

---

## 1.4 Manfaat

Adapun manfaat dari sistem ini adalah:

1. Membantu kurir dalam menentukan rute yang lebih efisien
2. Menghemat waktu dan biaya pengiriman
3. Memberikan gambaran penerapan graph dalam dunia nyata

---

# **BAB 2 – DASAR TEORI**

## 2.1 Struktur Data Graph

Graph merupakan struktur data yang terdiri dari sekumpulan node (vertex) dan edge yang menghubungkan antar node tersebut. Dalam sistem ini, node digunakan untuk merepresentasikan lokasi pengiriman, sedangkan edge merepresentasikan jalur antar lokasi.

Graph yang digunakan termasuk weighted graph karena setiap edge memiliki bobot berupa jarak. Selain itu, graph bersifat tidak berarah karena jalur antar lokasi dapat dilalui dua arah.

---

## 2.2 Decision Support System (DSS)

Decision Support System (DSS) adalah sistem yang digunakan untuk membantu dalam pengambilan keputusan. DSS biasanya memanfaatkan data dan model tertentu untuk menghasilkan rekomendasi.

Dalam penelitian ini, DSS digunakan untuk memberikan rekomendasi rute terbaik bagi kurir berdasarkan jarak terpendek.

---

## 2.3 Algoritma Dijkstra

Algoritma Dijkstra merupakan algoritma yang digunakan untuk mencari jalur terpendek dalam graph berbobot. Algoritma ini bekerja dengan memilih node dengan jarak terkecil secara bertahap hingga mencapai tujuan.

Kelebihan dari algoritma ini adalah mampu memberikan hasil yang akurat dan cukup efisien dalam pencarian jalur terpendek.

---

# **BAB 3 – ANALISIS DAN PERANCANGAN**

## 3.1 Analisis Masalah

Permasalahan utama dalam sistem ini adalah bagaimana menentukan rute tercepat dari satu lokasi ke lokasi lainnya. Banyaknya jalur yang tersedia membuat proses pemilihan rute menjadi tidak sederhana jika dilakukan secara manual.

Oleh karena itu, dibutuhkan suatu sistem yang dapat membantu memilih rute terbaik secara otomatis.

---

## 3.2 Desain Graph

Dalam sistem ini, graph digunakan untuk merepresentasikan hubungan antar lokasi. Setiap lokasi menjadi node, dan setiap jalur antar lokasi menjadi edge dengan bobot jarak.

Sebagai contoh:

* Node: Kantor Pusat, Hub Denpasar, Hub Kuta, Penerima
* Edge: hubungan antar lokasi dengan jarak tertentu

---

## 3.3 Flowchart Sistem

Alur kerja sistem secara umum adalah sebagai berikut:

1. Pengguna memasukkan data lokasi
2. Sistem membentuk graph
3. Pengguna memilih titik awal dan tujuan
4. Sistem menjalankan algoritma Dijkstra
5. Sistem menampilkan hasil rute terbaik

---

## 3.4 Use Case

Aktor dalam sistem ini adalah pengguna (admin atau kurir).
Pengguna dapat:

* Menambahkan lokasi
* Menentukan titik awal dan tujuan
* Melihat hasil rute

---

## 3.5 Struktur Node dan Edge

* Node: lokasi pengiriman
* Edge: jalur antar lokasi
* Bobot: jarak antar lokasi

---

# **BAB 4 – IMPLEMENTASI**

## 4.1 Implementasi Sistem

Sistem dibangun menggunakan Python dengan bantuan framework Streamlit untuk tampilan antarmuka. Graph direpresentasikan menggunakan adjacency list.

---

## 4.2 Penjelasan kode

Program bekerja dengan cara membaca data node dan edge, kemudian menjalankan algoritma Dijkstra untuk menentukan rute terpendek. Hasil yang diperoleh berupa jalur yang harus dilalui serta total jarak.

Struktur Graph dan node
****<img width="1124" height="369" alt="image" src="https://github.com/user-attachments/assets/a5d420be-66de-4c3d-9021-25da9464e23a" />

-Pada bagian ini dibuat sebuah class untuk merepresentasikan graph menggunakan adjacency list. Struktur ini digunakan untuk menyimpan hubungan antar node beserta bobot jaraknya.

-Dan yang dibawahnya memiliki fungsi ini digunakan untuk menambahkan hubungan (edge) antar node. Parameter weight menunjukkan jarak antar lokasi, sedangkan bidirectional menunjukkan bahwa hubungan bersifat dua arah.

Algoritma Dijkstra

<img width="1114" height="208" alt="image" src="https://github.com/user-attachments/assets/6df4ab02-bb5a-43e9-ad8a-c42da231263c" />

-Fungsi ini merupakan inti dari sistem yang digunakan untuk mencari rute terpendek menggunakan algoritma Dijkstra.

-Semua node diinisialisasi dengan jarak tak hingga, kemudian node awal diberikan nilai 0 sebagai titik awal perhitungan.

<img width="1107" height="597" alt="image" src="https://github.com/user-attachments/assets/9db2332d-1639-4eca-a486-cdca863793de" />

-di bagian ini akan mengatur alur proses navigasi dari sistem tersebut, sistem ini menggunakan priority queve untuk mengambil node dengan jarak yang paling dekat, bagian selanjutnya juga merupakan proses relaksasi yaitu  memperbarui jika ditemukan jalur yang lebih pendek dan terakhir ada bagian yang memiliki fungsi sebagai menyimpan jalur yang dilalui sehingga membentuk rute terakhir


## 4.3.Tampilan Sistem
<img width="1365" height="677" alt="image" src="https://github.com/user-attachments/assets/08f0b527-bcef-42fe-bdd0-bf292bf6e7e9" />


-Seperti inilah tampilan dari sistemnya ini belum melakukan sebuah proses pencarian rute tercepat,dari matriks ketetanggaan menggunakan adjacency list, serta kami menggunakan map bali sebagai contoh nyata pada visualisasi spasial



---

## 4.4 Fitur Sistem

Sistem yang dibuat memiliki beberapa fitur utama, yaitu:

1. Input data lokasi dan hubungan antar lokasi
2. Visualisasi lokasi dalam bentuk peta interaktif
3. Proses pencarian rute menggunakan algoritma Dijkstra
4. Menampilkan hasil rute terbaik
5. Menampilkan proses perhitungan algoritma
6. Tampilan sistem yang interaktif

---

# **BAB 5 – PENGUJIAN DAN ANALISIS**

<img width="1365" height="678" alt="image" src="https://github.com/user-attachments/assets/7970dc78-54f3-4d03-a448-8bee7be10b16" />

<img width="1365" height="677" alt="image" src="https://github.com/user-attachments/assets/6e8c230b-b603-499e-ab37-dadb561205f2" />


## 5.1 Skenario Pengujian

Pengujian sistem dilakukan dengan memilih titik awal dan tujuan pengiriman melalui antarmuka yang tersedia. Pada pengujian ini, pengguna memilih titik awal Kantor Pusat dan titik tujuan Penerima C.

Setelah itu, sistem akan memproses data graph yang telah tersedia dalam bentuk adjacency list, yang berisi hubungan antar node beserta jarak masing-masing. Selanjutnya, pengguna menekan tombol “Hitung Rute Optimal” untuk memulai proses perhitungan.

---

## 5.2 Hasil Pengujian

Berdasarkan hasil pengujian, sistem berhasil menampilkan data graph dalam bentuk matriks ketetanggaan (adjacency list) yang berisi node dan jarak antar lokasi.

Selain itu, sistem juga menampilkan visualisasi rute dalam bentuk peta digital. Pada peta tersebut terlihat jalur distribusi yang menghubungkan titik awal hingga tujuan.

Rute yang dihasilkan merupakan jalur optimal yang telah dihitung menggunakan algoritma Dijkstra. Jalur tersebut ditampilkan secara visual dengan garis berwarna pada peta, sehingga memudahkan pengguna dalam memahami rute yang harus dilalui.

Sistem juga menunjukkan total jumlah node dan edge yang digunakan dalam graph, yaitu sebanyak 6 node dan 8 edge.

---

## 5.3 Analisis Hasil

Berdasarkan hasil yang diperoleh, sistem mampu menentukan rute distribusi dengan baik sesuai dengan data yang diberikan. Algoritma Dijkstra berhasil memilih jalur dengan jarak paling minimum dari titik awal menuju tujuan.

Visualisasi peta yang ditampilkan juga membantu dalam memahami hasil perhitungan secara lebih jelas, karena pengguna dapat melihat jalur secara langsung sesuai kondisi geografis.

Selain itu, penggunaan adjacency list sebagai representasi graph memudahkan sistem dalam melakukan proses pencarian jalur.

Namun, sistem masih memiliki keterbatasan, yaitu belum mempertimbangkan kondisi lalu lintas secara real-time. Oleh karena itu, pengembangan selanjutnya dapat menambahkan fitur tersebut agar hasil rute menjadi lebih akurat.

---

## 5.4 Kompleksitas Algoritma

Algoritma yang digunakan dalam sistem ini adalah algoritma Dijkstra untuk menentukan jalur terpendek. Dalam implementasinya, algoritma ini menggunakan struktur data priority queue untuk memilih node dengan jarak terkecil secara efisien.

Secara umum, kompleksitas waktu dari algoritma Dijkstra bergantung pada cara implementasinya. Pada sistem ini, karena menggunakan priority queue (heap), maka kompleksitas waktu yang dihasilkan adalah sekitar O(E log V), di mana:

V (Vertex) adalah jumlah node atau lokasi
E (Edge) adalah jumlah hubungan antar lokasi

Kompleksitas tersebut menunjukkan bahwa semakin banyak jumlah node dan edge dalam graph, maka waktu yang dibutuhkan untuk proses pencarian rute juga akan meningkat, namun masih dalam batas yang efisien.

Selain itu, kompleksitas ruang (space complexity) dari algoritma ini adalah O(V), karena sistem menyimpan data jarak dan jalur untuk setiap node.

Berdasarkan hasil pengujian yang telah dilakukan, algoritma Dijkstra mampu bekerja dengan baik dalam menentukan rute optimal meskipun jumlah node dan edge bertambah. Hal ini menunjukkan bahwa algoritma yang digunakan sudah cukup efisien untuk kebutuhan sistem penentuan rute kurir.

---

# **BAB 6 – KESIMPULAN**

## 6.1 Kesimpulan

Berdasarkan hasil yang diperoleh, dapat disimpulkan bahwa penggunaan graph sangat efektif untuk memodelkan sistem rute kurir. Algoritma Dijkstra juga terbukti mampu menentukan jalur terpendek dengan baik.

Selain itu, sistem DSS yang dibuat dapat membantu pengguna dalam menentukan rute secara lebih cepat dan efisien.

---

## 6.2 Saran

Untuk pengembangan selanjutnya, sistem dapat ditambahkan fitur seperti:

* Data lalu lintas secara real-time
* Pengembangan berbasis mobile
* Penggunaan algoritma lain untuk perbandingan hasil
