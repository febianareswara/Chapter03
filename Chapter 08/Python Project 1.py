#input bilangan
totalBil = int(input('Masukkan total bilangan bulat : '))
n = 0
data = []
while totalBil >= 0:
    if n == totalBil :
        break
    if n != totalBil :
        print ('Masukkan bilangan bulat : ', end='')
        i = str(input())
        data.append(i)
        n = n+1

data.sort(reverse=True)
print ('\n', data)
