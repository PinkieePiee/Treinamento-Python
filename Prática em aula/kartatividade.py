corrida = [] 
# ! Declarando uma mastriz

for corredor in range (6):
    voltas = [] #* como precisamos que ela seja esvaziada a cada novo for, declaramos ela dentro do primeiro, para que seja recriada
    print(f"Corredor número {corredor + 1}")

    for volta in range (10):
        tempo = float(input(f"Digite o tempo da volta {volta + 1}: "))
        voltas.append(tempo) # ! append está adicionando o que está entrando na vriável tempo ao final da lista voltas
        
    corrida.append(voltas) #! adição do tempo de cada volta na matriz corrida

print(corrida) #! vai mostrar o tempo de volta de cada corredor


melhor_tempo = float('inf')
melhor_volta = -1 #! Ambos são declarados como -1 porque precisamos que sejam valores não válidos, pra não confundir com uma posição da matriz existente
melhor_corredor = - 1

for corredor in range (6):
    for volta in range (10):
        if corrida[corredor][volta] < melhor_tempo:
            melhor_tempo = corrida[corredor][volta]
            melhor_corredor = corredor + 1
            melhor_volta = volta + 1

            #! o indíce do corredor/volta + 1 porque a contagem das posições em python começam no 0

print(f"A melhor volta foi do {melhor_corredor}° corredor em sua {melhor_volta}° volta com o tempo de {melhor_tempo:.2f} segundos.")



totais = []

for corredor in range(6):
    total = sum(corrida[corredor])
    totais.append((total, corredor +1))

totais.sort() #! ordena pelo menor, até o maior tempo (em ordem crescente)

print("Classificação final: ")
for posicao, (tempo, corredor) in enumerate(totais, start = 1): 
    #começa em 1 porque python começa a contagem em 0.
    print(f"{posicao}º lugar: Corredor {corredor} com {tempo:.2f} segundos.")



melhor_media = float('inf')  
melhor_volta = - 1

for volta in range(10):  #* Para cada volta 
    soma_volta = 0

    for corredor in range(6):  #! Soma dos tempos de todos os corredores nessa volta
        soma_volta += corrida[corredor][volta]

    media_volta = soma_volta / 6  #! Cálculo da média da volta

    if media_volta < melhor_media:  
        melhor_media = media_volta
        melhor_volta = volta + 1

print(f"A volta com a média mais rápida foi a volta {melhor_volta} com média de {melhor_media:.2f} segundos.")

