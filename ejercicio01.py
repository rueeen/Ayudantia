# Funcion print()
print("Hola mundo")
print('Hola mundo')
print(10)
print(True)
print(1.3)

# Funcion print por defecto hace un salto de linea y un espaciado entre argumentos
print("Saludos", "desde", "terminal") # Saludos desde terminal
print("Saludos", "desde", "terminal", sep=".") # Saludos.desde.terminal
print("Aca no hay salto de linea", end="@") # \n -> Representa un salto de linea
print("Esto aparece en la misma linea que lo anterior") # Aca no hay salto de linea@Esto aparece en la misma linea que lo anterior