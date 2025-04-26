# Suma de elementos
# Crea una lista de números y escribe un programa que calcule la suma total de sus elementos.

numeros = [1, 2, 3, 4, 5]

sumar = 0
for n in numeros: # n -> 1, 2, 3, 4, 5
    sumar += n

print(f'El resultado de la suma es: {sumar}')