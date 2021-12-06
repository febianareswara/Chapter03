print ('-Enskripsi Menggunakan Candi Caesar-')
print ('------------------------------------')
teksAsli = 'SAYA SUKA PYTHON'
print(teksAsli)
i = 0
a = int(input('Pergeseran sebanyak berapa kali ? '))
for n in range(len(teksAsli)):
    b = teksAsli[i]
    x = ord(b)
    if x==32:
        print(chr(x), end='')
    if x+a>90:
        print(chr(65+((x+a)-91)), end='')
    elif x!=32:
        x+=int(a)
        y = chr(x)
        print(y, end='')
    i+=1
