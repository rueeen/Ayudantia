print('Ejemplo break')
# Ejemplo while con break
contador = 10
while contador > 0: # 10, 9, 8, 7, 6, 5, 4,
    print(contador)
    contador -= 1
    if contador == 3:
        break
        print('Esto nunca se ejecuta')
    print('Esto se ejecuta siempre y cuando no haya un break')
print('Fuera del ciclo')

contador = 10
print('Ejemplo continue')
# Ejemplo while
while contador > 0: # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    print(contador)
    contador -= 1
    if contador == 3:
        continue
        print('Esto nunca se ejecuta')
    print('Esto se ejecuta siempre y cuando no haya un continue')
print('Fuera del ciclo')

# Ejemplo pass
if True:
    # Aca debe haber algo
    pass # Representa una instruccion valida, pero que no hace nada
print('Esto da error')