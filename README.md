# projectUas

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

## 4.2 Penjelasan Program

Program bekerja dengan cara membaca data node dan edge, kemudian menjalankan algoritma Dijkstra untuk menentukan rute terpendek. Hasil yang diperoleh berupa jalur yang harus dilalui serta total jarak.

---

## 4.3 Fitur Sistem

Sistem yang dibuat memiliki beberapa fitur utama, yaitu:

1. Input data lokasi dan hubungan antar lokasi
2. Visualisasi lokasi dalam bentuk peta interaktif
3. Proses pencarian rute menggunakan algoritma Dijkstra
4. Menampilkan hasil rute terbaik
5. Menampilkan proses perhitungan algoritma
6. Tampilan sistem yang interaktif

---

# **BAB 5 – PENGUJIAN DAN ANALISIS**

## 5.1 Skenario Pengujian

Pengujian dilakukan dengan memilih titik awal dan tujuan, kemudian sistem akan menghitung rute terbaik.

Contoh:
Dari Kantor Pusat ke Penerima
Hasil: sistem menampilkan jalur dengan jarak paling pendek.

---

## 5.2 Analisis Hasil

Berdasarkan hasil pengujian, sistem mampu menentukan rute dengan benar sesuai dengan perhitungan algoritma Dijkstra. Jalur yang dihasilkan merupakan jalur dengan total jarak minimum.

---

## 5.3 Kompleksitas Algoritma

Algoritma Dijkstra memiliki kompleksitas sekitar O(V²) pada implementasi sederhana, dan dapat lebih efisien jika menggunakan struktur data tambahan seperti priority queue.

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
