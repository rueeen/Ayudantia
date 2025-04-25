# Pide números y los suma hasta que se ingrese uno negativo.

numero = int(input('Ingrese un numero: '))
resultado = 0
resultado += numero
while resultado >= 0:
    numero = int(input('Ingrese un numero: '))
    resultado += numero
    print(f'El resultado es {resultado}')
print('El resultado es negativo')