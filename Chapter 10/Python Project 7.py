file = open('SandiCaesar.txt', 'r')
file2 = open ('DataTeksAsli.txt','a+')
isi = file.readlines()
data = isi[0].split('\n')
teks = data[0]
n = int(isi[1])
final = []
for i in teks :
    hasil = ord (i)+26-n
    if hasil >= 91:
        m = hasil%90
        hasil = 64+m
    if hasil >= 33 and hasil<= 64 :
        hasil = 32
    hasil2 = chr(hasil)
    final.append(hasil2)
gabung =''.join(final)
file2.write(gabung)
file2.seek(0,0)
jawab = file2.read()
print('TEKS ASLI : ', jawab)
file.close()
file2.close()
