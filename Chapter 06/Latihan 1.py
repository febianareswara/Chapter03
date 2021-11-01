import math

a = int(input('Sisi a      :'))
b = int(input('Sisi b      :'))
c = int(input('Sisi miring :'))

def isPythagoras(a, b, c) :
    return a**2 + b**2 == c**2
if (isPythagoras(a, b, c)):
    print ('True')
else :
    print ('False')
