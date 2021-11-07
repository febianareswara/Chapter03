nfile = input('Masukan nama file : ')
try :
    while True :
        file = open ('d:/dataMhs.txt', 'a')
        tambahData = input ('Data yang mau ditambahkan : ')
        file.write(tambahData)
        file.close()
        tanya = input ('Mau lagi (y/n) : ')
        if tanya == 'y' :
            tambahData
        else :
            break
except FileNotFoundError :
    print ('File tidak ditemukan')
