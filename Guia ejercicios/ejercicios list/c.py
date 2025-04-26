# Buscar el número mayor y menor
# Dada una lista de números, encuentra el número más grande y el más pequeño sin usar las funciones max() ni min().

numeros = [2, 10, 5, 22, 2, -4, 33, 1]

# Forma dificil
menor = 0
mayor = 0
for i in range(len(numeros)): # n -> 2
    if i == 0:
        menor = numeros[i]
        mayor = numeros[i]

    if numeros[i] > mayor:
        mayor = numeros[i]

    if numeros[i] < menor:
        menor = numeros[i]

print(f'El mayor es {mayor} y el menor es {menor}')

# Forma facil
numeros.sort() # La ordena de menor a mayor
print(f'El mayor es {numeros[-1]} y el menor es {numeros[0]}')