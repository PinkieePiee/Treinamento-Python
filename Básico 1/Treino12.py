larg = float(input(print('Qual a largura da parede? ')))
alt = float(input(print('Qual é a altura da parede? ')))
area = larg * alt

print('Sua parede tem as dimensões de {} x {} m**2. E sua area é igual a {}'.format(larg, alt, area))
tinta = area / 2
print('Sua parede irá precisar de {} L de tinta. '.format(tinta)) 