mhs = ['K001:ROSIHAN ARI:01/09/1979:SOLO', 
       'K002:DWI AMALIA FITRIANI:17/09/1979:KUDUS',
       'K003:FAZA FAUZAN:28/01/2005:KARANGANYAR']
print ('=================================================================')
print ('NIM	 NAMA MAHASISWA	        TGL LAHIR	     TEMPAT LAHIR')
print ('-----------------------------------------------------------------')
from datetime import datetime as dtm
for i in mhs:
    split = i.split(':')
    nim = split[0]
    nama = split[1]
    tglText = split[2]
    tglDate = dtm.strptime(tglText,'%d/%m/%Y')
    splitTgl = tglText.split('/')
    tahun = splitTgl[0]
    bulan = splitTgl[1]
    hari = splitTgl[2]

    tempatlahir = split[3]
    print (nim.ljust(8), nama.ljust(23), tglText.ljust(19), tempatlahir)
print ('-----------------------------------------------------------------')
