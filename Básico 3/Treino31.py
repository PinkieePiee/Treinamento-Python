num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print(f'Os números que você digitou foram os {num}')

print(f'O valor 9 apareceu {num.count(9)} vezes. ') 
#Count se usa para contar quantas vezes apareceu determinado elemento.

if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}° posição.')
else:
    print('O valor 3 não está presente na tupla.')

print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

