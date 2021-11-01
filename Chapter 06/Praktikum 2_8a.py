def luasSegitiga(alas, tinggi):
    luas1 = alas * tinggi / 2
    return luas1

alas = 10
tinggi = 20
print('Luas segitiga dg alas', alas,
      'dan tinggi ', tinggi,
      'adalah', luasSegitiga(alas, tinggi))
    
def luasSegitiga2(alas2, tinggi2):
    luas2 = alas2 * tinggi2 / 2
    return luas2

alas2 = 15
tinggi2 = 45
print('Luas segitiga ke 2 dg alas', alas2,
      'dan tinggi ', tinggi2,
      'adalah', luasSegitiga2(alas2, tinggi2))

def totalLuasSegitiga(luas1, luas2):
    totalLuas = luas1 + luas2
    return totalLuas

luas1 = (alas * tinggi) / 2
luas2 = (alas2 * tinggi2) / 2
print ('Jadi luas total kedua segitiga adalah', totalLuasSegitiga(luas1, luas2))
