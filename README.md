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
![Screenshot (27)](https://github.com/calamities17/PERTEMUAN11/assets/147371058/59d462db-f31b-419d-b582-9297bcea320c)


<H1>PRAKTIKUM</H1>

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

