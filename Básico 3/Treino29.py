numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Que número de 0 a 20 você deseja que seja lido?'))

if numero in range (0, len(numeros)):
    print(f'O número que você selecionoi foi o {numeros[numero]}!')
else:
    print('Ops! Opção inválida, digite novamente.')