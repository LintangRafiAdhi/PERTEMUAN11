# PERTEMUAN11
<H1>LATIHAN</H1>

```python
import math

a = lambda x: x**2
b = lambda x, y: math.sqrt(x**2 + y**2)
c = lambda *args: sum(args)/len(args)
d = lambda s: "".join(set(s))

# Memanggil fungsi lambda a(x)
result_a = a(9)
print(result_a)

# Memanggil fungsi lambda b(x, y)
result_b = b(6, 8)
print(result_b)

# Memanggil fungsi lambda c(*args)
result_c = c(2, 3, 4, 5, 6)
print(result_c)

# Memanggil fungsi lambda d(s)
result_d = d("hello")
print(*result_d, sep="")

```

<p>Kode tersebut menggunakan fungsi lambda (fungsi anonim) dalam Python untuk melakukan beberapa operasi matematika dan manipulasi string. Berikut adalah penjelasan langkah demi langkah:<p></p>

1. **Mendefinisikan Fungsi Lambda:**
   - Fungsi lambda `a` menerima satu parameter `x` dan mengembalikan nilai `x` pangkat 2.
   - Fungsi lambda `b` menerima dua parameter `x` dan `y`, kemudian mengembalikan nilai akar kuadrat dari jumlah kuadrat `x` dan `y`.
   - Fungsi lambda `c` menerima parameter sejumlah variabel panjang (`*args`) dan mengembalikan rata-rata dari semua argumen.
   - Fungsi lambda `d` menerima satu parameter string `s` dan mengembalikan string unik dengan karakter-karakter unik di dalamnya.

2. **Memanggil Fungsi Lambda:**
   - Memanggil fungsi lambda `a` dengan argumen 9 dan menyimpan hasilnya dalam variabel `result_a`.
   - Memanggil fungsi lambda `b` dengan argumen 6 dan 8, menyimpan hasilnya dalam variabel `result_b`.
   - Memanggil fungsi lambda `c` dengan argumen 2, 3, 4, 5, 6, menyimpan hasilnya dalam variabel `result_c`.
   - Memanggil fungsi lambda `d` dengan argumen "hello", menyimpan hasilnya dalam variabel `result_d`.

3. **Menampilkan Hasil:**
   - Mencetak hasil pemanggilan fungsi lambda `a`.
   - Mencetak hasil pemanggilan fungsi lambda `b`.
   - Mencetak hasil pemanggilan fungsi lambda `c`.
   - Mencetak hasil pemanggilan fungsi lambda `d` setelah mengubah hasilnya menjadi string dan menghilangkan karakter-karakter duplikat.

4. **Output yang Dihasilkan:**
   - Hasil pemanggilan `a(9)` adalah `81`.
   - Hasil pemanggilan `b(6, 8)` adalah `10.0`.
   - Hasil pemanggilan `c(2, 3, 4, 5, 6)` adalah `4.0`.
   - Hasil pemanggilan `d("hello")` adalah `helo`. (tanpa duplikat)

Jadi, kode ini menggunakan fungsi lambda untuk membuat fungsi kecil yang dapat digunakan dalam berbagai operasi matematika dan manipulasi string.

