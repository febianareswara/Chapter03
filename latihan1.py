print ('Rental Mobil Surakarta')
nama = input ('Nama : ')
alamat = input ('Alamat : ')
jam_keluar = int(input('jam pengambilan mobil :'))
jam_keluarmenit = int(input('menit pengambilan mobil :'))
jam_kembali = int(input('jam pengembalian mobil :'))
jam_kembalimenit = int(input('menit pengambilan mobil :'))
total_jamkeluar = abs((jam_keluar-jam_kembali)*60)
total_menitkeluar = (jam_keluarmenit + jam_kembalimenit + total_jamkeluar)
if total_menitkeluar <= 720 :
    total_biaya = 200000

else :
    total_biaya= ((total_menitkeluar - 720)/60* 10000) + 200000
print ('Total lama peminjaman mobil atas nama', nama, 'selama', total_menitkeluar , 'menit')
print ('Total biaya yang anda harus bayarkan sebesar Rp.', total_biaya)
print ('Terimakasih sudah menggunakan jasa Rental Mobil kami')
