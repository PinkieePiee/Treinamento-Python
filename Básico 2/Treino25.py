nota_1 = input('Digite a sua primeira nota: ')
nota_2 = input ('Digite a sua segunda nota: ')

n1 = eval(nota_1)
n2 = eval(nota_2)

media = 0.4 * n1 + 0.6 * n2
 
if media >= 5:
    print('Você foi aprovado. Parabéns!') 
else:
    print('Você foi reprovado. Mas não desista, está tudo bem.')