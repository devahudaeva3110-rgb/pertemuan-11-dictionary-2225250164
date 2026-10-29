
def cari_mahasiswa(data, nim):
    if nim in data:
        print("\nData mahasiswa ditemukan:")
        print("NIM   :", nim)
        print("Nama  :", data[nim]["nama"])
        print("Kelas :", data[nim]["kelas"])
        print("Nilai :", data[nim]["nilai"])
    else:
        print("Mahasiswa tidak ditemukan.")


def rata_rata_nilai(data):
    if len(data) == 0:
        return 0

    total = sum(m["nilai"] for m in data.values())
    return total / len(data)


def tambah_mahasiswa(data):
    nim = input("Masukkan NIM: ").strip()

    if nim in data:
        print("NIM sudah terdaftar.")
        return

    nama = input("Masukkan nama: ").strip()
    kelas = input("Masukkan kelas: ").strip().upper()

    try:
        nilai = float(input("Masukkan nilai: "))

        if not 0 <= nilai <= 100:
            print("Nilai harus antara 0 sampai 100.")
            return
    except ValueError:
        print("Nilai harus berupa angka.")
        return

    data[nim] = {
        "nama": nama,
        "kelas": kelas,
        "nilai": nilai
    }

    print("Data mahasiswa berhasil ditambahkan.")


def perbarui_nilai(data):
    nim = input("Masukkan NIM mahasiswa: ").strip()

    if nim not in data:
        print("Mahasiswa tidak ditemukan.")
        return

    try:
        nilai_baru = float(input("Masukkan nilai baru: "))

        if not 0 <= nilai_baru <= 100:
            print("Nilai harus antara 0 sampai 100.")
            return
    except ValueError:
        print("Nilai harus berupa angka.")
        return

    data[nim]["nilai"] = nilai_baru
    print("Nilai mahasiswa berhasil diperbarui.")


def tampilkan_rekap(data):
    if len(data) == 0:
        print("Data mahasiswa masih kosong.")
        return

    print("\n========== REKAP MAHASISWA ==========")

    kelas_list = sorted(set(m["kelas"] for m in data.values()))

    for kelas in kelas_list:
        data_kelas = {
            nim: m for nim, m in data.items()
            if m["kelas"] == kelas
        }

        print(f"\nKelas {kelas}")
        print("-" * 35)

        for nim, m in data_kelas.items():
            print(
                f"{nim} | {m['nama']} | "
                f"Nilai: {m['nilai']}"
            )

        print(
            f"Rata-rata kelas {kelas}: "
            f"{rata_rata_nilai(data_kelas):.2f}"
        )


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}


while True:
    print("\n===== MENU DATA MAHASISWA =====")
    print("1. Cari mahasiswa")
    print("2. Tambah mahasiswa")
    print("3. Perbarui nilai")
    print("4. Tampilkan rekap")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nim = input("Masukkan NIM: ").strip()
        cari_mahasiswa(data_mahasiswa, nim)

    elif pilihan == "2":
        tambah_mahasiswa(data_mahasiswa)

    elif pilihan == "3":
        perbarui_nilai(data_mahasiswa)

    elif pilihan == "4":
        tampilkan_rekap(data_mahasiswa)

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")
