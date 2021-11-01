from math import floor
def starFormation1(n):
    for i in range (0, n):
        for x in range (0, i):
                print('* ', end='')
                x+=1
        print('')

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
n = 7
n = floor(n/2)+1
starFormation1(n)
starFormation2(n)
