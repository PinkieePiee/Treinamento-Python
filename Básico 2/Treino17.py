genero = str(input('Qual é seu gênero? [F/M/NB/GF/Outro]')).strip().upper()[0]
print(genero)
while genero not in 'FfMmNBnbOutrooutro':
    print('Inválido! Digite novamente. ')
    str(input('Por favor digite seu gênero novamente: '))
print('Cadastro realizado com sucesso')


#strip() elimina os espaços em branco
#upper() deixa tudo em maiúsculo 
#[0] pega apenas a primeira letra