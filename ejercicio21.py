# Lista vacia
lista = [] # NO tiene elementos
# Lista con elementos
lista = [1, 2, 3, 4, 5] # tiene elementos
lista_mixta = [1, 2, 3, "cuatro", "cinco", 6.0] # tiene elementos de diferentes tipos
#              0  1  2      3        4      5

print(lista_mixta) # imprime la lista mixta [1, 2, 3, "cuatro", "cinco", 6.0]
print(lista_mixta[4]) # imprime el elemento en la posicion 4 de la lista mixta "cinco"
# Los indices de la listas son de tipo INT y empiezan en 0.

# Modificar un elemento de la lista
lista_mixta[4] = 5 # Cambia el elemento en la posicion 4 de la lista mixta a 5
print(lista_mixta) # imprime la lista mixta [1, 2, 3, "cuatro", 5, 6.0]
# lista_mixta[100] = 100 # Error, no existe el indice 100 en la lista mixta

# Fucion len(): Entrega el tamaño de la lista
print(f'El tamaño de la lista es: {len(lista_mixta)}') # imprime el tamaño de la lista mixta 6