dataFile = open("Data.mhs.txt", "r")
datalist = []
data = dataFile.readlines()

for i in range(len(data)):
    pecahData = data[i].split("|")
    dataDict = {'NIM': pecahData[0],'Nama': pecahData[1],'Alamat': pecahData[2]}
    datalist.append(dataDict)
    
print(datalist)

dataFile.close()
