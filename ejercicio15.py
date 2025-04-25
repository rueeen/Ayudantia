# Instruccion if

acepto = input('Acepta terminos y condiciones? si/no: ')
#   condicion
if acepto == 'si': # Solo evalua condiciones verdaderos
    print('Ha aceptado terminos y condiciones y puede utilizar el software')
   # print('Esto da error') CUIDEN LOS ESPACIOS
# Va siempre despues del if, y puedo tener las que yo quiera
elif acepto == 'Si':
    print('Ha aceptado terminos y condiciones y puede utilizar el software') 
elif acepto == 'SI':
    print('Ha aceptado terminos y condiciones y puede utilizar el software')
elif acepto == 'no': # Es una condicion alternativa
    print('Ha rechazado terminos y condiciones y no puede utilizar el software')
elif acepto == 'NO':
    print('Ha aceptado terminos y condiciones y puede utilizar el software')
elif acepto == 'No':
    print('Ha aceptado terminos y condiciones y puede utilizar el software')
else: # Opcion por defecto si no se cumple ninguna condicion de la cascada
    print('No se ingreso una opcion correcta')

print('Esto esta fuera del bloque if')
