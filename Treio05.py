import random
import time

from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador pensar, ou seja, sorteia aleatoriamente
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5 . Tente adivinhar... ')
print('-=-' *20)
jogador = int(input('Em que número estou pensando? ')) #Jogador tenta adivinhar
print('PENSANDO...')
sleep(3)
if jogador == computador:
  print('PARABÉNS! Você acertou!')

else:
  print('GANHEI!! Você errou! Eu pensei no número {} e não no {}'.format(computador, jogador))