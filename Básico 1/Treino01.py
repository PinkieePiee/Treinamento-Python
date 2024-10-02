m1 = input('Digite um número: ')
m2 = int(input('Digite mais um número: '))
print(type(m1))
print(type(m2))

p1 = int(input('Digite um valor: '))
p2 = int(input('Digite mais um valor: '))
p3 = p1 + p2
print('A soma entre' , p1, 'e', p2, 'é igual a', p3)
print('A soma entre o número {} e o número {} é {}' .format(p1, p2, p3))


n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2

print ('A soma vale:', s)
print ('A soma dos números vale {}'.format(s))

#métodos de teste de tipo
u = input('Digite alguma coisa:')
print(type(u))
print(u.isnumeric())
print(u.isalpha())
print(u.isalnum())
print(u.isupper())