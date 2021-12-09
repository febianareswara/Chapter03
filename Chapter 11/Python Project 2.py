from datetime import *
print('--- Data Peminjaman Buku--- ')
print('----------------------------')
print(' Perpustakaan Kota Surakarta ')
tglPinjam = date.today()
tglKembali= tglPinjam + timedelta(days=7)
DataPeminjam = open('DataPeminjaman.txt', 'a+')

while True :
    kode = input('Masukkan Kode Member : ')
    nama = input('Masukkan Nama Member : ')
    buku = input('Masukkan Judul Buku  : ')
    dataMasuk = kode +'|' + nama +'|' + buku + '|' + str(tglPinjam) +'|' + str(tglKembali) +'\n'
    DataPeminjam.write(dataMasuk)
    ulangi = input('Ulangi lagi ? (y/n) : ')
    if ulangi =='y':
        continue
    else :
        print('')
        break
DataPeminjam.close()
file = open('DataPeminjaman.txt', 'r')
data = file.read()
print(data)
file.close()
    
