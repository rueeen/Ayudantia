# Pide al usuario un número e indica si es positivo, negativo o cero. 

numero = float(input('Ingrese un numero: '))

if numero == 0:
    print('El numero es cero')
elif numero > 0:
    print('El numero es positivo')
else:
    print('El numero es negativo')
