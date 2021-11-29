mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
print ('================================================================')
print ('NIM	 NAMA MAHASISWA	        TGL LAHIR	    TEMPAT LAHIR')
print ('----------------------------------------------------------------')
for i in mhs:
    split = i.split(':')
    nim = split[0]
    nama = split[1]
    tglLahir = split[2]
    splitTgl = tglLahir.split('-')
    tgl = splitTgl[2]
    bln = splitTgl[1]
    thn = splitTgl[0]

    tempatlahir = split[3]
    print(nim.ljust(8), nama.ljust(23), tglLahir.ljust(19), tempatlahir)
print ('----------------------------------------------------------------')
