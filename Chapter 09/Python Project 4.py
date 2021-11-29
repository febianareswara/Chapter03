import random
def randomString (x, n):
    daftarKata = []
    i = 0
    while i < n:
        kata = ' '.join(random.sample(x, len(x)))
        if kata not in daftarKata :
            daftarKata.append(kata)
            i += 1
        else:
            continue
    return daftarKata

print(randomString(input("Masukkan kata : "), int(input('Masukkan angka: ' ))))
