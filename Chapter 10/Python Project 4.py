dataFile = open("Data.mhs.txt", "r")
dataList = []
data = dataFile.readlines()

for i in range(len(data)):
    pecahData = data[i].split("|")
    dataDict = {'NIM': pecahData[0],'Nama': pecahData[1],'Alamat': pecahData[2]}
    dataList.append(dataDict)
while True:
    cari = input('Masukkan Nim yang mau dicari : ')
    for i in range(len(dataList)):
        if cari in dataList[i]['NIM']:
            print()
            print('Data Mahasiswa')
            print('NIM    :'+str(dataList[i]['NIM']))
            print('Nama   :'+str(dataList[i]['Nama']))
            print('Alamat :'+str(dataList[i]['Alamat']))
            
    if cari not in dataList[0]['NIM']:
        if cari not in dataList[1]['NIM']:
            if cari not in dataList[2]['NIM']:
                print("\"Data mahasiswa tidak ditemukan\"")

    print()
    ulang = input('Cari Lagi ?(y/n): ')
    print()
    if ulang in ('N', 'n'):
        print('')
        break
dataFile.close()
