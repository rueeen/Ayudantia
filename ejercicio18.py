# Ejemplo sobrecarga range

for i in range(5):
    print(i) # 0, 1, 2, 3, 4

for i in range(2, 5):
    print(i) # 2, 3, 4

for i in range(1, 6, 2):
    print(i) # 1, 3, 5

print('Detalles a considerar')
# Esto no sirve
for i in range(-10): # El inicio debe ser positivo
    print(i)

for i in range(10, 5): # El inicio debe ser menor que el fin
    print(i)

# Esto si sirve
for i in range(10, 5, -1):
    print(i) # 10, 9, 8, 7, 6