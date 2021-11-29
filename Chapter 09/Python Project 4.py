import random
print ('Program Pengacakan Huruf dalam Kata ')
print ('------------------------------------')
def random_string (x, n):
    kumpulanKata = []
    i = 0
    while i < n:
        kata = ' '.join(random.sample(x, len(x)))
        if kata not in kumpulanKata :
            kumpulanKata.append(kata)
            i += 1
        else:
            continue
    return kumpulanKata
print(random_string(input
    ('Kata yang diinginkan : '),
    int(input('Jumlah pengacakan    : ' ))))
print ('------------------------------------')
