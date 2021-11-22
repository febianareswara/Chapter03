#membuat data sayur
print("Menu :")
print("A. Tambah data sayur")
print("B. Hapus data sayur")
print("C. Tampilkan Data Sayur")

datasayur = ['bayam', 'kangkung', 'wortel', 'selada']
pilih = str(input("masukkan pilihan anda : "))
if pilih == "A":
    print("Tambah data sayur")
    datasayur.append(input("Masukkan nama sayur yang ingin ditambahkan : "))
    print("data baru : ", datasayur)
elif pilih == "B":
    try:
        print("Hapus data sayur")
        datasayur.remove(input("Masukkan nama sayur yang ingin dihapus : "))
        print("data baru : ", datasayur)
    except ValueError:
        print("Data tidak ditemukan")
elif pilih == "C":
    print("Tampilkan Data Sayur")
    print("Data sayur : ", datasayur)
