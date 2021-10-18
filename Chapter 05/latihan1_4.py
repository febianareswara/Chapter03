#identitas karyawan
kode = int(input('Masukan kode karyawan : '))
nama = input('Masukan nama karyawan : ')
gol = input('Masukan golongan karyawan : ')
#golongan
if (gol == 'A'):
    GajiPokok = 10000000
    potongan = 2.5
elif (gol == 'B'):
    GajiPokok = 8500000
    potongan = 2.0
elif (gol == 'C'):
    GajiPokok = 7000000
    potongan = 1.5
elif (gol == 'D'):
    GajiPokok = 5500000
    potongan = 1.0
else :
    gol = False
    print ('Golongan tidak terdaftar dalam data')
#struk gaji
if (gol != False):
    print ('===============================================')
    print ('           STRUK RINCIAN GAJI KARYAWAN         ')
    print ('-----------------------------------------------')
    print ('Nama Karyawan            :', nama, 'Kode', kode)
    print ('Golongan                 :', gol)
    print ('-----------------------------------------------')
    PotonganGaji = int(GajiPokok*potongan/100)
    GajiBersih = GajiPokok - PotonganGaji
    print ('Gaji Pokok               :', GajiPokok)
    print ('Potongan(',potongan,'% )        :', PotonganGaji)
    print ('----------------------------------------------- -')
    print ('Gaji Bersih              : ', GajiBersih)
