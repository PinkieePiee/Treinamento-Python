lanche = ('Hambúrguer', 'Suco', 'Pizza' , 'Pudim', 'Batata Frita') #() para tuplas / [] para listas / {} para dicionários
#Tuplas são imutáveis
print(lanche[-4]) #Referenciar usa sempre conchetes
print(lanche[1:])
#Python sempre ignora o último elemento, por isso deixar vazio é a melhor alternativa quando se quer mostrar tudo

for cont in range (0, len(lanche)):
    print(f'Hoje eu vou comer {lanche[cont]}') #Estudar mais sobre

for conti in range (0, len(lanche)):
    print(f'Hoje irei papar {lanche[conti]} na posição {conti}')

for comida in lanche:
    print(f'Hoje eu vou jantar {comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer na janta hoje {comida} na posição {pos}')

print(sorted(lanche))
print(lanche)


print('Nossa, comi demais!')
