# TC1
 Tugas 1 II4031 Kriptografi dan Koding Semester II Tahun 2023/2024
 # Dibuat Oleh
 Muhammad Rafi Haidar - 18221134
 Raditya Azka Prabaswara - 18221152
# Deskripsi
Program ini bertujuan untuk melakukan enkripsi dan dekripsi pada teks maupun berkas. Program ini menyediakan beberapa cipher atau algoritma yang dapat dipilih oleh pengguna untuk melakukan enkripsi dan dekripsi. Program ini dibuat dengan menggunakan Python dengan menggunakan Tkinter library untuk GUI.
# Batasan
- Python 3.12 atau terbaru
- Untuk enkripsi teks maupun enkripsi berkas teks (.txt) hanya dapat mengandung karakter yang terdapat pada "latin1"
- Ukuran file input sebaiknya berukuran lebih kecil dari 10 KB
# Fitur
Berikut adalah cipher yang tersedia :
Cipher | Teks/Berkas Teks | Berkas Sembarang
| :---:   | :---: | :---: |
Vigenere | Alfabet (26 karakter) | Tidak
Extended Vigenere | ASCII (256 karakter) | Ya
Playfair | Alfabet (26 karakter) | Tidak
Product | Alfabet (26 karakter) | Tidak
Affine | Alfabet (26 karakter) | Tidak
Autokey Vigenere | ASCII (256 karakter) | Ya
# Petunjuk Penggunaaan
1. Unduh berkas Zip kode sumber dari repository atau clone repository Github
2. Buka direktori yang sudah berisi kode sumber melalui CLI seperti terminal atau command prompt, atau buka direktori kode sumber di aplikasi IDE seperti Visual Studio Code
3. Jalankan berkas main.py, apabila menggunakan command prompt, ketik
   > python main.py
   > 
tidak perlu menjalankan virtual environment karena hanya memakai built-in package Python

4. Pilih metode cipher yang diinginkan
5. Masukkan key berupa string sembarang
6. Pilih tipe masukan (berkas atau teks)
7. Masukkan string sembarang untuk teks atau unggah berkas jika memilih berkas
8. Untuk memulai aksi, tekan tombol enkripsi atau dekripsi
9. Hasil enkripsi/dekripsi akan muncul sebagai string dalam pengkodean karakter latin1 (8 bit) dan Base64 (6 bit), yang dapat disalin
10. Hasil enkripsi/dekripsi dapat disimpan ke dalam berkas dengan menekan tombol "Save File"


