# Crea una función que reciba dos números y devuelva su suma.

def sumar(a, b): 
    return a + b

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
resultado = sumar(num1, num2)

print(f'El resultado de la suma es: {resultado}')