![Screenshot (27)](https://github.com/calamities17/PERTEMUAN11/assets/147371058/59d462db-f31b-419d-b582-9297bcea320c)


<H1>PRAKTIKUM</H1>

<p>Buat program sederhana dengan mengaplikasikan penggunaan fungsi yang akan menampilkan daftar nilai mahasiswa, dengan ketentuan:</p>
 
*Fungsi tambah() untuk menambah data*

*Fungsi tampilkan() untuk menampilkan data*

*Fungsi hapus(nama) untuk menghapus data berdasarkan nama*

*Fungsi ubah(nama) untuk mengubah data berdasarkan nama*

<p>jangan lupa install pretty table untuk menampilkan table.Anda dapat menginstal pustaka PrettyTable menggunakan pip, yang merupakan manajer paket standar untuk Python. Buka terminal atau command prompt, lalu jalankan perintah berikut:</p>

```python
pip install prettytable
```

<p>Pastikan Anda memiliki koneksi internet yang stabil karena pip akan mengunduh dan menginstal pustaka PrettyTable dari Python Package Index (PyPI). Setelah proses instalasi selesai, Anda dapat mengimpor PrettyTable ke dalam skrip atau program Python Anda dengan menggunakan pernyataan import.</p>

```python
from prettytable import PrettyTable
```
<p>sekarang kita masuk ke praktikum</p>

```python
from prettytable import PrettyTable

def hitung_nilai_akhir(tugas, uts, uas):
    nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
    return nilai_akhir

def tambah_data(data_mahasiswa):
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    data_mahasiswa[nama] = {"NIM": nim, "Tugas": tugas, "UTS": uts, "UAS": uas, "Nilai Akhir": nilai_akhir}
    print("Data mahasiswa berhasil ditambahkan.")

def ubah_data(data_mahasiswa):
    nama = input("Masukkan nama mahasiswa yang akan diubah datanya: ")
    if nama in data_mahasiswa:
        tugas = float(input("Masukkan nilai tugas baru: "))
        uts = float(input("Masukkan nilai UTS baru: "))
        uas = float(input("Masukkan nilai UAS baru: "))
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        data_mahasiswa[nama] = {"Tugas": tugas, "UTS": uts, "UAS": uas, "Nilai Akhir": nilai_akhir}
        print("Data mahasiswa berhasil diubah.")
    else:
        print("Nama mahasiswa tidak ditemukan.")

def hapus_data(data_mahasiswa):
    nama = input("Masukkan nama mahasiswa yang akan dihapus datanya: ")
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("Nama mahasiswa tidak ditemukan.")

def tampilkan_data(data_mahasiswa):
    tabel = PrettyTable()
    tabel.field_names = ["Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai Akhir"]

    for nama, nilai in data_mahasiswa.items():
        tabel.add_row([nama, nilai["NIM"], nilai["Tugas"], nilai["UTS"], nilai["UAS"], nilai["Nilai Akhir"]])

    print("\nDaftar Nilai Mahasiswa:")
    print(tabel)
1

def cari_data(data_mahasiswa):
    nama = input("Masukkan nama mahasiswa yang akan dicari: ")
    if nama in data_mahasiswa:
        tabel = PrettyTable()
        tabel.field_names = ["Nama", "Tugas", "UTS", "UAS", "Nilai Akhir"]
        nilai = data_mahasiswa[nama]
        tabel.add_row([nama, nilai["Tugas"], nilai["UTS"], nilai["UAS"], nilai["Nilai Akhir"]])
        print("\nData mahasiswa ditemukan:")
        print(tabel)
    else:
        print("Nama mahasiswa tidak ditemukan.")

#Program utama
data_mahasiswa = {}

while True:
    print("\nMenu Pilihan:")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")

    pilihan = input("Masukkan pilihan (1-6): ")

    if pilihan == "1":
        tambah_data(data_mahasiswa)
    elif pilihan == "2":
        ubah_data(data_mahasiswa)
    elif pilihan == "3":
        hapus_data(data_mahasiswa)
    elif pilihan == "4":
        tampilkan_data(data_mahasiswa)
    elif pilihan == "5":
        cari_data(data_mahasiswa)
    elif pilihan == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Masukkan angka 1-6.")

```

![Screenshot (28)](https://github.com/calamities17/PERTEMUAN11/assets/147371058/33aaac3e-fee5-4bf0-971d-45ddbbafb085)


<H1>FLOWCHART</H1>

![flc2](https://github.com/calamities17/PERTEMUAN11/assets/147371058/c9dd73b6-53e8-441e-be70-74afa06f1634)

<p>penjelasan</p>
Berikut adalah penjelasan flowchart dari kodingan yang Anda berikan:

1. **Start:** Program dimulai.
2. **Inisialisasi data_mahasiswa:** Membuat dictionary kosong sebagai tempat penyimpanan data mahasiswa.
3. **Perulangan Utama:**
   - Mencetak menu pilihan untuk pengguna.
   - Menerima input pilihan dari pengguna.
   - Jika pilihan adalah "1", maka langkah ke `tambah_data`.
   - Jika pilihan adalah "2", maka langkah ke `ubah_data`.
   - Jika pilihan adalah "3", maka langkah ke `hapus_data`.
   - Jika pilihan adalah "4", maka langkah ke `tampilkan_data`.
   - Jika pilihan adalah "5", maka langkah ke `cari_data`.
   - Jika pilihan adalah "6", maka mencetak "Program selesai" dan keluar dari perulangan utama.
   - Jika pilihan tidak valid, mencetak "Pilihan tidak valid. Masukkan angka 1-6."
4. **Tambah Data (tambah_data):**
   - Menerima input nama, nim, nilai tugas, uts, dan uas dari pengguna.
   - Menghitung nilai akhir menggunakan fungsi `hitung_nilai_akhir`.
   - Menambahkan data mahasiswa ke dalam `data_mahasiswa` dengan format dictionary.
   - Mencetak "Data mahasiswa berhasil ditambahkan."
5. **Ubah Data (ubah_data):**
   - Menerima input nama mahasiswa yang akan diubah datanya.
   - Jika nama ditemukan di dalam `data_mahasiswa`, menerima input nilai tugas, uts, dan uas baru.
   - Menghitung nilai akhir baru.
   - Mengubah data mahasiswa yang sesuai.
   - Mencetak "Data mahasiswa berhasil diubah."
   - Jika nama tidak ditemukan, mencetak "Nama mahasiswa tidak ditemukan."
6. **Hapus Data (hapus_data):**
   - Menerima input nama mahasiswa yang akan dihapus datanya.
   - Jika nama ditemukan di dalam `data_mahasiswa`, menghapus data mahasiswa tersebut.
   - Mencetak "Data mahasiswa berhasil dihapus."
   - Jika nama tidak ditemukan, mencetak "Nama mahasiswa tidak ditemukan."
7. **Tampilkan Data (tampilkan_data):**
   - Membuat objek PrettyTable untuk menampilkan data dalam bentuk tabel.
   - Menambahkan field names ke tabel.
   - Mengisi tabel dengan data mahasiswa.
   - Mencetak tabel sebagai daftar nilai mahasiswa.
8. **Cari Data (cari_data):**
   - Menerima input nama mahasiswa yang akan dicari.
   - Jika nama ditemukan di dalam `data_mahasiswa`, membuat tabel dan menampilkan data mahasiswa tersebut.
   - Jika nama tidak ditemukan, mencetak "Nama mahasiswa tidak ditemukan."
9. **Selesai:** Program mencetak "Program selesai" dan berakhir.

Semua proses dalam flowchart tersebut mewakili langkah-langkah yang diambil dalam program dan cara program berinteraksi dengan pengguna serta data mahasiswa.


