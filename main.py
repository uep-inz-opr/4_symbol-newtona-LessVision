import math

zrodlo = input()
lista_el = zrodlo.split(' ')

n = int(lista_el[0])
k = int(lista_el[1])

newton = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
print(int(newton))