#Pide un número y muestra su tabla de multiplicar del 1 al 10.
# 2
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6

numero = int(input('Ingrese un numero: '))

for i in range(1, 11):
    print(f'{numero} x {i} = {i * numero}')