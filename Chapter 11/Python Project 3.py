file = open('DataPeminjaman.txt', 'r')

member = []
nama = []
judul = []
tglPinjam = []
tglKembali = []

for data in file:
    pecahData = data.split('|')
    member.append(pecahData[0])
    nama.append(pecahData[1])
    judul.append(pecahData[2])
    tglPinjam.append(pecahData[3])
    tglKembali.append(pecahData[4].strip())
    
while True:
    cari = input('Masukkan Kode Member Yang Dicari : ')
    print('')
    if cari in member :
        data = True
        import datetime
        
        n = member.index(cari)
        tglSkrg = datetime.datetime.now()
        from datetime import datetime

        x = tglKembali[n]
        z = datetime.strptime(x, '%Y-%m-%d')
        hasil = z - tglSkrg
        akhir = datetime.date(tglSkrg)
        batas = datetime.date(z)
        if data:
            rumus = akhir - batas
            day = rumus.days
            denda = 0
            if day <= 0:
                bayar = 0
            elif day >= 0:
                bayar = 2000 * int(day)
                denda += bayar

            print('Data Peminjam Buku')
            print('Kode Member                  :', member[n])
            print('Nama Member                  :', nama[n])
            print('Judul Buku                   :', judul[n])
            print('Tanggal Mulai Peminjaman     :', tglPinjam[n])
            print('Tanggal Maksimal Peminjaman  :', tglKembali[n])
            print('Tanggal Pengembalian         :', akhir)
            print('Terlambat                    :', day, 'hari')
            print('Denda                        :', 'Rp.', denda)

    else:
        print('Data Tidak Ditemukan')

    print('')
    lagi = input('Ingin Mencari Lagi? (y/n): ')
    if lagi == 'y':
        print('')
        continue
    else:
        break
