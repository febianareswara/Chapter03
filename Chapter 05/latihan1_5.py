#identitas karyawan
kode = int(input('Masukan kode karyawan : '))
nama = input('Masukan nama karyawan : ')
gol = input('Masukan golongan karyawan : ')
status = int(input('Masukan status(1: Menikah, 2: belum) :'))
jmlAnak = int(input('Masukan jumlah anak : '))
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
#tunjangan
TotalPotongan = GajiPokok*(potongan/100)
if(status==1):
    tunjangan= GajiPokok*(10/100)
    tunjanganAnak= GajiPokok*(5/100)*jmlAnak
    GajiKotor= GajiPokok + tunjangan + tunjanganAnak
    GajiBersih= GajiKotor - TotalPotongan
GajiBersih2= GajiPokok - TotalPotongan
        
    
#struk gaji
if (gol != False):
    print ('===============================================')
    print ('           STRUK RINCIAN GAJI KARYAWAN         ')
    print ('-----------------------------------------------')
    print ('Nama Karyawan            :', nama, 'Kode', kode)
    print ('Golongan                 :', gol)
    print ('Status                   :', end='')
    if (status==1):
        print('Menikah')
    else :
        print('Belum Menikah')
    if (status==1):
        print('Jumlah anak              :', jmlAnak)
    print ('-----------------------------------------------')
    print ('Gaji Pokok               : Rp.', GajiPokok)
    if (status==1):
        print ('Tunjangan Istri/Suami    : Rp.', tunjangan)
        print ('Tunjangan Anak           : Rp.', tunjanganAnak)
    print ('----------------------------------------------- +')
    print ('Gaji Kotor               : Rp.', GajiKotor)
    print ('Potongan(',potongan,'% )        : Rp.', TotalPotongan)
    print ('----------------------------------------------- -')
    if (status == 1):
        print ('Gaji Bersih              : Rp.', GajiBersih)
    else :
        print ('Gaji Bersih              : Rp.', GajiBersih2)
    print ('=================================================')
