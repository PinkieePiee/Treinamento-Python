times = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Internacional', 'São Paulo', 'Bahia', 'Cruzeiro', 'Atlético-MG', 'Vasco da Gama', 'Criciúma', 'Grêmio', 'Fluminense', 'EC Vitória', 'Athletico-PR', 'Bragantino', 'Juventude', 'Corinthians', 'Cuiabá', 'Atlético-GO')
#Lembre de deixar por linha apenas 4 itens, porém todos devem estar dentro dos parênteses()

print('=-='*10)
print(f'A lista dos times do Brasileirão é {times}')
print('=-='*10)

for f in times:
    print(f)
print('=-='*10)

print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('=-='*10)

print(f'Os quatro últimos colocados são: {times[16:]}') #[-4:]
print('=-='*10)

print(sorted(times))
print('=-='*10)

print(f'A posição do time Flamengo é a {times.index('Flamengo')+1}° posição')
#puxa a posição do item solicitado
print('=-='*10)
