from random import randint

numeros = (randint(1, 10),
     randint(1, 10),
     randint(1, 10),
     randint(1, 10),
     randint(1, 10))

print(f'Eu sorteei os valores: ')
for i in numeros:
    print(f'{i} ')

print(f'O maior valor sorteado foi {max(numeros)} e o menor valor sorteado foi {min(numeros)}')