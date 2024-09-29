import random
import time

from random import randint
from time import sleep
itens = ('Pedra' , 'Tesoura', 'Papel')
computador = randint(0, 2)
print('''Suas opções são:
[0] PEDRA
[1] TESOURA
[2] PAPEL''')
jogador = int(input('Qual é a sua jogada? '))
print('-=-'*10)
print('JO!')
sleep (1)
print('KEN!')
sleep(1)
print('PO!!')
sleep(1)
print('-=-'*10)
if jogador < 0 or jogador > 2:
    print('Jogada inválida! Tente novamente.')
else:
    print('Computador jogou {} '.format(itens[computador]))
    print('Jogador jogou {} '.format(itens[jogador]))
    print('-=-'*10)

if computador == 0:
    if jogador == 0:
      print('Empatou!')
    elif jogador == 1:
      print('Jogador perdeu!')
    elif jogador == 2:
      print('Jogador venceu!')

elif computador == 1:
    if jogador == 0:
      print('Jogador venceu!')
    elif jogador == 1:
      print('Empatou!')
    elif jogador == 2:
      print('Jogador perdeu! ')


elif computador == 2:
      if jogador == 0:
        print('Jogador perdeu!')
      elif jogador == 1:
          print('Jogador venceu!')
      elif jogador == 2:
          print('Empatou!')

