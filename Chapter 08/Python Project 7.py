#harga buah termahal
hargaBuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print (hargaBuah)
harga = sorted(hargaBuah.items(), key=lambda x:x[1], reverse=True)
print('Urutan harga buah dari yang termahal hingga yang termurah adalah :')
for x in harga :
    print(x[0])

