def rataRataHarga ():
    harga = list(buah.values())
    total = 0
    banyak = 0
    for i in harga :
        total += i
        banyak += 1
    ratarata = total/banyak
    return ratarata
buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print (rataRataHarga())
