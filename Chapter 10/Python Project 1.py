print ('-----------------------------------')
print ('BANYAKNYA BILANGAN GANJIL DAN GENAP')
print ('-----------------------------------')
try:
    bilVertikal = open('DataBilVertikal.txt', 'r')
    baca = bilVertikal.read(1)
    genap = 0
    ganjil = 0
    for i in bilVertikal:
        if (int(i)%2 == 0):
            genap += 1
        elif (int(i)%2 == 1):
            ganjil += 1  
    print('Banyaknya Bilangan Genap  : ', genap)
    print('Banyaknya Bilangan Ganjil : ', ganjil)
    bilVertikal.close()
except FileNotFoundError:
    print('File tidak ditemukan')
print ('-----------------------------------')
