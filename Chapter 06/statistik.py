def sum (*bilangan):
    hasil = 0 
    for i in bilangan:
        hasil += i
    print (hasil)
def average (*bilangan):
    hasil = 0 
    x = 0
    for i in bilangan:
        hasil += i
        x += 1
    print (hasil/x)
def maks (*bilangan):
    hasil = 0 
    for i in bilangan:
        if i >= hasil :
            hasil = i
    print (hasil)
def min (*bilangan):
    hasil = 99999999 
    for i in bilangan:
        if i <= hasil:
            hasil = i
    print (hasil)



