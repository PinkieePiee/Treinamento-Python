
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()


for i in range(3):  # Laço externo
    for j in range(3):  # Laço interno
        print(f"i = {i}, j = {j}")


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

for i in lista1:
    for j in lista2:
        print(f"{i} x {j} = {i * j}")


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


for i in range(1, 4):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Separar as tabuadas

