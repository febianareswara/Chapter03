print ('Surat Keterangan Kelulusan Mahasiswa')

#input nilai
BahasaIndonesia = int(input('Masukkan nilai Bhs Indonesia	: '))
IPA = int(input('Masukkan nilai IPA	        : '))
Matematika = int(input('Masukkan nilai Matematika	: '))

if (BahasaIndonesia < 0) or(IPA < 0) or (Matematika < 0):
    print ('Maaf input ada yang tidak valid')
#kelulusan
elif (BahasaIndonesia > 60) and (IPA > 60) and (Matematika > 70):
    print ('Status Kelulusan :  LULUS')
else:
    print ('Status Kelulusan :  TIDAK LULUS')
    

