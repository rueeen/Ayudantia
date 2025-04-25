# Funciones con retorno
def validar_edad(edad):
    if edad >= 18:
        return True
        print('Esto no se ejecuta')
    return False

edad = int(input('Ingresa tu edad: '))

respuesta = validar_edad(edad) # respuesta puede ser True o False

if respuesta:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

def retorno_multiple():
    return 5, 'hola'

numero, palabra = retorno_multiple()
print(numero)
print(palabra)