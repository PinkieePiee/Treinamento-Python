import math
from math import factorial

import time
from time import sleep

n = int(input('Digite um número para saber seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))

c = n
f = 1 #Como manter uma multiplicação limpa.

print('Calculando {}! = '.format(n), end = '')
sleep (1)
while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1 #Faz com que a cada volta c perca uma posição, indo de modo decrescente.
print('{}'.format(f))
