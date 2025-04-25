# Ejemplo funcion

# Siempre se definen al inicio
def saludar(): # Funcion sin parametros
    print('Hola mundo desde funcion')

print('Primera linea de codigo ejecutada')
saludar() # Invocacion de funcion
print('Fin algoritmo')

# Que no hacer
# sumar(2, 3) # Error: Invocando funcion antes de ser declarada

def resta(a, b): # Con parametros
    print(a - b)

# Invocando funcion
resta(2, 3) # Debo enviar 2 argumentos posicionales -> resultado -1
# resta(2) # Error: Falta 1 argumento
# resta(2, 3, 4) # Error: Se envio 1 argumento de mas

a = 2
b = 3
resta(b, a) # resultado -> 1

nombre = 'Perico los Palotes'
def mostrar_nombre():
    nombre = 'Maria las Petunias'

mostrar_nombre()
print(nombre) # Perico los Palotes