def faktorial(n):
    a = 1
    for i in range (1, n+1):
        a = a * i
    print(a)
def c(x, y):
    a = 1
    for i in range (1, x + 1):
        a = a * i
    b = 1
    for i in range (1, y + 1):
        b = b * i
    c = 1
    for i in range (1,x - y + 1):
        c = c * i
    print(a /(b * c))
def p(x, y):
    a = 1
    for i in range (1, x + 1):
        a = a * i
    b = 1
    for i in range (1, y + 1):
        b = b * i
    print(a / b)

faktorial(3)
c (5, 3)
p (10, 7)
