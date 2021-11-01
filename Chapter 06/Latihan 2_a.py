def starFormation1(n):
    n = n + 1
    for i in range(0, n):
        for x in range (0, i):
            print ('*', end='')
            x+=1
        print('')
n = 4
starFormation1(n)
