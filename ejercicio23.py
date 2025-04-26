# Recorriendo lista
#         0    1    2    3    4
#        -5   -4   -3   -2   -1
lista = ['a', 'b', 'c', 'd', 'e']

for i in range(len(lista)): # len(lista) -> range(5) -> [0, 1, 2, 3, 4]
    # Asi accedemos tanto al valor como al indice
    print(f'Indice: {i} Valor: {lista[i]}')
print('------------------') 

for v in lista:
    # Solo accedemos al valor
    print(v)