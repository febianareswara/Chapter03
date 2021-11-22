#langkah kerja no 1 - 3
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
a.insert(3, 10)
b.insert(2, 15)
a.insert(10, 4)
b.insert(10, 8)
print(a)
print(b)

#langkah kerja no 4
a.sort()
b.sort()
print(a)
print(b)

#langkah kerja no 5
c = (a[:8])
d = (b[2:10])
print (c)
print (d)


#langkah kerja no 6
e=[]
i=0
for i in range(len(c)):
    r=c[i]+d[i]
    e=e+[r]
print (e)

#langkah kerja no 7
listE= tuple(e)
print(listE)

#langkah kerja no 8
nilaiMax= max(listE)
nilaiMin= min(listE)
jumlah= sum(listE)
print(nilaiMax)
print(nilaiMin)
print(jumlah)

#langkah kerja no 9
myString = "python adalah bahasa pemrograman yang menyenangkan"
print(myString)

#langkah kerja no 10
penyusun=set(myString)
print(penyusun)

#langkah kerja no 11 
buatlist= list(penyusun)
buatlist.sort()
print(buatlist)
