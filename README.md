
# Pertemuan 11 - Dictionary/Map

Nama: Hudaeva
NIM: 2225250164
Kelas: 3E

## Tujuan

Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Data

Program menggunakan dictionary `data_mahasiswa` untuk menyimpan data mahasiswa.

NIM digunakan sebagai key utama, sedangkan value berupa dictionary yang berisi nama, kelas, dan nilai mahasiswa.

Contoh struktur data:

- Key: `"A001"`
- Value: `{"nama": "Ayu", "kelas": "A", "nilai": 85}`

Dictionary digunakan untuk mempermudah pencarian, penambahan, dan pembaruan data mahasiswa berdasarkan NIM.

## Cara Menjalankan

Jalankan program melalui terminal VS Code dengan perintah:

```bash
python3 prakt ik/data_mahasiswa.py
```

Jika nama folder program adalah `praktik`, gunakan perintah berikut:

```bash
python3 praktik/data_mahasiswa.py
```

## Test Case

| Kasus | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| Pencarian tersedia | A003 | Data Citra ditampilkan | Data Citra ditampilkan | Berhasil |
| Pencarian tidak tersedia | A999 | Data tidak ditemukan | Data tidak ditemukan | Berhasil |
| Pembaruan nilai | A002 menjadi 82 | Nilai A002 berubah menjadi 82 | Nilai A002 berubah menjadi 82 | Berhasil |
| Penambahan data | A006 | Key A006 tersedia setelah ditambahkan | Key A006 tersedia setelah ditambahkan | Berhasil |
| Rekap | items() | Semua NIM dan data tampil | Semua NIM dan data tampil | Berhasil |

## Refleksi

Kesalahan yang dapat terjadi saat menggunakan dictionary adalah mengakses key yang tidak tersedia sehingga menyebabkan `KeyError`.

Kesalahan tersebut dapat diperbaiki dengan memeriksa keberadaan key menggunakan `if nim in data` sebelum mengakses data. Dengan cara ini, program dapat menampilkan pesan bahwa data tidak ditemukan tanpa mengalami error.

Selain itu, penggunaan `items()` memudahkan program untuk menampilkan seluruh key dan value dalam dictionary.

## Kesimpulan

Dictionary memudahkan penyimpanan dan pengelolaan data mahasiswa menggunakan NIM sebagai key. Program dapat melakukan pencarian, penambahan, pembaruan nilai, menampilkan seluruh data, serta menghitung rata-rata nilai mahasiswa.
