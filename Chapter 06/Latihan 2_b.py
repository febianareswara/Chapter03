def starFormation2(n):
    m = n
    i = 0
    while(i < n):
        j = 0
        while(j < m):
                print ('* ', end='')
                j+=1
        print('')
        i+=1
        m-=1
n = 4
starFormation2(n)
