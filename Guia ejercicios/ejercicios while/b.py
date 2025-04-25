# Pide al usuario que ingrese una contraseña hasta que sea la correcta (predefinida).

password_predefinida = 'inacap2025'

password_ingresada = input('Ingrese password: ')

while password_ingresada != password_predefinida:
    password_ingresada = input('Incorrecta, intente nuevamente: ')

print('Password correcto !')