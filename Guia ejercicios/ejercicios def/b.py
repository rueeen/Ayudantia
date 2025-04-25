# Crea una función que reciba un número y diga si es par o impar.

def validar_par_impar(num):
    if num % 2 == 0:
        print('Es par')
    else:
        print('Es impar')

num = int(input('Ingresa un numero: '))

validar_par_impar(num)