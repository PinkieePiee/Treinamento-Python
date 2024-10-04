import time
from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('-=-'*10)
    print('''
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
#Dentro das aspas ''' não se faz necessário a identação

    print('-=-'*10)
    sleep (1)
    opcao = int(input('>>>>>> Qual é a sua opção? '))
    if opcao == 1:
        n3 = n1 + n2
        print('A soma entre {} + {} é {}'.format( n1, n2, n3))
    elif opcao == 2:
        n4 = n1 * n2
        print('A multiplicação entre {} X {} é {}'.format( n1, n2, n4))
    elif opcao == 3:
        if n1 > n2: #maior = n1
            print ('O maior número é {}'.format(n1))
        else: #maior = n2
            print('O maior número é {}'.format(n2))
    elif opcao == 4:
        n1 = int(input('Qual será o novo valor? '))
        n2 = int(input('Qual será o segundo novo número? '))
    elif opcao == 5:
        sleep (1)
        print('Obrigada por participar. Espero que tenha se divertido!')
        sleep(2)
        print('Finalizando...')
    else:
        print('Número inválido! Tente novamente. ')
    print('-=-'*10)
    sleep (2)
print('Fim do programa! Volte sempre!')