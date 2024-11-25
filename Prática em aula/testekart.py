voltas = []  # Declarada aqui para evitar que acumule valores errados

for corredor in range(3):  # Vamos testar com 3 corredores
    print(f"Corredor {corredor + 1}")

    for volta in range(3):  # Vamos testar com 3 voltas
        tempo = float(input(f"Digite o tempo da volta {volta + 1}: "))
        voltas.append(tempo)  # Adiciona o tempo na lista voltas

print(voltas)  # Mostra o que está acumulado
