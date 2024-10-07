print('Gerador de PA:')
print('-=-'*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('A razão: '))

termo = primeiro 
cont = 1
while cont <= 10:
    print('{} -> '.format(termo))
    termo +=razao
    cont += 1

print('FIM!')