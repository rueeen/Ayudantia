# Solicita dos números y una operación (+, -, *, /) y muestra el resultado.

numero1 = float(input('Ingrese un numero: '))
numero2 = float(input('Ingrese un numero: '))
operacion = input('Ingrese una operacion (+, -, *, /): ')

if operacion == '+':
    print(f'El resultado de la suma es {numero1 + numero2}')
elif operacion == '-':
    print(f'El resultado de la resta es {numero1 - numero2}')
elif operacion == '*':
    print(f'El resultado de la multiplicacion es {numero1 * numero2}')
elif operacion == '/':
    if numero2 == 0:
        print('No se puede dividir por cero')
    else:
        print(f'El resultado de la division es {numero1 / numero2}')
else:
    print('Operacion ingresada no valida')