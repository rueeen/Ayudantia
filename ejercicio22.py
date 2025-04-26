lista = []
print(f'El tamaño de la lista es: {len(lista)}')
print(f'Lista: {lista}')

# Agregar elemnto a la lista
nombre = input('Ingrese su nombre: ') # Perico
# metodo append() agrega un elemento al final de la lista
lista.append(nombre) # ['Perico']
print(f'El tamaño de la lista es: {len(lista)}')
print(f'Lista: {lista}')

nombre = input('Ingrese su nombre: ') # Maria
lista.append(nombre) 
print(f'El tamaño de la lista es: {len(lista)}')
print(f'Lista: {lista}') # ['Perico', 'Maria']
#                               0        1

# metodo insert() agrega un elemento en la posicion que se le indique
nombre = input('Ingrese su nombre: ') # Juan
#       indice, valor         0         1       2
lista.insert(1, nombre) # ['Perico', 'Juan', 'Maria']

nombre = input('Ingrese su nombre: ') # Pedro
lista.insert(100, nombre) # Si funciona, pero no es recomendable
print(f'El tamaño de la lista es: {len(lista)}')
print(f'Lista: {lista}') # ['Perico', 'Juan', 'Maria', 'Pedro']

# Eliminar un elemento de la lista
nombre = input('Ingrese su nombre: ') # Perico
# metodo remove() elimina el primer elemento que coincida con el valor
# Si no existe el elemento, lanza un error
lista.remove(nombre) # ['Juan', 'Maria', 'Pedro']
# lista.remove('Josue') # Error: ValueError: list.remove(x): x not in list. No existe el valor Josue en la lista

# metodo pop() elimina el elemento en la posicion que se le indique
# Si no se le indica la posicion, elimina el ultimo elemento de la lista    
eliminado = lista.pop()
print(f'Eliminado: {eliminado}') # Pedro
print(f'El tamaño de la lista es: {len(lista)}')
print(f'Lista: {lista}') # ['Juan', 'Maria']

lista.append('Perico')
lista.append('Pedro')
#                             0        1       2        3
print(f'Lista: {lista}') # ['Juan', 'Maria', 'Perico', 'Pedro']
eliminado = lista.pop(1) # Elimina el elemento en la posicion 1
print(f'Lista: {lista}') # ['Juan', 'Perico', 'Pedro']

# instruccion del para eliminar
del lista[2] # Elimina el elemento en la posicion 2
print(f'Lista: {lista}') # ['Juan', 'Perico']

# Cuidado con esto
del lista # Elimina la lista completa
# print(f'Lista: {lista}') # Error: NameError: name 'lista' is not defined. La lista ya no existe