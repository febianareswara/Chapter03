def tampilkan_data(data):
    print('-------------------------------')
    print('Daftar buah dan harganya :')
    i = 1
    for key, value in buah.items():
        print(i,'.', key, ':', value)
        i += 1

buah = {'apel'  : 5000,
        'jeruk' : 8500,
        'mangga': 7800,
        'duku'  : 6500}

tampilkan_data(buah)
total_semua = 0

print('-------------------------------')
nama = (input('Nama buah yang dibeli : '))
harga = buah[nama]
massa = int(input('Berapa Kg             : '))
total_harga = harga * massa
print ('Total harga           :', harga, 'x', massa, '=', total_harga)
print ('Terima kasih telah berbelanja di toko kami')
