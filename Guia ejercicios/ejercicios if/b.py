# Solicita tres números e imprime cuál es el mayor.
numero1 = float(input('Ingrese un numero: ')) # 1
numero2 = float(input('Ingrese un numero: ')) # 2
numero3 = float(input('Ingrese un numero: ')) # 3

# operador AND (Y) y permite realizar conjuncion de condiciones
# si condicion a es True y condicion b es True -> True
# si condicion a es True y condicion b es False -> False
# si condicion a es False y condicion b es True -> False
# si condicion a es False y condicion b es False -> False

if numero1 > numero2 and numero1 > numero3:
        print(f'El mayor es {numero1}')
elif numero2 > numero1 and numero2 > numero3:
        print(f'El mayor es {numero2}')
elif numero3 > numero1 and numero3 > numero2:
        print(f'El mayor es {numero3}')