def bintang(n):
    space = 2*n-1
    for a in range (n):
        JumlahA = 2*a+1
        HasilA = '*'*JumlahA
        print (HasilA.center(space))
    for b in range (n-1, 0, -1):
        JumlahB = 2*b-1
        HasilB = '*'*JumlahB
        print (HasilB.center(space))
bintang(7)

