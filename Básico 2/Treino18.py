import random
from random import randint

computador = randint (0,10)
print('Sou seu computador.. Acabei de pensar em um número entre 0 e 10. ')
print('Será que você consegue adivinhar? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Quase... aumente um pouco! ')
        else:
            print('Quase... tente diminuir!')
print('Acertou!!!')
print('Sua quantidade de palpites foi {}'.format(palpites))

#Não aceita complemento, apenas caso entre abaixo um outro if
#ElIF aceita complemento e finaliza 