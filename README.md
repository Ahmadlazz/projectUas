# projectUas

📘 BAB 1 – PENDAHULUAN

1.1 Latar Belakang

Dalam era digital saat ini, proses pengiriman barang menjadi semakin penting dalam mendukung aktivitas bisnis dan logistik. Kurir sering menghadapi permasalahan dalam menentukan rute pengiriman yang optimal karena banyaknya pilihan jalur yang tersedia. Pemilihan rute yang tidak efisien dapat menyebabkan keterlambatan pengiriman serta peningkatan biaya operasional.

Dengan memanfaatkan struktur data graph, permasalahan tersebut dapat dimodelkan secara matematis, di mana setiap lokasi direpresentasikan sebagai node dan jalur antar lokasi sebagai edge. Oleh karena itu, diperlukan sebuah Decision Support System (DSS) yang mampu membantu menentukan rute terbaik secara otomatis.

1.2 Rumusan Masalah

Bagaimana merepresentasikan sistem rute kurir menggunakan graph?

Bagaimana menentukan rute tercepat antar lokasi?

Bagaimana mengimplementasikan algoritma graph dalam DSS?

1.3 Tujuan

Membuat model graph untuk sistem rute kurir

Mengimplementasikan algoritma Dijkstra

Menghasilkan rekomendasi rute terbaik

1.4 Manfaat

Membantu kurir menentukan rute optimal

Menghemat waktu dan biaya

Meningkatkan efisiensi distribusi

📘 BAB 2 – DASAR TEORI

2.1 Struktur Data Graph

Graph adalah struktur data yang terdiri dari node (vertex) dan edge (hubungan antar node). Dalam kasus ini:

Node = lokasi pengiriman
Edge = jalur antar lokasi
Bobot = jarak atau waktu tempuh

Graph yang digunakan adalah weighted graph, karena setiap edge memiliki nilai.

2.2 Decision Support System (DSS)

DSS adalah sistem yang membantu dalam pengambilan keputusan dengan memanfaatkan data dan model tertentu. Dalam penelitian ini, DSS digunakan untuk memberikan rekomendasi rute terbaik bagi kurir.

2.3 Algoritma Dijkstra

Algoritma Dijkstra digunakan untuk mencari jalur terpendek dari satu node ke node lainnya dalam graph berbobot. Algoritma ini bekerja dengan memilih node dengan jarak terkecil secara bertahap hingga mencapai tujuan.

Kelebihan:

Akurat untuk graph berbobot positif
Efisien untuk pencarian rute

📘 BAB 3 – ANALISIS DAN PERANCANGAN

3.1 Analisis Masalah

Permasalahan utama adalah menentukan rute tercepat dari titik awal ke tujuan dengan mempertimbangkan jarak antar lokasi.

3.2 Desain Graph

Contoh graph:

Node:
A (Gudang), B, C, D (Tujuan)
Edge (jarak):
A–B = 5 km
A–C = 10 km
B–D = 3 km
C–D = 2 km
3.3 Flowchart Sistem

Alur sistem:

Input data lokasi
Input jarak antar lokasi
Proses algoritma Dijkstra
Menampilkan rute terbaik
3.4 Use Case

Aktor: User (admin/kurir)

Fungsi:

Input data graph
Menjalankan perhitungan
Melihat hasil rute
3.5 Struktur Node dan Edge
Node: lokasi pengiriman
Edge: jalur antar lokasi
Weight: jarak

📘 BAB 4 – IMPLEMENTASI

4.1 Implementasi Sistem

Sistem dibangun menggunakan bahasa pemrograman (misalnya Python). Graph direpresentasikan menggunakan adjacency list.

4.2 Penjelasan Program

Program bekerja dengan:

Membaca data graph
Menjalankan algoritma Dijkstra
Menghasilkan rute terpendek

4.3 Tampilan Sistem

Sistem memiliki fitur:

Input lokasi
Input jarak
Tombol proses
Output rute

📘 BAB 5 – PENGUJIAN DAN ANALISIS

5.1 Skenario Pengujian

Contoh:
Dari node A ke D

Hasil:
Rute terbaik: A → B → D
Total jarak: 8 km

5.2 Analisis Hasil

Hasil menunjukkan bahwa sistem mampu menentukan rute terpendek secara akurat berdasarkan data yang diberikan.

5.3 Kompleksitas Algoritma

Algoritma Dijkstra memiliki kompleksitas:

O(V²) (versi sederhana)
O(E log V) (menggunakan priority queue)

📘 BAB 6 – KESIMPULAN

6.1 Kesimpulan

Graph efektif untuk memodelkan rute kurir
Algoritma Dijkstra berhasil menentukan jalur optimal
DSS membantu pengambilan keputusan secara cepat dan akurat
6.2 Saran
Menambahkan data real-time (traffic)
Mengembangkan sistem berbasis web/mobile
Menggunakan algoritma lain seperti A*
