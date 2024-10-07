print('Gerador de PA:')
print('-=-'*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('A razão: '))

termo = primeiro 
cont = 1
total = 0
mais= 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end = '')
        termo +=razao
        cont += 1

    print('Pausa!')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('FIM!')
print('Progressão finalizada, o total de termos usados foi de {}.'.format(total))
