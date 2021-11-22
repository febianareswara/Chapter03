
while True :
    n = int(input('Jumlah nama mahasiswa yang akan diinputkan : '))
    break
print ('Silakan input {0} mahasiswa'. format (n))
mhs = []
while n > 0:
    try:
        namaMhs = str(input ('Masukan nama mahasiswa : '))
    except:
        print('Bukan nama mahasiswa')
    mhs.append (namaMhs)
    n -= 1
    ans = input ('Lagi (y/n)? ')
    if ans in ('N', 'n') :
        break
mhs.sort()
print (mhs)
print ('Susunan karakter huruf')
for x in mhs:
    print('{0} ({1} Karakter )' . format(x, len(x)))
    
