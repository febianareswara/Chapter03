print ('****  Kalkulator  Ajaib  ****')
print ('-----------------------------')
print ('  PROGRAM HITUNG RATA-RATA   ')
print ('-----------------------------')

sum = 0
jumlah = 0
while True :
    try :
        bil = int(input('Masukkan bilangan bulat: '))
        lagi = input('Lagi (y/n) : ')
        if lagi == 'n':
            print ('rata ratanya adalah :', rerata )
            break
        
        sum += int(bil)
        jumlah += 1
        rerata = sum / jumlah
    
    except ValueError:
        print('Bukan bilangan bulat')
    except NameError :
        print ('Maaf terjadi kesalahan')
        error = input('Keluar dari program (y/n) :')
        if error == 'y' :
            print ('Anda telah keluar dari program')
            break
