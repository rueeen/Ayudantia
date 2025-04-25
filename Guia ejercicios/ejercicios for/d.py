#Muestra todos los números desde 1 hasta el numero ingresado pares usando for y range.

numero = int(input('Ingrese un numero: '))

for i in range(1, numero + 1): # 1, 2, 3, 4, ..., n 
    if i % 2 == 0:
        print(i)