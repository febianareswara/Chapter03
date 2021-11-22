#Membuat function 
def kuadrat(bil):
    if(isinstance(bil, list)):
        for i in range(len(bil)):
            bil[i] **= 2
        return bil
    return False

def listNew():
    loop = 0
    data = []
    while loop < 5:
        bilangan = int(input("masukkan bilangan bulat:"))
        data.append(bilangan)
        loop += 1

    return data
datalist = listNew()
#Hasil kuadrat
if(datalist):
    print("Hasil kuadrat dari :", datalist)
    hasil = kuadrat(datalist)
    print('Jawab :', hasil)
