print ('--------Data Mahasiswa---------')
try :
    data = open ('DataMahasiswa.txt','a')
    while True :
        nim = input  ('Masukkan NIM    :')
        nama =input  ('Masukkan Nama   :')
        alamat =input('Masukkan Alamat :')
        isi = nim + '|' + nama + '|' + alamat + '\n'
        data.write(isi)
        Ulangi =input('Ulangi input lagi? y/n :')
        if (Ulangi=='y'):
            continue
        elif (Ulangi=='n'):
            break
        
    data.close()
except FileNotFoundError :
    print ('file tidak ditemukan')
print('')
try :
     data = open ('DataMahasiswa.txt','r')
     biodata = data.read()
     print(biodata)
     data.close()
except FileNotFoundError:
    print ()
