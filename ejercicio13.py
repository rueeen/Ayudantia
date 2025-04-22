# Sumar 2 numeros
# Ideal convertir el tipo en el momento del input()

numero1 = int(input('Ingrese numero 1: ')) # int(str) -> int
numero2 = float(input('Ingrese numero 2: '))

print(numero1 + numero2) # 5.0

# Formas de mostrar datos por pantalla
print('El resultado de la suma es', numero1+numero2)
print('El resultado de la suma es ' + str(numero1+numero2)) # Concatenando convirtiendo a str
# Utilizando format
print('El resultado de la suma es {}'.format(numero1 + numero2))
print(f'El resultado de la suma es {numero1 + numero2}')