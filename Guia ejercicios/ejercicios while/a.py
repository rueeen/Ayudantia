# Muestra un menú que se repita hasta que el usuario seleccione "Salir".

while True:
    print('1. Continuar')
    print('2. Salir')

    opcion = input('Ingrese su opcion: ') # str

    if opcion == '2':
        break
    

    print('Continuando...')

print('Saliendo...')