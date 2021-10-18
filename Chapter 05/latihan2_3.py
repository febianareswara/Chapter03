hitung = 0
sum = 0
for i in range (100):
    bil = i+1
    if bil % 2 == 1:
        hitung = hitung + 1
        sum = sum + bil
        print (bil)

print('Banyak Bilangan Ganjil   : ', str(hitung))
print ('Jumlah Seluruh Bilangan : ', str(sum))
