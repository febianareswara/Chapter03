def dataStat (*semua):
    data = list(semua)
    for x in data :
        myTuple = tuple(data)
        dataA = sum(myTuple)
        b = max (myTuple)
        c = min (myTuple)
        a = dataA/len (myTuple)
        d = [a, b, c]
        dataD = list(d)
    print('Keterangan :[Nilai rata rata, nilai tertinggi, nilai terendah]')
    print(dataD)
    
dataStat (6,3,2,5,8)
